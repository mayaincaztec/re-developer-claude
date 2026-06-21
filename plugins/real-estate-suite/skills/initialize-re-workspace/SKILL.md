---
name: initialize-re-workspace
description: Use when creating or validating a real-estate data workspace for Real Estate Suite without placing deal data inside the plugin.
version: 1.0.0
license: Proprietary
---

# Initialize RE Workspace

Use `scripts/initialize_workspace.py`.

- Default target is the current working directory.
- Run `--check` before `--apply`.
- Create only missing directories and starter files.
- Never overwrite a non-empty `CLAUDE.md` or `re-workspace.yaml`.
- Keep deals, internal knowledge and outputs outside the plugin.
- The canonical workspace structure is `../../references/workspace-layout.md` — follow it when creating deal folders, and seed each new deal with `../../templates/deal-dossier.md` as `deals/<deal-id>/_dossier.md`.
- Explain that local `templates-local/` may override plugin templates by filename when the user explicitly requests that behavior.
