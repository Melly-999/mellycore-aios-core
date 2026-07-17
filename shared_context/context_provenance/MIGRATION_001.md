# Migration 001 -- Preview to Canonical

Migrated by `MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001`'s `apply --migrate-preview`,
per `docs/specs/MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001.md` Section 3.

Relocation, not re-decision: every `ContextSource` and `gate_audit` field below was
verified byte-for-byte identical between the preview and canonical copy before either
file was written. Only the envelope (`preview`/`record_status` removed, `envelope` added)
changed.

Migrated at: 2026-07-17

| source_id | preview SHA-256 | canonical SHA-256 | fields identical |
|---|---|---|---|
| `ctx-2026-07-17-dashboard-preview-committed` | `db60de2d1ce58dfed3f9fdf09dd04bce05cd59552a13dd84cc518e3117634490` | `d10cede3d3939e566f13edeb2ddc105aef0551307d905157e1868956edad5eb4` | yes |
| `ctx-2026-07-17-gate-spec-exists` | `89a6aa76e28956fc246d391a8b56d51b09719bd0d79e26d1496d923bc04ab10d` | `097fd590c51ba7d40ecf0fdc369ced582eb8f5185fded292f2372b181c70f750` | yes |
| `ctx-2026-07-17-milestone-a-closed` | `2bca902876ee068b97186f6192807a639e443a84104cfd31e1d9dc2e0df96fed` | `2c7e3da13b784e6f39ae68e60842a8f4d75d6b081814115b113a82edb9f20161` | yes |
| `ctx-2026-07-17-project-health-two-runs` | `874e115c99eaddd09d52f9fbac638bfa7e7d678258db92374a5f42849cd2941a` | `13504aaf74a629e34ff1236e6d30655a24b56b1c71868924e9817d660e516a32` | yes |
| `ctx-2026-07-17-provenance-spec-exists` | `adb67d456d64ab0815004025b2bb045c6d40c0ed3035333e27955f33a6d4e9e0` | `0381a774182542333c4265a2f1a7f368ff33e92f512d17f779acf6a8eb7d08db` | yes |
| `ctx-2026-07-17-safety-posture-summary` | `62a82a465b03e849bbaae8d72a060351bc37e815ac07c197998aa85361e00528` | `85e2aedb7d913a453750b7bd7d5f80c69fe0dd82a656c23fbb4de95db51064a9` | yes |

The refusal log's first line (`shared_context/context_provenance/refusals/REFUSAL_LOG.jsonl`) is the C7 historical backfill from `docs/tasks/MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001.md`'s "C7 refusal detail" section, so the log is complete from the workflow's true beginning.

This migration is one-time and idempotent: re-running it once `MIGRATION_001.md` exists is refused (`ALREADY_MIGRATED`), not repeated.
