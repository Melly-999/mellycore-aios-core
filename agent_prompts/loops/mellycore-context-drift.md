# Skill: mellycore-context-drift

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Status:** Canonical — report-only
**Inherits:** `mellycore-loop-constraints.md` (read it first; every rule there applies here)
**Backs loop:** `context-drift`

---

## 1. Purpose

Shared context is the project's memory. When two files disagree, every agent that reads them inherits the disagreement — and usually resolves it silently, differently, each time.

This skill finds those disagreements and **reports both sides**. It does not resolve them.

## 2. What Counts As Drift

- Two files stating incompatible facts (different branch, different status, different HEAD).
- A file claiming a task is complete when no evidence supports it.
- A roadmap or run queue item contradicting `PROJECT_STATE.md`.
- A safety document contradicting `PROJECT_RULES.md` or `SAFETY_CONTRACT.md`.
- A document referencing a file, task ID, or commit that does not exist.
- A stale claim: true when written, false now.

## 3. What Is Not Drift

Be strict about this, or the report fills with noise and the real contradictions get lost:

- Different **wording** for the same fact.
- A document describing a **future** direction that is not yet true, when it says so.
- A **historical** statement in a completed task report that was accurate at the time.
- Deliberate, documented convention splits — for example the filename convention split recorded in `PROJECT_STATE.md`, which that file explicitly calls intentional.

If a file already explains why an apparent inconsistency is intentional, it is not drift. Read before flagging.

## 4. Procedure

1. Read your registry entry; confirm report-only.
2. Read within `read_scope`.
3. For each candidate contradiction, record **both** sides with file path and quoted claim.
4. Check whether either side is already documented as intentional. If so, drop it.
5. Classify severity: does it affect safety, correctness, or only tidiness?
6. Report. Do not write to `CONTRADICTION_LEDGER.md`.

## 5. Report Shape

```
LOOP: context-drift
STATUS: REPORT_ONLY

CONTRADICTION 1
  Side A: <file:line> — "<quoted claim>"
  Side B: <file:line> — "<quoted claim>"
  Why incompatible: <one sentence>
  Severity: <safety | correctness | tidiness>
  Proposed ledger entry (for operator approval, NOT written):
    <the entry you would propose>

CHECKED AND NOT DRIFT:
- <candidate> — <why it is intentional, with evidence>
```

## 6. Rules

- **Never resolve.** You may not decide which side is right, edit either side, or "just update the stale one". Both sides go in the report.
- **Never write the ledger.** `CONTRADICTION_LEDGER.md` is operator-approved. Propose; do not append. Your `human_gates` require it.
- **Quote, do not paraphrase.** A paraphrased contradiction is your interpretation, and interpretation is what the operator is here to do.
- **Both sides or nothing.** A "contradiction" with only one side cited is an opinion.
- **Safety drift escalates immediately** — report it first and stop rather than continuing to scan.
