# Loop State Persistence — Design And Safety Review

**Task ID:** MELLYCORE-LOOP-STATE-PERSISTENCE-REVIEW-001
**Version:** 1.0
**Status:** Design review (docs-only). Nothing here is implemented.
**Source run:** `MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001` → `EXERCISED_EXTERNALLY_NOT_REGISTERED`
**Scope:** Specify a safe contract for persisting real report-only loop run evidence, and correct the token-measurement ambiguity that run surfaced. Design only — no code, schema, or state file is changed by this task.

---

## 1. Current-State Evidence

Observed directly from the repository at HEAD `6c67fc5bf28999882e26a45d12cc7eab639228e1`, branch `publish/mellycore-main-001`:

- `shared_context/loops/states/` contains only `README.md`. **No state file exists for any loop.** Every registry entry sets `state_file_is_template: true`.
- `shared_context/loops/LOOP_STATE_SCHEMA.json` already defines `run_history[].ledger_ref` — a pointer field — which implies the schema's own author anticipated that ledgers live **somewhere other than** the state file itself. This review formalizes where that "somewhere" is; it does not invent the idea.
- `scripts/loop_ops/readiness.py`'s `_real_run_count()` (`readiness.py:63`) counts a run as real only if its `run_history` entry has both a `run_id` and a `finished_at`. It does **not** currently open or validate the file `ledger_ref` points to — it trusts the state file's own claim at face value. This is a real gap this review flags (Section 7, threat "silent trust inflation").
- `scripts/loop_ops/guard.py`'s budget checks (`guard.py:242-271`) enforce only `tokens.measured == true` values, via `RunLedger.measured_run_tokens` and `RunLedger.has_unmeasured_tokens` (`models.py:255-265`).
- The `MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001` run produced a real, schema-parseable ledger, external to the repository, and the guard returned `CONTINUE` with `per_run_budget: pass` — **not** `unenforceable` — even though the run's tokens were explicitly unmeasured. That report already named the mechanism; Section 5 here specifies the fix.
- `py -3.9 -m scripts.loop_ops audit --json`, re-run before and after that dry run, was **byte-identical** on the summary block. The audit has no path to recognize evidence that lives outside `shared_context/loops/states/`.

None of this is a code defect in the sense of "broken and failing" — the foundation behaves exactly as built. The gap is that persistence of real evidence was never designed, so "exercised" currently has no honest way to become true.

## 2. Identified Defects

Two are load-bearing for this review; the rest are gaps this design closes.

| # | Defect | Where | Severity |
| --- | --- | --- | --- |
| D1 | `tokens.total` is typed `integer, minimum 0` with no `null`, so "not measured" and "measured, and it was zero" are both written as `0` and become indistinguishable. | `RUN_LEDGER_SCHEMA.json:56-68`, `models.py:230` (`tokens_total: int = 0`) | **Blocking** — directly caused the dry run's `per_run_budget: pass` mis-classification |
| D2 | `has_unmeasured_tokens` infers "unmeasured" from `tokens_total > 0 and not measured`, i.e. it looks at the *value* to guess measured-ness instead of trusting the `measured` flag alone. | `models.py:264-265` | **Blocking** — root cause of D1's symptom |
| D3 | No persisted-evidence path exists at all; `runs/` does not exist. | n/a (absence) | Blocking for the stated goal, not a bug |
| D4 | `_real_run_count` trusts `run_history` entries without validating the ledger the entry references. | `readiness.py:63-78` | Non-blocking today (no state files exist), but must be closed before persistence ships |
| D5 | `run_id` has no format constraint in the schema — no pattern restricting characters, unlike `loop_id`'s `^[a-z0-9]+(-[a-z0-9]+)*$` in `LOOP_REGISTRY_SCHEMA.json`. | `RUN_LEDGER_SCHEMA.json:20` | Must be closed before any filesystem path is derived from it |
| D6 | Per-run budget enforcement sums only measured iterations and ignores whether *other* iterations in the same run were unmeasured — a mixed run could pass on a partial sum. | `guard.py:248-259` | Must be closed as part of the same fix as D1/D2 |

## 3. Proposed Persistence Architecture

Three concepts, kept structurally separate — this separation is the core of the design:

1. **Immutable run evidence** — the run ledger. What actually happened, once, permanently.
2. **Current loop state** — a small, mutable, derived summary: lifecycle status, failure streak, last progress marker, and *pointers* to evidence. Never itself primary evidence.
3. **Audit/readiness classification** — never persisted. Always computed fresh from (2) and the registry, exactly as `readiness.py` already does today. This review does not change that invariant — it is correct and should stay that way permanently.

