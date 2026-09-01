# AUTONOMOUS EDITING VERTICAL SLICE GATE

**Status: NOT YET VERIFIED.**

This document defines the minimum proof required before the program may claim that Motion.OS × AVE (or either engine independently) can autonomously edit real video.

## Input contract
Use a small but real production package:
- explicit video brief / objective;
- 3–10 editing references where available;
- multiple real source clips, not a preassembled timeline;
- dialogue/audio where applicable;
- music or music-selection constraints;
- logo / brand assets;
- screenshots / graphics if required;
- exact copy for text that must be preserved;
- target platform, aspect ratio, duration and export specification.

## Required pipeline

```text
INGEST REAL MEDIA
→ INDEX / TRANSCRIBE / UNDERSTAND
→ SELECT USABLE MOMENTS
→ EDIT PLAN / STORY STRUCTURE
→ BUILD TIMELINE
→ ROUGH CUT
→ B-ROLL / CAPTIONS / MOTION AS REQUIRED
→ AUDIO / MUSIC / MIX
→ COLOR / NORMALIZATION AS REQUIRED
→ RENDER V1
→ FULL-VIDEO TEMPORAL + SEMANTIC + ART-DIRECTION CRITIC
→ TARGETED REPAIR
→ RENDER V2
→ EXPORT MASTER
→ PROVENANCE MANIFEST
```

## Required artifacts
- input manifest with hashes/metadata;
- semantic media index/transcript where applicable;
- selects/edit-plan artifact;
- machine-readable timeline/project artifact;
- V1 render;
- critic report tied to V1;
- repair plan identifying exact temporal regions/parameters;
- changed timeline/project artifact;
- V2 render;
- comparison/QA result;
- final export;
- run manifest with engine versions + Git SHAs + dependencies.

## Pass criteria
1. The system receives raw source media rather than a human-built final timeline.
2. At least one material editorial decision is autonomous and evidenced (select, order, cut timing, b-roll placement, caption/motion decision, audio decision, etc.).
3. V1 is a playable non-empty video with coherent timeline semantics.
4. QA evaluates the complete temporal artifact.
5. At least one QA finding triggers a targeted autonomous repair.
6. V2 preserves unrelated correct regions while changing the targeted defect.
7. Final master exports successfully to the requested delivery spec.
8. Every major output can be traced to an exact run/commit/input set.
9. Human review confirms the result is not merely technically valid but plausibly usable as an edit candidate.

## Automatic FAIL conditions
- mocked/stubbed renderer used as final evidence;
- pre-edited input masquerading as autonomous editing;
- only unit tests / JSON validation, no rendered output;
- frame-only QA presented as full temporal QA;
- repair is a full random regeneration with no causal link to critic findings;
- human secretly performs the key edit while system receives the result;
- capability inferred from README/module name only.

## Ownership to determine during audit
For each stage identify `motion-OS`, `ave`, `shared`, `external` or `unknown` ownership with evidence.

## Student boundary
The vertical slice is infrastructure evidence. The eventual student should see only the useful operating abstraction: provide brief/references/media/assets, review first cut, communicate semantic changes, approve/export. Engine plumbing remains hidden unless it directly helps operation.
