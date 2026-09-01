# AUTHORITY GRAPH

## Purpose
Resolve contradictions deterministically across training state, execution engines, artifacts and conversation history.

## Authority order
1. Repository-specific canonical state on `main` (`GOAL.md`, `STATE.md`, `HANDOFF.md`, tested code, release manifests).
2. Verified CI / QA / render evidence tied to an exact commit SHA.
3. Generated artifacts whose provenance points to an exact commit/run.
4. Append-only decision/evidence ledgers in this control plane.
5. Conversation memory and historical prose.

## Repository ownership
- `rotprods/viral-carrousels-`: training/control-plane truth.
- `rotprods/motion-OS`: autonomous motion-design engine truth.
- `rotprods/ave`: autonomous video-editor engine truth.

## Conflict resolution
When two sources disagree:
1. identify the claim;
2. record both sources;
3. prefer the source with higher authority and newer verified evidence;
4. if verification is absent, mark `UNRESOLVED`;
5. never silently overwrite the losing claim;
6. append the resolution to `control-plane/EVIDENCE_LEDGER.jsonl` and, if architectural, `control-plane/DECISIONS.md`.

## Product boundary
Student-facing truth is what has passed the exact artifact's release gates. Engine READMEs are capability claims until corroborated by code/tests/renders.
