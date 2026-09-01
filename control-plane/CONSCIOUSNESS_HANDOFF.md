# CONSCIOUSNESS HANDOFF — /CGEV2

Checkpoint: 2026-09-01 18:14 Europe/Madrid
Purpose: preserve the operative state, hard-won lessons, intent and next mission so a zero-context agent can recover the program without this chat.

## 1. Mission frame

This repository is the durable control plane for an AI-native creative training program.

Current program state:

- Module 01 — Premium Carousels / `Pinterest → Visual DNA → DESIGN.md → SKILL → assets + briefing → generation → QA` — **FROZEN / GOOD ENOUGH**.
- Module 02 — AI-native autonomous video editing — **NEXT ACTIVE MISSION**.

Do not reopen Module 01 for invisible engineering hygiene unless a real learner-facing bug appears. The human is explicitly finished with the iteration loop around hosting/Pages/CI polish.

## 2. Core distinction for Module 02

`rotprods/motion-OS` and `rotprods/ave` are **not the training**.

They are candidate autonomous execution engines / capability sources for professional AI video editing and motion production.

The learner-facing goal is not “learn AVE” or “learn Motion.OS”.

The target capability is:

`brief + references + footage + audio + brand assets → autonomous edit → temporal/semantic/art-direction QA → repair → export`

The training should teach a human how to operate that paradigm, while hiding internal engine complexity unless it directly helps execution.

## 3. Authority rule

Durable GitHub evidence > tests / real renders / runtime outputs > generated artifacts > conversation memory > assumptions.

A README or status file is a claim until corroborated by code, tests and preferably real rendered output.

## 4. Mandatory recovery order

A zero-context agent should read, in order:

