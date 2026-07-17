# MELLYCORE-CONTEXT-PROVENANCE-AND-SENSITIVITY-SPEC-001

## Task ID

`MELLYCORE-CONTEXT-PROVENANCE-AND-SENSITIVITY-SPEC-001`

## Outcome

`PASS_SPEC_COMMITTED_NO_IMPLEMENTATION`

## Scope

Design the provenance and sensitivity tagging system that is the foundation of Milestone B ("One Brain"): durable, trustworthy context with a defined trust/sensitivity model, before any ingestion gate, database, or runtime is built. Docs/spec only — no implementation, no provider calls, no secrets, no ingestion of private files, no backend or dashboard code change.

## 1. Preflight

- Repo root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` (canonical, confirmed)
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `befaee59066887805671c518f102bfac38207c36`
- Working tree: clean before any edit

## 2. Research: existing spec ecosystem read before writing

Read the four existing Milestone B-adjacent specs in full before drafting, to avoid duplicating or contradicting them: `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `shared_context/SOURCE_INGEST_WORKFLOW.md`, `shared_context/CONTRADICTION_LEDGER.md`, `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md`. The new spec is deliberately designed to generalize and sit above these — extending `SOURCE_INGEST_WORKFLOW.md`'s ten-step process rather than replacing it, and leaving room for `CONTEXT_GRAPH_SCHEMA.md`'s `SafetyDisplayState` to later be derived from this spec's `sensitivity_level` (not done here — flagged as future reconciliation work).

## 3. Deliverable: the spec document

`docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md` — see that file for full detail. Summary of what it defines, matching the six requested deliverables:

1. **The `ContextSource` record** (Section 3 of the spec): source identity, source type, trust level, sensitivity level, allowed use, expiry/staleness, plus full audit-trail fields (`proposed_by`, `reviewed_by`, `decision`, `decision_rationale`) and an immutability rule reusing the loop-evidence system's write-once pattern.
2. **Five sensitivity labels** (Section 5): `public`, `internal`, `private`, `secret`, `regulated_high_risk` — with a hard rule that `secret` and `regulated_high_risk` are refused at admission by default, and an `allowed_use` default matrix per label.
3. **Provenance labels** (Section 4): `user_provided`, `repo_derived`, `generated`, `externally_sourced` as `source_type`, plus `verified`/`unverified` as a second axis, with a `trust_level` default lookup table over both.
4. **Admission workflow** (Section 8): generalizes `SOURCE_INGEST_WORKFLOW.md`'s ten steps into eight steps applicable to any context, ending at mandatory human review before anything is `admitted`.
5. **Future dashboard fields** (Section 9): source count, stale items, contradiction count, sensitive items blocked, latest accepted context pack — specified as a future "Context" tab, explicitly not built.
6. **Staleness and contradiction handling** (Sections 6-7): a staleness policy directly motivated by the two real stale-claim bugs found in `MELLYCORE-OPERATIONAL-TRUST-REVIEW-001`, and contradiction precedence guidance that always still routes to `CONTRADICTION_LEDGER.md` for human resolution — never auto-resolved.

## 4. Key design decisions