```
shared_context/loops/
  runs/
    <loop-id>/
      <run-id>.json        <-- immutable evidence (NEW, this review)
  states/
    <loop-id>.state.json   <-- derived, mutable, pointer-bearing (EXISTS, schema unchanged in shape)
```

`states/<loop-id>.state.json` is unchanged in shape — `LOOP_STATE_SCHEMA.json` already has `run_history[].ledger_ref`. This review specifies that `ledger_ref` is a repository-relative path of the form `shared_context/loops/runs/<loop-id>/<run-id>.json`, and that it must point to a file that actually exists and actually validates — closing D4.

### Why `runs/`, not folding evidence into `states/`

- The existing schema already separates them via `ledger_ref`; a design that stuffed full ledgers into the state file would contradict the schema that shipped with the foundation.
- `states/` is the one file a human-approved action is allowed to *rewrite in place* (status changes, failure counters). `runs/` must never be rewritten once a file exists. Mixing an append-only concern into a mutable file invites exactly the kind of "quietly edit out a failure" risk the run ledger's own iteration-append-only rule already guards against (`registry.py`'s duplicate/out-of-order index rejection).
- Grouping by `<loop-id>/` keeps one loop's history together and avoids one flat directory holding every loop's runs.

## 4. Run-Ledger vs. State-File Distinction

| | Run ledger (`runs/<loop-id>/<run-id>.json`) | State file (`states/<loop-id>.state.json`) |
| --- | --- | --- |
| What it is | One run's full record | The loop's current summary |
| Mutability | Write-once, never rewritten | Rewritten by each approved persist action |
| Cardinality | One per run | One per loop |
| Who writes it | The future `persist-run` action, from a ledger already produced by whoever operated the loop | Same action, in the same invocation, derived *from* the ledger just persisted |
| Trust model | Primary evidence — everything else is computed from this | Derived — must be recomputable from the set of ledgers alone |
| Contains tokens/cost | Yes — the actual measured-or-not record | No — state does not re-store token figures; it only stores pointers and lifecycle facts |

A rule this review treats as load-bearing: **state must always be reconstructible from the set of persisted ledgers plus registry defaults.** If a state file were ever lost, replaying every `runs/<loop-id>/*.json` file in order must be able to rebuild it. This is why state stores *pointers*, not copies — a copy could drift from its source; a pointer cannot.

## 5. Token Measurement Contract (Correction)

This is the specific fix the dry run's Section 7 finding demanded. **Specification only — `models.py`, `registry.py`, `guard.py`, and `RUN_LEDGER_SCHEMA.json` are unchanged by this task.**

1. **`measured: false` must never imply zero cost.** It must mean "no claim about cost is made," full stop.
2. **When unmeasured, `total` (and `input`/`output`) must be `null`, or the whole `tokens` object omitted — never numeric `0`.** `RUN_LEDGER_SCHEMA.json`'s `tokens.total` must change from `{"type": "integer", "minimum": 0}` to `{"type": ["integer", "null"], "minimum": 0}`.
3. **`measured: true` requires a non-negative numeric `total`.** A ledger with `measured: true` and `total: null`/absent is itself invalid — a claimed measurement with no value is a contradiction, not an edge case to tolerate.
4. **The guard must check `measured` before ever comparing totals**, never infer measured-ness from the value. Today's `has_unmeasured_tokens` (`models.py:264-265`) does the inference backwards — it should become "any iteration where `measured is False`," full stop, independent of what `total` happens to hold.
5. **Unmeasured per-run and daily budgets must return `unenforceable`.** Concretely: if *any* iteration in a run is unmeasured, the whole run's `per_run_budget` check must be `unenforceable` — not a partial pass computed only over the measured iterations. Today's sum-of-measured-only approach (`guard.py:248`) can silently pass a run that mixes measured and unmeasured iterations, hiding the fact that the true total is unknown. This closes D6.
6. **Unmeasured cost must block promotion beyond `REPORT_ONLY`.** The future persist action must refuse to record `human_approval.granted: true`, or any state implying increased trust, for a loop whose most recently persisted run contains an unmeasured iteration. "We didn't measure it" is an absence of evidence, not a clean bill of health, and must never be read as one.

## 6. Guard vs. Semantic Escalation vs. Operator Approval

