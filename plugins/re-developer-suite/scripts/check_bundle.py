#!/usr/bin/env python3
"""Static checks for the RE Developer Suite bundle."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors = 0

    manifest = json.loads((root / ".claude-plugin" / "plugin.json").read_text("utf-8"))
    if manifest.get("name") != root.name:
        fail("plugin folder and manifest name differ")
        errors += 1

    skills = sorted((root / "skills").glob("*/SKILL.md"))
    expected_skills = {
        "re-hq",
        "initialize-re-workspace",
        "re-inv-dd-coordinator",
        "re-inv-deal-structuring",
        "re-project-design-planning",
        "re-legal-doc-renamer",
        "re-legal-counsel",
        "re-legal-writing",
        "re-legal-licensing",
        "re-legal",
        "re-legal-operations",
        "re-legal-verification-rules",
        "re-inv",
        "re-inv-operating-matrix",
        "re-inv-screening",
        "re-inv-preliminary-report",
        "re-inv-feasibility-study",
        "re-inv-full-report",
        "re-inv-verification-rules",
        "re-rnd",
        "re-project",
    }
    if {path.parent.name for path in skills} != expected_skills:
        fail("skill set does not match expected v1 bundle")
        errors += 1

    # English headers that the authoring guide requires to be Vietnamese in skill bodies.
    forbidden_headers = {
        "overview",
        "when to use",
        "workflow",
        "output shapes",
        "common pitfalls",
        "common mistakes",
        "verification checklist",
    }
    vietnamese_chars = re.compile(r"[À-ÿĀ-ſẠ-ỹƠơƯưĐđ]")
    for path in skills:
        text = path.read_text("utf-8")
        if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
            fail(f"invalid skill frontmatter: {path}")
            errors += 1
        lowered = text.lower()
        for forbidden in ("profile=\"chrome-relay\"", "~/.openclaw", "hermes-native"):
            if forbidden in lowered:
                fail(f"legacy runtime reference in {path}: {forbidden}")
                errors += 1
        description = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
        if description and len(vietnamese_chars.findall(description.group(1))) > 5:
            fail(f"description must be mostly English (trigger language; short Vietnamese glosses OK) in {path}")
            errors += 1
        for line in text.splitlines():
            if line.startswith("#"):
                header = line.lstrip("#").strip().lower()
                if header in forbidden_headers:
                    fail(f"English section header '{line.strip()}' in {path} — use Vietnamese per skill-authoring-guide")
                    errors += 1

    forbidden_suffixes = {".db", ".lock", ".log", ".env"}
    forbidden_names = {
        "memory.md",
        "config.yaml",
        "auth.json",
        "auth.lock",
        "models_dev_cache.json",
        "provider_models_cache.json",
        "ollama_cloud_models_cache.json",
        "context_length_cache.yaml",
    }
    for path in root.rglob("*"):
        if path.is_file():
            if path.suffix.lower() in forbidden_suffixes or path.name.lower() in forbidden_names:
                fail(f"forbidden runtime artifact: {path}")
                errors += 1
            lowered_parts = {part.lower() for part in path.parts}
            if lowered_parts.intersection({"sessions", "cache", "logs", "memories"}):
                fail(f"forbidden runtime directory content: {path}")
                errors += 1

    if errors:
        print(f"Bundle check failed with {errors} error(s).", file=sys.stderr)
        return 1
    print(f"Bundle check passed: {len(skills)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
