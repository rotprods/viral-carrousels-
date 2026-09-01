# AGENTS.md

## Mission
Maintain **AI SLOP → BRAND SYSTEM** and its successor modules as a production-grade, student-facing AI-native creative systems training program, while preserving a recoverable execution/control plane for autonomous agents.

## Mandatory zero-context boot
Before material work, read in order:
1. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.md`
2. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.json`
3. `control-plane/AUTHORITY_GRAPH.md`
4. `control-plane/RECOVERY_PROTOCOL.md`
5. `control-plane/NEXT_AGENT_BOOTSTRAP.md`
6. `GOAL.md`
7. `STATE.md`
8. `HANDOFF.md`
9. `CHANGELOG.md`

For Module 02 also read `handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md` and recover `rotprods/motion-OS` + `rotprods/ave` from their own durable state.

## Source of truth
1. Repository-specific canonical files on `main` + verified code/tests/renders.
2. `control-plane/` authority, evidence, decision, risk and recovery records.
3. `prompts/` canonical prompt library.
4. `templates/`, `skills/`, `adapters/` portable executable system.
5. `qa/` and browser/visual evidence tied to an exact commit/artifact.
6. `CHANGELOG.md` + `versions/` append-only release history.
7. Generated artifacts with explicit provenance.
8. Conversation memory is convenience only and never authoritative.

## Hard rules
- Never replace real images with transparent placeholders or JS hydration registries.
- Every CORE image must render without JavaScript.
- Every copy button must pass copy→paste verification.
- Every export action must produce a non-empty file.
- Student CORE must not depend on hidden modes, localStorage, debug registries or internal QA metadata.
- Prompts have one canonical textual source; UI may surface them but must not silently diverge.
- `visual-dna.json` records observations; `DESIGN.md` records decisions; `SKILL.md` records executable behavior.
- Brand A assets may never silently define Brand B.
- Do not call a release PASS until responsive + functional tests pass on the exact commit/artifact being released.
- Motion.OS and AVE are execution substrates, not Module 02 curriculum.
- Engine documentation is a capability claim until corroborated by code/tests/renders.
- Module 02 course design is blocked until the Motion.OS × AVE forensic capability audit passes.
- Every audited capability must be labeled `VERIFIED`, `PARTIAL`, `STUB`, `ASPIRATIONAL`, `BLOCKED`, or `UNKNOWN` with evidence.
- Do not add generic infrastructure unless it closes an active P0/P1 or measurably improves creative output/recoverability.

## Agent workflow
1. Recover durable state and resolve contradictions.
2. State the active mission/gate and highest-value next action.
3. Make the smallest coherent change.
4. Verify behavior/output, not merely element/code presence.
5. Run deterministic + browser/visual QA where applicable.
6. Append evidence/decisions/risks when state changes.
7. Update canonical STATE/HANDOFF/CHANGELOG as required.
8. Write a session checkpoint conforming to `control-plane/SESSION_CHECKPOINT.schema.json`.
9. Open a scoped PR for code/product changes; do not accumulate unrelated refactors.

## Quality gate
Before commit: simplify. Reject unnecessary abstractions, duplicate prompt sources, JS-only asset loading, dead navigation, inaccessible controls, decorative UI with no teaching function, capability theater and infrastructure that does not close a current risk/gap.
