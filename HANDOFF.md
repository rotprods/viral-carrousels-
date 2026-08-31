# HANDOFF.md

## Zero-context recovery
Start with `AGENTS.md`, `GOAL.md`, `STATE.md`, then `CHANGELOG.md`. Do not infer current truth from chat history.

## Immediate validation
1. Reconstruct the site bundle using the same commands as CI.
2. Run `python scripts/qa.py _site/index.html`.
3. Open the exact artifact at 390×844, 430×932 and 1440×1000.
4. Click/copy every prompt and template recipe.
5. Test all export actions.
6. Confirm Extractor ADN Visual v2 opens the intended GPT.
7. Confirm every CORE image remains visible with JavaScript disabled.

## External dependency
GitHub Pages may require one-time repository configuration: **Settings → Pages → Build and deployment → GitHub Actions**.
