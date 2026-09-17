import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'lib'))

try:
    from review_policy import validate_settings, select_review
except ImportError:
    validate_settings = select_review = None


class RoutingTests(unittest.TestCase):
    def settings(self, enabled=True):
        self.assertIsNotNone(validate_settings, 'review policy not implemented')
        return validate_settings({'review': {'isolation': 'same_context', 'model': 'normal',
            'large_change': {'enabled': enabled, 'source_line_threshold': 300,
                             'changed_line_threshold': 500, 'changed_file_threshold': 5,
                             'cross_module_trigger': True, 'isolation': 'separate_context',
                             'model': 'reviewer'}}})

    def measure(self, lines=300, changed=500, files=5, modules=1, unknown=False):
        return dict(max_implementation_lines=lines, changed_lines=changed,
                    changed_files=files, module_count=modules, unknown=['fixture'] if unknown else [])

    def test_missing_settings_preserve_default(self):
        self.assertIsNotNone(validate_settings, 'review policy not implemented')
        self.assertEqual(select_review(validate_settings({}), self.measure())['isolation'], 'same_context')

    def test_threshold_boundaries(self):
        settings = self.settings()
        for metric, values in [('lines', [299, 300, 301]), ('changed', [499, 500, 501]),
                               ('files', [4, 5, 6])]:
            for value in values:
                with self.subTest(metric=metric, value=value):
                    result = select_review(settings, self.measure(**{metric: value}))
                    self.assertEqual(result['isolation'], 'separate_context' if value == values[-1] else 'same_context')

    def test_cross_module_trigger(self):
        self.assertEqual(select_review(self.settings(), self.measure(modules=2))['model'], 'reviewer')

    def test_disabled_does_not_override(self):
        self.assertEqual(select_review(self.settings(False), self.measure(lines=999, unknown=True))['model'], 'normal')

    def test_unknown_requests_decision(self):
        self.assertEqual(select_review(self.settings(), self.measure(unknown=True))['isolation'], 'ask')

    def test_known_trigger_is_not_downgraded_by_unknown(self):
        self.assertEqual(select_review(self.settings(), self.measure(lines=301, unknown=True))['isolation'], 'separate_context')

    def test_invalid_settings_rejected(self):
        self.assertIsNotNone(validate_settings, 'review policy not implemented')
        for section in [{'enabled': 'false'}, {'changed_line_threshold': -1},
                        {'changed_file_threshold': True}, {'isolation': 'typo'},
                        {'cross_module_required': True}, {'token_budget': 0}]:
            with self.subTest(section=section), self.assertRaises(ValueError):
                validate_settings({'review': {'large_change': section}})
        with self.assertRaises(ValueError):
            validate_settings({'review': {'model': 'host\nname'}})
