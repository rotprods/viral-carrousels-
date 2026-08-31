# Release Gates

A release is BLOCKED unless every required gate passes on the exact commit being released.

## Content
- [ ] Golden Path complete.
- [ ] Extractor ADN Visual v2 link present.
- [ ] P00–P17 canonical prompts present.
- [ ] JSON → traceable DESIGN.md documented.
- [ ] DESIGN.md → SKILL.md documented.
- [ ] Codex / Claude Code / Higgsfield adapters present.

## Functional
- [ ] Every COPY action works by copy→paste verification.
- [ ] Every export produces a non-empty file.
- [ ] Fullscreen / image interactions work when used.
- [ ] Zero console/page errors in release browser tests.

## Visual / responsive
- [ ] 390×844 PASS.
- [ ] 430×932 PASS.
- [ ] 1440×1000 PASS.
- [ ] Zero hard horizontal overflow.
- [ ] Critical teaching visuals are not destructively cropped.

## Integrity
- [ ] Zero duplicate DOM IDs.
- [ ] Zero broken internal links.
- [ ] Zero missing image ALT.
- [ ] No transparent 1×1 image placeholders.
- [ ] `STATE.md` and `CHANGELOG.md` updated.

## Release
Only after all gates pass:
- merge scoped PR;
- deploy GitHub Pages from the same commit;
- tag `module-01-vX.Y.Z`;
- update `STATE.md` with deployed URL.
