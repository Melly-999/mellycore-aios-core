# Run Queue

This file contains actionable sequencing and gates. Completed-task detail belongs
in `docs/tasks/` and Git history, not duplicated here.

## Vercel Static Root — Accepted, Verified, Published, State-Synced, Merged

`https://mellycore-aios-core.vercel.app` is the accepted production static
showcase host. The static-root fetch defect is fixed, reviewed `PASS`, and
merged into canonical `main` via PR #23 (merge commit
`177128cfc6513090b45491d16e9f0c594451636d`). Production redeploy smoke
passed and post-deploy verification (including a screenshot artifact) is
recorded in `docs/tasks/MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001.md`,
merged into canonical `main` via PR #24 (merge commit
`be3ead9b1b27a80bb6029acb7acba0c98c6ba4c6`). The deployment-state
synchronization itself (`MELLYCORE-DEPLOYMENT-STATE-SYNC-001`), after a
documentation-consistency remediation
(`MELLYCORE-DEPLOYMENT-STATE-SYNC-REMEDIATION-001`), merged into canonical
`main` via PR #25 (merge commit
`ca1f762a0cdd43b80282b885bfd7885d2740288a`, 2026-07-24T13:51:58Z). This
deployment/verification/state-sync chain is complete; no deployment-state
remediation or merge-retry task remains pending. GitHub Pages remains
containment/maintenance only, not a product host.

