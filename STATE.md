# STATE.md

## Current
Canonical repository bootstrap is active on `feat/canonical-course-system`.

## Canonical public artifact
GitHub Pages reconstructs and deploys the exact student artifact from `site-bundle/`.

## Implemented in this branch
- Agent continuity files.
- P00–P17 prompt system.
- Traceable DESIGN.md + SKILL.md architecture.
- Codex / Claude Code / Higgsfield adapters.
- GitHub Pages workflow.
- Deterministic static QA.
- Responsive student build with direct image assets inside the deployable site bundle.

## Release gate
Run CI on the PR. If repository Pages is not configured yet, enable **Settings → Pages → Build and deployment → GitHub Actions** once.
