# MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I1-001

## Task ID

`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I1-001`

## Outcome

`PASS_CONTEXT_GATE_I1_READ_ONLY_COMMITTED`

Phase I1 of the Context Gate CLI is implemented as a Python 3.9-compatible,
standard-library-only, read-only package. It adds `validate-record` and
`preview`, implements the full R1-R9 preview checks and fixed outcome
precedence, produces deterministic human/JSON output, and includes 50 focused
tests. No write-capable command or canonical store exists.

## Preflight

- Repo: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `ba810ba7a7acf11a856b6e0dc03ac97b38981510`
  (`docs(aios): specify context gate implementation`)
- Working tree: clean before implementation
- Required specs, the first-admission review, preview README, all six decided
  preview records, mandatory shared context, Loop Operations conventions,
  blocklists, and contradiction-ledger template were read before editing.

## Commands Added

```text
py -3.9 -m scripts.context_gate preview --batch <manifest.json> [--json]
py -3.9 -m scripts.context_gate validate-record --file <record.json> [--json]
```

Exit codes are stable and tested:

- `0`: command completed with no invalid/refused item.
- `1`: malformed command/input or invalid `ContextSource` record.
- `2`: preview completed and at least one item received `REFUSE`.

Running with no subcommand prints help, returns `1`, and takes no action.
There is deliberately no `apply`, `rebuild-index`, or `audit` command in I1.

## Models And Record Validation

`scripts/context_gate/models.py` defines the preview/canonical
`ContextSource` shape, enum vocabularies, trust/default-use matrices, exact ISO
date parsing, structural findings, canonical deterministic JSON bytes, and
aggregate-safe secret-shape detection.

`validate-record` accepts draft, decided-preview, and future canonical record
shapes. It checks required fields, enums, dates, conditional `review_after`,
decision metadata, override rationales, gate-audit/envelope structure,
field-level secret shapes, and sorted UTF-8/LF serialization for canonical
records. Findings report only stable codes, field names, and safe messages;
they never echo rejected values.

All six admitted records currently shipped under
`shared_context/context_provenance_preview/` pass this validator. They were
read only; none was changed or migrated.

## Preview Checks And Outcomes

`scripts/context_gate/checks.py` implements the gate-spec order and stable
reason codes:

- R1 `secret_content`
- R2 `regulated_high_risk`
- R3 `forbidden_path`
- R4 `incomplete_metadata`
- R5 `allowed_use_loosening`
- R6 `trust_cap_violation`
- R7 `id_collision`
- R8 `inadmissible_input_class`
- R9 `field_level_secret`

After the hard checks, preview computes trust, warnings, private/override/
external-age/supersession/sensitivity parking, stale-implicated records,
staleness contagion, and contradiction drafts. Outcome precedence is exactly:

`REFUSE > CONTRADICTION_FOUND > NEEDS_HUMAN_REVIEW > ACCEPT_WITH_WARNINGS > ACCEPT`

`ACCEPT` remains only gate eligibility for Step 7 human review; it never means
admitted. Preview emits deterministic sorted JSON and, for `ACCEPT` /
`ACCEPT_WITH_WARNINGS`, the exact deterministic record bytes represented by
that manifest state. A manifest containing human decision fields can therefore
be previewed again before a future I2 apply.

Refused items are aggregate-safe by construction: their result object retains
only item index, `REFUSE`, and reason codes. It retains and prints no
`source_id`, `source_identity`, claim, notes, or refused value.

## Deterministic Manifest Controls

The upstream specs define candidate fields but intentionally do not define a
semantic model/provider call for contradiction detection. I1 therefore uses
optional, manifest-only deterministic controls:

- `subject` and `claim_dimension` identify the comparison slot.
- `contradicts` explicitly names known conflicting source IDs.
- `depends_on` supports staleness-contagion warnings.
- `supersedes` supports the human-review parking rule.
- `sensitivity_uncertain` and `review_after_override` express other parking
  conditions without gate-side guessing.
- `status: blocked`, `origin_task`, and `operator_question` represent the
  implementation spec's blocked-item lifecycle.

