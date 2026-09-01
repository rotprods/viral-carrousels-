# /CGEV2 — MODULE 02 · AI-NATIVE VIDEO EDITING · ZERO-CONTEXT HANDOFF

Checkpoint: 2026-09-01
Authority: GitHub durable state > conversation memory.

## 0. Mission

A fresh agent must design the next training module for José Ramón after Module 01 (premium carousels / visual brand system).

The objective is **NOT** to teach Motion.OS or AVE as software projects.

Motion.OS and AVE are autonomous AI video-production/editing systems that must be audited because they may already contain most of the capabilities needed to automate professional editing.

The training must teach the student how to operate an **AI-native autonomous video editing workflow**, not how to become an engineer of AVE or Motion.OS.

## 1. Correct mental model

The target student journey is:

```text
BRIEF / INTENT
    ↓
EDITING REFERENCES
    ↓
EDIT DNA
    ↓
FOOTAGE + AUDIO + BRAND ASSETS
    ↓
EDITING.md / EDIT SYSTEM
    ↓
EXECUTABLE EDITING SKILL / AGENT
    ↓
AUTONOMOUS ROUGH CUT
    ↓
STORY + RHYTHM + B-ROLL + CAPTIONS + MOTION + SOUND + COLOR
    ↓
TEMPORAL / SEMANTIC / ART-DIRECTION QA
    ↓
AUTONOMOUS REPAIR LOOP
    ↓
EXPORT MASTER
```

The user should ultimately be able to provide:

- a brief;
- editing references;
- footage;
- dialogue / voice / music;
- logos / brand assets;
- screenshots / graphics;
- exact copy where needed;
- desired platform / aspect ratio / duration;

and have an AI system autonomously construct, evaluate, repair and export a professional edit.

## 2. Existing systems to recover first

### A. `rotprods/motion-OS`

Known North Star:

> Brief in → professional motion-design master out with autonomous research, reference intelligence, assets, composition, motion, audio, QA, graph-native repair and reproducible release.

Current durable state at checkpoint:

- GitHub source of truth active on `main`.
- Product phase: creative convergence / generalization validation.
- Release remains BLOCKED.
- Control plane is ahead of creative engine.
- Remaining P0s include production renderer verification, authoritative full-video temporal multimodal critic, and convergence to creative/semantic >=9.
- Motion.OS is therefore a **motion-design / visual-production autonomous engine**, not a training curriculum.

Canonical files to read first:

```text
README.md
GOAL.md
STATE.md
HANDOFF.md
TASKS.md
forensics/forensic_report.md
state/project_state.json
state/checkpoints.json
```

### B. `rotprods/ave`

Known North Star:

> Agent Video Editor — A2A-native AI video editing engine intended to compete functionally with Premiere Pro / After Effects / DaVinci Resolve while being agent-native.

Documented capability families include:

- timeline;
- trim / media / proxies;
- effects;
- transitions;
- transform;
- motion graphics;
- captions / transcription;
- color / ACES / HDR / LUT;
- audio / dialogue isolation / foley / surround;
- semantic editing;
- project version history;
- rendering / render queue / distributed render / farm;
- AI generation / upscaling / interpolation / removal / replacement;
- collaboration;
- export;
- MCP / SDK / OpenAPI / A2A protocol.

Durable status currently reports:

- PRODUCTION-100 structurally completed;
- 1942/1942 local tests at last recorded checkpoint;
- UI still unvalidated;
- voice loop not complete;
- real LLM dependency blocked on API configuration / credits;
- product validation remains unfinished.

Canonical files to read first:

```text
README.md
STATUS.md
PLANS/production-100/GOAL-STATE.md
docs/PROTOCOL.md
docs/AGENT_STATE_GRAPH.md
_project_intelligence/
```

AVE is therefore an **autonomous editing engine / execution substrate**, not the syllabus itself.

## 3. First task for the fresh agent

Do NOT immediately build HTML or lesson slides.

Perform a forensic capability audit of Motion.OS × AVE.

Produce a capability graph answering:

1. What can AVE actually execute today?
2. What can Motion.OS actually execute today?
3. Which capabilities overlap?
4. Which capabilities are complementary?
5. Which capabilities are aspirational / stubbed / unverified?
6. Which system should own:
   - media ingestion;
   - edit planning;
   - timeline construction;
   - captions;
   - b-roll selection;
   - motion graphics;
   - sound design;
   - color;
   - semantic editing;
   - visual QA;
   - temporal QA;
   - repair loops;
   - rendering;
   - export;
   - provenance / reproducibility?
7. What minimum integration would enable a truly autonomous edit from a real briefing and real footage?
8. Which pieces should the student see and which must remain hidden infrastructure?

## 4. Product / training boundary

### Hidden infrastructure

The student should NOT need to understand:

- A2A protocol internals;
- Kubernetes;
- render-farm implementation;
- graph persistence internals;
- OpenAPI plumbing;
- test harness internals;
- recovery state machinery;
- distributed-system architecture;
- internal benchmark governance.

