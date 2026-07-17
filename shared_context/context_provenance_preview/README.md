# Context Provenance — PREVIEW DRAFTS ONLY

**This is not the canonical `ContextSource` record store.**

Everything in this directory was produced by `MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001`, a **hand-exercised preview pass** of the ingestion gate specified in `docs/specs/MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001.md`. No gate implementation exists; every check was evaluated by hand against the spec and recorded in the dry-run report at `docs/tasks/MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001.md`.

Rules for this directory:

- Every record here is a **draft**: `preview: true`, `record_status: DRAFT_PENDING_HUMAN_REVIEW`, `reviewed_by: null`, `decision: null`. **Nothing here is admitted.** Per the provenance spec, no record reaches `decision: admitted` without a human reviewer at admission-workflow Step 7 — that review has not happened for these drafts.
- The canonical future home (`shared_context/context_provenance/records/`, per gate spec Section 12) is deliberately **not** created here; the gate spec reserves creating it for a future, separately approved implementation task. This preview directory exists precisely so the dry run does not squat on the canonical location.
- Refused items get no draft file — only an aggregate-safe entry in the dry-run report (reason code, date, proposer; never refused content).
- Items parked `NEEDS_HUMAN_REVIEW` get no draft file until the human decision is made.
- Files here follow write-once discipline: a draft is superseded by a new file, never edited in place, except that the future Step 7 review task may fill `reviewed_by` / `decision` / `decision_at` / `decision_rationale` on these exact drafts (that is the one intended mutation, turning a draft into a decided record — or the review task may instead copy decided records to the canonical home and mark these superseded; that choice belongs to the review task).

No secrets, credentials, `.env` values, account identifiers, or MellyTrade content may ever appear in any file in this directory.
