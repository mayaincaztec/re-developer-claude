# Acceptance Checklist

## Static

- `.claude-plugin/marketplace.json` resolves `./plugins/re-developer-suite`.
- `plugins/re-developer-suite/.claude-plugin/plugin.json` is valid and version matches the marketplace.
- 22 skills are discovered (`scripts/check_bundle.py` passes), plus 4 agents in `agents/` and 4 slash commands in `commands/`.
- All intra-bundle relative references resolve (`tests/test_bundle.py` passes).
- Bundle contains no credentials, databases, logs or deal folders.

## Personal Pilot

- Install the marketplace from an immutable release tag, install the plugin, start a new thread.
- Initialize a temporary RE workspace and confirm an existing `CLAUDE.md` is preserved.
- Run one task for each department (Legal, Investment & Finance, Market Research, Project & Design).
- Run one ambiguous routing task through RE-HQ.
- Run the deal lifecycle through RE-Investment-Finance: screening → preliminary report → FS → full report/IC → structuring + LOI → DD.
- Confirm a legal task uses `tvpl` to verify legal-text status (or states it could not).
- Confirm outputs distinguish confirmed, inferred, assumed and unresolved items.
- Confirm current web sources include links and access dates.

## Company Promotion

- Install the same tested tag, not `main`.
- Repeat plugin and skill discovery checks.
- Confirm company permissions allow private marketplace installation.
- Confirm no private workspace content is sent externally without approval.
- Record the installed plugin version.
