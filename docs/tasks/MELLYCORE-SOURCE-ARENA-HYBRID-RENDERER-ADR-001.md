# MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001

Status: complete (docs-only). ADR status recorded as PROPOSED, not accepted or
integrated. No site/runtime code touched, no dependency downloaded or vendored,
no `ContextSource`/refusal-log/loop-evidence change, no push, no PR, no merge.
Model: Claude Code (Sonnet 5). Effort: High.

Purpose: create and locally commit the architecture decision that narrowly
permits a Hybrid (WebGL-enhanced, CSS-complete-fallback) Source Arena renderer,
following the operator's Hybrid rendering decision and the corrected scope from
the read-only draft prep tasks that preceded this one.

## Preflight (confirmed before any write)

- Repository identity: `clean-origin` resolves to `Melly-999/mellycore-aios-core`
  (canonical), confirmed via local remote configuration; the unrelated `origin`
  (`Melly-999/mellycore-aios`) was not contacted.
- Canonical `main` re-verified via `git fetch clean-origin main` at the start of
  this task: `06a7a421a06abbe38450d276af94985da8ddeba0`, matching the
  previously-observed SHA — no drift.
- The pre-existing worktree at `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`
  was confirmed to belong to another agent, on branch
  `docs/mellycore-operations-data-contract-001` (HEAD `036ff244a…`), working
  tree clean. It was left untouched for the entire duration of this task —
  verified unchanged (same HEAD, clean status) both before and after this
  task's work.
