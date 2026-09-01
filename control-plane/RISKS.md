# RISK REGISTER

## R-001 — Capability theater
**Severity:** P0
**Risk:** documented AVE/Motion.OS features may be stubs or weakly verified.
**Mitigation:** evidence-backed capability audit before course design.

## R-002 — Local/repo/deploy divergence
**Severity:** P0
**Risk:** strongest local artifact differs from `main` or public site.
**Mitigation:** exact-artifact hashes, one production entrypoint, release evidence tied to commit.

## R-003 — Pedagogy contaminated by infrastructure
**Severity:** P1
**Risk:** student experience becomes engine documentation.
**Mitigation:** CORE/OPTIONAL/HIDDEN_INFRA classification for every capability.

## R-004 — False QA confidence
**Severity:** P0
**Risk:** unit/DOM tests pass while visual/interaction product fails.
**Mitigation:** Playwright interaction + visual QA + real outputs/renders.

## R-005 — Temporal critic gap
**Severity:** P0
**Risk:** autonomous editor cannot reliably judge whole-video rhythm/story/art direction.
**Mitigation:** prove or integrate authoritative temporal multimodal critic before claiming autonomous repair.

## R-006 — Overengineering recurrence
**Severity:** P1
**Risk:** control-plane complexity grows faster than creative output quality.
**Mitigation:** every new abstraction must close a current P0/P1 or improve measured output.

## R-007 — Context-loss regression
**Severity:** P1
**Risk:** a fresh agent repeats old failures or treats hypotheses as truth.
**Mitigation:** mandatory recovery protocol + checkpoint schema + decision/evidence ledgers.