Unless specifically relevant to an advanced optional lesson.

### Student-facing concepts

The student DOES need to understand:

- how to choose editing references;
- how to reverse-engineer an editing style;
- how to provide footage and assets correctly;
- how to write a good editing brief;
- how to define rhythm / story / hook / pacing;
- how to communicate desired b-roll and graphics;
- how to preserve brand identity;
- how to let the AI assemble a first cut;
- how to evaluate a cut;
- how to issue corrections semantically;
- how to use approved outputs to make future edits more consistent;
- how to export appropriately for platform and delivery.

## 5. Candidate autonomous editing model

The agent should test whether the right abstraction is:

```text
REFERENCES
    ↓
edit-dna.json
    ↓
EDITING.md
    ↓
EDITING_SKILL.md
    ↓
BRIEF + FOOTAGE + AUDIO + ASSETS
    ↓
AVE / Motion.OS execution substrate
    ↓
rough-cut.json / timeline
    ↓
render
    ↓
multimodal temporal critic
    ↓
repair loop
    ↓
final master
```

Do not assume this is correct until the repositories are audited.

## 6. Questions that must be answered before designing the course

- Can AVE ingest arbitrary real footage and create a timeline autonomously today?
- Can it inspect dialogue and select clips based on semantic content?
- Can it construct J/L cuts and pacing intentionally rather than mechanically?
- Can it search/select b-roll?
- Can it generate/position captions robustly?
- Can it perform professional sound design automatically?
- Can it perform useful color normalization / grading automatically?
- Does Motion.OS add better visual/motion composition than AVE?
- Which renderer path is actually reliable?
- Is there a real temporal critic or only frame-level QA?
- Can the system compare an edit against reference videos?
- Can it autonomously repair specific timeline defects?
- Can it preserve a human editor's style over multiple projects?
- Can we represent editing style as `edit-dna.json` + `EDITING.md`?
- Can approved edits become reusable examples / memory?
- What can be demonstrated live in a ~2h training session without faking capabilities?

## 7. Training objective

At the end of Module 02, José should be able to take a real project and operate an AI-native editing system approximately like this:

```text
1. Define what the video must achieve.
2. Collect 3–10 editing references.
3. Provide all footage + audio + brand assets.
4. Give the AI an explicit editing brief.
5. Let the system analyze media and produce an edit plan.
6. Generate a rough cut autonomously.
7. Review story / rhythm / visual treatment / sound.
8. Issue semantic corrections instead of manually rebuilding every cut.
9. Run QA.
10. Export the finished master.
11. Persist what worked so the next edit improves.
```

## 8. Likely pedagogical modules

Do not lock these until the capability audit is complete, but investigate:

```text
00 · HOW AI-NATIVE EDITING WORKS
01 · REFERENCES / EDIT DNA
02 · BRIEFING
03 · FOOTAGE + ASSET INGESTION
04 · STORY / SELECTS / EDIT PLAN
05 · AUTONOMOUS ROUGH CUT
06 · RHYTHM / B-ROLL / CAPTIONS / MOTION
07 · SOUND / MUSIC / COLOR
08 · TEMPORAL QA + REPAIR
09 · EXPORT
10 · REUSABLE EDITING SYSTEM / SKILL
```

## 9. Definition of Done for the forensic phase

Do not start designing the final HTML until all are true:

```text
Motion.OS current state reconstructed      PASS
AVE current state reconstructed            PASS
Verified capability matrix                 PASS
Aspirational/stub capability map           PASS
Overlap map                                PASS
Integration boundary                       PASS
Student-facing vs hidden boundary           PASS
Real autonomous vertical slice identified  PASS
Risks / blockers documented                PASS
Module learning outcomes locked            PASS
```

## 10. Lessons inherited from Module 01

Module 01 required too many iterations because UI and architecture were built before the student journey was fixed.

Canonical lessons:

- student journey before architecture;
- explain the entire process at the top;
- one primary action per step;
- no dead buttons;
- no duplicate prompts;
- no technical infrastructure exposed as primary UX;
- real assets over AI invention;
- output contract for every step;
- Playwright + visual QA before release;
- mobile-first;
- durable repository state instead of chat memory;
- do not call a release PASS because an element merely exists in the DOM;
- test the actual interaction and actual output.

## 11. Start command for the next chat

```text
/CGEV2-ZERO-CONTEXT-RECOVERY

Recover Module 02 from durable GitHub state only.
Read this handoff first:
rotprods/viral-carrousels-/handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md

Then forensically recover:
- rotprods/motion-OS
- rotprods/ave

Do not treat Motion.OS or AVE as the training itself. They are autonomous AI video editing / motion-production engines to audit as potential execution substrates.

Reconstruct their real verified capabilities, identify stubs vs production functions, create the Motion.OS × AVE capability graph, define the minimum autonomous editing vertical slice, and only then design José Ramón's AI-native video editing training.
```

## 12. Governing rule

**The new chat must not rely on this conversation for continuity. GitHub durable state is authoritative.**
