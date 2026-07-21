# Truthful State Labels

**Status:** Documentation reference only. Folded in from
`docs/mellycore-operations-data-contract-001` (2026-07-19) via
`MELLYCORE-OPERATIONS-DATA-CONTRACT-AI-ESTATE-SKILLGAP-MEMORY-001`, adapted
for this directory's current, consolidated schema.

This file mirrors — and is not a substitute for — two documents:

- `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` §1.9, the
  **canonical** definition of the ten-value `truthful_state` glossary below.
- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` §1.6, which
  additionally defines the seven-value `dashboard_status` UI-facing
  projection every entity in `OPERATIONS_DATA_CONTRACT_SCHEMA.json` also
  carries. `truthful_state` alone (without `dashboard_status`) was this
  directory's original convention before that consolidation; every entity
  added or folded into `OPERATIONS_DATA_CONTRACT_SCHEMA.json` now carries
  **both** fields.

This file exists so a schema description can point at one file path
(`shared_context/operations/TRUTHFUL_STATE_LABELS.md`) rather than each
restating the glossary. If this file and either source document above ever
appear to disagree, the source documents win — this file is not itself
authoritative.

| Label | Meaning |
|---|---|
| `IMPLEMENTED` | Exists in the repository and is exercised or directly readable today. |
| `LEGACY_PROTOTYPE` | Historical prototype/demo code retained as evidence; not current product direction. |
| `SPECIFIED` | Defined by an accepted specification; not implemented. |
| `PLANNED` | Named on the roadmap; not yet specified in full or implemented. |
| `SIMULATED` | Deterministic local placeholder/demo content; carries its label and is never presented as live. |
| `UNAVAILABLE` | A source that should exist could not be reached or read at observation time. |
| `DEGRADED` | Partially available; some fields present, others missing or unverified. |
| `STALE` | Was valid but has passed its freshness/review boundary and has not been re-verified. |
| `UNKNOWN` | No value is known; explicitly distinct from zero, empty, or false. |
| `ERROR` | Processing failed; the datum could not be produced or parsed. |

## Rules

- `PLANNED`, `SIMULATED`, `STALE`, and `UNKNOWN` MUST NOT be silently presented
  as live verified state by any future reader of these contracts.
- Every record in `OPERATIONS_DATA_CONTRACT_SCHEMA.json` carries a
  `truthful_state` field drawn from exactly this ten-value set — no entity
  may invent an eleventh value or a synonym.
- All fixtures in `OPERATIONS_DATA_CONTRACT.example.json` are labeled
  `SIMULATED` and additionally carry `dashboard_status: "fixture/example"`.
  None is `IMPLEMENTED`, because no reader/validator/backend for these
  contracts exists yet.
