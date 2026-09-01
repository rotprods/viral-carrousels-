# /COS-GRAPH-ENGINE-V2 — MASTER CONTINUITY CHECKPOINT

Checkpoint: 2026-09-01 Europe/Madrid
Authority rule: durable GitHub state > generated artifacts > conversation memory.
Purpose: allow a zero-context agent to reconstruct the entire current project state if the current agent/chat disappears.

---

## 0. Mission graph

This project is not a single HTML file. It is a training + execution-system program with two active modules:

```text
PROGRAM: AI-NATIVE CREATIVE SYSTEMS TRAINING
│
├── MODULE 01 · VIRAL CAROUSELS / VISUAL BRAND SYSTEM
│   ├── references / Pinterest
│   ├── Extractor ADN Visual v2
│   ├── visual-dna.json
│   ├── DESIGN.md
│   ├── SKILL.md
│   ├── templates T01–T09
│   ├── briefing + assets
│   ├── generation
│   ├── QA / repair
│   └── portable runtime adapters
│
└── MODULE 02 · AI-NATIVE AUTONOMOUS VIDEO EDITING
    ├── Motion.OS forensic recovery
    ├── AVE forensic recovery
    ├── capability graph
    ├── autonomous editing vertical slice
    ├── edit-dna.json hypothesis
    ├── EDITING.md hypothesis
    ├── editing skill / agent
    └── training design only AFTER capability audit
```

The student-facing training and the autonomous execution engines are separate layers.

---

## 1. Canonical repositories

### Training / control-plane repo

`rotprods/viral-carrousels-`

Purpose:
- Module 01 durable state;
- prompts P00–P17;
- templates;
- skill/adapters;
- QA;
- versioning;
- training handoffs;
- future Module 02 continuity.

Canonical files already present:

```text
AGENTS.md
GOAL.md
STATE.md
HANDOFF.md
CHANGELOG.md
README.md
prompts/PROMPTS.md
templates/DESIGN.template.md
templates/visual-dna.template.json
templates/WORKBOOK.md
skills/visual-brand-system/SKILL.md
adapters/CODEX.md
adapters/CLAUDE_CODE.md
adapters/HIGGSFIELD_SUPERCOMPUTER.md
qa/RELEASE_GATES.md
scripts/qa.py
tests/pages.spec.js
versions/manifest.json
handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md
```

### Motion engine

`rotprods/motion-OS`

Durable North Star:

> Brief in → professional motion-design master out with autonomous research, reference intelligence, assets, composition, motion, audio, QA, graph-native repair and reproducible release.

Current known durable product truth:
- release BLOCKED;
- control plane ahead of creative engine;
- creative convergence / generalization validation;
- production renderer verification remains P0;
- authoritative temporal multimodal critic remains P0;
- creative/semantic release threshold not yet met.

This is an execution substrate, NOT the training syllabus.

### Autonomous video editor

`rotprods/ave`

Durable North Star:

> Agent Video Editor — agent-native editing engine targeting the functional space of Premiere / After Effects / Resolve.

Documented capability families:
- timeline;
- media ingest / proxies;
- trim / transforms;
- transitions / effects;
- captions / transcription;
- semantic editing;
- motion graphics;
- color / ACES / HDR / LUT;
- audio / dialogue / foley / surround;
- rendering / queue / distributed render;
- export;
- project versioning;
- MCP / SDK / OpenAPI / A2A;
- multiple AI media operations.

Current known durable product truth:
- PRODUCTION-100 structurally completed in historical status;
- 1942/1942 local tests reported at last checkpoint;
- UI not fully validated;
- voice loop incomplete;
- real LLM integration requires configured API dependency;
- product validation incomplete.

AVE is an execution substrate, NOT the training syllabus.

---

## 2. Module 01 — product truth

### Correct student mental model

