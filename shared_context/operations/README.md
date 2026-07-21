# Operations Data Contract Fixtures

This directory holds the machine-readable companions to
`docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`:

- `OPERATIONS_DATA_CONTRACT_SCHEMA.json` — one JSON Schema (draft-07) document
  defining fourteen fixture-level entities: eleven authored fresh
  (`operation_run`, `task_record`, `agent_identity`, `model_provider_usage`,
  `token_cost_record`, `validation_result`, `artifact_record`,
  `environment_capability_snapshot`, `approval_gate`, `safety_status`,
  `recommendation_ledger_entry`) plus three (`ai_estate_asset`,
  `skill_gap_candidate`, `memory_freshness_record`) folded in from reviewed
  prior art via `MELLYCORE-OPERATIONS-DATA-CONTRACT-AI-ESTATE-SKILLGAP-MEMORY-001`.
  Documentation contract only — not runtime config, not live data ingestion,
  not execution authority.
- `OPERATIONS_DATA_CONTRACT.example.json` — one hand-authored, explicitly
  labeled example fixture per entity, matching the schema above.
- `TRUTHFUL_STATE_LABELS.md` — a folded-in reference doc mirroring (not
  replacing) the canonical ten-value glossary; see that file for details.

## Truthfulness

Every object in `OPERATIONS_DATA_CONTRACT.example.json` carries
`dashboard_status: "fixture/example"`, `truthful_state: "SIMULATED"`, and an
`example_notice` field. None of it is live telemetry, evidence of a real run,
or provider-account data. The dashboard status vocabulary
(`implemented` / `planned` / `simulated` / `fixture/example` / `not present` /
`blocked` / `requires operator approval`) and the underlying ten-value
`truthful_state` glossary are both defined in the spec document, Section 1.6.

## Scope

No script in `scripts/` reads, imports, or validates the files in this
directory as of this task. No backend, database, runtime adapter, provider
integration, or hardware-telemetry agent exists or is implied by these files.
`environment_capability_snapshot` in particular is always
`source: operator_provided` and can never be `implemented` under this
contract version — see the spec document, Section 2.8.

## Relationship to prior work

An earlier, unpushed local branch (`docs/mellycore-operations-data-contract-001`,
2026-07-19) contains a differently-scoped attempt at an operations data
contract (AI Estate Inventory, Unified Run Ledger, Skill Gap Candidate,
Memory Freshness, Recommendation Ledger, Approval Record, and a ten-value
Truthful-State Labels reference). That branch itself was never merged,
rebased, or pushed. Three of its entities (AI Estate, Skill Gap, Memory
Freshness) and its Truthful-State Labels reference were reviewed and folded
into this directory, adapted to add `dashboard_status`; the other three
(Unified Run Ledger, Recommendation Ledger, Approval Record) were judged
conceptually superseded by this directory's finer decomposition and were not
folded in. See the spec document, Sections 1.3 and 6, for the full
comparison and decision record.
