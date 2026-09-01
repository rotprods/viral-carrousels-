# STATE.md

## Current
Canonical repository bootstrap is ready for merge on `feat/canonical-course-system` pending the latest CI run.

## Public artifact in this PR
`docs/index.html` is the responsive GitHub Pages control plane for **AI SLOP → BRAND SYSTEM**. The Pages workflow stages `docs/index.html` plus the canonical `prompts/`, `templates/`, `skills/` and `adapters/`, validates that exact staged artifact, then deploys it.

## Implemented
- Agent continuity: AGENTS / GOAL / STATE / HANDOFF / CHANGELOG.
- Canonical P00–P17 Prompt OS with one source of truth.
- Traceable `visual-dna.json` → `DESIGN.md` → `SKILL.md` architecture.
- Codex / Claude Code / Higgsfield Supercomputer adapters.
- Responsive Pages control plane with direct P00–P17 COPY actions sourced from `PROMPTS.md`.
- Static QA and Playwright Browser QA on 390×844, 430×932 and 1440×1000.
- Browser copy-to-clipboard verification for P00–P17.
- QA-gated Pages deployment workflow.
- 29-asset historical semantic ledger with SHA-256 checksums.
- Version manifest for v3.0, v7.1 and v8.0-pro-responsive ancestry.
- Hard release gates + PR template.

## Remaining P0 — Issue #1
Import the full image-heavy interactive student course artifact and historical visual binaries into repository-managed Pages assets. Semantic provenance and hashes are already persisted in `assets/manifest.json`; the binary import must match them rather than inventing a new corpus.

## Release gate
1. Latest `QA` and `Browser QA` on the PR head must pass.
2. Merge the canonical control plane to `main`.
3. If Pages has never been configured, enable **Settings → Pages → Build and deployment → GitHub Actions** once.
4. Resolve Issue #1 in a scoped visual-import PR; require image/runtime/390/430/1440 gates before tagging the first full student visual release.
