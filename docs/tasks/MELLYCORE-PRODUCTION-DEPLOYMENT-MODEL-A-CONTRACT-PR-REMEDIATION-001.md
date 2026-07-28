# MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-PR-REMEDIATION-001

## Purpose

Fix the single blocking finding (B-01) and bundled non-blocking note (N-01)
identified by the independent PR #29 review, via one additional
documentation-only commit pushed normally to the existing PR #29 branch.
This task changes no substantive Model A policy, no migration trigger, no
implementation/vendor/workflow file, and does not touch PR #28 or physical
Gate B.

## Confirmed PR Review Outcome (input to this task)

`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-PR-REVIEW-001` returned
`REMEDIATION_REQUIRED_MODEL_A_DEPLOYMENT_CONTRACT_PR_REVIEW` against PR #29
head `ec5182b811de35313a57072a8d068e3986b1fa50`.

## B-01 Evidence (fixed)

`chatgpt-codex-connector[bot]` inline review comment,
`shared_context/SAFETY_CONTRACT.md:35`, against commit `ec5182b8…`: the
document stated in present tense that it "requires [merge and Production
publication] to be treated as requiring separate explicit authorization,"
directly contradicting the Model A section immediately below it, which
states combined per-merge authorization. Fixed by placing the former
requirement explicitly in the past and restating the current rule.

## N-01 Evidence (fixed, bundled)

`shared_context/PROJECT_STATE.md`'s "Interim operating rule, effective
until resolved" lead-in remained present-tense despite Model A having
already been selected. Reframed as "Pre-decision interim operating rule —
superseded on 2026-07-27 by the temporary Model A contract below and
retained here as historical context"; the substantive warning text that
follows is otherwise unchanged.

## Exact Wording Corrections

**`SAFETY_CONTRACT.md`** — before:
> "…even though this document requires that they be treated as requiring
> separate explicit authorization."

After:
> "…Before the Operator selected temporary Model A on 2026-07-27, this
> document required them to be treated as separately authorized. Under the
> current Model A contract below, explicit approval of one specific merge
> also authorizes only the automatic Production publication caused by that
> merge."

**`PROJECT_STATE.md`** — before:
> "Interim operating rule, effective until resolved: every proposed merge
> into `main` must be treated as…"

After:
> "Pre-decision interim operating rule — superseded on 2026-07-27 by the
> temporary Model A contract below and retained here as historical context:
> every proposed merge into `main` must be treated as…"

## Files Changed

- `shared_context/SAFETY_CONTRACT.md` — B-01 fix.
- `shared_context/PROJECT_STATE.md` — N-01 fix.
- `shared_context/RUN_QUEUE.md` — recorded the PR review outcome, this
  remediation, and the new next-task pointer.
- `shared_context/AGENT_HANDOFF.md` — added the latest handoff entry;
  relabeled the previous top entry to "Previous Update."
- `docs/tasks/MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-PR-REMEDIATION-001.md`
  (this file) — new task report.

**N-02 was not modified** (out of scope, remains separately non-blocking).

## Model A Substance — Confirmed Unchanged

The Operator's verbatim statement in `DECISIONS.md`, the per-merge
authorization rule, the no-blanket-authorization prohibition, the
mandatory Production-impact warning, the post-merge verification
requirement, the rollback boundary, and all nine blocking migration
triggers are unchanged by this task — verified by consistency sweep below.

## Consistency Sweep

Searched `AGENTS.md shared_context docs` for
`separate explicit authorization|separately authorized|effective until
resolved|superseded|Model A|Model B|blanket|standing|batch|Production
publication|PR #28|Gate B`. Result: no live statement claims the current
contract requires separate merge/Production approvals; both corrected
locations now use past-tense/superseded framing; Model A remains explicitly
temporary; every merge remains individually authorized; no blanket
authorization introduced anywhere; all nine migration triggers unchanged
and still framed as blocking; PR #28 and Gate B statements unchanged
throughout.

## Validators

- `git diff --check` — clean, exit 0.
- `py -3.9 scripts/validate_project_state.py` — `PASS`, exit 0.
- `py -3.9 -m unittest discover -s tests -v` — 245 tests passed, 0 failures.

## Commit and Push

- New commit parent: `ec5182b811de35313a57072a8d068e3986b1fa50`.
- Subject: `docs: resolve Model A authorization wording`.
- Pushed normally (no force, no rewrite) to
  `clean-origin/docs/mellycore-production-deployment-model-a-contract-001`.

## Updated PR #29 State

Recorded in the operator-facing final report for this task: updated head
SHA, commit count, changed-file count, checks snapshot, and Preview result.
The Codex inline comment was not resolved or replied to.

## PR #28 and Gate B

Unaffected. PR #28 remains open, non-draft, unmerged, mergeable,
intentionally paused. Physical Android Chromium Gate B remains
`OPEN / NOT EXECUTED`. No waiver, deferment, or risk acceptance was created.

## No-Merge / No-Production Confirmation

No merge occurred. No auto-merge was enabled. No Production deployment was
authorized or triggered by this task; only the disclosed, expected Preview
deployment for the new commit is anticipated.

## Next Task

`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-PR-REMEDIATION-REVIEW-001`
— a fresh-session, independent, read-only review of the updated PR #29
head, deciding whether B-01 and N-01 are resolved and reassessing all
current-head reviews and comments. Not authorized to merge, resolve
comments, or deploy, and unrelated to closing PR #28's Gate B.