Three distinct authorities, previously conflated in practice (the dry run declared `WAITING_HUMAN` for a reason the mechanical guard has no way to evaluate, and both were correct — but only if kept distinct):

1. **Mechanical guard decision** (`guard.py`) — a pure function of the ledger and the registry's numeric/lifecycle limits: attempts, stagnation, no-progress, consecutive failures, budgets, kill switch, and transition legality. It has zero knowledge of what a finding's *content* says. It answers only: *does this ledger, taken as given, violate a mechanical limit?*
2. **Semantic finding escalation** — a judgment the loop (or the agent operating it) makes about what it found — e.g. "this matches my own `escalation_condition` text." Expressed by choosing `status_after` (and, optionally, an `open_escalation` block in state). The guard validates only that the chosen transition is *legal*, per `transition_allowed()` — it does not evaluate whether the escalation was *warranted*.
3. **Operator approval** — a fact about the world: a named human decided something. Recorded only in `human_approval`, only by an explicit action, never inferred from (1) or (2).

**Binding rule for any future summary or report:** a ledger where the guard returned `CONTINUE` must **not** be summarized as "no escalation occurred" without separately checking whether `status_after` differs from `status_before` in an escalating direction, or whether `open_escalation` is set. These are two independent signals. The dry run's `CONTINUE` + `WAITING_HUMAN` combination was correct, not contradictory — but only because both signals were reported side by side rather than one being inferred from the other.

## 7. Threat Model

| Threat | Vector | Mitigation specified here |
| --- | --- | --- |
| Fabricated or altered ledger claims a run that didn't happen, or a better outcome than occurred | A careless or compromised agent writes a ledger by hand | Full schema validation; guard re-evaluated *at persist time* and its exact decision recorded alongside the persisted copy, not trusted from the submitter's own claim; persistence is a separate, explicit, human-invoked action, never a side effect of running a loop |
| Secret committed via a ledger, permanently, into git history | An error signature, note, or raw output field carries a credential-shaped string | Mandatory `redact-check` (existing `scan_text`) with **zero findings required** before any write — a finding blocks persistence entirely, fail-closed, no "persist with a warning" path |
| Path traversal — `loop_id` or `run_id` engineered to escape `shared_context/loops/runs/` | e.g. `run_id = "../../../secrets/x"` | `loop_id` already constrained by `LOOP_REGISTRY_SCHEMA.json`'s `^[a-z0-9]+(-[a-z0-9]+)*$` (reuse, don't reinvent); `run_id` needs an equivalent pattern (closes D5); the resolved path must be checked to stay strictly under `shared_context/loops/runs/` after normalization before any write |
| Symlink escape | A loop-id or run directory is (or is replaced by) a symlink pointing outside the repo | Reject if any path segment is a symlink, checked immediately before the write, not only at directory-creation time |
| Silent overwrite / history tampering | Something rewrites an already-persisted ledger to erase a failure | Strict no-overwrite: refuse if the target file already exists. `runs/` is append-only by rule, the same way a ledger's own `iterations` array is already append-only (duplicate/out-of-order index rejection in `registry.py`) |
| Silent trust inflation | State claims `exercised`/`human_approved` without real backing evidence | Closes D4: the persist action (not the audit) is responsible for verifying the ledger before ever writing a `run_history` pointer; `readiness.py`'s tier logic is unchanged and stays strict |
| Cross-repository / cross-HEAD confusion | A ledger produced elsewhere, or against a different commit, is persisted as if it happened here | Record (do not silently block) any `repository`/`head_sha` mismatch in the persisted copy — historical evidence from elsewhere is still real evidence, but the mismatch must be visible, not hidden |
| Unapproved automatic promotion | A future code path silently flips `production_enabled` or similar from persisted data alone | `human_approval` stays a separate, explicit, named fact forever — never inferred from a guard decision, a semantic escalation, or a file merely existing |

## 8. Audit Tiers (Unchanged In Substance, Extended In Evidence)

The five tiers already defined in `models.py` (`TIER_CONFIGURED` … `TIER_PRODUCTION_ENABLED`) are correct and are **not** being redesigned. This review only tightens what counts as evidence for the middle tier:

| Tier | Today | With this design adopted |
| --- | --- | --- |
| `configured` | Registry entry exists | Unchanged |
| `validated` | Passes `validate` | Unchanged |
| `exercised` | `run_history` entry with `run_id` + `finished_at` present in state, trusted at face value | Same fields **plus** the referenced `ledger_ref` file must exist under `runs/<loop-id>/` and independently pass full ledger validation — closes D4 |
| `human_approved` | `human_approval.granted: true` with a named `granted_by` | Unchanged, **plus**: must be refused if the most recent persisted run for that loop contains an unmeasured iteration (Section 5, rule 6) |
| `production_enabled` | Structurally false while `phase == 1` | Unchanged — still structurally false in Phase 1, regardless of any of the above |

