# MellyCore Loop Skills — Canonical

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Version:** 1.0
**Status:** Phase 1 — report-only
**Scope:** Canonical, tool-neutral instructions for operating MellyCore loops

---

## 1. Why This Directory Exists

These are the **canonical** loop skills. They are written once, here, and are not duplicated per tool.

Duplicating the same safety text into a Claude copy and a Codex copy guarantees the two will drift, and the moment they drift there is no answer to "which one is the rule". Instead: this directory owns the content, and `agent_prompts/claude/README.md` and `agent_prompts/codex/README.md` reference it.

If a tool needs its own wrapper, the wrapper points here. It does not restate.

## 2. The Skills

| Skill | Purpose |
| --- | --- |
| `mellycore-loop-constraints.md` | The rules every loop skill inherits. Read first, always. |
| `mellycore-loop-triage.md` | Decide what a loop should look at. Report-only. |
| `mellycore-context-drift.md` | Find contradictions in shared context. Report-only. |
| `mellycore-loop-verifier.md` | Independently verify work. Defaults to REJECT. |
| `mellycore-loop-budget-guard.md` | Read the deterministic circuit breaker and obey it. |
| `mellycore-worktree-audit.md` | Read-only worktree inspection. |

## 3. Required Read Order

Every skill here begins by requiring the same reading, and none of it is optional:

1. `[[../../shared_context/SAFETY_CONTRACT]]`
2. `[[../../docs/safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]`
3. `[[../../shared_context/loops/LOOP_REGISTRY]]` — the loop's own entry
4. `[[../../shared_context/loops/LOOP_CONSTRAINTS]]`
5. `mellycore-loop-constraints.md` in this directory

An agent that has not read the registry does not know its scope, and an agent that does not know its scope must not act.

## 4. Non-Negotiables

- **No skill may authorize anything `[[../../PROJECT_RULES]]` forbids.** If a skill here ever appears to permit something PROJECT_RULES prohibits, PROJECT_RULES wins and the skill is a defect.
- **Every skill is report-only in Phase 1.**
- **The verifier never implements the fix it verifies.** An agent grading its own work is not verification.
- **The verifier defaults to REJECT** until evidence passes.
- **Triage never acts.** It reports what it would look at and what it found.

## 5. Wrappers

- `[[../claude/README]]` — Claude Code wrapper
- `[[../codex/README]]` — Codex wrapper

Both defer to this directory.