1. `control-plane/CONSCIOUSNESS_HANDOFF.md` — this file.
2. `control-plane/CONSCIOUSNESS_HANDOFF.json`.
3. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.md`.
4. `handoffs/COS_GRAPH_ENGINE_V2_MASTER_CHECKPOINT_2026-09-01.json`.
5. `handoffs/MODULE_02_VIDEO_AI_CGEV2_ZERO_CONTEXT.md`.
6. `control-plane/AUTHORITY_GRAPH.md`.
7. `control-plane/RECOVERY_PROTOCOL.md`.
8. `control-plane/DECISIONS.md`.
9. `control-plane/RISKS.md`.
10. `control-plane/EVIDENCE_LEDGER.jsonl`.
11. `control-plane/BENCHMARK_GATES.md`.
12. `control-plane/AUTONOMOUS_EDITING_VERTICAL_SLICE_GATE.md`.
13. `AGENTS.md`, `GOAL.md`, `STATE.md`, `HANDOFF.md`, `CHANGELOG.md`.
14. Recover `rotprods/motion-OS` from its durable state and source tree.
15. Recover `rotprods/ave` from its durable state and source tree.

## 5. Module 01 — what actually matters

The high-value learner workflow discovered through the carousel project is:

`references → structured DNA → human-readable system rules → executable skill → real assets + briefing → generation → QA → reuse`

The exact Module 01 form is:

`Pinterest → Extractor ADN Visual v2 → visual-dna.json → DESIGN.md → SKILL.md → briefing + assets → carousel → QA`

The reusable learning pattern is more important than the HTML implementation.

### Hard-won lessons

1. **Student journey before architecture.** The learner must understand what to do in the first 30–60 seconds.
2. **One primary action per step.** Avoid duplicate CTAs, internal IDs and technical navigation dominating UX.
3. **No dead or misleading controls.** Every button needs action → observable result → success/failure state.
4. **Infrastructure is not UX.** Repos, manifests, ledgers, adapters, CI and graph internals stay behind the learner-facing product.
5. **Do not make AI invent source assets that can be supplied.** Faces, products, footage, logos, screenshots, audio and brand assets should be attached when available.
6. **Browser + visual QA beats structural QA alone.** Real bugs previously passed DOM/static checks while layouts were visually broken.
7. **Mobile-first.** Training is likely to be consumed on phones.
8. **Stop when good enough.** Do not turn teaching material into an infinite engineering exercise.
9. **Do not build UI before the learning graph is clear.** This was the major source of the long Module 01 iteration loop.
10. **Anti-overengineering is a permanent gate.** A new layer must materially improve learning, execution, reliability, portability or quality.

## 6. Module 01 current closure state

Module 01 is closed operationally.

- Repository Static QA: green after scope reconciliation.
- Repository Browser QA: green after scope reconciliation.
- GitHub Pages deployment is deliberately manual and not on the critical path.
- Historical image-heavy HTML exists in Library and has been fingerprinted, but synchronizing it to a public production entrypoint is **not a current priority**.
- Do not spend more time on Pages/hosting unless explicitly requested again.

## 7. Module 02 north star

Create the best possible training for **AI-native autonomous video editing**, based on what the real engines can actually do.

The likely learner mental model is:

`REFERENCES + EDIT DNA + EDITING.md + EDIT SKILL + FOOTAGE/AUDIO/BRAND ASSETS/BRIEF = PROFESSIONAL AI-NATIVE EDIT → TEMPORAL QA → REPAIR → MASTER`

Do not assume this exact model is final until the capability audit finishes.

## 8. Required Motion.OS × AVE forensic audit

For each major capability classify as:

- `VERIFIED_PRODUCTION`
- `VERIFIED_PARTIAL`
- `TEST_ONLY`
- `STUB`
- `ASPIRATIONAL`
- `BLOCKED_EXTERNAL`
- `UNKNOWN`

Audit at minimum:

- media ingest / proxies / transcripts / semantic indexing;
- reference intelligence / edit-style reverse engineering;
- planning / selects / storyboard / EDL / timeline planning;
- autonomous clip selection, trim, sequencing, rough cut, J/L cuts, pacing, b-roll, speaker cuts, reframing;
- captions, typography, motion, overlays, transitions;
- dialogue cleanup, music, beat alignment, ducking, SFX, loudness;
- normalization, grading, LUT/look matching, shot consistency;
- temporal QA, narrative coherence, continuity, pacing, sync, brand consistency;
- autonomous repair loop;
- export / codecs / aspect ratios / batch variants.

## 9. Core question before curriculum

Can Motion.OS × AVE today execute a meaningful autonomous editing vertical slice on real media?

Candidate minimum:

`brief → ingest → understand → select → rough cut → pacing → b-roll/captions → sound → basic color/look → temporal QA → repair → export`

For each stage identify:

- engine owner;
- implementation path;
- evidence;
- confidence;
- blockers;
- whether learner exposure is needed;
- human fallback.

## 10. Curriculum gate

Do **not** build the new HTML/site first.

Required order:

1. zero-context recovery;
2. Motion.OS forensic audit;
3. AVE forensic audit;
4. cross-repo capability graph;
5. autonomous editing readiness verdict;
6. minimum working vertical slice;
7. learning outcomes;
8. learner Golden Path;
9. examples/assets/exercises;
10. only then training interface / HTML / site.

## 11. Pedagogical target

The learner should finish able to say:

> “I can give an AI editing system a professional briefing, references, footage and assets; get a strong first edit; evaluate temporal quality; repair weaknesses; export the master; and reuse the system.”

Avoid API-documentation tone. Use natural Spanish. Every section should ideally answer:

- qué vamos a hacer;
- por qué;
- qué necesitas;
- qué le das a la IA;
- qué debe devolverte;
- qué compruebas;
- cuál es el siguiente paso.

## 12. Likely training scope

Original Class 1 context combined Premium Carousels + Video Editing and was approximately 2 hours total. Module 02 should therefore remain compact unless evidence justifies otherwise.

Target expectation:

- roughly 45–75 minutes explanation;
- one guided practical exercise;
- ideally one real short-form video + one alternate version.

## 13. Persistent operating loop

Every meaningful iteration:

`READ → RECONSTRUCT → VERIFY → MAP → DECIDE → IMPLEMENT → TEST → ADVERSARIAL REVIEW → SIMPLIFY → PERSIST`

Never:

`ASSUME → BUILD → PATCH → PATCH → PATCH`

## 14. Highest-priority next action

Start a fresh chat and run `/CGEV2-VIDEO-TRAINING-ZERO-CONTEXT-V1`.

The first execution should recover durable state and forensically audit Motion.OS and AVE. It should **not** build HTML.

The first useful answer should contain:

- recovered state;
- Motion.OS reality;
- AVE reality;
- Motion.OS × AVE capability graph;
- autonomous editing readiness;
- P0/P1/P2 gaps;
- minimum working autonomous editor;
- implications for the training;
- single next executable action.

## 15. Human intent / working preference relevant to this project

The human wants professional output quickly, with deep thinking but without unnecessary iteration. The system should protect against both superficial work and overengineering. When the learner-facing goal is met, stop. Prefer verified execution over ornamental architecture.

## 16. Recovery success condition

A future agent has recovered correctly when it can continue Module 02 without asking the human to restate:

- what Module 01 taught us;
- why Motion.OS and AVE matter;
- why they are not the syllabus;
- what must be audited;
- what the vertical-slice goal is;
- why HTML is gated;
- what must be persisted before ending the next session.