```text
PINTEREST / VISUAL REFERENCES
        ↓
EXTRACTOR ADN VISUAL v2
        ↓
visual-dna.json
        ↓
DESIGN COMPILER
        ↓
DESIGN.md
        ↓
SKILL COMPILER
        ↓
SKILL.md
        ↓
BRIEFING + COPY + BRAND ASSETS + VISUAL ASSETS + REFERENCES
        ↓
CARRUSEL
        ↓
QA / REPAIR
        ↓
REUSABLE BRAND SYSTEM
```

This sequence MUST be obvious immediately to a new student.

### External tool

Extractor ADN Visual v2:

`https://chatgpt.com/g/g-697fac8775c081919387509ec73c69a5-extractor-adn-visual-v2`

### Prompt OS

Canonical prompt IDs: `P00` through `P17`.

Important prompts include:
- P02: references → Visual DNA;
- P03: JSON → traceable DESIGN.md;
- P13: DESIGN.md + JSON → SKILL.md;
- P14: runtime adapter;
- P15: execute Brand System;
- P16: learn from approved outputs;
- P17: release audit.

Do not duplicate prompt bodies in multiple UI locations. `prompts/PROMPTS.md` should remain the canonical prompt source in the repo.

### Template OS

Primary visual families: `T01–T09`.

A template is a visual grammar, not an image to copy literally.

Correct UX:
- select one template;
- one global CTA;
- recipe associated with selected template;
- do not render 18 redundant per-card buttons.

---

## 3. Module 01 — HTML history and hard lessons

Many iterations occurred because implementation began before the student journey was fully locked.

Hard-earned invariants:

1. Student journey before architecture.
2. Explain the whole process near the top.
3. Maximum one primary action per step.
4. No dead buttons.
5. No misleading controls.
6. No duplicate actions.
7. No duplicated prompts as separate sources of truth.
8. Technical infrastructure must not dominate student UX.
9. Real assets should be supplied instead of asking AI to invent brand-critical content.
10. Each step requires: INPUT → ACTION → OUTPUT → NEXT.
11. Images must be visibly present, not merely registered in JS.
12. Do not use transparent placeholders + hydration for standalone course HTML.
13. Copy tests must verify actual clipboard/paste text, not only `COPIADO ✓` UI.
14. Responsive QA must inspect child intrinsic widths, not only document width.
15. Playwright + visual inspection are release gates.
16. `PASS` means the exact delivered artifact was tested.
17. Future changes should be subtractive unless a demonstrated learner gap requires new functionality.

### Major bugs previously found and fixed locally

- export panel visible by default as a bottom-right square;
- fixed/sticky controls covering content;
- mobile grids producing >1000px intrinsic children while document overflow was hidden;
- System three-layer block clipping on mobile;
- redundant runtime/tool sections;
- misleading `USE TEMPLATE` buttons all routing to P00;
- excessive duplicate prompt controls;
- broken image architecture in v7 due to JS asset hydration;
- missing export engine in older versions;
- mismatch between UI prompt count and P00–P17 reality.

Do not reintroduce these.

---

## 4. Latest Module 01 visual artifact state

The strongest locally validated HTML from this session is conceptually:

`MODULE_01_AI_SLOP_TO_BRAND_SYSTEM_FINAL_VISION_QA.html`

It was tested with Playwright / vision at mobile and desktop sizes and included fixes for:
- hidden export modal by default;
- mobile layout containment;
- reduced sticky/floating noise;
- compact technical sections;
- 18-prompt labeling;
- actual template selection;
- student flow clarity.

IMPORTANT:
The repo's current `docs/index.html` historically lagged behind this final local course. Do NOT assume the current GitHub Pages entrypoint equals the strongest local build unless verified by hash/content.

---

## 5. Hosting / publication state

### GitHub Pages

Repository has workflows for:
- static QA;
- Browser QA;
- Pages deploy.

Historical state:
- Browser QA on `main` passed;
- GitHub Pages administrative activation was still blocked because the Actions token could not create/enable the Pages site;
- repository metadata previously reported `has_pages: false`;
- a release branch `release/pages-course-v1` was created;
- a site bundle upload/reconstruction approach was explored because the connector could not directly upload local binary assets conveniently.

