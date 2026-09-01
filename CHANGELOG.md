# CHANGELOG

## [0.2.1] — CI / Pages reconciliation
- Decoupled GitHub Pages deployment from every `main` push; deployment is now manual until the repository-level Pages site is enabled.
- Removed automatic Pages enablement from the workflow so repository permissions/bootstrap failures no longer masquerade as product-test failures.
- Renamed static and browser workflows to make their current scope explicit: they validate the repository Pages/control-plane artifact, not the historical image-heavy student build.
- Reconciled the staging logic used by static QA, browser QA and Pages deployment.
- Verified fresh `main` runs: Repository Static QA = success; Repository Browser QA = success.
- Recovered the historical image-heavy `Carruseles premium .html` artifact from durable Library storage and fingerprinted it as SHA-256 `03bd15f32553dbbe710ff50cf144e42cabc053b6cccf17aa2825b6773c71271d` (3,883,638 bytes, 33 `<img>` elements). It is not yet claimed as the repository/public production artifact.
- Kept R-002 open: exact student artifact synchronization + product-specific QA + public URL verification remain required before a Module 01 production-release claim.

## [0.2.0] — COS Graph Engine V2+ continuity / evidence control plane
- Promoted repository scope from a single carousel artifact to an AI-native creative systems training program with explicit Module 01 and Module 02 boundaries.
- Added `/COS-GRAPH-ENGINE-V2` human and machine-readable zero-context master checkpoints.
- Added `control-plane/` authority graph, deterministic recovery protocol and next-agent bootstrap.
- Added append-only decision, risk and evidence/event registers.
- Added machine-readable capability-audit and session-checkpoint schemas.
- Added explicit benchmark gates preventing README/test-count capability theater.
- Added an end-to-end autonomous editing vertical-slice gate requiring real media, timeline/render evidence, full-video criticism, targeted repair and provenance.
- Reconciled stale `GOAL.md`, `STATE.md` and `HANDOFF.md` with the current active mission.
- Locked the Module 02 boundary: Motion.OS and AVE are execution substrates to audit, not the training syllabus.
- Blocked Module 02 training artifact design until the Motion.OS × AVE forensic capability audit and evidence gates pass.
- Preserved Module 01 publication divergence as an explicit risk rather than silently treating a local HTML or control-plane page as production.

## [0.1.0] — Canonical repository bootstrap
- Established Git-backed project continuity with AGENTS / GOAL / STATE / HANDOFF.
- Added responsive GitHub Pages control plane for AI SLOP → BRAND SYSTEM.
- Added canonical P00–P17 Prompt OS with runtime COPY from one source of truth.
- Added traceable `visual-dna.json` / `DESIGN.md` / `SKILL.md` architecture.
- Added Codex, Claude Code and Higgsfield Supercomputer adapters.
- Added deterministic static QA and Playwright Browser QA for 390×844, 430×932 and 1440×1000.
- Added copy-to-clipboard interaction tests for P00–P17 and published-source availability tests.
- Added QA-gated GitHub Pages deployment.
- Added 29-asset historical semantic manifest with SHA-256 checksums.
- Added version ancestry manifest for v3.0, v7.1 and v8.0-pro-responsive.
- Replaced chat-only continuity with repository state and explicit release gates.
- Tracked the remaining full visual binary import as P0 Issue #1 instead of silently dropping or fabricating assets.
