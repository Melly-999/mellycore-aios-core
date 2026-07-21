# Run Queue

This file contains actionable sequencing and gates. Completed-task detail belongs
in `docs/tasks/` and Git history, not duplicated here.

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
   preserving historical evidence. Status: `IMPLEMENTED_LOCALLY_PENDING_REVIEW`
   / `DRAFT_PR_OPEN_PENDING_VISUAL_ACCEPTANCE` — implemented on branch
   `fix/mellycore-source-arena-nasa-runtime-retirement-001` (one commit ahead
   of canonical `main` at the time of this entry), pushed, and opened as a
   draft PR. Not merged. Replaces the executable NASA Images fetch/parse/boot
   path in `site/js/dashboard.js` with a local, deterministic Source Archive
   dataset (zero external requests, no API key) and renames the `nasa-*`
   runtime namespace to `source-arena-*` per this ADR's Appendix A mapping.
   Does not implement task 4 (the 3D scene foundation), vendor Three.js, or
   touch the CSS-fallback/renderer boundary. Exact next task:
   `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-VISUAL-ACCEPTANCE-001`.
4. `MELLYCORE-3D-SCENE-FOUNDATION-001` — implement the shared state, complete
   CSS fallback, vendored/pinned Three.js enhanced renderer, lifecycle,
   context-loss recovery, and mobile-first Source Arena. Not started.
5. `MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001` — keyboard/screen-reader
   parity, reduced-motion, forced-fallback, context-loss, memory/RAF cleanup,
   mobile and desktop performance. Not started.
6. `MELLYCORE-3D-SCENE-INTEGRATION-REVIEW-001` — independent final review
   before any merge or release claim. Not started.

Task 3 (NASA runtime retirement) is `IMPLEMENTED_LOCALLY_PENDING_REVIEW` with
a draft PR open, not merged (see item 3 above). Tasks 4–6 remain
`NOT_STARTED` and are not implemented, active, or authorized by this entry
alone. Task 1 (the ADR decision) is accepted at the decision/specification
level and its architecture milestone is now `CLOSED_IN_CANONICAL_MAIN` —
merged into canonical `main` via PR #8 (2l above). This does not implement,
vendor, or release anything; the 3D scene foundation (task 4) remains
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
  vendoring, NASA runtime retirement, or release/deployment exists. That
  entry's then-next-task,
  `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-REVIEW-001`,
  has since completed (see the Parallel Decision Track above, items 2n–2r),
  as has the subsequent `-P2-REMEDIATION-005` review/publish/merge chain
  (items 2s–2u): PR #11 merged into canonical `main` via merge commit
  `cad4e07f73f80c5794f9af2897fc10d922637ab3`. No Three.js implementation,
  dependency vendoring, NASA runtime retirement, or release/deployment
  exists at any point in this chain. The current exact next task is
  `MELLYCORE-DOCS-INTEGRATION-REVIEW-001`.

## Standing Safety Gate

No push, PR, merge, force operation, rebase, squash, branch deletion, tag,
release, deploy, workflow mutation, trading behavior, credential storage, or
retired-remote contact without explicit operator authorization.
