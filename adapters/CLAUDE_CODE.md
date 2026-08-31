# Runtime Adapter — Claude Code

## Load
Keep `DESIGN.md`, `visual-dna.json`, and `SKILL.md` in the project context.

## Run instruction
Treat `SKILL.md` as the procedure and `DESIGN.md` as the visual source of truth. Read both before acting. Do not mutate either file unless the user explicitly asks to approve a proposed patch.

INPUT:
- idea: [IDEA]
- objective: [OBJECTIVE]
- audience: [AUDIENCE]
- format: [FORMAT]