DO NOT treat Pages as production until:

```text
latest course == deployed index.html
static QA PASS
Playwright PASS
Pages enabled
public URL resolves
```

### ChatGPT Sites

Desired product direction was considered:
- Site = student product;
- GitHub = source/control plane.

However, this conversation did not have a direct ChatGPT Sites publishing connector. No public ChatGPT Site URL was created here.

### Vercel

Vercel connector exists in this environment and may be used as a fallback static host if Pages remains administratively blocked.

---

## 6. Module 02 — actual mission

The next training module is **AI-native autonomous video editing**.

Clarification:

Motion.OS and AVE are NOT the curriculum.

They are candidate autonomous production/editing engines whose verified capabilities must be mapped first.

The student should eventually be able to provide:

```text
BRIEF
+ EDITING REFERENCES
+ FOOTAGE
+ AUDIO
+ LOGOS / BRAND ASSETS
+ SCREENSHOTS / GRAPHICS
+ EXACT COPY WHERE NEEDED
+ PLATFORM / RATIO / DURATION
        ↓
AI EDITING SYSTEM
        ↓
EDIT PLAN
        ↓
AUTONOMOUS ROUGH CUT
        ↓
STORY / RHYTHM / B-ROLL / CAPTIONS / MOTION
        ↓
SOUND / COLOR / POLISH
        ↓
TEMPORAL + SEMANTIC + ART-DIRECTION QA
        ↓
AUTONOMOUS REPAIR
        ↓
MASTER EXPORT
```

The training should teach how to operate this workflow, not how to implement Kubernetes, A2A or renderer internals.

---

## 7. Module 02 — mandatory forensic phase

Before designing slides/HTML/course content, a fresh agent MUST audit Motion.OS × AVE and produce a capability graph.

Required questions:

1. What can AVE actually execute today?
2. What can Motion.OS actually execute today?
3. What is verified vs stubbed vs aspirational?
4. Which owns media ingest?
5. Which owns dialogue/semantic analysis?
6. Which owns selects?
7. Which owns timeline construction?
8. Can either create intentional J/L cuts?
9. Can either control pacing from references?
10. Can either choose/use b-roll?
11. Can either create captions robustly?
12. Can either perform useful sound design?
13. Can either normalize/grade color?
14. Which owns motion graphics?
15. Which renderer paths are real and reliable?
16. Is there a true full-video temporal critic?
17. Can the critic compare against editing references?
18. Can the system autonomously repair timeline defects?
19. Can approved edits become reusable memory/style evidence?
20. Can editing style be represented as `edit-dna.json + EDITING.md`?
21. What minimum integration yields a real autonomous vertical slice?
22. What can be demonstrated honestly in a ~2h training session?

### Forensic Definition of Done

```text
Motion.OS state reconstructed             PASS
AVE state reconstructed                   PASS
verified capability matrix                PASS
stub/aspirational map                     PASS
overlap graph                             PASS
ownership boundaries                      PASS
minimum autonomous vertical slice         PASS
student-facing vs hidden infrastructure   PASS
blockers documented                       PASS
learning outcomes locked                  PASS
```

Only after this may the course be designed.

---

## 8. Candidate Module 02 graph — HYPOTHESIS ONLY

Do not treat as confirmed until repo audit:

```text
EDITING REFERENCES
      ↓
edit-dna.json
      ↓
EDITING.md
      ↓
EDITING_SKILL.md
      ↓
BRIEF + FOOTAGE + AUDIO + ASSETS
      ↓
AVE / Motion.OS execution layer
      ↓
rough-cut timeline
      ↓
render
      ↓
temporal multimodal critic
      ↓
repair loop
      ↓
master
```

Possible student-facing chapters:

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

Again: hypothesis only.

---

## 9. Source-of-truth graph

```text
GitHub
├── viral-carrousels-  → training/control-plane truth
├── motion-OS          → motion engine software truth
└── ave                → autonomous editor software truth

Heavy generated artifacts / screenshots / local HTML
→ local or Drive artifacts only
→ never override GitHub state silently

Conversation memory
→ convenience only
→ NEVER authoritative
```

