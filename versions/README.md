# Version policy

- `site-bundle/` reconstructs the current student release candidate.
- Release manifests and QA evidence live in `qa/`.
- Every production change updates `CHANGELOG.md` and `STATE.md`.
- Tag verified releases as `module-01-vX.Y.Z`.
- Never overwrite or delete history to hide a regression; record failure and fix.
- The exact commit deployed to Pages must be the exact commit that passed QA.
