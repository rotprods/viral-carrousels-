# STATE.md

## Current
Canonical repository bootstrap is ready for review on `feat/canonical-course-system`.

## Public artifact in this PR
`docs/index.html` is a responsive GitHub Pages control plane for the course system. The Pages workflow stages `docs/` plus `prompts/`, `templates/`, `skills/` and `adapters/`, validates the exact staged artifact, then deploys it.

## Implemented
- Agent continuity: AGENTS / GOAL / STATE / HANDOFF / CHANGELOG.
- Canonical P00–P17 Prompt OS.
- Traceable `visual-dna.json` → `DESIGN.md` → `SKILL.md` architecture.
- Codex / Claude Code / Higgsfield Supercomputer adapters.
- Responsive Pages control plane with direct P00–P17 copy actions from canonical `PROMPTS.md`.
- QA-gated GitHub Pages workflow.
- Deterministic static QA + hard release gates + PR template.

## Remaining P0
Import the full image-heavy interactive student course artifact and historical visual corpus into repository-managed Pages assets. The connector used for this bootstrap can write repository text reliably but cannot directly upload the existing local binary image corpus, so the control plane is intentionally not misrepresented as the final visual course.

## Release gate
1. PR CI must pass.
2. If Pages has never been configured, enable **Settings → Pages → Build and deployment → GitHub Actions** once.
3. Import the full visual artifact in a scoped follow-up PR, run 390/430/1440 visual QA, then tag the first student release.
