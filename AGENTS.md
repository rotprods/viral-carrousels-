# AGENTS.md

## Mission
Maintain **AI SLOP → BRAND SYSTEM** as a production-grade, student-facing training system for premium viral carousels and executable visual brand systems.

## Source of truth
1. `GOAL.md` — North Star and acceptance criteria.
2. `STATE.md` — current release state and next gate.
3. `prompts/` — canonical prompt library.
4. `templates/`, `skills/`, `adapters/` — portable executable system.
5. `qa/` — release evidence.
6. `CHANGELOG.md` + `versions/` — append-only release history.
7. `site-bundle/` — exact student artifact deployed to GitHub Pages.

## Hard rules
- Never replace real images with transparent placeholders or JS hydration registries.
- Every CORE image must render without JavaScript.
- Every copy button must pass copy→paste verification.
- Every export action must produce a non-empty file.
- Student CORE must not depend on hidden modes, localStorage, debug registries or internal QA metadata.
- Prompts have one canonical textual source; UI may surface them but must not silently diverge.
- `visual-dna.json` records observations; `DESIGN.md` records decisions; `SKILL.md` records executable behavior.
- Brand A assets may never silently define Brand B.
- Do not call a release PASS until responsive + functional tests pass on the exact commit being released.

## Agent workflow
1. Read `GOAL.md`, `STATE.md`, `HANDOFF.md`.
2. Make the smallest coherent change.
3. Rebuild the site bundle if the student artifact changes.
4. Run deterministic QA.
5. Review mobile 390/430 and desktop 1440.
6. Update `STATE.md` and `CHANGELOG.md`.
7. Open a scoped PR; do not accumulate unrelated refactors.

## Quality gate
Before commit: simplify. Reject unnecessary abstractions, duplicate prompt sources, JS-only asset loading, dead navigation, inaccessible controls and decorative UI with no teaching function.