- A new dedicated worktree and branch were created from verified
  `clean-origin/main`: branch `docs/mellycore-3d-renderer-hybrid-adr-001` at
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-3d-renderer-hybrid-adr-001`.
  Neither the branch name nor the worktree path pre-existed.
- `AGENTS.md` reviewed: read-order and safety rules noted and followed (no
  secrets, no destructive git, no push/merge/deploy without approval, docs-first
  posture, update `AGENT_HANDOFF.md`).
- Operations Data Contract confirmed **not** an ancestor of `clean-origin/main`
  (`git merge-base --is-ancestor` returned false) — still
  `NOT_PRESENT_PENDING_INTEGRATION`. Not modified, not reordered, not treated as
  integrated by this task.
- AI Operations Intelligence specification confirmed **integrated** into
  canonical `main` via PR #7 (`git log clean-origin/main` shows the merge commit
  as `main`'s HEAD) — its modules remain `SPECIFIED`, not runtime-implemented.
  This corrects the earlier read-only draft's stale characterization.

## Corrections applied relative to the earlier read-only draft

1. **Supersession scope** narrowed to exactly Holographic UI Spec §4, §5.4,
   §5.9 (dependency/renderer clause only), and §8 — every other clause,
   including all of E10's non-dependency items, stays binding.
2. **NASA decision** changed from "isolate indefinitely" to: active NASA
   Images search/fetch/runtime integration will be **removed** from the active
   Source Arena surface during the future implementation phase; new
   identifiers must not use `nasa-*`; historical reports/evidence untouched;
   no site change occurs in this docs-only task.
3. **Renderer lifecycle** changed from "dispose on every tab switch" to a
   suspend/resume model: pause rendering when hidden, preserve reusable
   resources during ordinary tab switching where practical, full disposal
   reserved for permanent teardown, unload, unrecoverable init failure, or
   repeated context-loss failure. Idempotence and leak-freedom across ordinary
   transitions must still be proven separately from full-disposal correctness.
4. **Capability detection** changed from "presence of `WebGLRenderingContext`"
   to a guarded, actual `canvas.getContext(...)` attempt in `try`/`catch`,
   performed after the reduced-motion check.
5. **Truthful status**: every new/amended document states plainly that neither
   renderer is implemented, Three.js has not been vendored, and NASA runtime
   retirement has not been performed — verified by direct re-read of this
   task's own diff before commit (see Validation below).

## Files created

- `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`
- `docs/tasks/MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001.md` (this file)

## Files modified

- `docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` — one additive amendment
  notice inserted after the existing 2026-07-18 positioning notice; no
  historical section rewritten or removed.
- `README.md` — "What Exists Today" table gains one row; "Source Arena Visual
  Direction" and "NASA Images Disposition" sections each gain one short,
  clearly-labeled proposed-decision paragraph.
- `shared_context/DESIGN_SYSTEM.md` — "Leading Visual Metaphor" section gains
  one paragraph describing the proposed dual-renderer selection.
- `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md` — one forward-looking note
  added, plus a related-documents link; existing guarantees not altered.
- `docs/3d/README.md` — expanded from a 3-line stub to distinguish the two
  unrelated 3D concepts in this repository (Source Arena Hybrid renderer vs.
  the separate Obsidian Knowledge Graph page concept).
- `shared_context/PROJECT_STATE.md`, `shared_context/RUN_QUEUE.md`,
  `shared_context/AGENT_HANDOFF.md` — synced to record this task, the ADR's
  PROPOSED status, and the future task sequence, without reordering or
  claiming integration of the Operations Data Contract.
- `shared_context/ROADMAP.md` — one new subsection recording the future task
  sequence as a parallel decision track, explicitly not reordering the primary
  Data-Contract-first roadmap sequence.

## Files explicitly not touched

Everything under `site/`, `scripts/`, `tests/`; any `ContextSource` record,
provenance store record, refusal log, or loop evidence file; any workflow YAML;
any dependency file (`package.json`, lockfiles); any Three.js distribution;
historical NASA-related task/evidence files; the other agent's worktree or
branch.

## Future task sequence recorded

1. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001` — this task.
2. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001` — independent
   Codex/GPT-5.6 Sol review of supersession boundaries, consistency, Git diff,
   and acceptance criteria.
3. `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001` — remove active NASA
   API calls and `nasa-*` active runtime handles, preserving historical
   evidence; may run as the first bounded slice of the foundation task if the
   accepting review prefers that grouping.
4. `MELLYCORE-3D-SCENE-FOUNDATION-001` — implement the shared state, the full
   CSS fallback, the vendored/pinned Three.js enhanced renderer, lifecycle,
   context-loss recovery, and the mobile-first Source Arena.
5. `MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001` — keyboard/screen-reader
   parity, reduced-motion, forced-fallback tests, context-loss tests,
   memory/RAF cleanup, mobile and desktop performance.
6. `MELLYCORE-3D-SCENE-INTEGRATION-REVIEW-001` — independent final review
   before any merge or release claim.

No task in this sequence is marked complete, active, or implemented by this
task beyond item 1.

## Validation

All commands executed from the repository root of this dedicated worktree,
after the full documentation diff was in place, before staging the commit:

- `py -3.9 -B -m scripts.context_gate audit --json` → **PASS**: `finding_count: 0`,
  `index_status: "current"`, `writes_performed: 0` (7 valid records, matching
  the pre-existing baseline; this task touched no `ContextSource` file).
- `py -3.9 -B -m scripts.loop_ops validate` → **PASS**: "no findings; registry
  is valid for Phase 1" (9 registered loops).
- `py -3.9 -B scripts/validate_project_state.py` → **PASS**: "MellyCore project
  scaffold validation passed".
- `py -3.9 -B -m unittest discover` → **PASS**: `Ran 245 tests in 1.060s — OK`
  (245/245, matching the repository's documented baseline exactly).
- `git diff --check` → clean (exit 0), no whitespace/conflict-marker errors.
- Manual scope check: `git status --short` after `git add -A` confirmed exactly
  11 changed paths, all within `README.md`, `docs/`, and `shared_context/`; no
  path under `site/`, `scripts/`, or `tests/` appears in the diff; no
  dependency file (`package.json`, lockfile) and no Three.js distribution is
  present.
- Manual secret/credential scan of every changed file: none found (no key,
  token, `.env` value, or account identifier introduced).
- Manual contradiction scan for `implemented`, `vendored`, `accepted`,
  `build step`, and `external network` across every changed file: every
  occurrence of "implemented" is a negation ("is not implemented", "no...is
  implemented"); every reference to the ADR states its PROPOSED status; no
  sentence asserts the renderer, the vendored dependency, or NASA retirement as
  already implemented; "build step" and "external network" only ever appear in
  sentences preserving the zero-build/zero-external-network guarantees.

## Safety confirmation

Docs-only. No site/runtime code changed. No Three.js file downloaded or
vendored. No dependency file added. No push, PR, merge, or deploy performed.
No destructive Git operation used. The other agent's worktree and branch were
read only (via `git status`/`rev-parse`) and remain exactly as found. The
Operations Data Contract's integration state was not changed and is not
claimed as integrated.

## Next recommended task

`MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001`
