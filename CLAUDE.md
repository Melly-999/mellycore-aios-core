# CLAUDE.md

@AGENTS.md

`AGENTS.md`, imported above, is the canonical shared multi-agent policy for
MellyCore AIOS: authority hierarchy, preflight, edit discipline, safety
posture, validation honesty, review principles, commit/handoff convention,
and stop conditions. Read it first. This file holds only what is specific
to running as Claude Code in this repository.

## Claude Code commands

`.claude/commands/` holds Claude-Code-specific procedures that implement
`AGENTS.md`'s rules — use them rather than re-deriving the same discipline
from scratch each session:

- `plan-task.md` — read-only planning before non-trivial work.
- `review.md` — independent review of another session's work.
- `diff-audit.md` — pre-commit / pre-handoff audit of a pending change.

Do not restate their procedures here or in `AGENTS.md`.
