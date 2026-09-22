from datetime import datetime
import os
import tomllib

from support import Repositories, commit, git


class DistributionTests(Repositories):
    def test_literal_project_text(self):
        value = r'Price $5 @home / a&b \\ "quoted"'
        self.copy('--project-name', value)
        self.assertIn(value, (self.target/'docs/collaboration/project-conventions.md').read_text())

    def test_copy_distributes_claude_skill_mirror(self):
        self.copy()
        shared = sorted(p.relative_to(self.target/'.agents/skills')
                        for p in (self.target/'.agents/skills').rglob('SKILL.md'))
        mirror = sorted(p.relative_to(self.target/'.claude/skills')
                        for p in (self.target/'.claude/skills').rglob('SKILL.md'))
        self.assertTrue(shared)
        self.assertEqual(mirror, shared)
        for rel in shared:
            self.assertEqual((self.target/'.claude/skills'/rel).read_bytes(),
                             (self.target/'.agents/skills'/rel).read_bytes())
        self.assertFalse((self.target/'.claude/settings.local.json').exists())

    def test_copy_preserves_existing_marker(self):
        self.copy()
        marker = self.target/'.collaboration-template-version'
        old = marker.read_text()
        with (self.source/'AGENTS.md').open('a') as stream:
            stream.write('\nNew version.\n')
        commit(self.source)
        self.copy()
        self.assertEqual(marker.read_text(), old)

    def test_branch_collision_preserves_target(self):
        new = self.update_fixture()
        branch = f'process/update-collab-template-{datetime.now():%Y%m%d}-{new[:8]}'
        git(self.target, 'branch', branch)
        before = (self.target/'AGENTS.md').read_bytes()
        result = self.command('update-ai-collaboration-files.sh', '--source', str(self.source),
                              '--delivery', 'local', '--non-interactive')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.target/'AGENTS.md').read_bytes(), before)
        self.assertEqual(git(self.target, 'status', '--porcelain'), '')
        self.assertEqual(git(self.target, 'branch', '--show-current'), 'main')

    def test_dirty_source_rejected_before_copy(self):
        (self.source/'AGENTS.md').write_text('uncommitted')
        result = self.command('copy-ai-collaboration-files.sh')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.target/'AGENTS.md').exists())

    def test_untracked_distributed_source_rejected(self):
        (self.source/'docs/collaboration/untracked.md').write_text('not in SHA')
        self.assertNotEqual(self.command('copy-ai-collaboration-files.sh').returncode, 0)

    def test_dirty_source_rejected_before_update(self):
        self.update_fixture()
        before = git(self.target, 'rev-parse', 'HEAD')
        (self.source/'AGENTS.md').write_text('uncommitted')
        result = self.command('update-ai-collaboration-files.sh', '--source', str(self.source),
                              '--delivery', 'local', '--non-interactive')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.target, 'rev-parse', 'HEAD'), before)
        self.assertEqual(git(self.target, 'status', '--porcelain'), '')

    def test_configuration_refuses_overwrite_and_keeps_new_sections(self):
        self.copy()
        result = self.command('configure-ai-collaboration.sh', '--non-interactive')
        self.assertEqual(result.returncode, 0, result.stderr)
        path = self.target/'docs/collaboration/runtime-routing.toml'
        before = path.read_bytes()
        data = tomllib.loads(before.decode())
        self.assertFalse(data['review']['large_change']['enabled'])
        self.assertEqual(data['source_structure']['source_file_line_threshold'], 300)
        self.assertNotEqual(self.command('configure-ai-collaboration.sh', '--non-interactive').returncode, 0)
        self.assertEqual(path.read_bytes(), before)

    def test_update_preserves_target_owned_settings(self):
        new = self.update_fixture()
        settings = self.target/'docs/collaboration/runtime-routing.toml'
        settings.write_text('[review]\nisolation="ask"\n')
        commit(self.target)
        result = self.command('update-ai-collaboration-files.sh', '--source', str(self.source),
                              '--delivery', 'local', '--non-interactive')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(tomllib.loads(settings.read_text())['review']['isolation'], 'ask')
        self.assertIn(new, (self.target/'.collaboration-template-version').read_text())
        self.assertEqual(git(self.target, 'status', '--porcelain'), '')

    def test_model_backslash_roundtrip(self):
        self.copy()
        value = r'host\name'
        result = self.command('configure-ai-collaboration.sh', '--non-interactive', '--review-model', value)
        self.assertEqual(result.returncode, 0, result.stderr)
        config = tomllib.loads((self.target/'docs/collaboration/runtime-routing.toml').read_text())
        self.assertEqual(config['review']['model'], value)

    def test_model_line_break_is_rejected_without_writing(self):
        self.copy()
        result = self.command('configure-ai-collaboration.sh', '--non-interactive',
                              '--review-model', 'host\nname')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.target/'docs/collaboration/runtime-routing.toml').exists())

    def github_stub(self):
        bindir = self.work/'bin'
        bindir.mkdir()
        log = self.work/'gh.log'
        stub = bindir/'gh'
        stub.write_text('#!/bin/sh\nprintf "%s\\n" "$@" >> "$GH_LOG"\nprintf "fixture-pr\\n"\n')
        stub.chmod(0o755)
        remote = self.work/'remote.git'
        git(self.work, 'init', '--bare', '-q', str(remote))
        git(self.target, 'remote', 'add', 'origin', str(remote))
        return dict(os.environ, PATH=str(bindir)+os.pathsep+os.environ['PATH'], GH_LOG=str(log)), log

    def test_selected_base_is_passed_to_github(self):
        self.update_fixture()
        git(self.target, 'branch', 'release')
        env, log = self.github_stub()
        result = self.command('update-ai-collaboration-files.sh', '--source', str(self.source),
                              '--delivery', 'github', '--base-branch', 'release', '--non-interactive', env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('--base\nrelease\n', log.read_text())

    def test_number_collision_blocks_auto_merge(self):
        self.update_fixture()
        (self.source/'docs/architecture/adr/0099-upstream.md').write_text('upstream')
        commit(self.source)
        (self.target/'docs/architecture/adr/0099-local.md').write_text('local')
        commit(self.target)
        env, log = self.github_stub()
        result = self.command('update-ai-collaboration-files.sh', '--source', str(self.source),
                              '--delivery', 'github', '--merge-pr', '--non-interactive', env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(log.exists())