These controls are excluded from emitted `ContextSource` bytes. Different
claim text conflicts only inside the same explicit/derived subject and claim
dimension; different dimensions do not conflict. This is why the documented
"two persisted runs" versus `exercised: 1` loops-vs-runs near-miss is covered
as a no-contradiction regression test. This implementation decision is also
recorded in `shared_context/DECISIONS.md`.

## Tests Added

- `tests/context_gate_fixtures.py` — synthetic candidates/records and
  canonical-byte helpers; no real secret value.
- `tests/test_context_gate_checks.py` — each R1-R9 refusal, passing twins,
  all eight trust-lookup cells, above/below-default trust behavior, all five
  warning conditions, all five parking categories, blocked/private cases,
  fixed outcome precedence, stale-implicated/staleness-contagion behavior,
  store and same-batch contradictions, loops-vs-runs near-miss, and preview
  determinism.
- `tests/test_context_gate_tools.py` — draft/decided/canonical validation,
  all six shipped preview records, canonical serialization, CLI surface/exit
  codes, aggregate-safe refusal JSON, no-write proof, malformed-input safety,
  and repeated-output byte determinism.

Focused total: **50 tests**.

## Validation

| Command | Result |
| --- | --- |
| `py -3.9 -m scripts.loop_ops validate` | PASS — 9 loops, 0 findings |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | PASS — 150 tests |
| `py -3.9 scripts/validate_project_state.py` | PASS |
| `py -3.9 -m unittest discover -s tests -p "test_context_gate*.py"` | PASS — 50 tests |
| `py -3.9 -m compileall -q scripts/context_gate tests/context_gate_fixtures.py tests/test_context_gate_checks.py tests/test_context_gate_tools.py` | PASS |
| `git diff --check` | PASS |

`py -3.9 -m black --check ...` could not run because Black is not installed in
the Python 3.9 environment. No dependency was installed because I1 is required
to remain standard-library-only; focused tests, compileall, and diff checks are
the formatting/syntax evidence for this task.

## Files Changed

- `scripts/context_gate/__init__.py`
- `scripts/context_gate/__main__.py`
- `scripts/context_gate/cli.py`
- `scripts/context_gate/models.py`
- `scripts/context_gate/checks.py`
- `tests/context_gate_fixtures.py`
- `tests/test_context_gate_checks.py`
- `tests/test_context_gate_tools.py`
- `docs/tasks/MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I1-001.md`
- `shared_context/ROADMAP.md`
- `shared_context/RUN_QUEUE.md`
- `shared_context/PROJECT_STATE.md`
- `shared_context/AGENT_HANDOFF.md`
- `shared_context/DECISIONS.md`

## Safety Confirmation

- Read-only by construction: neither command opens a file for writing.
- No `apply` flag or command; no canonical record/refusal/ledger write path.
- No `shared_context/context_provenance/` directory created.
- No migration, refusal log, `INDEX.json`, audit command, or dashboard change.
- No provider/model call, network, MCP, database, scheduler, watcher, backend,
  dependency, workflow YAML, or secret.
- No decided preview record changed.
- No MellyTrade path was read or written by the gate; R3 refuses it.
- No push, rebase, force push, merge, deploy, or destructive git action.

## Remaining I2/I3/I4 Work

1. **I2:** separately approve and implement `apply`, full operator/HEAD/clean-tree
   gating, write-once store, structurally whitelisted refusal-log writer, the
   hash/parsed-field-verified migration of all six preview records, historical
   C7 refusal backfill, and preview-store tombstone. The blocked C8 repo-path
   operator decision should be answered before or during I2.
2. **I3:** separately approve and implement deterministic `rebuild-index` and
   read-only `audit --json`, including index drift, stale, supersession,
   refusal-count, and blocked-item findings.
3. **I4/dashboard:** separately approve the local read-only Context tab under
   the dashboard-read contract; never render `internal_reasoning_only` content.

## Recommended Next Task

`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001` after the operator answers the
blocked C8 question. Recommended model/effort: **Codex, High** because I2 adds
the first write path, immutable-store semantics, migration atomicity, and
aggregate-safe refusal logging.

## Local Commit

One local commit is created for this task:

```text
feat(aios): add read-only context gate preview
```

Not pushed.