- **Generalize, don't replace.** `SOURCE_INGEST_WORKFLOW.md` already defines a correct, human-gated process for graph fixtures. Rather than inventing a second, competing ingestion process, this spec's Section 8 is explicitly the same shape (classify → detect contradictions → human review → publish) applied to any context. Divergent processes for the same underlying problem is exactly the kind of thing that produces the stale/contradictory docs this project has already had to fix twice.
- **`generated` content is capped at `trust_level: medium`, never `high`, even when verified.** An agent's fluent synthesis can be wrong in ways a direct file read cannot; the default deliberately withholds full trust from AI-generated claims regardless of review, requiring an explicit human override with a stated rationale to go higher.
- **`secret` and `regulated_high_risk` are refused at the admission boundary, not filtered at display time.** This mirrors the existing `SafetyDisplayState.hidden` philosophy in `CONTEXT_GRAPH_SCHEMA.md` ("nothing sensitive should ship in the fixture file at all, visible or not") and extends the same boundary already enforced by `LOOP_REGISTRY.json`'s `global_forbidden_paths` (`**/MellyTrade/**`, `.env*`, etc.) from "forbidden loop read scope" to "forbidden context admission" — one consistent boundary, not a second one that could drift from the first.
- **Staleness is a first-class field, not a review afterthought.** `staleness_policy` and `review_after` exist specifically because `MELLYCORE-OPERATIONAL-TRUST-REVIEW-001` found the same stale-claim bug twice within three tasks. Making every context record declare how it can go stale is intended to catch that class of bug going forward without depending on a human remembering to re-review.
- **Precedence guidance, never auto-resolution.** Section 7 gives reviewers a faster starting point for contradictions (trust level, then historical-vs-volatile, then recency, then repo-derived-vs-generated) but every contradiction still requires a human-set `resolution_decision` in `CONTRADICTION_LEDGER.md`. No shortcut was added that could silently override a human.
- **Immutability reused, not reinvented.** A `ContextSource` record, once decided, is never edited in place — a change produces a new record with `superseded_by` on the old one, exactly like `shared_context/loops/runs/**` evidence. Reusing a pattern this project has already proven (and tested) is safer than inventing a second immutability convention.

## 5. What remains intentionally unimplemented

- No `ContextSource` record has been created anywhere in the repository.
- No ingestion gate exists — this spec is explicitly the prerequisite Milestone B's own roadmap lists before that item.
- No code, script, or CLI implements the admission workflow (Section 8 of the spec) — it is a process specification only, matching `SOURCE_INGEST_WORKFLOW.md`'s own existing scope.
- No dashboard tab, panel, or field described in Section 9 has been built; `site/dashboard.html` and its JS/CSS were not touched.
- No approval process for `regulated_high_risk` content has been defined — flagged explicitly as a future, separately-scoped gap; the safe default until then is refusal.
- No reconciliation between this spec's `sensitivity_level` and `CONTEXT_GRAPH_SCHEMA.md`'s `SafetyDisplayState.visibility` was made; `CONTEXT_GRAPH_SCHEMA.md` itself was not edited.

## 6. Validation

Docs-safe validators re-run to confirm this task caused no regression (no code was touched, so no change was expected):

| Command | Result |
| --- | --- |
| `py -3.9 -m scripts.loop_ops validate` | PASS, 9 loops, 0 findings |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 150 tests, OK |
| `py -3.9 scripts/validate_project_state.py` | PASS |

No implementation exists to test — this task added specification and documentation only.

## 7. Files changed

- `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md` (new — the spec itself)
- `docs/tasks/MELLYCORE-CONTEXT-PROVENANCE-AND-SENSITIVITY-SPEC-001.md` (this file)
- `shared_context/ROADMAP.md` (Milestone B's first bullet marked completed; ingestion gate marked recommended next)
- `shared_context/RUN_QUEUE.md` (item 47 added)
- `shared_context/PROJECT_STATE.md` (new "Milestone B — One Brain: started" section; HEAD line updated; next-tasks list updated)
- `shared_context/AGENT_HANDOFF.md` (top summary and "Next recommended task" line updated, to avoid recreating the exact staleness problem `MELLYCORE-OPERATIONAL-TRUST-REVIEW-001` just fixed)
- `shared_context/DECISIONS.md` (one line added recording the "spec before ingestion gate" and "refuse secret/regulated content at admission" decisions)

No code, loop registry, schema, CLI, evidence, state, or dashboard file was touched.

## 8. Safety posture confirmed

- Docs-only change; no provider/network/MCP call; no secrets read or written; no private file ingested.
- No ingestion gate, database, or backend implementation.
- No dashboard rewrite — `site/` was not touched.
- No scheduler installed or proposed.
- No push. No destructive git command. Nothing touched `C:\.git` or the MellyTrade workspace.

## 9. Recommended next task

`MELLYCORE-CONTEXT-INGESTION-GATE-SPEC-001` — a docs-only spec for the actual gate logic that enforces this task's provenance/sensitivity model (i.e., the validation checks an admission attempt must pass before a `ContextSource` record can be `admitted`), matching this project's established spec-before-code pattern. No ingestion, database, MCP, or runtime implementation should be authorized until that spec exists and is reviewed.
