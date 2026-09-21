from pathlib import Path
import sys
import tempfile
import unittest

from support import ROOT, commit, init, run


class InvisibleUnicodeTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='unicode-case-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        init(self.root)
        (self.root/'README.md').write_text('# 日本語と English の通常テキスト\n', encoding='utf-8')

    def check(self):
        return run(sys.executable, str(ROOT/'scripts/check-invisible-unicode.py'),
                   '--root', str(self.root))

    def track(self, name, content):
        path = self.root/name
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding='utf-8')
        commit(self.root)

    def assert_rejected(self, content, expected):
        self.track('AGENTS.md', content)
        result = self.check()
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(expected, result.stderr)

    def test_visible_text_passes(self):
        commit(self.root)
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('1 text file', result.stdout)

    def test_zero_width_space_is_rejected_with_location(self):
        self.assert_rejected('line one\nhidden' + chr(0x200B) + 'text\n',
                             'AGENTS.md:2:7: U+200B ZERO WIDTH SPACE')

    def test_bidirectional_override_is_rejected(self):
        self.assert_rejected('a' + chr(0x202E) + 'b\n', 'U+202E RIGHT-TO-LEFT OVERRIDE')

    def test_tag_characters_are_rejected(self):
        tags = ''.join(chr(0xE0000 + ord(c)) for c in 'run')
        self.assert_rejected('ok' + tags + '\n',
                             'U+E0072 TAG LATIN SMALL LETTER R')

    def test_variation_selector_is_rejected(self):
        self.assert_rejected('x' + chr(0xFE0F) + '\n', 'U+FE0F VARIATION SELECTOR-16')

    def test_byte_order_mark_is_rejected(self):
        self.assert_rejected(chr(0xFEFF) + 'AGENTS\n', 'AGENTS.md:1:1: U+FEFF')

    def test_binary_file_is_skipped(self):
        self.track('image.bin', b'\x00\xe2\x80\x8b binary')
        self.assertEqual(self.check().returncode, 0)

    def test_untracked_file_is_ignored(self):
        commit(self.root)
        (self.root/'scratch.md').write_text(chr(0x200B), encoding='utf-8')
        self.assertEqual(self.check().returncode, 0)


if __name__ == '__main__':
    unittest.main()
