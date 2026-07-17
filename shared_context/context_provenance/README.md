# Context Provenance -- Canonical Store

This is the canonical `ContextSource` record store, created by
`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001` per
`docs/specs/MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001.md` Section 2.

Rules:

- `records/*.json` files are **write-once**: an identical-bytes rewrite is idempotent
  recovery (a no-op); any differing write to an existing file is refused. The only
  permitted mutation to a decided record is setting `superseded_by`, and even that is
  done only via a future, separately approved `apply` call, never by hand.
- `refusals/REFUSAL_LOG.jsonl` is append-only and aggregate-safe: reason code, date,
  `proposed_by`, `batch_id`, `gate_spec_version` only -- never refused content or
  identity. See the gate spec Section 4/7.
- `MIGRATION_001.md` is the hash-verified manifest of the one-time relocation of the
  project's first six admitted `ContextSource` records from
  `shared_context/context_provenance_preview/`.
- `INDEX.json` does not exist yet -- it is derived data reserved for implementation
  Phase I3 (`rebuild-index`). Nothing in this store depends on it existing.
- No secrets, credentials, `.env` values, account identifiers, or MellyTrade content
  may ever appear in any file in this directory.
