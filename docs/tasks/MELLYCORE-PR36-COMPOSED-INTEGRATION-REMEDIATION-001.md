# MELLYCORE-PR36-COMPOSED-INTEGRATION-REMEDIATION-001

## Purpose

Resolve only `PR36-INT-001`, the P1 living canonical-state truth-drift finding
from `MELLYCORE-PR36-COMPOSED-INTEGRATION-REVIEW-001`, without changing the M2
site, product model, architecture, runtime, providers, tests, Roadmap, or
deployment configuration.

## Pinned input

- PR: #36
- Source SHA: `a71846f1800b921b509995ac2b65b317fcf290bf`
- Expected canonical base: `947f33d27d5546775186e96bdc61e30db78c0b3d`
- Source remote branch: `review/mellycore-m2-showcase-acceptance-003`
- Remediation branch: `fix/mellycore-pr36-composed-integration-remediation-001`
- Remediation worktree:
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-pr36-composed-integration-remediation-001`

Preflight independently reverified that PR #36 was open and non-draft, its head
was the exact source SHA above, and `clean-origin/main` was the exact expected
base before the isolated worktree was created.

## Reconciled current state

- M2: `COMPLETE`
- M2 Acceptance: `ACCEPTED_WITH_NON_BLOCKING_LIMITATIONS`
- `SHOWCASE_READY = YES`
- Accepted release SHA:
  `a71846f1800b921b509995ac2b65b317fcf290bf`
- Push: `COMPLETE`
- Remote branch: `review/mellycore-m2-showcase-acceptance-003`
- PR: #36 `OPEN`
- Merge: `NOT PERFORMED` / `NOT AUTHORIZED`
- `PUBLIC_SHOWCASE = NOT_RELEASED` for this M2 release
- Production verification for PR #36: `NOT PERFORMED`
- Provider/runtime activation: `NO`
- Composed Integration Review: `NEEDS_REMEDIATION`
- Finding: `PR36-INT-001` — P1 living canonical-state truth drift
- Remediation: this task, local governance-only commit
- Next task:
  `MELLYCORE-PR36-COMPOSED-INTEGRATION-REMEDIATION-REVIEW-001`
- Production-impacting merge: `BLOCKED` pending independent remediation review
  and later exact-head, explicit Operator authorization

## Pointer model

The living owners now distinguish four concepts:

1. **Repository-wide global pointer:**
   `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains the
   independently governed `IN_PROGRESS` priority umbrella. It is not a provider
   execution authorization, and its internal gate must be verified from its
   separate lineage and newest task/Git/GitHub evidence.
2. **Currently authorized executable lane:** this PR #36 governance
   remediation. The remediation record completes locally in this commit.
3. **M2/public-release lane next task:**
   `MELLYCORE-PR36-COMPOSED-INTEGRATION-REMEDIATION-REVIEW-001`.
4. **Blocked/gated actions:** PR #36 merge and automatic Production publication
   remain blocked; Stage C, provider connection, runtime activation, and spend
   remain unauthorized.

The OpenAI Batch final canonical-state reconciliation review is retained only
as creation-time history. PR #34 already merged that reconciliation into
canonical `main` at `947f33d27d5546775186e96bdc61e30db78c0b3d`.

## Files changed

- `shared_context/PROJECT_STATE.md` — concise current M2/PR/release truth and
  composed-review gate.
- `shared_context/TASK_INDEX.md` — actual M2 release task statuses, exact next
  review task, and clarified global-pointer semantics.
- `shared_context/RUN_QUEUE.md` — coherent global versus executable versus M2
  lane ordering, plus historical reconciliation completion.
- `shared_context/AGENT_HANDOFF.md` — current push/PR/review/remediation state
  and safety boundary.
- `docs/tasks/MELLYCORE-PR36-COMPOSED-INTEGRATION-REMEDIATION-001.md` — this
  durable record.

## Scope and safety

No `site/**`, `scripts/**`, `tests/**`, `docs/specs/**`, `docs/decisions/**`,
`shared_context/ROADMAP.md`, `shared_context/DESIGN_SYSTEM.md`, or
`shared_context/SAFETY_CONTRACT.md` file changes. Product Vision, the exact
two-layer / ten-workspace / 4-3-3 model, M2 design, provider/runtime code, Agent
Runtime architecture, M3, 3D, and Drift implementation remain unchanged.

No push, PR update, merge, deployment, Production verification, provider call,
runtime execution, credential access, or external mutation is authorized or
performed by this task.

## Validation contract

Before the one local commit:

- `git diff --check`
- stage only the five authorized paths
- `git diff --cached --check`
- `py -3.9 scripts/validate_project_state.py`
- verify the exact changed-file allowlist
- verify `site/**`, `shared_context/ROADMAP.md`, and provider/runtime code are
  byte-identical to the source SHA
- verify exactly two top-level layers, ten workspaces, and 4 / 3 / 3 waves
- verify no living M2 state says Showcase Acceptance is next or the accepted
  release lineage is unpushed
- verify PR #36 remains represented as open, merge remains unauthorized,
  `PUBLIC_SHOWCASE = NOT_RELEASED`, and pointers remain coherent

## Decision boundary

This remediation does not approve PR #36 for merge. Its exact next gate is:

`MELLYCORE-PR36-COMPOSED-INTEGRATION-REMEDIATION-REVIEW-001`
