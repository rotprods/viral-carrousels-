# ZERO-CONTEXT RECOVERY PROTOCOL

## Objective
A fresh agent must reconstruct the current operational state without asking the human to repeat durable information.

## Phase 0 — Identity
Confirm repository, default branch and current commit SHA. Do not assume historical counts are current.

## Phase 1 — Program control plane
Read, in order:
1. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.md`
2. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.json`
3. `control-plane/AUTHORITY_GRAPH.md`
4. `AGENTS.md`
5. `GOAL.md`
6. `STATE.md`
7. `HANDOFF.md`
8. `CHANGELOG.md`
9. `handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md`

## Phase 2 — Cross-repository recovery
Recover `rotprods/motion-OS` and `rotprods/ave` from their own durable files. Treat documentation as claims until corroborated.

## Phase 3 — Evidence
Inspect tests, CI, renders, current open P0/P1, relevant issues/PRs and real code paths. Build a claim table with status: `VERIFIED`, `PARTIAL`, `STUB`, `ASPIRATIONAL`, `BLOCKED`, `UNKNOWN`.

## Phase 4 — Reconciliation
Produce:
- authority/conflict report;
- current North Star;
- active wave/gate;
- verified capability graph;
- blockers;
- next highest-value action.

## Phase 5 — Execution gate
Do not design Module 02 training until Motion.OS × AVE forensic capability audit passes its DoD.

## Phase 6 — Persistence
Before ending any state-changing session:
- update canonical state;
- append evidence/decision/risk entries;
- write a session checkpoint;
- leave a heartbeat even if no material state changed.

## Recovery success criteria
A fresh agent can answer: what this program is, what is authoritative, what is complete, what is blocked, what is hypothesis, what must happen next, and why — without using chat memory.
