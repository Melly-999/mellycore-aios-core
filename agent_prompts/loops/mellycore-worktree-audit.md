# Skill: mellycore-worktree-audit

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Status:** Canonical — read-only
**Inherits:** `mellycore-loop-constraints.md` (read it first; every rule there applies here)
**Backs loop:** `worktree-hygiene`

---

## 1. Purpose

MellyCore runs multiple agents across linked git worktrees. That is what keeps concurrent tasks from colliding — and it only works if someone notices when two worktrees start claiming the same work, or when one is quietly abandoned mid-task.

This skill reports. It never cleans.

## 2. The Command

```powershell
py -3.9 -m scripts.loop_ops worktree-audit
py -3.9 -m scripts.loop_ops worktree-audit --json
```

It runs read-only git inspection (`git worktree list --porcelain`, and `git status --porcelain` per worktree) and reports path, branch, HEAD, dirty state, and risks.

## 3. Absolutely Forbidden

You may not run, request, or suggest running:

- `git worktree remove`
- `git worktree prune`
- `git worktree unlock`
- `git reset`
- `git clean`
- `git branch -d` / `-D`
- any command that modifies a worktree, branch, or working tree

There is no exception for "obviously stale", "clearly abandoned", or "it's just a prune". A worktree you believe is abandoned may hold the only copy of someone's in-progress work, and prune is not reversible by you. **Cleanup is an operator decision, always.**

The tooling has no code path that mutates a worktree. Do not add one, and do not reach for raw git to work around its absence.

## 4. Risks Reported

| Risk | Meaning |
| --- | --- |
| `duplicate_branch` | Two worktrees on the same branch |
| `duplicate_task_ownership` | Two worktrees whose branches imply the same task |
| `dirty_worktree` | Uncommitted changes present |
| `detached_head` | Not on a branch |
| `possibly_stale` | Recorded path no longer exists |
| `path_missing` | Path in git's records is gone from disk |

`dirty` may also be **unknown** when it could not be determined safely. Report unknown as unknown. Do not report it as clean — "I could not tell" and "there is nothing there" are different claims, and only one of them is true.

## 5. Procedure

1. Confirm your registry entry is `REPORT_ONLY` with an empty `allowed_write_scope`.
2. Run the audit command.
3. For each risk, state what it is and what the operator might consider — as an option, not an instruction.
4. Report. Stop.

## 6. Report Shape

```
WORKTREE AUDIT (read-only)
COUNT: <n>

<path>
  branch: <branch or (detached)>
  head:   <short sha>
  state:  <clean | dirty | unknown>
  risks:  <risks or none>

RISKS FOR OPERATOR REVIEW:
- <risk> on <path> — <what it means> — <option the operator may consider>

NOTE: This audit performed read-only inspection only. Nothing was removed,
pruned, unlocked, reset, or cleaned.
```

## 7. Escalate When

- Two worktrees claim the same task or branch — a real collision risk; the operator decides which survives.
- A worktree is dirty and its owner is unclear.
- A recorded path is missing from disk.

Report and stop. Do not tidy.
