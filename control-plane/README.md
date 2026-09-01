# COS GRAPH ENGINE V2+ — CONTROL PLANE

## Purpose
This directory is the operational control plane for the AI-native creative systems training program. It exists so a zero-context agent can recover truth, distinguish claims from evidence, identify the active gate and continue without relying on chat memory.

## Core execution graph

```text
CLAIM
  ↓
EVIDENCE
  ↓
VERIFICATION STATUS
  ↓
DECISION / RISK
  ↓
CHECKPOINT
  ↓
NEXT HIGHEST-VALUE ACTION
```

## Files
- `AUTHORITY_GRAPH.md` — source hierarchy and conflict resolution.
- `RECOVERY_PROTOCOL.md` — deterministic zero-context recovery algorithm.
- `NEXT_AGENT_BOOTSTRAP.md` — minimum boot sequence and required first output.
- `CAPABILITY_AUDIT_SCHEMA.json` — evidence-backed capability record for Motion.OS × AVE.
- `BENCHMARK_GATES.md` — gates that prevent capability/release theater.
- `AUTONOMOUS_EDITING_VERTICAL_SLICE_GATE.md` — exact end-to-end proof required before claiming autonomous editing.
- `DECISIONS.md` — append-only architectural decisions.
- `RISKS.md` — active risk register.
- `EVIDENCE_LEDGER.jsonl` — append-only event/evidence stream. This is also the canonical event ledger; do not create a second generic event log.
- `SESSION_CHECKPOINT.schema.json` — schema for every session checkpoint.
- `checkpoints/` — durable point-in-time recovery records.

## Current active gate
Module 02 is in **FORENSIC CAPABILITY AUDIT**. Course design remains blocked until Motion.OS × AVE capabilities and the minimum autonomous editing vertical slice are verified with code/test/render evidence.

## Repository roles
- `rotprods/viral-carrousels-` — training/control-plane truth.
- `rotprods/motion-OS` — motion-design engine truth.
- `rotprods/ave` — autonomous editing engine truth.

## Mutation contract
A state-changing agent session must:
1. recover from durable state;
2. identify contradictions;
3. execute the smallest coherent highest-value action;
4. attach evidence to capability/release claims;
5. update decisions/risks when materially changed;
6. reconcile `STATE.md` and `HANDOFF.md`;
7. append to `EVIDENCE_LEDGER.jsonl`;
8. write a checkpoint conforming to `SESSION_CHECKPOINT.schema.json`.

## Anti-overengineering
Do not add another ledger, graph layer, database or abstraction unless it closes an active P0/P1 or materially reduces recovery time / improves measured creative output. The control plane is a means to production evidence, not the product itself.
