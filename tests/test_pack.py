"""Exercise independent distribution and corrupt packages in disposable directories."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_pack import check_pack, check_skill

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "pack"
        self.root.mkdir()
        for name in (".agents", ".codex"):
            shutil.copytree(ROOT / name, self.root / name)
        for name in ("README.md", "README.zh-CN.md", "AGENTS.md", "LICENSE"):
            shutil.copy2(ROOT / name, self.root / name)
        for name in ("docs", "tests", "scripts"):
            shutil.copytree(ROOT / name, self.root / name, ignore=shutil.ignore_patterns("__pycache__"))

    def skill(self, name="software-delivery"):
        return self.root / ".agents" / "skills" / name

    def append_link(self, target):
        entry = self.skill() / "SKILL.md"
        with entry.open("a", encoding="utf-8") as stream:
            stream.write(f"\n[Referenced resource]({target})\n")

    def test_current_pack_and_every_standalone_skill(self):
        self.assertEqual([], check_pack(self.root))
        for folder in sorted((self.root / ".agents" / "skills").iterdir()):
            if not (folder / "SKILL.md").exists():
                continue
            with self.subTest(skill=folder.name):
                destination = Path(self.temporary.name) / "standalone" / folder.name
                shutil.copytree(folder, destination)
                self.assertEqual([], check_skill(destination))

    def test_missing_asset_is_rejected(self):
        (self.skill() / "assets" / "checkpoint.md").unlink()
        self.assertTrue(any("missing resource" in error for error in check_pack(self.root)))

    def test_sibling_skill_dependency_is_rejected(self):
        self.append_link("../requirements-design/SKILL.md")
        self.assertTrue(any("escapes its package" in error for error in check_pack(self.root)))

    def test_titled_missing_asset_and_escape_are_rejected(self):
        self.append_link('assets/missing.md "details"')
        self.append_link('../../README.md "details"')
        errors = check_pack(self.root)
        self.assertTrue(any("missing resource" in error for error in errors))
        self.assertTrue(any("escapes its package" in error for error in errors))

    def test_reference_link_and_image_destinations_are_checked(self):
        entry = self.skill() / "SKILL.md"
        with entry.open("a", encoding="utf-8") as stream:
            stream.write('\n[Read reference][missing]\n\n[missing]: assets/missing.md "details"\n')
            stream.write('\n![Preview][image]\n\n[image]: ../../README.md\n')
        errors = check_pack(self.root)
        self.assertTrue(any("missing resource" in error for error in errors))
        self.assertTrue(any("escapes its package" in error for error in errors))

    def test_valid_titled_link_and_code_examples_do_not_fail(self):
        self.append_link('assets/checkpoint.md "details"')
        entry = self.skill() / "SKILL.md"
        with entry.open("a", encoding="utf-8") as stream:
            stream.write('\n```markdown\n[example](not-an-actual-resource.md)\n```\n')
        self.assertEqual([], check_pack(self.root))

    def test_encoded_escape_is_rejected(self):
        self.append_link("%2e%2e/%2e%2e/%2e%2e/README.md")
        self.assertTrue(any("escapes its package" in error for error in check_pack(self.root)))

    def test_absolute_resource_is_rejected(self):
        for target in ("/machine/file.md", "C:/machine/file.md", "file:///machine/file.md"):
            with self.subTest(target=target):
                self.append_link(target)
                self.assertTrue(any("portable relative path" in error for error in check_pack(self.root)))

    def test_malformed_frontmatter_is_rejected(self):
        (self.skill() / "SKILL.md").write_text("---\nname: [\n---\n", encoding="utf-8")
        self.assertTrue(any("invalid YAML" in error for error in check_pack(self.root)))

    def test_empty_description_is_rejected(self):
        entry = self.skill() / "SKILL.md"
        entry.write_text("---\nname: software-delivery\ndescription: ''\n---\n", encoding="utf-8")
        self.assertTrue(any("description" in error for error in check_pack(self.root)))

    def test_renamed_duplicate_skill_cannot_be_distributed(self):
        shutil.copytree(self.skill(), self.skill("duplicate-delivery"))
        self.assertTrue(any("match its distribution folder" in error for error in check_pack(self.root)))

    def test_default_prompt_must_invoke_actual_skill(self):
        interface = self.skill() / "agents" / "openai.yaml"
        interface.write_text(interface.read_text(encoding="utf-8").replace("$software-delivery", "$wrong-skill"), encoding="utf-8")
        self.assertTrue(any("default_prompt must name" in error for error in check_pack(self.root)))

    def test_null_prompt_is_reported_without_crashing(self):
        interface = self.skill() / "agents" / "openai.yaml"
        interface.write_text('interface:\n  display_name: "Delivery"\n  short_description: "Deliver a capability"\n  default_prompt: null\n', encoding="utf-8")
        self.assertTrue(any("missing interface.default_prompt" in error for error in check_pack(self.root)))

    def test_duplicate_agent_identity_is_rejected(self):
        folder = self.root / ".codex" / "agents"
        shutil.copy2(folder / "delivery-reviewer.toml", folder / "duplicate.toml")
        self.assertTrue(any("duplicate agent identity" in error for error in check_pack(self.root)))

    def test_invalid_agent_and_fake_permission_override_are_rejected(self):
        path = self.root / ".codex" / "agents" / "delivery-reviewer.toml"
        path.write_text('name = [', encoding="utf-8")
        self.assertTrue(any("invalid TOML" in error for error in check_pack(self.root)))
        path.write_text('name = "reviewer"\nsandbox_mode = "read-only"\n', encoding="utf-8")
        errors = check_pack(self.root)
        self.assertTrue(any("missing agent developer_instructions" in error for error in errors))
        self.assertTrue(any("cannot override inherited" in error for error in errors))

    def test_cli_reports_a_broken_package_without_modifying_it(self):
        entry = self.skill() / "SKILL.md"
        self.append_link("missing.md")
        before = entry.read_bytes()
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_pack.py"), "--root", str(self.root)], capture_output=True, text=True)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("missing resource", result.stderr)
        self.assertEqual(before, entry.read_bytes())


if __name__ == "__main__":
    unittest.main()