The Control Plane specification task,
`MELLYCORE-OMNIROUTER-INSPIRED-CONTROL-PLANE-SPEC-001`, completed authoring
and publication on branch
`docs/mellycore-omnirouter-inspired-control-plane-spec-001` in
[PR #27](https://github.com/Melly-999/mellycore-aios-core/pull/27). Its initial
review identified two specification blockers; targeted remediation commit
`ea662ab…` resolved them and corrected the status-dimension count. Publication,
initial review, targeted remediation, remediation publication, and targeted
re-review are complete. The targeted re-review outcome was
`PASS_WITH_NOTES_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC_REMEDIATION_REVIEW`,
with no blocking finding and all required checks passing.

At the time of that update, PR #27 was open, reviewed, remediation-complete,
and merge-ready, but not yet merged. It subsequently merged into canonical
`main` as `e7c8ce5f116e93a11a591ee539272f223af110d1`.

The Control Plane specification and this lifecycle correction define no
frontend, backend, provider integration, runtime, secrets flow, deployment,
or 3D implementation. A successful merge does not automatically require a
post-merge synchronization task; another sync is warranted only if a concrete
live canonical statement becomes false.

## Current — OpenAI Batch Final Canonical State Reconciliation Gate

Completed:
`MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-MERGE-001`. PR #32 merged
by GitHub merge commit at `2026-07-30T22:19:15Z`; canonical `main` was
`5e7628a72a22fc10ecd0f9a25515ab61eb7223b9`. Its automatic Vercel Production
deployment succeeded (`5683195625` /
`dpl_Bvijm1GRww7nVaLG4TwnUWBkZmuw`, `READY`, accepted host HTTP 200), while
the static `site` tree remained unchanged at
`5df8bb686ebeb5b13bcf1fe2ad2ef6bc796bfc5d`.

Completed: PR #33 governance state-sync, remediation 001
(`c0f69c5…`), remediation 002 (`ab5a6d7…`), publication/reconciliation, and
independent review 002
(`PASS_MELLYCORE_OPENAI_BATCH_API_CONTROLLED_ACTIVATION_POST_MERGE_STATE_SYNC_PR_REVIEW_002`)
all completed. `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-POST-MERGE-STATE-SYNC-MERGE-001`
merged [PR #33](https://github.com/Melly-999/mellycore-aios-core/pull/33) at
`2026-07-31T15:52:54Z` via GitHub merge commit
`f118110181fe5428940ac86256dedc63f52282a6` (first parent
`5e7628a72a22fc10ecd0f9a25515ab61eb7223b9`, second parent exact reviewed
head `ab5a6d775ff86bc051788ca2927e17c3d8eab880`; merge tree
`e49a392614b10be2e235dcb85ad374004bbced0b` identical to the reviewed-head
tree). Canonical `main` is now that merge commit. PR #33's exact
three-commit, five-file documentation-only scope is canonical; the static
`site` tree remained unchanged at
`5df8bb686ebeb5b13bcf1fe2ad2ef6bc796bfc5d`; the Codex thread
(`discussion_r3690288402`) is resolved with a published evidence reply; the
source branch is preserved. The automatic Vercel Production deployment
succeeded for the exact merge commit (GitHub deployment `5694313001`,
`success`); the accepted host `https://mellycore-aios-core.vercel.app`
returned HTTP 200; no manual deployment action or page-level visual
acceptance occurred.

**Current gate:**
`MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-FINAL-CANONICAL-STATE-RECONCILIATION-001`
records the merged, Production-verified state above as the durable Stage B
governance baseline across this queue, `PROJECT_STATE.md`, `AGENT_HANDOFF.md`,
and `ROADMAP.md`. At creation of its local documentation commit
(`docs: reconcile final Batch activation state`, parent
`f118110181fe5428940ac86256dedc63f52282a6`), that commit is local-only and
unreviewed. This is a time-scoped task-creation statement, not a permanent
workflow invariant.

**Exact immediate next task at creation of the local reconciliation
commit:**
`MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-FINAL-CANONICAL-STATE-RECONCILIATION-REVIEW-001`.

Only after that review returns PASS may
`MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-FINAL-CANONICAL-STATE-RECONCILIATION-PUSH-001`
push the exact reviewed local head by normal SHA-to-ref fast-forward, then
`-RECONCILIATION-PR-CREATION-001` open a PR, then
`-RECONCILIATION-PR-REVIEW-001` independently review it, then
`-RECONCILIATION-MERGE-001` merge it into canonical `main` and verify the
resulting automatic Production deployment. That publication/merge chain is
incomplete if any step's evidence (push, PR body accuracy, review outcome,
merge identity, deployment verification) does not match the actual live
state; a mismatch must produce a partial or blocked outcome and must not
advance to the next step.

Once this reconciliation content is independently reviewed, merged into
canonical `main`, and its automatic Production deployment is verified, the
canonical state it describes is the final reconciled Stage B governance
baseline. No further state-sync task is required solely to restate the PR
#33 merge already recorded above. Only then may
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` be considered as a
separate decision task, not live execution authorization.

Task-record next-task fields are creation-time historical snapshots,
superseded by this queue and `AGENT_HANDOFF.md`.

This queue entry does not authorize Stage C or live execution.
`STAGE_C_LIVE_BATCH_SMOKE_NOT_AUTHORIZED`,
`USD_0_01_SPEND_NOT_AUTHORIZED`, and
`MIGRATION_TRIGGER_5_NOT_YET_CROSSED` remain binding. Provider policy remains
`LIVE_PROVIDER_CONNECTION_BLOCKED_BY_MIGRATION_TRIGGER_5` (exit code `78`).
F1 and N1–N7 remain deferred non-blocking observations; the prior PyPI lookup
policy violation remains disclosed. PR #28 remains directly untouched, open,
unmerged, intentionally paused, and `CONFLICTING / DIRTY`; Gate B remains
`OPEN / NOT EXECUTED`.

## 3D Scene Foundation — PR #28 Paused State

The durable product successor after Control Plane specification acceptance,
`MELLYCORE-3D-SCENE-FOUNDATION-001`, is implemented on branch
`feat/mellycore-3d-scene-foundation-001` and published as
[PR #28](https://github.com/Melly-999/mellycore-aios-core/pull/28) (head
`57bb841e67e9a5d557f88bf096537eba78df1cd8`, two commits, twelve changed
files). PR #28 remains **open, unmerged, and intentionally paused**; GitHub
reports **`CONFLICTING / DIRTY`**. It is **not authorized to merge**.

Repository-verified evidence: independent foundation review returned
`PASS_WITH_NOTES_3D_SCENE_FOUNDATION_REVIEW`; desktop accessibility/
performance Gate A passed. Recorded as **operator-confirmed external/session
evidence, dated 2026-07-27, not independently repository-verified** (no
corresponding PR review, commit, or `docs/tasks/` report exists for either in
this repository — this sync is the first canonical repository record of
them): `PASS_WITH_NOTES_3D_SCENE_FOUNDATION_REMEDIATION_REVIEW` and
`PASS_WITH_NOTES_3D_SCENE_INTEGRATION_REVIEW`.

Physical Android Chromium **Gate B remains `OPEN / NOT EXECUTED`**
(`BLOCKED_3D_SCENE_QA_REFERENCE_DEVICE_UNAVAILABLE`): the operator has no
named physical Android Chromium reference device available. This is an
environmental/process blocker, not an application defect and not evidence of
correctness. **Do not rerun Gate B** until a named physical device is
confirmed available for ~15–20 minutes of testing. No waiver, deferment, risk
acceptance, merge, or deployment is authorized; Gate B remains a strict
pre-merge blocker with no repository-defined waiver process
(`RECOMMEND_KEEP_PREMERGE_BLOCKER_3D_SCENE_PHYSICAL_QA`).

`MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REVIEW-001`
confirmed merge into canonical `main` currently causes automatic public
Production publication via the Vercel Git integration (5/5 recent merges →
Production within 8–14s), with no separate technically-enforced
deployment-approval step. `MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-MODEL-DECISION-001`
then presented Model A and Model B as options; **the Operator has selected
Model A** (temporary, static-phase-only combined merge/deployment
authorization), recorded verbatim in `shared_context/DECISIONS.md` and
detailed in full in `PROJECT_STATE.md`'s "Production Deployment
Authorization — Model A Contract (Temporary, Static-Phase Only)". Each
individual merge approval authorizes only the Production publication that
specific merge causes — not blanket authorization — every merge request
must warn of immediate public-publication impact, and nine canonical,
blocking migration triggers require Model B reconsideration before any
affected implementation or merge proceeds. This selection does not unblock,
waive, or otherwise affect PR #28 — its physical Gate B is an independent
gate. `MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-REVIEW-001`
completed with outcome `PASS_WITH_NOTES_MODEL_A_DEPLOYMENT_CONTRACT_REVIEW`.
The contract was then published as PR #29
(https://github.com/Melly-999/mellycore-aios-core/pull/29,
head `ec5182b8…`). An independent PR review
(`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-PR-REVIEW-001`) found one
blocking finding (B-01: `SAFETY_CONTRACT.md` self-contradicted on whether
separate deployment authorization is still required) and one bundled
non-blocking note (N-01: a stale "effective until resolved" framing in
`PROJECT_STATE.md`); both are corrected by this remediation commit on PR
#29's branch. N-02 (validator evidence not embedded in task reports)
remains separately non-blocking and untouched. At the time of that
remediation, the next task was
`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-PR-REMEDIATION-REVIEW-001`
— a fresh-session, independent, read-only review of the updated PR #29
head, responsible for deciding whether B-01 and N-01 are resolved and for
reassessing all current-head reviews and comments; not authorized to merge,
resolve comments, or deploy, and unrelated to closing PR #28's Gate B. The
following historical description of the original review task is retained
below: an
independent, read-only review of this contract's implementation. Not a
publication, merge, deployment, or configuration task, and not related to
closing PR #28's Gate B.

That review completed with outcome
`PASS_WITH_NOTES_MODEL_A_CONTRACT_PR_REMEDIATION_REVIEW`, confirming both
B-01 and N-01 resolved, no blocking current-head review finding, all checks
passing, a successful Preview, no Production deployment for the head, and
245 tests passing; it also identified one new non-blocking note, N-03: two
statements in `PROJECT_STATE.md` still named the already-completed
`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-REVIEW-001` as the exact
next task. The subsequent merge-readiness assessment
(`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-MERGE-READINESS-001`)
returned `REMEDIATION_REQUIRED_MODEL_A_CONTRACT_PR_29_MERGE_READINESS`,
judging N-03 as requiring correction before merge given that any merge
under Model A immediately triggers public Production publication. This
task (`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-PR-REMEDIATION-002`)
corrects N-03 by reframing both `PROJECT_STATE.md` statements as historical
records rather than replacing them with another live pointer — this file,
`shared_context/RUN_QUEUE.md`, remains the canonical live task-sequencing
source, echoed in `shared_context/AGENT_HANDOFF.md`. No Model A policy, no
migration trigger, no PR #28 wording, and no Gate B wording was changed.
Known note N-04 (the PR #29 body's stale reference to the already-resolved
N-01 wording) is GitHub metadata, was intentionally left unmodified by this
task, and remains for the next review to assess. This task creates exactly
one new documentation-only commit, pushed normally (no force, no rewrite)
to `clean-origin/docs/mellycore-production-deployment-model-a-contract-001`;
it does not merge PR #29, does not enable auto-merge, and does not
authorize Production publication. That task's then-exact-next-task,
`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-PR-REMEDIATION-002-REVIEW-001`
— a fresh-session, independent, read-only review of the updated PR #29
head, verifying N-03 is resolved without re-adjudicating unrelated settled
policy, and reassessing current-head reviews, checks, Preview, and N-04—
has since completed, and **PR #29 has since merged into canonical `main`**
(merge commit `4d8f29e91783179be145241df723d797d99da63a`). Post-merge
verification found that canonical `main`'s repository-wide WebGL/Three.js
absence statements (in this file and eight other documentation files)
contradicted the fact that paused, open, unmerged PR #28 already implements
that renderer foundation. Two prior remediation attempts stopped short
(`BLOCKED_MODEL_A_CONTRACT_POST_MERGE_STATE_SYNC_SCOPE_CONFLICT`,
`BLOCKED_MODEL_A_POST_MERGE_STATE_SYNC_ADDITIONAL_SCOPE_DISCOVERED`); a
read-only scope-lock audit then identified exactly nine files requiring
correction
(`PASS_MODEL_A_POST_MERGE_STATE_SYNC_SCOPE_LOCK_COMPLETE`). This task,
`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-POST-MERGE-STATE-SYNC-003`,
applies that nine-file, documentation-only correction (this file among
them) on a dedicated local branch, with one local commit and no push. It
does not merge, deploy, waive Gate B, or authorize Model B. **Exact next
task:** `MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-POST-MERGE-STATE-SYNC-REVIEW-003`
— independent review of this commit, required before it may be pushed,
reviewed as a PR, and merged. Model B
(`MELLYCORE-MODEL-B-DEPLOYMENT-SEPARATION-DECISION-001`) remains **blocked,
not started**, and is not immediately executable: it requires this review
to pass, a separately authorized push, PR review, merge, and post-merge
truthful-state verification first. Not authorized to merge, resolve
comments, or deploy, and unrelated to closing PR #28's Gate B.

## Historical Option B Deploy Path — Completed

The operator selected Option B: first deploy bundles the Source Arena static
renderer slice, an OpenRouter Model/Cost Observatory (static snapshot only,
no live calls/keys/backend), and safety-state labels. Full sequence and
gating detail: `shared_context/ROADMAP.md`'s "Option B Deploy Path" section.

**Closed steps.** PR #17 (branch
`feat/mellycore-source-arena-renderer-static-slice-001`, reviewed head
`4af0402d9ded634ba65d14f2013d7280b46296db`) is **merged into canonical `main`**
via merge commit `537a84c8132bcb5fec568b1776bc4c656af3f0c2`
(2026-07-23T11:41:42Z). The Sourcery XSS/static-analysis finding was remediated
before merge, so both the XSS triage and the merge gate are closed. The
post-merge living-docs sync is canonical via PR #19, merge commit
`b72bcbdacb61435f7cbc150fffc50ff87d1f3db9`. The OpenRouter Observatory spec is
**merged into canonical `main` via PR #20**, merge commit
`f1e177e38a26cfc80e047c8481d7932ad4419487`.

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001` added the
Observatory tab (Model Constellation, Cost Radar, Route Advisor, Budget
Estimator, Capability Matrix, Fallback Chain, Safety Boundary Strip) against
a local static fixture in
`site/js/dashboard.js`/`site/dashboard.html`/`site/css/dashboard.css` only.
All cost/context-window fields are `null` (no reviewed pricing source on
file) — the estimator correctly shows `INSUFFICIENT PRICING DATA` throughout,
per spec.

Its full gate chain, all on branch
`feat/mellycore-openrouter-model-observatory-static-snapshot-slice-001`:
`-REVIEW-001` returned `NEEDS_FIXES` (one P1 mobile horizontal-page-scroll
defect caused by `.obs-main { display: contents }` breaking width
containment for descendant grids/flex rows/tables; one P3
`obs-matrix-body` class/id naming collision) → `-REMEDIATION-001` fixed both
(every direct Observatory card pinned to `width:100%; max-width:100%;
min-width:0` at the mobile breakpoint; matrix wrapper renamed) →
`-REVIEW-002` returned `PASS_STATIC_SNAPSHOT_SLICE_REVIEW_002` →
`-VISUAL-ACCEPTANCE-001` returned
`NEEDS_POLISH_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE` (catalogue-like
constellation, routing decision too low, mobile catalogue before advisor) →
`-VISUAL-POLISH-001` fixed it with a CSS/DOM router core, orbital model
lanes, restored first-viewport decision hierarchy, and corrected mobile
order → `-VISUAL-ACCEPTANCE-002` returned
`NEEDS_POLISH_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE_002` (Budget Estimator
began behind the fixed footer at 1440×900) → `-VISUAL-POLISH-002` fixed it
with a desktop-only spacing rule → `-VISUAL-ACCEPTANCE-003` returned
`PASS_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE_003`.

**`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-PUBLISH-001`
is complete: pushed the four-commit branch, opened, reviewed, and merged
[PR #21](https://github.com/Melly-999/mellycore-aios-core/pull/21) into
canonical `main` via merge commit
`6897b5f31528c47f1a5186de4f854484dc3d71de` (2026-07-23T16:19:42Z).** The
OpenRouter Observatory static snapshot slice is now canonical, not merely
branch/PR-scoped. No live API, key, backend, or deploy work occurred at any
point in this chain.

Historical next task at that point:
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-POST-MERGE-STATE-SYNC-001`
(that docs-sync entry, since completed). This pointer is retained only as
historical sequencing evidence and is **not** the current repository-wide
next task — see the "Vercel Static Root" section above for the current
pointer.

Historical sequence, in order (all subsequently completed):

1. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-POST-MERGE-STATE-SYNC-PUBLISH-001`
   — push, PR, review, merge this docs sync.
2. `MELLYCORE-STATIC-DEPLOYMENT-READINESS-001`
3. `MELLYCORE-STATIC-SHOWCASE-DEPLOYMENT-001` (only if explicitly authorized)
4. `MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001`
5. `MELLYCORE-DEPLOYMENT-STATE-SYNC-001`

At the time this sequence was queued, no later gate had started and each
still required its own pass in order. This is historical sequencing context;
the sequence has since closed as recorded above. No WebGL/Three.js or
OpenRouter live-API implementation was authorized ahead of those gates.

## Integration Status (AI Operations Intelligence)

`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001` is **integrated into canonical
`main` via PR #7**. This gate is closed; it is recorded here only as history,
not as a pending step.

## Operations Data Contract — Integration Status

`MELLYCORE-OPERATIONS-DATA-CONTRACT-001` (branch
`docs/mellycore-operations-data-contract-001-v2`, tip commit `44dde78`) is
**integrated into canonical `main` via PR #13**
(https://github.com/Melly-999/mellycore-aios-core/pull/13), merge commit
`e0db28f06613d29028df96a2d651b6dfdf2f2aa8`. This gate is closed; it is
recorded here only as history, not as a pending step.

Integration is documentation/schema/fixture scope only: the fourteen
entities defined in `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`,
and their companion JSON Schema and example fixtures in
`shared_context/operations/`, now exist on canonical `main`. No adapters,
backend execution, autonomous improvement, runtime-consumed schema,
scheduler, or safety-rule mutation was implemented or authorized by this
merge; no script in `scripts/` reads, imports, or validates these files (see
`shared_context/operations/README.md`).

`MELLYCORE-OPERATIONS-DATA-CONTRACT-BRANCH-RECONCILIATION-001` had already
selected `docs/mellycore-operations-data-contract-001-v2` as the canonical
integration candidate ahead of this merge (see spec Section 6). The original,
differently-scoped `docs/mellycore-operations-data-contract-001` branch
(2026-07-19) was never merged, rebased, deleted, or pushed and remains a
superseded local branch; its adoptable content (`AI_ESTATE`,
`SKILL_GAP_CANDIDATE`, `MEMORY_FRESHNESS` schema/example pairs, and
`TRUTHFUL_STATE_LABELS.md`) had already been folded into `-v2` before this
merge by `MELLYCORE-OPERATIONS-DATA-CONTRACT-AI-ESTATE-SKILLGAP-MEMORY-001`.

Full merge evidence and validation: durable report
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-POST-MERGE-STATE-SYNC-001.md`.
The original task report,
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-001.md`, is a historical
snapshot of local-only state prior to reconciliation and merge; it is not a
current-state claim.

Exact next task:
`MELLYCORE-OPERATIONS-DATA-CONTRACT-POST-MERGE-STATE-SYNC-REVIEW-001`
(independent re-review of this state sync; not started). No Operations Data
Contract implementation, adapter, backend, or runtime task is authorized by
this entry.

## Later Roadmap Domains

After a reviewed intelligence specification, separately approved work may address
real adapters, guarded operations, observability UI, and validation evidence.
No implementation task is authorized by this queue entry.

## Parallel Decision Track — Source Arena Renderer

This track is independent of, and does not reorder, the primary roadmap
sequence above. `MELLYCORE-OPERATIONS-DATA-CONTRACT-001` integration has
**no ordering relationship** with this track: it is not a prerequisite, gate,
blocker, dependency, sequencing step, or required prior task for this track
or for `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`, and it does not
supersede this track. This track's work may be independently authorized and
reviewed on its own gates regardless of whether that contract's integration
is pending, in progress, or complete.

1. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001` — complete (docs-only).
   Records `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`, status
   PROPOSED.
2. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001` — independent
   review complete. Outcome: **`NEEDS_FIXES`** (findings HR-01 through HR-06).
2a. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REMEDIATION-001` — complete.
   Closed HR-01 through HR-06 in the ADR, the Holographic UI Spec amendment
   notice, this file, and other shared-context files; ADR status remained
   PROPOSED.
2b. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-002` — independent
   re-review complete. Outcome: **`NEEDS_FIXES`** on two residual findings
   (RF-01, RF-02); HR-01 through HR-06 confirmed closed.
2c. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REMEDIATION-002` — complete
   (this commit, docs-only). Closed RF-01 (corrected
   `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md`'s "What this serves"
   section, which previously described the whole `site/` scaffold as having
   no JavaScript) and RF-02 (added an Appendix A §A.1 row mapping the
   Holographic UI Spec §6.2.4 planned README truthfulness-table entry to its
   future provider-neutral replacement); ADR status remains PROPOSED. Exact
   next task: `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-003`
   (independent re-review; not started). Implementation remains blocked
   pending that review's PASS and separate operator acceptance of the ADR.
2d. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-003` — independent
   re-review complete. Outcome: **`PASS_HYBRID_RENDERER_ADR_REVIEW_003_COMPLETE`**;
   RF-01 and RF-02 confirmed closed alongside HR-01 through HR-06; three valid
   signed commits; exact scope confirmed; 245/245 tests passing.
2e. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-001` — complete
   (docs-only). The operator explicitly accepted the ADR on
   2026-07-20 at reviewed baseline `b95a741231d18ef712379837c7167aa22b37d42f`.
   ADR status became **ACCEPTED** (decision/specification level only — see
   `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`'s acceptance
   record). No Three.js implementation, dependency acquisition, or NASA
   retirement was authorized by this acceptance.
2f. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-REVIEW-001` —
   independent re-review. Outcome: `NEEDS_FIXES` — two persisted gating-text
   contradictions in ADR Section 7's table header and Appendix A's NASA-row.
2g. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-REMEDIATION-001` —
   closed both findings with two localized wording corrections; no
   architecture, scope, or status change.
2h. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-REVIEW-002` —
   independent re-review. Outcome:
   **`PASS_HYBRID_RENDERER_ADR_ACCEPTANCE_REVIEW_002_COMPLETE`**.
2i. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-001` — pushed the branch to
   canonical `clean-origin` and opened draft PR
   [#8](https://github.com/Melly-999/mellycore-aios-core/pull/8). No merge,
   implementation, or NASA action.
2j. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-REVIEW-001` — independent
   PR review. Outcome: `PASS_HYBRID_RENDERER_ADR_PR_REVIEW_COMPLETE`.
2k. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-READY-001` — marked PR #8
   ready for review. Sourcery's ready-state check did not trigger a fresh run
   (its own external weekly diff-character quota was already exhausted);
   recorded as `WAIVED_UNAVAILABLE_BY_OPERATOR` /
   `EXTERNAL_WEEKLY_RATE_LIMIT_NOT_CODE_FAILURE`, never reported as passing.
   `main` has no branch protection or required status checks.
2l. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-MERGE-001` — merged PR #8
   into canonical `main` via merge commit
   `f93be7018a1da3bba50eb66346b1f9e627a46dd2` (parents
   `06a7a421a06abbe38450d276af94985da8ddeba0` and
   `dcfcd8db2089e6f27b5aea59446244bf964f4aea`), confirmed by independent
   pre- and post-merge fresh-clone validation (245/245 tests each). ADR
   status is now **`ACCEPTED_CANONICAL_MAIN`**. No renderer implementation,
   Three.js vendoring, NASA retirement, or release/deployment occurred.
2m. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-001` —
   synchronized current documentation to the merged state and resolved a
   non-blocking Codex clarity finding in ADR Section 31. Its independent
   review did not remain "not started": it ran to completion through the
   chain recorded in 2n–2r below.
2n. Independent post-merge canonical-state review (read-only) — after PR #9
   merged 2m into canonical `main` at `c7e24b8207598c600bb168a07959aeec7bebe003`,
   this review found `shared_context/AGENT_HANDOFF.md` self-contradictory on
   whether Operations Data Contract integration gates
   `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`. Outcome: `NEEDS_FIXES`.
2o. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-P2-REMEDIATION-002`
   — fixed that contradiction (docs-only); its own review
   (`-REVIEW-001`) passed; opened PR
   [#10](https://github.com/Melly-999/mellycore-aios-core/pull/10);
   `-PR-REVIEW-001` found no blocking issue, but the pre-merge gate check
   (`-MERGE-001`) itself surfaced a new Codex P2 finding — residual "does not
   begin before" wording still readable as an ordering constraint — and
   stopped with `NEEDS_FIXES` before merging.
2p. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-P2-REMEDIATION-003`
   — removed that residual wording, replacing it with an explicit
   "no ordering relationship" statement; its own review (`-REVIEW-001`)
   passed; pushed to PR #10 (`-PUSH-001`); `-PR-REVIEW-002` found no
   blocking issue; `-MERGE-001` passed every gate and merged PR #10 into
   canonical `main` via merge commit
   `b3b4f8b0124b8ee10c8ab6e5334cd35cf059fc88` (parents
   `c7e24b8207598c600bb168a07959aeec7bebe003` and
   `416a6f2ef1a69dd53c957e6a77cc5cd9633c1ad4`).
2q. A fresh independent canonical-state review of that merged state returned
   `NEEDS_FIXES`: residual "does not begin before" wording persisted in this
   file (above) and in ADR Section 31; `AGENT_HANDOFF.md`'s living
   "Exact next task" pointer still named the already-completed PR #9
   publication task; and this file's own item 2m still described its review
   as "not started" after it had, in fact, completed (2n above).
2r. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-P2-REMEDIATION-004`
   — removed the residual ordering wording from this file and ADR Section
   31, corrected `AGENT_HANDOFF.md`'s stale task pointer, and corrected this
   file's stale review-status claim. No renderer, CSS fallback, Three.js,
   NASA, runtime, release, or deployment change. That entry's then-next-task
   did not remain "not started": it ran to completion, recorded in 2s–2t
   below.
2s. Independent review of `-P2-REMEDIATION-004` returned `NEEDS_FIXES`: a
   further stale, unqualified "exact next task" pointer to the
   already-completed `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-REVIEW-001`
   remained in this file's Deferred Work summary for the renderer ADR
   (above).
2t. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-P2-REMEDIATION-005`
   — this entry (docs-only): corrected that pointer. No renderer, CSS
   fallback, Three.js, NASA, runtime, release, or deployment change. That
   entry's then-next-task ran to completion, recorded in 2u below.
2u. `-P2-REMEDIATION-005-REVIEW-001` returned `PASS` (no blocking finding) →
   `-PUBLISH-001` pushed the branch to `clean-origin` and opened
   [PR #11](https://github.com/Melly-999/mellycore-aios-core/pull/11) →
   `-PR-REVIEW-001` found no blocking review (Sourcery and Codex both
   `COMMENTED`, non-blocking) → `-MERGE-001` merged PR #11 into canonical
   `main` via merge commit `cad4e07f73f80c5794f9af2897fc10d922637ab3`
   (parents `b3b4f8b0124b8ee10c8ab6e5334cd35cf059fc88` and
   `48c1622610f0d3ac258c0f5c2b1b3a2b63209032`) → `-POST-MERGE-VERIFY-001`
   confirmed the merge commit, parentage, and changed-file scope
   independently. `-P2-CLOSEOUT-001` (this entry's closeout) closes this
   documentation-remediation chain: no renderer, CSS fallback, Three.js,
   NASA, runtime, release, or deployment change occurred at any step. Exact
   next task: `MELLYCORE-DOCS-INTEGRATION-REVIEW-001` (docs/spec-scope
   review; not started).
3. `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001` — remove active NASA
   API calls and `nasa-*` active runtime handles from the Source Arena surface,
   preserving historical evidence. Status: `MERGED_INTO_CANONICAL_MAIN` —
   implemented on branch `fix/mellycore-source-arena-nasa-runtime-retirement-001`,
   merged via PR #15, merge commit `e0cbc332ff90f8787d981c9d86be717633f22d4d`
   (reviewed head `1478b95c82cb85fd5e0efdf433e928ca92cac69b`). Replaced the
   executable NASA Images fetch/parse/boot path in `site/js/dashboard.js`
   with a local, deterministic Source Archive dataset (zero external
   requests, no API key) and renamed the `nasa-*` runtime namespace to
   `source-arena-*` per this ADR's Appendix A mapping. Visual acceptance
   (`...-FINAL-REVIEW-001`) returned `PASS_WITH_NON_BLOCKING_NOTES`; VA-01
   (procedural swatch palette) and VA-02 (mission-rail scrollbar) were
   resolved before merge; VA-03 through VA-09 remain deferred, non-blocking
   backlog polish. Does not implement task 4 (the 3D scene foundation),
   vendor Three.js, or touch the CSS-fallback/renderer boundary. Exact next
   task: `MELLYCORE-SOURCE-ARENA-NASA-RETIREMENT-POST-MERGE-STATE-SYNC-PUBLISH-001`
   (push this docs-sync commit, open a PR, review, and merge if clean).
4. `MELLYCORE-3D-SCENE-FOUNDATION-001` — implement the shared state, complete
   CSS fallback, vendored/pinned Three.js enhanced renderer, lifecycle,
   context-loss recovery, and mobile-first Source Arena. Implemented in
   [PR #28](https://github.com/Melly-999/mellycore-aios-core/pull/28), open
   and **intentionally paused** — see "3D Scene Foundation — PR #28 Paused
   State" above.
5. `MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001` — keyboard/screen-reader
   parity, reduced-motion, forced-fallback, context-loss, memory/RAF cleanup,
   mobile and desktop performance. Desktop Gate A passed (repository-verified).
   Physical Android Chromium Gate B remains `OPEN / NOT EXECUTED`
   (`BLOCKED_3D_SCENE_QA_REFERENCE_DEVICE_UNAVAILABLE`) — the durable open
   acceptance gate; do not rerun until a named physical device is available.
6. `MELLYCORE-3D-SCENE-INTEGRATION-REVIEW-001` — independent final review
   before any merge or release claim. Outcome
   `PASS_WITH_NOTES_3D_SCENE_INTEGRATION_REVIEW` recorded as
   operator-confirmed external/session evidence, dated 2026-07-27 — not
   independently repository-verified prior to this sync.

Task 3 (NASA runtime retirement) is `MERGED_INTO_CANONICAL_MAIN` via PR #15,
merge commit `e0cbc332ff90f8787d981c9d86be717633f22d4d` (see item 3 above).
Task 4 is implemented in PR #28 (open, paused, unmerged); task 5 remains open
only on physical-device Gate B after desktop Gate A passed; task 6's outcome
is recorded as operator-confirmed session evidence, not yet independently
repository-verified. None of these entries authorizes merge, waiver, or
deployment of PR #28. Task 1 (the ADR decision) is accepted at the
decision/specification level and its architecture milestone is now
`CLOSED_IN_CANONICAL_MAIN` — merged into canonical `main` via PR #8 (2l
above).

A narrow, separate precursor — `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-001`
— is `MERGED_INTO_CANONICAL_MAIN` (branch
`feat/mellycore-source-arena-renderer-static-slice-001`, reviewed head
`4af0402d9ded634ba65d14f2013d7280b46296db`, merged via PR #17, merge commit
`537a84c8132bcb5fec568b1776bc4c656af3f0c2`, 2026-07-23T11:41:42Z). It restyles
the Source Arena stage into a static CSS/DOM holographic source map (orbital
source nodes around a central core, command inspector), replacing the prior
social-feed-style media card. It is CSS/DOM only: it does not start task 4,
vendor Three.js, add WebGL/Canvas, or implement the ADR's CSS-complete
fallback spec — all of which remain `NOT_IMPLEMENTED`/`NOT_STARTED`.

## Parallel Decision Track — Enterprise Provider Integration

This track is **independent of, and does not reorder,** the primary live
sequence above — `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`
remains the current live next task for that sequence (see "Current —
OpenAI Batch Final Canonical State Reconciliation Gate"). It records newly
incorporated architectural research, not previously completed repository
work, per `MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001`.

1. `MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001` — synchronizes
   `PROJECT_STATE.md`, `ROADMAP.md`, this file, and `AGENT_HANDOFF.md` with
   completed enterprise-provider architectural research (integration
   fabrics, OpenClaw, cybersecurity/marketing provider tiers, Cloudflare
   P0 candidacy and legacy exclusions). **Complete: one local documentation
   commit, not pushed.** Durable report:
   `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001.md`.
2. `MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001` — canonical
   provider-selection and integration-fabric decision record. **Complete:
   one local documentation commit, not pushed.** Canonical decision:
   `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`.
   Durable report:
   `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001.md`.
3. `MELLYCORE-CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001` — Cloudflare
   capability/authorization/approval/audit/rollout/legacy-exclusion
   contract. **Complete: one local documentation commit, not pushed.**
   Canonical contract:
   `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
   (specification-level acceptance only — no implementation, credential,
   authentication, API execution, MCP, or deployment authorization).
   Durable report:
   `docs/tasks/MELLYCORE-CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001.md`.
   `MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001`
   (documentation-integrity correction, not a new architectural milestone)
   subsequently corrected fifteen stale internal section cross-references
   in the accepted ADR and recorded the preceding task's single
   unpublished-commit amend as a classified procedural deviation
   (`PASS_WITH_PROCEDURAL_DEVIATION`) via an append-only commit — no
   existing commit was rewritten and no substantive Cloudflare-contract or
   ADR decision changed. **Complete: one local documentation commit, not
   pushed.** Durable report:
   `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md`.
4. `MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001` — extends the
   Provider Registry contract for enterprise SaaS, marketing, and
   cybersecurity systems. **Complete: one local documentation commit, not
   pushed.** Canonical contract:
   `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
   (specification-level acceptance only — no registry implementation,
   adapter, credential, provider authentication, provider API call
   including read-only, MCP or fabric connection, or deployment
   authorization). Extends, without modifying,
   `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`'s
   §7.2 entity catalogue and §9.1 Provider Registry module. Durable
   report:
   `docs/tasks/MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001.md`.
5. `MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001` — trust boundary
   between MellyCore, direct adapters, MCP servers, and integration
   fabrics. **Specification complete after recovery remediation and
   validation; publication remains local and unpushed.**
   Canonical contract:
   `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
   (specification-level acceptance only — no Gateway implementation,
   adapter, credential, provider authentication, provider API call
   including read-only, MCP or fabric connection, webhook registration, or
   deployment authorization). It is the Data Plane architecture and threat
   model that
   `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` §3.2
   requires before any future Data Plane may consume approved manifests,
   and it extends that spec's §9.6 Integration Gateway display module
   without modifying it. Of the two items the Provider Registry contract
   deferred here, it resolved the **shape** of tenant-provider and
   tenant-capability authorization records (explicit, separate,
   independently revocable, absence denies) and assigned their storage and
   issuance workflow to the Provider Registry and their runtime resolution to
   the Integration Gateway. The fabric equivalence-evidence standard was
   subsequently resolved by item 8's remediation. Durable report:
   `docs/tasks/MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001.md`.
6. `MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001` — first read-only
   cybersecurity provider pack. **Specification complete; publication
   remains local and unpushed.** Canonical specification:
   `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`
   (P0 Microsoft Defender XDR / Microsoft Graph Security, GitHub Advanced
   Security, Cloudflare, and Okta; P1 Splunk and CrowdStrike Falcon; P2
   Snyk; R0-R2 only, with R3-R5 deferred). Specification-level acceptance
   only — no provider connection, credential, adapter, runtime, provider
   API call, MCP/fabric connection, webhook registration, or deployment
   authorization. Durable report:
   `docs/tasks/MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001.md`.
7. `MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001` — first read-only
   marketing analytics/CRM provider pack. **Specification complete;
   publication remains local and unpushed.** Canonical specification:
   `docs/specs/MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001.md` (P0 HubSpot,
   Google Analytics 4, Google Ads, Meta Marketing API, LinkedIn Marketing
   API, and Twilio Segment; P1 Salesforce Marketing Cloud, Braze, and
   Klaviyo; P2 Adobe Experience Platform; R0-R2 only, with R3-R5 deferred).
   Specification-level acceptance only — no provider connection, credential,
   adapter, runtime, tracking, audience/campaign operation, provider API call,
   MCP/fabric connection, webhook registration, or deployment authorization.
   Durable report:
   `docs/tasks/MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001.md`.
8. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001` — final
   integration review across 25 documents, 26 dimensions, and 12 scenarios.
   **Complete; `FAIL_REMEDIATION_REQUIRED` (P0 = 0, P1 = 4, P2 = 2,
   P3 = 3).** Canonical review:
   `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md`.
   `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001` claimed all
   nine findings closed; canonical fabric comparison:
   `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md`. Item 9
   independently verified eight as `CLOSED` and `P1-003` as
   `PARTIALLY_CLOSED`.
9. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002` — independent
   post-remediation integration gate across 19 documents and 16 determinism
   scenarios. **Complete; `FAIL_REMEDIATION_REQUIRED` (P0 = 0, P1 = 1, P2 = 0,
   P3 = 3).** Blocking finding `P1-201`: Provider Registry §13.2's closed,
   mandatory eight-value credential-profile-class catalogue cannot express the
   accepted Cloudflare connector contract's `CF_MCP_OPERATOR` profile, nor
   state the `CF_READ` mapping unambiguously, and Integration Gateway
   §§34.1–34.6 still present `CF_*` values as "Credential class" although
   Gateway §14.2 now denies anything that is not one exact Registry §13.2
   identifier. Canonical review:
   `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md`.
   Durable report:
   `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002.md`.
   The documentation gate has **not** passed.
10. `MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001`
   — **complete in one local documentation-only commit; not pushed.** Registry
   §13.2 now owns a closed nine-value canonical credential-profile-class
   catalogue, including `restricted_operator_investigation`. Cloudflare's four
   provider-specific requirement labels and residual coarse
   `credential_class: investigation` metadata now project deterministically to
   exactly one canonical class before Gateway evaluation. Gateway §§34.1–34.6
   use only canonical class identifiers, and the three P3 maintenance findings
   are routed. The documentation gate has **not** passed; `P1-201` closure is
   not independently verified. Durable report:
   `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001.md`.
11. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003` — **complete in
   one local documentation-only commit; not pushed. Gate failed.**
   `FAIL_REMEDIATION_REQUIRED` with P0 = 0, P1 = 2, P2 = 1, P3 = 2 across 17
   documents and 16 determinism scenarios. `P1-201` is `PARTIALLY_CLOSED` —
   the ninth canonical class, the one-class D4 binding, the derived
   non-normative `credential_class: investigation` value, and the `CF_READ`
   projection are independently verified closed. Open: `P1-301`, the Gateway
   acting-identity model (§9.2, Rule 16.7, §17 step 13, §23) admits only
   `delegated_user` or `service_account` and cannot express
   `restricted_operator_investigation`'s `mellycore_operator` identity; and
   `P1-302`, Registry §26.1's `required_scope_dimensions: tenant, account,
   zone` for provider `cloudflare` contradicts Cloudflare §11.2 rule 2's
   mandatory empty D4 account/zone/resource binding. Both fail in the deny
   direction; 58 capability rows and 13 prohibition rows are byte-identical to
   the pre-remediation commit and no safety regression was found. Canonical
   review:
   `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_003.md`.
   Durable report:
   `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003.md`.
   The documentation gate has **not** passed.
12. `MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001`
   — **exact next task; not started.** Must reconcile the Integration Gateway
   acting-identity model and the Provider Registry provider-record scope model
   with `restricted_operator_investigation`, without weakening any fail-closed
   default and without granting that class provider-account, provider-API, or
   mutation authority, and must route the remaining P2 and P3 findings. A
   further independent review must follow before scaffold eligibility is
   reconsidered.
13. `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` — **blocked**, not started,
   ineligible, and not authorized. May only be considered after item 12 and a
   further passing independent review, and separate explicit
   Operator authorization is issued, independent of Model A/B deployment
   authorization and independent of the OpenAI Batch Stage C gate.

Blocked pending this track's own gates and separate explicit authorization,
regardless of any other track's state: provider credentials of any kind,
provider runtime, any MCP connection to a provider, any Cloudflare API
call or mutation — **including read-only Cloudflare API calls, which
acceptance of the item 3 connector contract does not unblock** (that
contract is specification-level only; its Section 35 keeps read-only access
blocked until the full documentation gate passes and a separate explicit
Operator authorization is given) — any marketing campaign action, any
cybersecurity remediation action, and provider adapter scaffolding.

## Deferred Work

- Cross-agent context smoke testing remains a separate clean-worktree task.
- Provider/runtime integrations, deployment, releases, and Holographic UI
  implementation remain separately gated.
- Legacy NASA prototype cleanup is a future implementation decision, not part of
  the current product roadmap and not performed by the positioning task.

## Completed Milestone Index

- Static homepage and Living Context Graph prototype — historical reports under
  `docs/tasks/` and showcase evidence under `docs/showcase/`.
- Operational Trust / Loop Operations — closed; architecture and task evidence
  under `docs/architecture/`, `docs/research/`, and `docs/tasks/`.
- Context Gate I1–I4 — implemented; canonical evidence under
  `shared_context/context_provenance/` and completed reports under `docs/tasks/`.
- Live Cockpit V2 / `v0.2.0` — historical release and legacy prototype evidence.
- Holographic UI specification / PR #4 — accepted documentation; Source Arena
  hero contract preserved, implementation not claimed.
- Positioning refresh — integrated into canonical main; durable report at
  `docs/tasks/MELLYCORE-POSITIONING-REFRESH-001.md`.
- AI Operations Intelligence specification — integrated into canonical `main`
  via PR #7; durable report at
  `docs/tasks/MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001.md`.
- Source Arena Hybrid renderer ADR — status **`ACCEPTED_CANONICAL_MAIN`**
  (decision/specification level only); merged into canonical `main` via PR #8,
  merge commit `f93be7018a1da3bba50eb66346b1f9e627a46dd2`, 2026-07-20; durable
  report at
  `docs/tasks/MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001.md`. Full review
  chain (all durable reports under `docs/tasks/`): review 001 `NEEDS_FIXES` →
  remediation 001 → review 002 `NEEDS_FIXES` → remediation 002 → review 003
  `PASS` → operator acceptance → acceptance review 001 `NEEDS_FIXES` →
  acceptance remediation 001 → acceptance review 002 `PASS` → pushed and
  opened as PR #8 → PR review `PASS` → marked ready (Sourcery waived as
  unavailable, not passed) → merged. No Three.js implementation, dependency
  vendoring, NASA runtime retirement, or release/deployment exists. That
  entry's then-next-task,
  `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-REVIEW-001`,
  has since completed (see the Parallel Decision Track above, items 2n–2r),
  as has the subsequent `-P2-REMEDIATION-005` review/publish/merge chain
  (items 2s–2u): PR #11 merged into canonical `main` via merge commit
  `cad4e07f73f80c5794f9af2897fc10d922637ab3`. No Three.js implementation,
  dependency vendoring, NASA runtime retirement, or release/deployment
  exists at any point in this chain. Its then-current exact next task was
  `MELLYCORE-DOCS-INTEGRATION-REVIEW-001`; the live current pointer is the
  OpenAI Batch post-merge documentation gate above.

## Standing Safety Gate

No push, PR, merge, force operation, rebase, squash, branch deletion, tag,
release, deploy, workflow mutation, trading behavior, credential storage, or
retired-remote contact without explicit operator authorization.
