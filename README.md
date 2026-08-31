# AI SLOP → BRAND SYSTEM

Canonical repository for the **Viral Carousels / Visual Brand System** training module.

## North Star

A student arrives with an idea and leaves with a portable visual system that can reproduce premium branded carousels across tools and runtimes.

`idea → references → Extractor ADN Visual v2 → visual-dna.json → DESIGN.md → template → generation → QA → SKILL.md → Codex / Claude Code / Higgsfield Supercomputer`

## Repository map

```text
prompts/              P00–P17 canonical prompt library
skills/               executable visual brand system
templates/            visual-dna / DESIGN / workbook templates
adapters/             Codex / Claude Code / Higgsfield runtime adapters
site-bundle/          GitHub Pages deployable course bundle
scripts/              deterministic QA
qa/                   release evidence
versions/             version policy/history
AGENTS.md              agent operating rules
GOAL.md                North Star + acceptance criteria
STATE.md               current operational state
HANDOFF.md             zero-context recovery
CHANGELOG.md           append-only changes
```

## GitHub Pages

The course is deployed by `.github/workflows/pages.yml`. The workflow reconstructs the static site from the versioned text-safe site bundle, runs QA, and publishes the exact artifact.

If Pages has never been enabled for this repository, select **Settings → Pages → Build and deployment → GitHub Actions** once.

## Local QA

```bash
python scripts/qa.py _site/index.html
```

## Extractor ADN Visual v2

https://chatgpt.com/g/g-697fac8775c081919387509ec73c69a5-extractor-adn-visual-v2