No tier becomes easier to earn. `exercised` becomes *harder* to earn honestly, which is the intended direction.

## 9. Migration Strategy

- **`RUN_LEDGER.example.json`** is already labelled an example, not evidence, via its own `example_notice` field. Its current `tokens` blocks use numeric placeholders (`"total": 9200, "measured": false"`) — under the corrected contract this is exactly the ambiguous pattern being fixed, so the future implementation task must update the example to use `total: null` for its unmeasured iterations. This review does not edit that file (schema/example changes are out of scope here); it records that the example is pre-correction and must not be copied literally into a real ledger until updated.
- **State files**: `shared_context/loops/states/` currently holds no loop state files (only `README.md`), so there is no backfill burden. The design can be adopted with a clean slate.
- **The dry-run ledger** from `MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001` remains in the operator's scratchpad, outside this repository, exactly as that task left it. It is **not** persisted by this task, and it predates this correction — its `tokens.total: 0, measured: false` is precisely the ambiguous pattern this review closes, so it should not be treated as a template for a correctly-typed ledger once the fix ships.
- **`registry.py`'s `_parse_iteration`**: the future task must relax the `tokens.total` type check to accept `None`, and add the cross-field rule (`measured=true` ⇒ numeric total; `measured=false` ⇒ `total` is `None`/absent).

## 10. Proposed Future File Changes

Listed for the *next* implementation task to scope — **none of these are made by this task**:

- `shared_context/loops/RUN_LEDGER_SCHEMA.json` — widen `tokens.total`'s type to include `null`; add a `run_id` format pattern; formalize `repository_mutation_count` / `remote_action_count` as named integer fields (ad hoc in the dry-run ledger today).
- `shared_context/loops/LOOP_STATE_SCHEMA.json` — clarify (in prose/description only, shape unchanged) that `run_history[].ledger_ref` must resolve under `shared_context/loops/runs/<loop-id>/`.
- `scripts/loop_ops/models.py` — `Iteration.tokens_total: Optional[int] = None`; correct `has_unmeasured_tokens` to key off `measured` alone.
- `scripts/loop_ops/guard.py` — per-run budget check becomes "unenforceable if any iteration is unmeasured," not "pass on the measured-only sum."
- `scripts/loop_ops/registry.py` — relax/extend `_parse_iteration`'s token validation per Section 5.
- `scripts/loop_ops/persist.py` (new) — implements the checklist in Sections 3–7: schema validation, uniqueness, no-overwrite, path/symlink safety, redaction gate, timestamp validation, transition legality, guard re-evaluation, and the state-file update — invoked only by an explicit human-approved CLI subcommand, never automatically.
- `scripts/loop_ops/cli.py` — a new `persist-run` subcommand wiring the above, requiring an explicit `--approved-by <name>` argument with no default.
- `tests/test_loop_ops_persist.py` (new) — implementing the acceptance tests in Section 11.
- `shared_context/loops/RUN_LEDGER.example.json` — update token placeholders to `null` per Section 9.

## 11. Acceptance Tests For The Future Implementation Task

Specified here as named cases with expected behavior. **Not created as executable test files by this task** — this task's required outputs are the two documents only.

**Token semantics**
1. `test_unmeasured_total_must_be_null_or_absent` — a ledger iteration with `measured: false, total: 5` is rejected at parse time.
2. `test_measured_true_requires_numeric_total` — `measured: true` with `total: null` is rejected at parse time.
3. `test_measured_zero_is_a_valid_real_measurement` — `measured: true, total: 0` is accepted and treated as a real, measured zero-cost run (distinct from case 1).
4. `test_has_unmeasured_tokens_keys_off_measured_not_value` — an iteration with `measured: false` and `total: null` is reported as unmeasured regardless of any other iteration's value.
5. `test_mixed_measured_and_unmeasured_run_is_unenforceable` — a two-iteration run, one measured (`total: 100`) and one unmeasured, yields `per_run_budget: unenforceable`, not a pass on the 100 alone.
6. `test_all_measured_run_enforces_normally` — a run where every iteration is measured enforces `per_run_budget` exactly as today, unchanged.

