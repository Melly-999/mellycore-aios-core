---
description: Read-only planning pass before non-trivial work — no mutation.
---

# plan-task

Produce a plan. Do not edit, create, delete, stage, commit, or run any
command that mutates the repository or its git state. This command is
read-only unless the user explicitly says, in a separate follow-up, to
proceed with the plan.

Safety posture and authority hierarchy: as `AGENTS.md`. This file only
specializes the planning procedure.

## Procedure

1. **Inspect instructions.** Read `AGENTS.md`, then the task's own
   instructions (task prompt, issue, or user request). Note anything that
   conflicts and cannot be resolved without the operator.
2. **Check repository state.** Run:
   - `git rev-parse --abbrev-ref HEAD`
   - `git rev-parse HEAD`
   - `git status --short`
   - `git diff --cached --name-only`
   - `git diff --name-only`
   Record branch, HEAD, and staged/unstaged/untracked files. If unrelated
   dirty state exists, note it and plan to leave it untouched.
3. **Identify affected files.** List the exact files the task will need to
   read and the exact files it may change. Nothing outside that list is in
   scope.
4. **Define scope.** State what this task will do and, as importantly,
   what it will not do.
5. **List allowed / not-allowed changes**, drawn from `AGENTS.md`'s safety
   posture and this task's own instructions.
6. **Identify validation.** State which validators are relevant (for
   example `git diff --check`, a secret-pattern scan, a project-specific
   test command) and which of them will actually be run versus which are
   not applicable.
7. **Define stop conditions.** State what would make this task stop and
   report rather than proceed, per `AGENTS.md`'s stop conditions plus
   anything task-specific.
8. **Return the plan.** Present branch/HEAD/status, affected files, scope,
   allowed/not-allowed changes, validation, and stop conditions. Wait for
   the operator, or the calling task, before taking any mutating action.

## Boundaries

- No commit, push, merge, deploy, or destructive git command.
- No file write, even a "harmless" one, during planning.
- If the repository state makes safe planning impossible (for example a
  detached HEAD with unclear provenance, or a conflict this command cannot
  resolve), report `BLOCKED` with the reason instead of guessing.
