# HANDOFF.md

## Zero-context entrypoint
Do not start from chat history or the old Pages workflow.

Start here:
1. `control-plane/README.md`
2. `control-plane/NEXT_AGENT_BOOTSTRAP.md`
3. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.md`
4. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.json`
5. `control-plane/AUTHORITY_GRAPH.md`
6. `control-plane/RECOVERY_PROTOCOL.md`
7. `GOAL.md`
8. `STATE.md`
9. `control-plane/DECISIONS.md`
10. `control-plane/RISKS.md`
11. latest `control-plane/checkpoints/*`

For Module 02 also read `handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md` and then recover `rotprods/motion-OS` + `rotprods/ave` from their own canonical files.

## Active gate
The active mission is **not** to build the video-training HTML.

It is:
`Motion.OS × AVE forensic recovery → evidence-backed capability graph → ownership/overlap map → autonomous editing vertical slice → benchmark gates → learning outcomes`.

Module 02 course design remains blocked until the evidence gates pass.

## Required first output from a fresh agent
Produce a compact reconstruction containing:
- sources/SHAs read;
- contradictions;
- current Motion.OS state;
- current AVE state;
- capability matrix and missing evidence;
- probable ownership boundaries;
- current P0/P1 blockers;
- status of the autonomous editing vertical slice;
- single next highest-value action.

## Evidence rules
- README/module presence is a claim, not proof.
- Unit-test count is not proof of professional editing quality.
- Render/temporal/repair claims need real end-to-end artifacts.
- Use `control-plane/CAPABILITY_AUDIT_SCHEMA.json`.
- Use `control-plane/BENCHMARK_GATES.md`.
- Use `control-plane/AUTONOMOUS_EDITING_VERTICAL_SLICE_GATE.md`.

## End-of-session persistence
Before a state-changing session ends:
- reconcile `STATE.md` / `HANDOFF.md` if needed;
- append evidence to `control-plane/EVIDENCE_LEDGER.jsonl`;
- append/supersede decisions and risks explicitly;
- write a checkpoint conforming to `control-plane/SESSION_CHECKPOINT.schema.json`.

## Module 01 note
Do not restart visual/course iteration unless a concrete learner/product defect is supplied. If publication work resumes, first verify that the exact tested student artifact equals the repo/public entrypoint; historical divergence remains an explicit risk.
