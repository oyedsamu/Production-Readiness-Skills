"""Failure fixtures for the Android starter package validation boundary."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_android_skills import validate


class AndroidValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / 'skills/android-example/SKILL.md'
        self.skill.parent.mkdir(parents=True)
        self.text = '---\nname: android-example\ndescription: Exercise a fixture behavior.\n---\n# Example\n\nDo the requested work.\n'
        self.skill.write_text(self.text)
        (self.root / 'README.md').write_text('- [`android-example`](skills/android-example/SKILL.md)\n')

    def assert_error(self, fragment):
        self.assertTrue(any(fragment in e for e in validate(self.root)), validate(self.root))

    def test_valid_independent_package(self):
        self.assertEqual(validate(self.root), [])

    def test_malformed_and_duplicate_yaml(self):
        for text in ['---\nname: [\n---\nBody', self.text.replace('description:', 'name: android-second\ndescription:')]:
            with self.subTest(text=text):
                self.skill.write_text(text)
                self.assertTrue(validate(self.root))

    def test_mismatched_name(self):
        self.skill.write_text(self.text.replace('name: android-example', 'name: android-other'))
        self.assert_error('Name must match')

    def test_empty_description_and_body(self):
        for text in [self.text.replace('Exercise a fixture behavior.', '""'), self.text.split('# Example')[0]]:
            with self.subTest(text=text):
                self.skill.write_text(text)
                self.assertTrue(validate(self.root))

    def test_broken_link_and_repair(self):
        self.skill.write_text(self.text + '\n[Evidence](references/evidence.md)\n')
        self.assert_error('missing link')
        (self.skill.parent / 'references').mkdir()
        (self.skill.parent / 'references/evidence.md').write_text('# Evidence\n')
        self.assertEqual(validate(self.root), [])

    def test_skill_link_cannot_escape_its_installable_folder(self):
        self.skill.write_text(self.text + '\n[Other](../../README.md)\n')
        self.assert_error('escapes package boundary')

    def test_nonportable_link(self):
        self.skill.write_text(self.text + '\n[Other](file:///tmp/example.md)\n')
        self.assert_error('nonportable link')

    def test_duplicate_missing_or_wrong_catalog_entry(self):
        for text in ['', '- [`android-example`](skills/android-other/SKILL.md)\n', '- [`android-example`](skills/android-example/SKILL.md)\n' * 2]:
            with self.subTest(text=text):
                (self.root / 'README.md').write_text(text)
                self.assert_error('catalog must link')

    def test_missing_skill_file(self):
        (self.root / 'skills/android-missing').mkdir()
        self.assert_error('missing SKILL.md')

    def test_symlink_rejected(self):
        (self.skill.parent / 'alias.md').symlink_to(self.skill)
        self.assert_error('symlinks')

    def test_absent_package(self):
        self.assertTrue(validate(self.root / 'absent'))


if __name__ == '__main__':
    unittest.main()