**Persistence safety**
7. `test_persist_rejects_unknown_loop_id` — a ledger for a `loop_id` absent from the registry is refused.
8. `test_persist_rejects_duplicate_run_id` — persisting a `run_id` that already has a file under `runs/<loop-id>/` is refused; the existing file is verified byte-unchanged afterward.
9. `test_persist_rejects_path_traversal_run_id` — a `run_id` containing `..`, `/`, or `\` is refused before any filesystem write is attempted.
10. `test_persist_rejects_symlinked_target` — if `runs/<loop-id>/` (or any ancestor) is a symlink, persistence is refused.
11. `test_persist_rejects_ledger_containing_secret_shaped_content` — a ledger whose `notes` or `error_signature` matches a `redact-check` pattern is refused, and it is verified that no partial file was written.
12. `test_persist_rejects_invalid_lifecycle_transition` — reuses `guard.transition_allowed`; a ledger declaring `DRAFT -> ASSISTED` is refused from persistence, matching the guard's own rejection.
13. `test_persist_rejects_future_timestamp` — a `started_at`/`finished_at` after the persist action's own wall-clock is refused.
14. `test_persist_rejects_finished_before_started` — `finished_at < started_at` is refused.
15. `test_persist_records_guard_decision_alongside_ledger` — after a successful persist, the guard's exact decision and exit code for that ledger are retrievable from the persisted record, not merely assumed.
16. `test_persist_never_writes_without_explicit_approver` — invoking persistence with no `--approved-by` value fails closed; no file is written.
17. `test_state_run_history_pointer_resolves_to_an_existing_validated_ledger` — closes D4: after persistence, `readiness.py`'s exercised check must open and validate the file `ledger_ref` names, not merely check the pointer's presence.
18. `test_head_sha_mismatch_is_recorded_not_blocking` — a ledger whose `head_sha` is not reachable in the current repository still persists, with the mismatch visibly recorded.
19. `test_mutation_count_nonzero_on_report_only_loop_is_rejected` — a ledger for a `REPORT_ONLY`-status loop with `repository_mutation_count > 0` is refused.
20. `test_state_reconstructible_from_ledgers_alone` — given only the set of files under `runs/<loop-id>/`, replaying them in `run_id`/timestamp order reproduces the same `states/<loop-id>.state.json` the persist action would have produced incrementally.
21. `test_human_approval_refused_when_latest_run_unmeasured` — closes Section 5 rule 6: an attempt to set `human_approval.granted: true` is refused if the most recently persisted ledger for that loop contains any unmeasured iteration.

## 12. Explicit Non-Goals

- Not designing or naming a scheduler, cron entry, or trigger of any kind.
- Not authorizing `ASSISTED` (L2) status, or any repository write scope, for any loop.
- Not writing to `shared_context/loops/runs/` or `shared_context/loops/states/` for real in this task — those directories are unchanged by this task (`runs/` does not exist after this task either).
- Not modifying `guard.py`, `models.py`, `registry.py`, `validators.py`, `readiness.py`, or any `.json` schema file.
- Not creating the `persist-run` command or any new test files.
- Not persisting, or deciding to persist, the `MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001` ledger — that remains an operator decision, to be made only once the corrected token contract exists.
- Not marking `project-health`, or any loop, as `exercised`.
- Not touching `PROJECT_STATE.md` or `ROADMAP.md`.

## 13. Recommendation

**ADOPT WITH REVISIONS.**

Adopt the three-layer separation (immutable evidence in `runs/<loop-id>/<run-id>.json`, derived state in `states/<loop-id>.state.json`, purely-computed audit tiers) — it is a natural extension of the schema already shipped, not a new invention, since `ledger_ref` already anticipated it.

**Do not implement persistence before the token-semantics correction (Section 5, defects D1/D2/D6) ships in the same implementation task.** Building a persist path on top of today's ambiguous `total: 0` semantics would durably enshrine exactly the ambiguity this review exists to close — once a ledger is persisted, it is meant to be immutable, so shipping the bug into permanent history is worse than shipping nothing.

## 14. Related Documents

- `[[../../shared_context/loops/README]]`
- `[[../../shared_context/loops/LOOP_STATE_SCHEMA]]`
- `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]`
- `[[../../shared_context/loops/LOOP_CONSTRAINTS]]`
- `[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]`
- `[[../safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]`
- `[[../tasks/MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001]]`
- `[[../tasks/MELLYCORE-LOOP-STATE-PERSISTENCE-REVIEW-001]]`
