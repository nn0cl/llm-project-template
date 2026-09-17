"""Local repository fixtures; never use a user's checkout as a mutation target."""
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


def run(*args, cwd=ROOT, env=None):
    return subprocess.run(args, cwd=cwd, env=env, text=True, capture_output=True)


def git(root, *args):
    result = run('git', *args, cwd=root)
    if result.returncode:
        raise AssertionError(result.stderr)
    return result.stdout.strip()


def init(root):
    root.mkdir(parents=True, exist_ok=True)
    git(root, 'init', '-q', '-b', 'main')
    git(root, 'config', 'user.name', 'Fixture')
    git(root, 'config', 'user.email', 'fixture@example.invalid')


def commit(root):
    git(root, 'add', '-A')
    git(root, 'commit', '-qm', 'fixture')
    return git(root, 'rev-parse', 'HEAD')


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class Repositories(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.storage = tempfile.TemporaryDirectory(prefix='collaboration-tests-')
        cls.snapshot = Path(cls.storage.name)/'snapshot'
        cls.snapshot.mkdir()
        # Include current maintenance edits, but never private/unrelated files.
        for item in ['AGENTS.md', 'CLAUDE.md', '.gitignore', '.github', '.agents',
                     '.grok', '.cursor', 'docs', 'scripts']:
            source, dest = ROOT/item, cls.snapshot/item
            if source.is_dir():
                shutil.copytree(source, dest, ignore=shutil.ignore_patterns('__pycache__', '.DS_Store'))
            else:
                shutil.copy2(source, dest)
        init(cls.snapshot)
        commit(cls.snapshot)

    @classmethod
    def tearDownClass(cls):
        cls.storage.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='collaboration-case-')
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.source = self.work/'source'
        shutil.copytree(self.snapshot, self.source)
        self.target = self.work/'target'
        init(self.target)

    def command(self, script, *args, env=None):
        return run('bash', str(self.source/'scripts'/script), '--target', str(self.target),
                   *args, env=env)

    def copy(self, *args):
        result = self.command('copy-ai-collaboration-files.sh', *args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def update_fixture(self):
        self.copy()
        commit(self.target)
        with (self.source/'AGENTS.md').open('a') as stream:
            stream.write('\nFixture upstream addition.\n')
        return commit(self.source)
