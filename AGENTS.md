# AGENTS.md

## Mission
Maintain **AI SLOP → BRAND SYSTEM** and its successor modules as a production-grade, student-facing AI-native creative systems training program, while preserving a recoverable execution/control plane for autonomous agents.

## Mandatory zero-context boot
Before material work, read in order:
1. `control-plane/README.md`
2. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.md`
3. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.json`
4. `control-plane/AUTHORITY_GRAPH.md`
5. `control-plane/RECOVERY_PROTOCOL.md`
6. `control-plane/NEXT_AGENT_BOOTSTRAP.md`
7. `GOAL.md`
8. `STATE.md`
9. `HANDOFF.md`
10. `CHANGELOG.md`

For Module 02 also read:
- `handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md`
- `control-plane/BENCHMARK_GATES.md`
- `control-plane/AUTONOMOUS_EDITING_VERTICAL_SLICE_GATE.md`

Then recover `rotprods/motion-OS` + `rotprods/ave` from their own durable state.

## Source of truth
1. Repository-specific canonical files on `main` + verified code/tests/renders.
2. `control-plane/` authority, evidence, decision, risk, benchmark and recovery records.
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
- Module 02 course design is blocked until the Motion.OS × AVE forensic capability audit passes G0/G1 and a real autonomous editing vertical slice passes G2; later claims of autonomous QA/repair require G3/G4.
- Every audited capability must be labeled `VERIFIED`, `PARTIAL`, `STUB`, `ASPIRATIONAL`, `BLOCKED`, or `UNKNOWN` with evidence.
- Unit-test counts and module counts do not substitute for rendered end-to-end evidence.
- `control-plane/EVIDENCE_LEDGER.jsonl` is the canonical evidence/event stream; do not create duplicate generic ledgers.
- Do not add generic infrastructure unless it closes an active P0/P1 or measurably improves creative output/recoverability.

## Agent workflow
1. Recover durable state and resolve contradictions.
2. State the active mission/gate and highest-value next action.
3. For Module 02, audit capabilities before proposing pedagogy.
4. Make the smallest coherent change.
5. Verify behavior/output, not merely element/code presence.
6. Run deterministic + browser/visual/render QA where applicable.
7. Append evidence/decisions/risks when state changes.
8. Update canonical STATE/HANDOFF/CHANGELOG as required.
9. Write a session checkpoint conforming to `control-plane/SESSION_CHECKPOINT.schema.json`.
10. Open a scoped PR for code/product changes; do not accumulate unrelated refactors.

## Quality gate
Before commit: simplify. Reject unnecessary abstractions, duplicate prompt sources, JS-only asset loading, dead navigation, inaccessible controls, decorative UI with no teaching function, capability theater and infrastructure that does not close a current risk/gap.