If contradictions appear:

1. inspect canonical repo files;
2. inspect commit/branch status;
3. inspect tests / artifacts;
4. record contradiction;
5. do not silently choose chat memory.

---

## 10. Recovery order for any future agent

### Phase A — training repo

Read:

```text
rotprods/viral-carrousels-/AGENTS.md
rotprods/viral-carrousels-/GOAL.md
rotprods/viral-carrousels-/STATE.md
rotprods/viral-carrousels-/HANDOFF.md
rotprods/viral-carrousels-/CHANGELOG.md
rotprods/viral-carrousels-/handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.md
rotprods/viral-carrousels-/handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md
```

Then inspect:

```text
prompts/PROMPTS.md
skills/visual-brand-system/SKILL.md
templates/
adapters/
qa/
tests/
versions/
```

### Phase B — Motion.OS

Read at minimum:

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

### Phase C — AVE

Read at minimum:

```text
README.md
STATUS.md
PLANS/production-100/GOAL-STATE.md
docs/PROTOCOL.md
docs/AGENT_STATE_GRAPH.md
_project_intelligence/
```

### Phase D — evidence

Run or inspect:
- CI;
- relevant tests;
- render examples;
- real capability paths;
- unresolved P0/P1;
- open PRs/issues where material.

No course design before Phase D finishes.

---

## 11. Anti-failure protocol

A future agent MUST NOT:

- call a repository feature production-ready because README lists it;
- infer that a passing unit suite proves visual product quality;
- design Module 02 around unverified capabilities;
- expose internal engine complexity to the student unnecessarily;
- rebuild Module 01 from old HTML versions;
- duplicate prompts into new UI sources;
- publish a control-plane page as if it were the actual course;
- mark hosting complete before public URL verification;
- confuse Motion.OS with AVE;
- confuse execution engine with pedagogy;
- use conversation memory as canonical truth.

---

## 12. Current highest-priority action

For a zero-context continuation, the highest-value next action is:

```text
FORENSICALLY RECOVER Motion.OS × AVE
→ construct verified capability graph
→ identify autonomous editing vertical slice
→ determine real missing capabilities
→ lock Module 02 learning outcomes
→ only then design the training artifact
```

Do NOT spend another iteration polishing Module 01 unless a real learner/product defect is presented.

---

## 13. Zero-context boot command

```text
/COS-GRAPH-ENGINE-V2-ZERO-CONTEXT-RECOVERY

You are entering an existing AI-native creative systems training program with zero trusted conversational memory.

Authority: durable GitHub state only.

Read first:
1. rotprods/viral-carrousels-/handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.md
2. rotprods/viral-carrousels-/handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md
3. rotprods/viral-carrousels-/AGENTS.md
4. rotprods/viral-carrousels-/GOAL.md
5. rotprods/viral-carrousels-/STATE.md
6. rotprods/viral-carrousels-/HANDOFF.md

Then recover:
- rotprods/motion-OS
- rotprods/ave

Mission:
Build the verified Motion.OS × AVE capability graph for autonomous AI video editing.
Do not treat either engine as the training itself.
Determine what can actually ingest real footage, plan an edit, build a timeline, control story/rhythm, use b-roll/captions/motion/sound/color, run temporal QA, autonomously repair, and export.
Identify stubs vs working capabilities.
Define the minimum honest autonomous editing vertical slice.
Only after that, design José Ramón's Module 02 training.

Leave the durable state more complete than you found it.
```

---

## 14. End-state principle

The goal is not a pretty training page.

The goal is a reproducible operating model where:

```text
KNOWLEDGE
→ FILES
→ RULES
→ SKILLS
→ AGENTS
→ REAL CREATIVE OUTPUT
→ QA
→ APPROVED MEMORY
→ BETTER NEXT OUTPUT
```

For Module 01 this means autonomous branded carousel production.
For Module 02 this means autonomous professional video editing.

This file exists so the program survives the current chat and current agent.
