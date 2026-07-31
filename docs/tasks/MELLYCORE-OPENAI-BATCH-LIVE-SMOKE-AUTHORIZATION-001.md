# MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001

## Decision

`AUTHORIZED_FOR_ONE_EXACT_FUTURE_LIVE_SMOKE_NOT_EXECUTED`

This is a documentation-only authorization decision. No provider connection,
file upload, Batch submission, status poll, output download, cancellation, or
paid operation occurred as part of this task. Migration trigger #5 is not
crossed by this record. Stage C is not executed by this record.

## Decision timestamp

`2026-07-31T18:45:00Z` (local wall-clock at task execution; see "Authorization
expiry" below for the binding expiry, which is independent of this timestamp).

## Canonical base

`947f33d27d5546775186e96bdc61e30db78c0b3d` — the exact merge commit produced
by `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-FINAL-CANONICAL-STATE-RECONCILIATION-MERGE-001`.
Independently re-verified live via `git ls-remote clean-origin refs/heads/main`
immediately before this worktree was created.

## Stage B completion evidence

- [PR #34](https://github.com/Melly-999/mellycore-aios-core/pull/34): `MERGED`
  at `2026-07-31T18:30:57Z`, merge commit `947f33d27d5546775186e96bdc61e30db78c0b3d`,
  first parent `f118110181fe5428940ac86256dedc63f52282a6`, second parent
  (exact independently reviewed head) `05e3f143116dda1d28192f8ec994e65d991bf713`.
  Merge tree `037a530d7b6f1e0502d404103ed32b666430c4c8` is identical to the
  reviewed-head tree. Static `site` subtree remained unchanged at
  `5df8bb686ebeb5b13bcf1fe2ad2ef6bc796bfc5d`.
- Final independent PR review outcome:
  `PASS_MELLYCORE_OPENAI_BATCH_API_CONTROLLED_ACTIVATION_FINAL_CANONICAL_STATE_RECONCILIATION_PR_REVIEW_002`.
- Merge task outcome:
  `SUCCESS_MELLYCORE_OPENAI_BATCH_API_CONTROLLED_ACTIVATION_FINAL_CANONICAL_STATE_RECONCILIATION_MERGE_001_PR34_MERGED_PRODUCTION_VERIFIED_STAGE_C_BLOCKED`.
- `FINAL_RECONCILED_STAGE_B_GOVERNANCE_BASELINE_ESTABLISHED` — confirmed
  current. No additional state-sync task is introduced by this record solely
  to restate the PR #34 merge.

## Production evidence

- GitHub deployment ID `5696334358`, SHA `947f33d27d5546775186e96bdc61e30db78c0b3d`,
  environment `Production`, source automatic Git deployment (Vercel Git
  integration), result `success`, created `2026-07-31T18:31:05Z`.
- Accepted host `https://mellycore-aios-core.vercel.app` returned HTTP 200
  (re-verified live during the prior merge task). This is reachability
  evidence only; no page-level visual acceptance is claimed by this record.
- Authenticated Vercel deployment ID: not obtainable in this read-only
  environment; not invented.

## Authorization scope

Exactly one future OpenAI Batch API live smoke, bounded as specified below.
This record does not itself execute any part of that smoke. It authorizes the
envelope; it does not mint a runtime one-time-use authorization artifact
(that artifact must be freshly constructed by the separately authorized
execution task at execution time — see "Required fresh execution preflight"
below).

## Canonical source files reviewed

- `scripts/mellycore_batch/openai_batch_pricing.json` (pricing-evidence
  manifest; dual-locked against Python constants).
- `scripts/mellycore_batch/activation.py` — `STAGE_B_MODEL`, `STAGE_B_ENDPOINT`,
  `STAGE_B_MAX_REQUESTS`, `STAGE_B_MAX_INPUT_BYTES`,
  `STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST`, `STAGE_B_MAX_TOTAL_OUTPUT_TOKENS`,
  `STAGE_B_HARD_COST_CAP_USD`, `STAGE_B_PRICE_INPUT_PER_MILLION`,
  `STAGE_B_PRICE_OUTPUT_PER_MILLION`, `STAGE_B_ALLOWED_BODY_KEYS`,
  `estimate_cost`, `enforce_cost_cap`, `enforce_request_envelope`,
  `validate_pricing_evidence`, `STAGE_B_MAX_AUTHORIZATION_LIFETIME` (15
  minutes), `StageBKillSwitch.stage_c_live_execution_authorized` (hardcoded
  `False`).
- `scripts/mellycore_batch/policy.py` — `get_active_policy()` /
  `enforce_live_connection_allowed()`; hardcoded `allowed=False`, no
  parameter, environment variable, or CLI flag can flip it.
- `scripts/mellycore_batch/models.py` — `BatchRequest`, exit codes
  (`EXIT_LIVE_BLOCKED = 78`), `MIGRATION_TRIGGER_5_ID`,
  `MIGRATION_TRIGGER_5_LABEL`, `LIVE_BLOCKED_CODE`.
- `scripts/mellycore_batch/jsonl.py` — `render_jsonl_bytes` (deterministic
  JSONL serialization used to compute the exact payload below).
- `shared_context/PROJECT_STATE.md` — "OpenAI Batch API — Stage B Merged,
  Stage C Unauthorized" section (governance chain, migration triggers, Model B
  decision reference).

No conflicting canonical evidence was found; the pricing manifest's own
`evidence_digest` field verifies against its content
(`validate_pricing_evidence` raised no exception), and every dual-locked
constant in `activation.py` agrees exactly with the manifest.

## Pricing source and freshness

- Source file: `scripts/mellycore_batch/openai_batch_pricing.json`.
- `verified_at`: `2026-07-28T22:00:34Z`.
- `valid_until`: `2026-08-27T22:00:34Z`.
- Current date at this decision: `2026-07-31` — within the validity window.
- Authoritative source URLs (already reviewed, dual-locked, unchanged):
  `https://developers.openai.com/api/docs/models/gpt-5.4-nano`,
  `https://developers.openai.com/api/docs/pricing`,
  `https://developers.openai.com/api/docs/guides/batch`,
  `https://help.openai.com/en/articles/9197833-batch-api-faq`.
- No external network request was made by this task; the manifest's existing,
  previously-verified evidence was read locally and its digest and freshness
  were re-validated deterministically against `2026-07-31` (well inside the
  window), not re-fetched from the network.

## Exact proposed model

`gpt-5.4-nano-2026-03-17` — the sole model permitted by `STAGE_B_MODEL` /
`enforce_exact_model`, matching the pricing manifest's `"model"` field
exactly. Not selected for being cheap; it is the only model this canonical
Batch contract accepts.

## Exact endpoint

`/v1/responses` — the sole endpoint permitted by `STAGE_B_ENDPOINT` /
`SUPPORTED_ENDPOINTS`, matching the pricing manifest's `"endpoint"` field.

## Exact payload

One JSONL line (one request), method `POST`, url `/v1/responses`:

```json
{"body": {"input": "MellyCore Stage C live-smoke probe. Reply with exactly one word: PONG.", "max_output_tokens": 16, "model": "gpt-5.4-nano-2026-03-17"}, "custom_id": "mellycore-live-smoke-001", "method": "POST", "url": "/v1/responses"}
```

Serialized exactly as `scripts/mellycore_batch/jsonl.py:render_jsonl_bytes`
would render it (`json.dumps(..., sort_keys=True, ensure_ascii=False)`,
UTF-8 encoded, single trailing newline). The `input` string is a fixed,
non-sensitive, deterministic test string proving only Batch lifecycle
completion and minimal response structure; it contains no secret, credential,
personal data, repository source, proprietary content, trading/brokerage
instruction, or external tool call. `body` contains only the three keys
`STAGE_B_ALLOWED_BODY_KEYS` permits (`model`, `input`, `max_output_tokens`);
`detect_prohibited_capabilities` and `validate_request` were run locally
against this exact request and found no finding. Any change to this payload
(the `custom_id`, `input` text, `max_output_tokens` value, `model`, or
`url`/`method`) invalidates this authorization.

## Input-file SHA-256

`a3794dd08e07124f522d56a2a4950e3c5011bc9b90affc0d2dd37a23ad344a6b`

Computed locally over the exact rendered JSONL bytes (238 bytes) using
`scripts/mellycore_batch/jsonl.py:render_jsonl_bytes` +
`hashlib.sha256`. Reproducible by any reviewer re-running the same
construction against this exact request object.

## Maximum input tokens

Stage B's cost methodology treats the raw input byte count as a direct,
deliberately conservative proxy for input tokens (1 byte assumed to cost as
much as 1 token) rather than estimating a lower real tokenized count — this
is the same worst-case methodology already reviewed and canonical for the
Stage B envelope (see `PROJECT_STATE.md`'s `USD 0.0075136` three-request
worst-case figure, independently reproduced here as consistent with this
payload's `estimate_cost` output). Worst-case input basis for this smoke:
**238 bytes** (well under the Stage B per-Batch cap of 65,536 bytes and far
under the true likely tokenized count, since English text tokenizes at
roughly 4 bytes/token — the byte-count basis is strictly pessimistic).

## Maximum output tokens

**16** (`max_output_tokens` on the sole request), well under the Stage B
per-request cap of 512 and the total cap of 1,536.

## Cost formula

Reproduced exactly via `scripts/mellycore_batch/activation.py:estimate_cost`
(Decimal arithmetic only, zero cached-input tokens assumed):

```
input_cost  = input_byte_count * (0.10 / 1,000,000)
output_cost = total_max_output_tokens * (0.625 / 1,000,000)
estimated_maximum_cost = input_cost + output_cost
```

With `input_byte_count = 238` and `total_max_output_tokens = 16`:

```
input_cost  = 238 * 0.10 / 1,000,000  = 0.0000238
output_cost = 16  * 0.625 / 1,000,000 = 0.00001
estimated_maximum_cost                = 0.0000338
```

## Worst-case cost

**USD 0.0000338** — computed by `estimate_cost()` and confirmed to pass
`enforce_cost_cap()` without exception against the canonical hard cap
`STAGE_B_HARD_COST_CAP_USD = Decimal("0.01")`.

## Safety margin

**USD 0.0099662** below the USD 0.01 hard cap — the worst-case estimate is
approximately **0.338%** of the authorized ceiling (a margin of
approximately 99.66%). This margin is not merely estimated: it is the exact
Decimal difference `Decimal("0.01") - Decimal("0.0000338")`.

## Maximum allowed spend

`USD 0.01` (`STAGE_B_HARD_COST_CAP_USD`, unchanged, hardcoded, dual-locked
against the pricing manifest). This authorization's proposed envelope
(`USD 0.0000338` worst case) never approaches this ceiling; the ceiling
itself is not raised, lowered, or reinterpreted by this record.

## One-file limit

Exactly one input JSONL file (the single-line payload above) may be uploaded
during the future execution. No second file, no file replacement, no
supplementary file.

## One-request limit

Exactly one request entry (`custom_id: "mellycore-live-smoke-001"`) may be
submitted. No request expansion, no additional `custom_id`.

## One-Batch limit

Exactly one Batch creation, one Batch identifier, and one result retrieval.
Bounded, read-only status polling may occur only within the future execution
task itself (see `scripts/mellycore_batch/activation.py:BoundedPollingConfig`
— `max_polling_attempts=12`, `min_polling_interval_seconds=60`), and must not
itself constitute a second submission.

## No-retry rule

Zero automatic retries (`STAGE_B_AUTOMATIC_RETRIES = 0`). If Batch submission
returns an ambiguous result, the future execution task must stop and report,
never retry automatically and never submit a second Batch.

## No-fallback rule

No alternative provider, no provider-router fallback, and no automatic model
fallback. OpenAI's Batch API only, at the exact model and endpoint above.

## No-model-substitution rule

`enforce_exact_model` rejects any model other than exactly
`gpt-5.4-nano-2026-03-17` with no fuzzy or prefix match. This authorization
does not extend to any other model string, however similar.

## Credential isolation

Provider credentials (e.g. `OPENAI_API_KEY`) must remain external to this
repository, supplied only in the operator's own local environment at
execution time. This task did not read, log, or record any credential value;
`policy.py:credential_material_present()` reports presence only as a
boolean and never participates in any allow/block decision. No secret,
`.env`, key, or token value is recorded anywhere in this authorization record
or in the four living documents it updates.

## Migration-trigger #5 boundary

`MIGRATION_TRIGGER_5_ID = "migration_trigger_5_first_live_provider_connection"`
remains uncrossed by this record. This authorization proposes that trigger
#5 may be crossed **only** during the separately approved future execution
task, for this exact one-request smoke, and the fail-closed posture
(`scripts/mellycore_batch/policy.py`'s hardcoded `allowed=False`) must be
restored immediately afterward regardless of the smoke's outcome. This task
itself performs zero provider connections and crosses no trigger.

## Required fresh execution preflight

The future execution task must independently re-run, immediately before any
provider access: pricing-evidence freshness and digest verification against
the wall clock at that time; construction of a fresh, single-use
`AuthorizationArtifact` (its own `authorization_id`, `issued_at`/`expires_at`
within the 15-minute `STAGE_B_MAX_AUTHORIZATION_LIFETIME` window, bound to
the then-current `canonical_base_sha` and `activation_commit_sha`); exact
re-validation of this payload's SHA-256, request envelope, and cost estimate;
and confirmation that canonical `main` has not drifted from the base recorded
by that execution task. This authorization record does not itself construct
or consume that artifact.

## Required explicit operator confirmation

The future execution task must obtain the operator's explicit, specific
approval for that exact execution — never inferred from this record, never
blanket, and never satisfied by this authorization alone — before any
provider connection occurs, consistent with the Model A per-merge/per-action
authorization discipline already in force for this repository.

## Required post-smoke fail-closed restoration

Immediately after the future smoke completes (success, failure, or partial),
the execution task must confirm and record that
`scripts/mellycore_batch/policy.py`'s hardcoded policy remains (or has been
explicitly, separately re-authorized to remain) `allowed=False`, that no
standing live-provider enablement was created, and that migration trigger #5
is treated as crossed historically for that one exact smoke only — not as a
standing capability for any further Batch, request, or provider operation.

## Execution stop conditions

The future execution must stop rather than proceed if: submission returns an
ambiguous result; canonical `main` has drifted from the base it expects;
pricing evidence has expired or its digest no longer verifies; the payload,
model, endpoint, or cost bound differs even slightly from this record; a
second Batch would be required; or explicit operator confirmation has not
been freshly obtained for that specific execution.

## Canonical publication, activation, and drift

This authorization is only a proposal while it exists locally or on a
non-canonical branch. It cannot be used for provider access or live
execution in that state.

The separately authorized GitHub merge of the exact independently reviewed
authorization head into canonical `main` is an explicitly sanctioned
publication transition. That exact publication merge does not invalidate
this authorization merely because canonical `main` advances beyond the
pre-publication branch base `947f33d27d5546775186e96bdc61e30db78c0b3d`.

The pre-publication base is an evidence anchor for branch origin. It is not
the post-publication activation baseline.

This authorization becomes eligible for a later execution decision only
after a fresh preflight verifies the actual authorization publication merge
commit and proves all of the following:

1. the merge was created from the exact independently reviewed authorization
   head;
2. the publication merge commit has exactly two parents;
3. its second parent is the exact reviewed authorization head;
4. its merge tree equals the reviewed authorization-head tree;
5. current canonical `main` equals that exact publication merge commit;
6. every other pricing, payload, model, policy, credential, expiry, and
   safety gate below remains valid.

That exact publication merge commit is the **activation baseline**.

Any later advancement of canonical `main` beyond the activation baseline
invalidates this authorization. Ancestry or containment alone does not
preserve validity after later canonical drift. A fresh authorization
decision and independent review are then required.

Canonical publication does not by itself authorize execution. The later
execution task still requires a fresh preflight (see "Required fresh
execution preflight" below) and explicit operator approval (see "Required
explicit operator confirmation" below).

## Authorization invalidation conditions

This authorization is single-use, exact-scope, and expiring. It is
automatically invalid, in whole, upon any of the following, whichever occurs
first:

- **Pricing-evidence expiry**: at or after `2026-08-27T22:00:34Z`
  (`valid_until` in `scripts/mellycore_batch/openai_batch_pricing.json`).
- **Canonical-main drift (post-activation)**: before this authorization is
  activated (see "Canonical publication, activation, and drift" above), the
  sanctioned publication merge of the exact reviewed authorization head into
  canonical `main` does **not** invalidate this authorization, even though it
  necessarily advances canonical `main` beyond the pre-publication base
  `947f33d27d5546775186e96bdc61e30db78c0b3d`. Once activated, if canonical
  `main` advances beyond the activation-baseline publication merge commit
  before the future execution task runs, that task must stop; ancestry or
  containment of the reviewed commit does not preserve validity; a fresh
  authorization decision and independent review are required rather than
  reusing this record.
- **Model/pricing/policy drift**: any change to `STAGE_B_MODEL`, the pricing
  manifest's rates, `STAGE_B_HARD_COST_CAP_USD`, or
  `scripts/mellycore_batch/policy.py`'s hardcoded policy.
- **Payload change**: any difference from the exact payload and SHA-256
  recorded above.
- **Credential unavailability**: if the operator's own external OpenAI
  credentials are not available at execution time, execution must not
  proceed, substitute another credential source, or widen scope to compensate.

This authorization cannot be reused for another model, request, file, Batch,
or dollar amount. It is not a blanket or standing approval.

## No provider operation occurred in this task

Confirmed: no OpenAI API connection, no file upload, no Batch submission, no
status poll against a live Batch, no output download, no cancellation, and no
SDK installation occurred during this authorization-decision task. All five
provider-backed CLI commands (`submit`, `status`, `list`, `download`,
`cancel`) remain blocked, returning exit code `78` with
`LIVE_PROVIDER_CONNECTION_BLOCKED_BY_MIGRATION_TRIGGER_5`.

## No spending occurred

Confirmed: `USD 0.00` was spent by this task. The `USD 0.01` ceiling remains
unreached and unauthorized for actual spend; only the bounded future proposal
is recorded here.

## Exact next workflow task

`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-REVIEW-001` — a fresh,
independent, read-only review of this authorization record (and, separately,
of the four updated living documents) before this proposed envelope may be
published, reviewed as a PR, merged, or acted upon by any future execution
task. That review must reconstruct this payload's SHA-256 and cost estimate
independently rather than trusting this record's numbers at face value.

## Independent-review requirement before publication or execution

This record must not be pushed, opened as a PR, or merged, and the proposed
smoke must not be executed, until
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-REVIEW-001` independently
passes. Passing that review authorizes only publication of this record for
further review/merge — it does not itself authorize provider connection,
upload, Batch submission, or spend. A separate, later, explicit
execution-approval task (not yet named or scheduled) is required after this
record's own review and merge before any provider access may occur.
