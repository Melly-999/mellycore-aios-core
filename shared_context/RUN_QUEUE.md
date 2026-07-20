# Run Queue

This file contains actionable sequencing and gates. Completed-task detail belongs
in `docs/tasks/` and Git history, not duplicated here.

## Integration Status (AI Operations Intelligence)

`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001` is **integrated into canonical
`main` via PR #7**. This gate is closed; it is recorded here only as history,
not as a pending step.

## Exact Next Roadmap Task

`MELLYCORE-OPERATIONS-DATA-CONTRACT-001`

Status: present only on its separate, unmerged branch
`docs/mellycore-operations-data-contract-001`; not present in canonical `main`.
Status in canonical `main`: `NOT_PRESENT_PENDING_INTEGRATION`. This entry does
not claim that branch's content is canonical and is not modified by this or
any other current task.

Type: documentation/fixture-and-schema specification.

Goal boundary: translate the approved logical contracts in
`docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` (AI Estate
Inventory, Unified Run Ledger, Skill Gap Detector, Memory Freshness Monitor,
Recommendation Ledger, and the exact operator-approval contract) into
fixture/schema artifacts and validation requirements.

Required posture:

- distinguish implemented evidence from planned capability;
- preserve operator approval for consequential action;
- preserve the existing run/token and Context Gate contracts, referencing rather
  than redefining them;
- define visibility, provenance, audit, freshness, and recommendation boundaries;
- do not implement adapters, backend execution, autonomous improvement, merge,
  deployment, scheduler, runtime-consumed schema, or safety-rule mutation;
- do not store provider keys or credentials.

## Later Roadmap Domains

After a reviewed intelligence specification, separately approved work may address
real adapters, guarded operations, observability UI, and validation evidence.
No implementation task is authorized by this queue entry.

## Parallel Decision Track — Source Arena Renderer

This track is independent of, and does not reorder, the primary roadmap
sequence above. It does not begin before, does not supersede, and does not
require `MELLYCORE-OPERATIONS-DATA-CONTRACT-001` to be integrated first.

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
   this entry; synchronizes current documentation to the merged state and
   resolves a non-blocking Codex clarity finding in ADR Section 31. Exact
   next task:
   `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-REVIEW-001`
   (independent review of this sync; not started).
3. `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001` — remove active NASA
   API calls and `nasa-*` active runtime handles from the Source Arena surface,
   preserving historical evidence; may run as the first bounded slice of task 4
   if the accepting review prefers that grouping. Not started.
4. `MELLYCORE-3D-SCENE-FOUNDATION-001` — implement the shared state, complete
   CSS fallback, vendored/pinned Three.js enhanced renderer, lifecycle,
   context-loss recovery, and mobile-first Source Arena. Not started.
5. `MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001` — keyboard/screen-reader
   parity, reduced-motion, forced-fallback, context-loss, memory/RAF cleanup,
   mobile and desktop performance. Not started.
6. `MELLYCORE-3D-SCENE-INTEGRATION-REVIEW-001` — independent final review
   before any merge or release claim. Not started.

None of tasks 3–6 is implemented, active, or authorized by this entry alone.
Task 1 (the ADR decision) is accepted at the decision/specification level and
its architecture milestone is now `CLOSED_IN_CANONICAL_MAIN` — merged into
canonical `main` via PR #8 (2l above). This does not implement, vendor,
retire, or release anything; runtime implementation for tasks 3–6 remains
`NOT_STARTED`.

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
  vendoring, NASA runtime retirement, or release/deployment exists; exact next
  task:
  `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-REVIEW-001`.

## Standing Safety Gate

No push, PR, merge, force operation, rebase, squash, branch deletion, tag,
release, deploy, workflow mutation, trading behavior, credential storage, or
retired-remote contact without explicit operator authorization.
