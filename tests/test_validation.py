"""Exercise packaging failures with disposable skill fixtures."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from sync_shared import ROOT, SHARED, sync
from validate_skills import validate


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills" / "cli-tool-completion"
        shutil.copytree(ROOT / "skills" / self.skill.name, self.skill)
        shutil.copytree(ROOT / "templates", self.root / "templates")
        (self.root / "docs").mkdir()
        (self.root / "docs/catalog.json").write_text(json.dumps([{"name": self.skill.name}]))
        (self.root / "README.md").write_text(f"[CLI](skills/{self.skill.name}/SKILL.md)\n")

    def append(self, path, text):
        path.write_text(path.read_text() + text)

    def assert_invalid(self, message):
        errors = validate(self.root)
        self.assertTrue(any(message in error for error in errors), errors)

    def test_one_copied_skill_is_independent(self):
        self.assertEqual(validate(self.root), [])

    def test_broken_reference_fails(self):
        self.append(self.skill / "SKILL.md", "\n[Missing](references/missing.md)\n")
        self.assert_invalid("missing link")

    def test_existing_external_reference_still_fails(self):
        self.append(self.skill / "SKILL.md", "\n[Outside](../../README.md)\n")
        self.assert_invalid("link escapes skill")

    def test_symlink_dependency_fails(self):
        (self.skill / "references/linked.md").symlink_to(self.root / "README.md")
        self.assert_invalid("symlinks break independent packaging")

    def test_duplicate_yaml_key_fails(self):
        entry = self.skill / "SKILL.md"
        entry.write_text(entry.read_text().replace("name: cli-tool-completion", "name: cli-tool-completion\nname: other"))
        self.assert_invalid("Duplicate YAML key")

    def test_mismatched_name_fails(self):
        entry = self.skill / "SKILL.md"
        entry.write_text(entry.read_text().replace("name: cli-tool-completion", "name: wrong-name"))
        self.assert_invalid("Name must match")

    def test_wrong_invocation_fails(self):
        entry = self.skill / "agents/openai.yaml"
        entry.write_text(entry.read_text().replace("$cli-tool-completion", "$other-skill"))
        self.assert_invalid("Default prompt must invoke")

    def test_missing_interface_fails(self):
        (self.skill / "agents/openai.yaml").write_text("interface: {}\n")
        self.assert_invalid("Missing interface")

    def test_malformed_interface_reports_error(self):
        (self.skill / "agents/openai.yaml").write_text("interface: wrong-type\n")
        self.assert_invalid("Expected interface to be a mapping")

    def test_frontmatter_delimiter_inside_description_is_valid(self):
        entry = self.skill / "SKILL.md"
        entry.write_text(entry.read_text().replace("for production release.", "for production release --- with evidence."))
        self.assertEqual(validate(self.root), [])

    def test_shared_check_is_read_only_and_sync_repairs_drift(self):
        target = self.skill / "references/reporting.md"
        target.write_text("local drift\n")
        before = target.read_bytes()
        self.assertTrue(sync(self.root, check=True))
        self.assertEqual(target.read_bytes(), before)
        self.assert_invalid("Shared reference drift")
        self.assertTrue(sync(self.root))
        self.assertEqual(target.read_bytes(), (self.root / "templates/reporting.md").read_bytes())
        self.assertEqual(sync(self.root), [])
        self.assertEqual(validate(self.root), [])

    def test_sync_restores_missing_shared_reference(self):
        (self.skill / "references" / SHARED[0]).unlink()
        self.assert_invalid("Shared reference drift")
        sync(self.root)
        self.assertEqual(validate(self.root), [])

    def test_duplicate_or_missing_catalog_entry_fails(self):
        catalog = self.root / "docs/catalog.json"
        catalog.write_text(json.dumps([{"name": self.skill.name}] * 2))
        self.assert_invalid("each skill exactly once")
        catalog.write_text("[]")
        self.assert_invalid("each skill exactly once")

    def test_readme_catalog_link_is_required(self):
        (self.root / "README.md").write_text("No catalog links\n")
        self.assert_invalid("README does not link")


if __name__ == "__main__":
    unittest.main()
