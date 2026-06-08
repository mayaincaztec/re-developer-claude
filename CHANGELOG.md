# Changelog

## 0.6.0 - 2026-06-08

- Merged superior content from the user's standalone skills into the plugin (dropping legacy "OpenClaw" branding, keeping tvpl/routing): `licensing-expert` gains `references/agencies-and-authority-2025.md` (post-merger agencies, 2-level local government from 01/07/2025, citation order) and a 4-level risk scale (🔴🟠🟡🟢) in the legal-status report template; `legal-counsel` gains `references/negotiation-and-dispute-playbook.md` (issue tiers, 3-round negotiation, dispute-resolution comparison, statute of limitations, arbitration).
- Vietnamese-principle audit: localized 125 English section headers and inline labels to Vietnamese across 22 skills (When to Use → Khi nào dùng, Workflow → Quy trình, Overview → Tổng quan, etc.); skill name/description stay English for triggering. Codified the header rule in `skill-authoring-guide.md`.
- English-deliverable support: added an Output-language rule to `operating-contract.md` (working language Vietnamese; deliverable language follows the user's request or governing context — e.g. English-form contract → English memo), wired into `legal-writing`, `legal-counsel`, and the authoring guide.

## 0.5.0 - 2026-06-08

- Unified template location: moved the 14 legal deliverable templates from `re-legal-deliverable-templates/references/` to the shared `templates/`; that skill now selects/points to `../../templates/...`. Convention (documented in `skill-authoring-guide.md`): deliverables live in `templates/`, only technical specs/guides live in a skill's `references/`.
- Strengthened RE-HQ for its arbitration/synthesis role: added a conflict-arbitration checklist and `templates/integrated-decision-memo.md`.
- Documented the naming convention + grandfather rule in `skill-authoring-guide.md`.

## 0.4.0 - 2026-06-08

- Removed all legacy Codex runtime artifacts: `agent-templates/*.toml`, `scripts/install_agents.py`, and the `setup-re-agents` skill. On Claude the departments are skills with no agent-install step.
- `initialize_workspace.py` now seeds `CLAUDE.md` (was `AGENTS.md`); updated the `initialize-re-workspace` skill and tests accordingly.
- Refreshed `check_bundle.py` (dropped agent-template validation), tests, README and `ACCEPTANCE.md` to the current 25-skill Claude bundle.
- Added an Excel prerequisite note (xlsx/openpyxl) to `re-feasibility-study`.
- Added `references/skill-authoring-guide.md` codifying suite conventions (frontmatter, language, references/link-integrity, routing ownership, naming, add/remove checklist).

## 0.3.1 - 2026-06-08

- Added `re-investment-operating-matrix` to standardize the RE-Investment-Finance bundle (task → skill → specialist pull → template → verification → escalation), at parity with the legal operating matrix.
- Added `test_internal_md_references_resolve` — a link-integrity test that verifies every intra-bundle relative reference (`../...md`, `references/...md`) resolves; fixed the broken/loose references it surfaced (re-hq, setup-re-agents, doc-renamer, tvpl-lookup-protocol, loi-and-offer-guide).
- Removed leftover empty `skills/deal-structuring/` directory.

## 0.3.0 - 2026-06-08

### Runtime cleanup & coherence
- Removed Codex residue across skills; pointed browser workflows to Claude in Chrome / WebFetch.
- Reframed `setup-re-agents` as legacy/compat (no agent install on Claude); fixed stale `check_bundle.py` and `tests/test_bundle.py` paths.
- Consolidated routing into a single source of truth (`references/routing-map.md`); trimmed duplicated routing in operating guides.
- Removed redundant `deal-structuring` skill; synced version/license frontmatter across all skills; removed the one-time `migration-manifest.json` and its test.

### tvpl legal integration
- Added `references/tvpl-lookup-protocol.md` and wired MCP `tvpl` (search / check_hieu_luc / get_dieu / get_luoc_do / so_sanh_dieu) into `licensing-expert`, `legal-counsel`, and `re-legal-verification-rules` for live legal-text and effect verification.

### RE-Investment-Finance — full deal lifecycle bundle
- `re-investment-finance` now owns the deal lifecycle. New skills: `re-investment-screening`, `re-preliminary-investment-report`, `re-feasibility-study` (spec + Excel generator), `re-full-investment-report`, `re-investment-verification-rules`.
- Moved `dd-coordinator` and `deal-structuring-advisor` (with FS→offer→LOI) from RE-HQ to RE-Investment-Finance; RE-HQ now executive-synthesis only. New templates: deal-screening-note, preliminary/full investment report, LOI.

### RE-Project-Design — design-planning specialist
- Added `design-planning` (1/500 planning-indicator calc engine + 9-step process + QCVN compliance + design review) with calculation-engine and standards references.

### Completed earlier
- Completed RE-Market-Research (engine `vn-re-research` wired in, verification checklist).

## 0.2.1 - 2026-06-07

- Ported the suite to the Claude Code / Cowork plugin standard.
- Added `.claude-plugin/marketplace.json` (repo root) and
  `plugins/re-developer-suite/.claude-plugin/plugin.json`.
- Removed Codex-only manifests (`.agents/plugins/marketplace.json`,
  `.codex-plugin/plugin.json`). Skills, references and templates unchanged.
- Rewrote README install instructions for `/plugin marketplace add` + `/plugin install`.

## 0.2.0 - 2026-06-07

- Migrated the complete selected legal reference, template and checklist library.
- Added detailed DD, deal structuring, legal intake, licensing, legal counsel,
  legal writing, document operations, quality-control and VN market workflows.
- Added all department operating guides and the cross-profile routing playbook.
- Normalized legacy runtime paths and tool instructions for Codex.
- Added a migration coverage manifest and hard exclusions for memory, sessions,
  cache, logs, databases, model configuration, authentication, runtime files
  and `.env` files.

## 0.1.0 - 2026-06-07

- Added the private Codex marketplace and `re-developer-suite` plugin.
- Added RE-HQ and four departmental workflow skills.
- Added DD and deal-structuring coordination workflows.
- Added four versioned custom-agent templates.
- Added safe agent installation and workspace initialization scripts.
- Added shared finding, handoff, DD, investment, market and design templates.
- Added static bundle checks and acceptance tests.

Migration note: Hermes/OpenClaw runtime configuration, caches, logs, memories,
sessions and credentials are intentionally excluded. Historical legal and tax
references must be re-verified against current primary sources.
