# MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REMEDIATION-001

## Purpose

Correct the documented production-deployment authorization contract so it
accurately reflects observed behavior, without silently accepting that
behavior as permanent governance policy. This task is documentation-only: it
does not touch Vercel, GitHub settings, deployments, PR #28, or the physical
Gate B requirement.

## Verified Initial State

Phase 0/1 (read-only), reverified against
`C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`:

- Worktree clean; branch `docs/mellycore-3d-scene-paused-state-sync-001`;
  HEAD `22517faaa566d684c0f23acb770830278e1ee854`; parent
  `e7c8ce5f116e93a11a591ee539272f223af110d1`; subject `docs: record paused 3D
  scene physical QA gate`.
- Canonical `clean-origin/main` unchanged at
  `e7c8ce5f116e93a11a591ee539272f223af110d1`.
- Local commit `22517fa…` confirmed contained by **no** remote branch
  (`git branch -r --contains` empty).
- `gh repo view` → `Melly-999/mellycore-aios-core`, `PUBLIC`, default branch
  `main`.
- `gh api branches/main/protection` → `404 "Branch not protected"`.
- `gh api rulesets` → `[]`.
- `gh api environments` → `Production` and `Preview` both
  `protection_rules: []`.
- Production-deployment correlation reverified unchanged: `e7c8ce5f…`,
  `3f8fd51c…`, `ca1f762a…`, `be3ead9b…`, `177128cf…`, `59b1408d…` all still
  present as `environment: Production` deployment records.
- `gh pr view 28` unchanged: `OPEN`, non-draft, unmerged, head
  `57bb841e67e9a5d557f88bf096537eba78df1cd8`, `MERGEABLE`, `CLEAN`,
  `mergeCommit: null`.

No material drift from
`MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REVIEW-001`'s
findings was found; the task proceeded.

## Review Outcome (input to this task)

`REMEDIATION_REQUIRED_PRODUCTION_DEPLOYMENT_AUTHORIZATION_CONTRACT_REVIEW`,
classified `OPERATIONAL_CONTROL_MISMATCH`, `TECHNICAL_ENFORCEMENT_GAP`,
`TRUTHFUL_STATE_OVERCLAIM`, severity `HIGH_PRIORITY_GOVERNANCE_MISMATCH`.

## Deployment-History Evidence and Preview-vs-Production Pattern

Five consecutive recent merges into `main` were each followed by a
successful Vercel Production deployment approximately 8–14 seconds later,
all created by `vercel[bot]`: `e7c8ce5f116e…` (PR #27), `3f8fd51c3ed6…`
(PR #26), `ca1f762a0cdd…` (PR #25), `be3ead9b1b27…` (PR #24),
`177128cfc651…` (PR #23). Feature-branch heads, including PR #28's
`57bb841e…`, deploy to `Preview` only. Pattern: feature branch → Preview;
merge commit on `main` → Production.

## Enforcement State

`main`: no branch protection. Repository: no rulesets. `Production`
environment: no protection rules. `Preview` environment: no protection
rules. No `.github/` workflow, `vercel.json`, `.vercel`, or `package.json`
exists on canonical `main`. Deployment trigger classification:
`VERCEL_GIT_INTEGRATION`. Merge authorization: procedural only (no technical
gate). Deployment authorization: not separately technically enforced.

## Files Changed and Purpose

- `shared_context/SAFETY_CONTRACT.md` — added a "Production Deployment —
  Current Enforcement State" subsection clarifying that "No deploy without
  explicit approval" is a norm not currently separately technically
  enforced after merge, without removing the norm itself.
- `shared_context/PROJECT_STATE.md` — added a "Production Deployment
  Authorization — Confirmed Mismatch" section (evidence, enforcement gap,
  interim rule, both unresolved models, next task); corrected the Safety
  Boundaries bullets that previously read as claiming deployment is
  separately, autonomously gated; updated the stale next-task pointer left
  by the prior paused-state sync.
- `shared_context/ROADMAP.md` — corrected the duplicate Safety Gates
  overclaim ("No autonomous … deployment …") that would otherwise
  contradict the corrected `PROJECT_STATE.md`, and added a pointer to the
  confirmed-mismatch record.
- `shared_context/RUN_QUEUE.md` — replaced the now-completed
  "next task: …CONTRACT-REVIEW-001" pointer with the review's outcome
  summary and the new "next task: …MODEL-DECISION-001" pointer.
- `shared_context/AGENT_HANDOFF.md` — added a new "Latest Update" entry
  recording this remediation; relabeled the previous top entry to
  "Previous Update".
- `AGENTS.md` — added an interim operating rule instructing agents to treat
  every proposed `main` merge as an immediate public-publication request
  until the authorization model decision resolves this.
- `docs/tasks/MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REMEDIATION-001.md`
  (this file) — new task report.

## Corrected Wording — Summary

- **A. Normative safety intention (preserved):** production publication
  requires explicit operator control; agents must not push, merge, or
  deploy without approval; deployment must not occur invisibly or without
  the operator understanding its consequence.
- **B. Observed operational reality (now stated explicitly):** the Vercel
  Git integration watches `main`; a merge to `main` automatically creates a
  Production deployment within seconds; the public host updates without a
  further human action; there is exactly one human decision point (merge
  approval).
- **C. Enforcement gap (now stated explicitly):** merge authorization is
  procedural only; deployment authorization is not separately enforced; no
  branch protection; no rulesets; no Production environment protection
  rules.
- **D. Interim operating rule (added):** until the model decision resolves
  this, every proposed merge into `main` must be treated as immediately
  production-affecting; no document or agent may describe merge and
  Production publication as independently gated; this does not itself
  authorize any merge or deployment, and does not establish that merge
  approval has become permanent deployment approval.

## Unresolved Operator Decision

Recorded, not selected: **Model A** (combined static-site authorization —
merge approval also authorizes the automatic Production publication that
follows during the current static-showcase phase) and **Model B** (separate
merge and deployment authorization, requiring current-capability research
and separately authorized Vercel/GitHub control changes). Neither is
implemented, prescribed, or chosen by this task.

## Effect on PR #28

None. PR #28 remains `OPEN`, non-draft, unmerged, `MERGEABLE`/`CLEAN`, head
`57bb841e…`, `mergeCommit: null`. Physical Android Chromium Gate B remains
`OPEN / NOT EXECUTED`. No waiver, risk acceptance, merge, or deployment was
authorized by this task.

## Validation

Recorded in the operator-facing final report for this task, including exact
`git diff --check`, `py -3.9 scripts/validate_project_state.py`, and
`py -3.9 -m unittest discover -s tests -v` commands and outcomes. This
report does not claim any validator ran or passed beyond what is explicitly
recorded there.

## Final Branch and Commit

Branch: `docs/mellycore-production-deployment-contract-remediation-001`,
created via `git switch -c` directly from local commit
`22517faaa566d684c0f23acb770830278e1ee854` (not from canonical `main`
directly — this branch stacks the remediation commit on top of the
paused-state commit, per authorization). Commit subject: `docs: align
production deployment authorization contract`. Exactly one new local commit
was created; the paused-state commit was not amended or squashed.

## No-Push State

No push occurred. No PR was created or mutated. No merge occurred. No
deployment or redeployment occurred. No GitHub or Vercel setting was
changed. No branch protection, ruleset, environment, or workflow change was
made.

## Next Task

`MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-MODEL-DECISION-001` — a
read-only operator-governance decision task selecting Model A or Model B.
Not configuration work, not deployment work, not merge authorization, and
independent of PR #28's physical Gate B.
