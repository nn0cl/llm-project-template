from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest

from support import commit, init, module


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='validator-case-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        init(self.root)
        issue = self.root/'docs/issues/LISS-0001-fixture.md'
        issue.parent.mkdir(parents=True)
        issue.write_text('fixture')
        sha = commit(self.root)
        now = datetime.now(timezone.utc)
        self.data = dict(schema_version=1, batch_id='fixture', status='in_progress',
                         approval_type='bounded-batch', approved_by='human',
                         approved_at=(now-timedelta(days=2)).isoformat(),
                         expires_at=(now+timedelta(days=2)).isoformat(),
                         execution_branch='batch/fixture', approval_commit=sha,
                         issue_ids=['LISS-0001'], approved_scope='fixture',
                         allowed_paths=['docs/**'], allowed_phases=['phase-1-red'],
                         allowed_operations=['test'], invalidating_triggers=['scope'],
                         post_review_required=True)
        self.record = self.root/'record.json'
        self.checker = module('check-execution-batch-reviews')

    def validate(self, branch='batch/fixture'):
        self.record.write_text(json.dumps(self.data))
        self.checker.validate_record(self.record, self.root, branch)

    def test_valid_active_batch(self):
        self.validate()

    def test_expired_active_batch_is_rejected(self):
        self.data['expires_at'] = (datetime.now(timezone.utc)-timedelta(days=1)).isoformat()
        with self.assertRaisesRegex(ValueError, 'expir'):
            self.validate()

    def test_post_reviewed_still_checks_paths(self):
        (self.root/'outside.txt').write_text('not permitted')
        commit(self.root)
        self.data.update(status='post_reviewed', post_reviewed_by='human',
                         post_reviewed_at=datetime.now(timezone.utc).isoformat(), post_review_notes='review')
        with self.assertRaisesRegex(ValueError, 'outside'):
            self.validate()

    def test_completed_historical_record_is_readable(self):
        self.data.update(status='post_reviewed', post_reviewed_by='human',
                         post_reviewed_at=datetime.now(timezone.utc).isoformat(), post_review_notes='review')
        self.data['expires_at'] = (datetime.now(timezone.utc)-timedelta(days=1)).isoformat()
        self.validate('main')

    def test_rejected_status_cannot_hide_outside_changes(self):
        (self.root/'outside.txt').write_text('not permitted')
        commit(self.root)
        self.data['status'] = 'rejected'
        with self.assertRaisesRegex(ValueError, 'outside'):
            self.validate()

    def test_current_register_needs_real_source(self):
        (self.root/'rule.md').write_text('rule')
        path = self.root/'canonical-document-register.md'
        path.write_text('| canonical_key | layer | status | entry_path | canonical_path | source_paths |\n'
                        '| --- | --- | --- | --- | --- | --- |\n'
                        '| rule | Canonical | Current | rule.md | rule.md | <missing> |\n')
        errors = []
        module('check-document-lifecycle').check_register(path, self.root, errors)
        self.assertTrue(errors)
