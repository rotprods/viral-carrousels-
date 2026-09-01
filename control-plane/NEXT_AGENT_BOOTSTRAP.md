# NEXT AGENT BOOTSTRAP — /COS-GRAPH-ENGINE-V2+

You are a zero-context agent. Do not trust conversational memory.

## Mission
Reconstruct the AI-native creative training program and advance Module 02: autonomous AI video editing.

## Mandatory boot sequence
1. Read `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.md`.
2. Read `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.json`.
3. Read `control-plane/AUTHORITY_GRAPH.md`.
4. Read `control-plane/RECOVERY_PROTOCOL.md`.
5. Read `control-plane/DECISIONS.md` and `control-plane/RISKS.md`.
6. Read `AGENTS.md`, `GOAL.md`, `STATE.md`, `HANDOFF.md`, `CHANGELOG.md`.
7. Read `handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md`.
8. Recover `rotprods/motion-OS` from its canonical state files.
9. Recover `rotprods/ave` from its canonical state files.
10. Audit real capabilities using `control-plane/CAPABILITY_AUDIT_SCHEMA.json`.

## Non-negotiable interpretation
- Motion.OS and AVE are autonomous execution engines, not the syllabus.
- Documentation lists are claims until supported by code/tests/renders.
- Module 02 design is BLOCKED until the capability audit DoD passes.
- A passing unit suite does not prove professional editing quality.
- The target is a real vertical slice: brief + references + footage + audio + assets → autonomous edit → temporal/semantic/art-direction QA → repair → export.

## Required first output
Produce one compact state reconstruction containing:
- authoritative sources read;
- contradictions;
- current Motion.OS state;
- current AVE state;
- verified capability matrix;
- missing evidence;
- likely ownership boundaries;
- P0/P1 blockers;
- minimum autonomous editing vertical slice;
- single next highest-value action.

Do not build HTML yet.

## Persistence contract
Before ending the session, write/update a checkpoint conforming to `control-plane/SESSION_CHECKPOINT.schema.json` and append evidence/decisions/risks if state changed.
