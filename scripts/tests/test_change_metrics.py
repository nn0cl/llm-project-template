from pathlib import Path
import tempfile
import unittest
import sys

from support import commit, git, init
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'lib'))
from change_metrics import measure
from review_policy import select_review, validate_settings


class MetricsTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='metrics-case-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        init(self.root)
        (self.root/'runtime.py').write_text('import sys\n' + '# line\n'*300)
        self.base = commit(self.root)
        self.settings = validate_settings({'review': {'large_change': {'enabled': True}},
            'source_structure': {'modules': {'runtime': ['*.py']}}})

    def test_extraction_keeps_base_size(self):
        (self.root/'runtime.py').write_text('from legacy import run\n')
        (self.root/'legacy.py').write_text('def run():\n    return 1\n')
        head = commit(self.root)
        result = measure(self.root, self.base, head, self.settings)
        self.assertEqual(result['max_implementation_lines'], 301)
        self.assertEqual(result['changed_files'], 2)
        self.assertEqual(select_review(self.settings, result)['isolation'], 'separate_context')
        runtime = next(x for x in result['files'] if x['path'] == 'runtime.py')
        self.assertEqual(runtime['imports'], ['legacy'])
        self.assertIn('source_file_line_threshold', runtime['structure_exceeded'])

    def test_delete_counts_old_source(self):
        git(self.root, 'rm', 'runtime.py')
        head = commit(self.root)
        result = measure(self.root, self.base, head, self.settings)
        self.assertEqual(result['max_implementation_lines'], 301)
        self.assertEqual(result['changed_lines'], 301)

    def test_binary_and_dirty_are_unknown(self):
        (self.root/'asset.bin').write_bytes(b'\0abc')
        head = commit(self.root)
        (self.root/'uncommitted.txt').write_text('new')
        result = measure(self.root, self.base, head, self.settings)
        self.assertEqual(len(result['unknown']), 2)
        self.assertEqual(select_review(self.settings, result)['isolation'], 'ask')

    def test_exclusions_and_rename_accounting(self):
        git(self.root, 'mv', 'runtime.py', 'renamed.py')
        head = commit(self.root)
        result = measure(self.root, self.base, head, self.settings)
        self.assertEqual(result['changed_files'], 2)
        self.assertEqual(result['changed_lines'], 602)
        self.settings['source_structure']['exclude_globs'] = ['*.py']
        self.assertEqual(measure(self.root, self.base, head, self.settings)['changed_files'], 0)

    def test_invalid_base_fails(self):
        import subprocess
        with self.assertRaises(subprocess.CalledProcessError):
            measure(self.root, 'missing-ref', 'HEAD', self.settings)

    def test_missing_module_owner_is_unknown(self):
        (self.root/'runtime.py').write_text('pass\n')
        head = commit(self.root)
        self.settings['source_structure']['modules'] = {}
        self.assertTrue(measure(self.root, self.base, head, self.settings)['unknown'])
