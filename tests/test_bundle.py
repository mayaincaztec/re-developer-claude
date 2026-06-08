from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "re-developer-suite"


class BundleTests(unittest.TestCase):
    def test_marketplace_points_to_plugin(self) -> None:
        marketplace = json.loads(
            (ROOT / ".claude-plugin" / "marketplace.json").read_text("utf-8")
        )
        entry = marketplace["plugins"][0]
        self.assertEqual(entry["name"], "re-developer-suite")
        self.assertEqual(entry["source"], "./plugins/re-developer-suite")

    def test_no_excluded_runtime_artifacts(self) -> None:
        forbidden_suffixes = {".db", ".lock", ".log", ".env"}
        forbidden_names = {
            "memory.md",
            "config.yaml",
            "auth.json",
            "auth.lock",
        }
        for path in PLUGIN.rglob("*"):
            if not path.is_file():
                continue
            self.assertNotIn(path.suffix.lower(), forbidden_suffixes, path)
            self.assertNotIn(path.name.lower(), forbidden_names, path)
            self.assertFalse(
                {part.lower() for part in path.parts}.intersection(
                    {"sessions", "cache", "logs", "memories"}
                ),
                path,
            )

    def test_internal_md_references_resolve(self) -> None:
        """Every intra-bundle relative path reference (../... or references/...)
        written inside a .md file must point to a file that exists.

        Scope is intentionally limited to parent-traversal paths (``../``) and
        skill-own ``references/`` paths — these are real cross-references. Paths
        that point at the external data workspace (``projects/``, ``reports/``,
        ``_config/``, ``[workspace_root]/`` …) are not matched and not checked.
        """
        pattern = re.compile(
            r"(?<![\w./-])(\.\./[\w./-]+\.md|references/[\w./-]+\.md)"
        )
        broken: list[str] = []
        for md in PLUGIN.rglob("*.md"):
            text = md.read_text("utf-8")
            for match in pattern.finditer(text):
                token = match.group(1)
                target = (md.parent / token).resolve()
                if not target.is_file():
                    broken.append(f"{md.relative_to(ROOT)} -> {token}")
        self.assertEqual(broken, [], "broken internal references:\n" + "\n".join(broken))

    def test_workspace_initializer_preserves_existing_claude_md(self) -> None:
        script = PLUGIN / "scripts" / "initialize_workspace.py"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            claude_md = root / "CLAUDE.md"
            claude_md.write_text("# Existing\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(script), "--apply", "--target", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("PRESERVE", result.stdout)
            self.assertEqual(claude_md.read_text("utf-8"), "# Existing\n")
            self.assertTrue((root / "deals").is_dir())
            self.assertTrue((root / "re-workspace.yaml").is_file())


if __name__ == "__main__":
    unittest.main()
