# Skill: mellycore-loop-triage

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Status:** Canonical — report-only
**Inherits:** `mellycore-loop-constraints.md` (read it first; every rule there applies here)

---

## 1. Purpose

Triage decides **what is worth looking at** and reports it. It never fixes anything.

This skill backs the `project-health` and `pr-review-monitor` loops, and any future loop that needs to answer "what is the state of things, and what deserves attention".

## 2. Procedure

1. Read your registry entry. Confirm `status` is `REPORT_ONLY` and `allowed_write_scope` is empty. If either is otherwise, stop and report.
2. Read only within `read_scope`.
3. Gather observations. For each, record the file and line that supports it.
4. Rank by whether it blocks work, not by how interesting it is.
5. Produce the report in section 3.
6. Stop.

## 3. Report Shape

```
LOOP: <loop id>
STATUS: REPORT_ONLY
READ: <files actually read>

FINDINGS (ranked):
1. <finding> — evidence: <file:line> — impact: <blocking | notable | minor>
2. ...

UNVERIFIABLE:
- <anything you could not substantiate, and why>

RECOMMENDED (for the operator to decide, not for you to do):
- <suggestion>

VALIDATORS:
- <command> — <passed | failed | not run | unavailable>   (report exactly what happened)
```

## 4. Rules

- **Every finding needs evidence.** A finding you cannot tie to a file and line goes under UNVERIFIABLE, or is dropped. It does not get reported as a fact.
- **Recommendation is not action.** You may say "the run queue looks stale". You may not update it.
- **Do not fix in passing.** Even a one-character obvious fix is a repository write, and you may not make one. Report it.
- **Report the validator outcome you observed.** Not run and unavailable are outcomes; report them as themselves rather than omitting them.
- **Do not pad.** No findings is a legitimate and useful result. Say so plainly rather than inventing something to justify the run.
- **Do not read `forbidden_paths`** — not to check, not to confirm, not to report on.

## 5. Escalate When

- A finding touches a safety rule.
- The repository state contradicts `shared_context` in a way you cannot resolve from evidence.
- You would need to write, push, comment, or install something to make progress.

Escalate by reporting and stopping.
