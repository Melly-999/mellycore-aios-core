# MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-IMPLEMENTATION-001

## Purpose

Implement the Operator's explicit Model A selection as a documentation-only
governance contract, replacing the unresolved Model A/Model B state recorded
by `MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-MODEL-DECISION-001` with a
canonical, mechanically inspectable temporary policy. This task changes no
Vercel/GitHub setting, no implementation, and no vendor file, and does not
touch PR #28 or physical Gate B.

## Operator Authorization (verbatim)

Recorded canonically in `shared_context/DECISIONS.md` (2026-07-27):

> I explicitly select Model A for the current static-showcase phase.
> For each individually approved pull-request merge into canonical `main`,
> my merge approval also authorizes the automatic Vercel Production
> publication caused by that specific merge.
> This is not blanket authorization for future merges.
> Every merge still requires separate explicit operator approval and must
> clearly warn that it immediately affects the public Production host.
> Model A is limited to the static, non-sensitive, non-runtime phase.
> Model A must be reconsidered before backend, authentication, stored data,
> secrets, provider integration, agent execution, external write capability,
> financial functionality, delegated merge authority, or multiple active
> maintainers are introduced.
> This authorization does not approve any current merge, deployment, push,
> PR creation, PR mutation, Vercel change, GitHub settings change, or
> implementation work.

## Verified Initial State

Phase 0 (read-only), reverified:

- Worktree clean; branch `docs/mellycore-production-deployment-contract-remediation-001`;
  HEAD `19eada06a8ba25b5cd980d4ec5226c3c288c8f6c`; parent
  `22517faaa566d684c0f23acb770830278e1ee854`; subject `docs: align production
  deployment authorization contract`.
- Canonical `clean-origin/main` unchanged at
  `e7c8ce5f116e93a11a591ee539272f223af110d1`.
- Both prior commits confirmed contained by no remote branch (unpushed).
- `gh pr view 28` unchanged: `OPEN`, non-draft, unmerged, head
  `57bb841e67e9a5d557f88bf096537eba78df1cd8`, `MERGEABLE`, `CLEAN`,
  `mergeCommit: null`.

## Selected Model

**Model A — combined static-site authorization.** Decision authority: the
Operator (sole authority). Scope: current static, non-sensitive, non-runtime
phase only.

## Per-Merge Authorization Contract

- Every merge into `main` requires explicit Operator approval for that
  specific PR — never blanket, standing, batch, inferred, or future
  authorization.
- Approval for one specific merge authorizes only the automatic Production
  publication caused by that specific merge.
- Every merge-authorization request must explicitly warn that merging into
  `main` immediately updates the public Production host.
- No agent may merge on its own initiative.

## Production-Impact Warning

Mandatory on every merge-authorization request an agent prepares, per the
per-merge rule above. Recorded in `AGENTS.md`, `SAFETY_CONTRACT.md`,
`PROJECT_STATE.md`, `ROADMAP.md`.

## Post-Merge Verification Requirement

After an authorized merge: verify the expected Production deployment
completed and the accepted public host remains reachable; verify the live
deployment corresponds to the expected canonical commit where evidence
permits; report verification honestly; never claim success without
evidence. This defines verification, not permission to merge.

## Rollback Boundary

Rollback must remain practical for the static-showcase phase; a concrete
rollback action still requires its own separate, explicit Operator
authorization. No rollback mechanism is claimed as already configured or
validated by this task.

## Mandatory Migration Triggers (blocking)

1. First backend endpoint.
2. First authentication flow.
3. First stored user data.
4. First runtime secret.
5. First live provider connection.
6. First execution-capable agent.
7. First external write-capable integration.
8. First financial or trading action.
9. Delegated merge authority or multiple active maintainers.

These are explicit, grep-able, and **blocking, not advisory**. While any
trigger applies: no affected implementation task may proceed to merge,
Model A must not silently continue, and a separate governance decision plus
capability-research task (`MELLYCORE-PRODUCTION-DEPLOYMENT-SEPARATION-CAPABILITY-RESEARCH-001`)
is required first.

## Branch-Protection Boundary

Model A creates no branch protection, ruleset, environment protection, or
CI enforcement. Reverified unchanged: `main` branch protection → `404
"Branch not protected"`; rulesets → `[]`; `Production`/`Preview` environment
`protection_rules: []`. Merge authorization remains procedural only; the
absence of branch protection is accepted only as a temporary condition of
the current sole-Operator boundary, and is itself covered by migration
trigger 9.

## Effect on PR #28

None. PR #28 remains `OPEN`, non-draft, unmerged, `MERGEABLE`/`CLEAN`, head
`57bb841e…`, `mergeCommit: null`. Physical Android Chromium Gate B remains
`OPEN / NOT EXECUTED`. Model A selection does not waive, replace, satisfy,
defer, or weaken Gate B. No physical-QA waiver or risk acceptance was
created. Any eventual PR #28 merge request must independently satisfy every
one of its own gates and separately include the Model A Production-impact
warning.

## Files Changed and Purpose

- `shared_context/DECISIONS.md` — added the dated, verbatim Operator
  decision entry (primary canonical record of the authorization statement).
- `shared_context/PROJECT_STATE.md` — added the full "Production Deployment
  Authorization — Model A Contract (Temporary, Static-Phase Only)" section
  (canonical detailed contract); updated the "3D Scene Foundation" pointer
  and the Safety Boundaries bullets to reflect the selection.
- `shared_context/ROADMAP.md` — updated the Safety Gates production-note
  from "unresolved" to "Model A selected."
- `shared_context/SAFETY_CONTRACT.md` — updated the enforcement-state
  section to record Model A as the current temporary policy.
- `AGENTS.md` — updated the interim operating rule to the Model A rule,
  preserving no-blanket-authorization, the mandatory warning, and
  no-agent-initiated-merge.
- `shared_context/RUN_QUEUE.md` — replaced the completed-review/unresolved
  next-task paragraph with the selection summary and the new next-task
  pointer.
- `shared_context/AGENT_HANDOFF.md` — added a new "Latest Update" entry;
  relabeled the previous top entry to "Previous Update."
- `docs/tasks/MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-IMPLEMENTATION-001.md`
  (this file) — new task report.

## Validation

Recorded in the operator-facing final report for this task, including exact
`git diff --check`, `py -3.9 scripts/validate_project_state.py`, and
`py -3.9 -m unittest discover -s tests -v` commands and outcomes, plus the
consistency-sweep results. This report does not claim any validator ran or
passed beyond what is explicitly recorded there.

## Final Branch and Commit

Branch: `docs/mellycore-production-deployment-model-a-contract-001`,
created via `git switch -c` directly from
`19eada06a8ba25b5cd980d4ec5226c3c288c8f6c`. Commit subject: `docs: adopt
temporary Model A deployment authorization`. Exactly one new local commit
was created; neither prior commit was amended or squashed.

## No-Push State

No push occurred. No PR was created or mutated. No merge occurred. No
deployment or redeployment occurred. No GitHub or Vercel setting was
changed. No branch protection, ruleset, environment, or workflow change was
made.

## Next Task

`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-REVIEW-001` — an
independent, read-only review verifying this contract's implementation. Not
a publication task, not a merge task, not deployment work, and not related
to closing PR #28's physical Gate B.
