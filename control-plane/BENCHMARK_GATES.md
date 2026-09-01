# BENCHMARK GATES — MODULE 02 AUTONOMOUS VIDEO EDITING

No gate may pass from README claims alone. Evidence must point to exact code/test/render/run/commit artifacts.

## G0 — Recovery integrity
PASS only if a fresh agent can reconstruct:
- program North Star;
- authority order;
- current Motion.OS state;
- current AVE state;
- active P0/P1 blockers;
- current execution gate;
- next highest-value action;
without conversation memory.

## G1 — Capability audit completeness
PASS only if every capability needed by the autonomous editing path has:
- stable capability ID;
- likely owner;
- VERIFIED/PARTIAL/STUB/ASPIRATIONAL/BLOCKED/UNKNOWN status;
- evidence references;
- inputs/outputs/dependencies;
- blockers;
- CORE/OPTIONAL/HIDDEN_INFRA student visibility.

Required domains include media ingest, transcription/semantic analysis, selects, timeline construction, pacing/J-L cuts, b-roll, captions, motion graphics, audio, color, rendering, temporal QA, repair and export.

## G2 — Autonomous vertical slice
PASS only when the exact vertical slice defined in `AUTONOMOUS_EDITING_VERTICAL_SLICE_GATE.md` runs end-to-end on real media and produces non-empty provenance-linked artifacts.

Unit tests alone cannot pass G2.

## G3 — Creative / temporal quality
PASS only when the rendered edit is evaluated as a whole video, not merely frame-by-frame. Evidence must cover at least:
- narrative/semantic coherence;
- hook and pacing;
- timing of cuts;
- dialogue continuity;
- reference/style adherence;
- b-roll relevance;
- caption readability/timing;
- audio balance/sound-design appropriateness;
- visual hierarchy/motion quality;
- color consistency;
- artifact/error detection.

A quality threshold for the integrated engine must be calibrated from real benchmark outputs. Do not invent a numeric threshold. Motion.OS may retain its own internal >=9 release threshold independently.

## G4 — Autonomous repair
PASS only if the critic can identify a concrete temporal/edit defect and the system can produce a targeted repair without rebuilding unrelated correct regions.

Required evidence:
`render_v1 → critic finding → repair plan → changed timeline/parameters → render_v2 → critic improvement`.

## G5 — Student abstraction readiness
PASS only if verified engine capabilities can be expressed as a human operating model without exposing implementation plumbing as required learning.

The student-facing path must be reducible approximately to:
`brief + references + footage/audio/assets → edit system → autonomous first cut → semantic corrections → QA → export`.

## G6 — Training artifact release
Only after G0–G5 pass may final Module 02 training artifacts be declared release candidates. They then require their own exact-artifact functional, responsive and visual QA.

## Failure rule
A failed or missing gate remains explicit. Never substitute architecture breadth, test count, module count or documentation completeness for end-to-end editing evidence.
