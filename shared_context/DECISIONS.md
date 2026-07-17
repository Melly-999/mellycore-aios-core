# Decisions

- MellyCore AIOS is a separate standalone project, not a MellyTrade runtime repo.
- The GLM/Z.ai workspace is reference only and must not be copied wholesale.
- Runtime app code is deferred until a later explicitly scoped run.
- Provider API keys stay outside the repository.
- Milestone B ("One Brain") starts with a provenance-and-sensitivity spec before any ingestion gate, database, or runtime is built — `secret` and `regulated_high_risk` content is refused at admission by default, not merely restricted in display.
- The ingestion gate's outcomes are validation verdicts, never admissions: `ACCEPT` still requires human review before any record is admitted, `REFUSE` is machine-binding, and the gate operates in no-write preview mode by default — a future apply mode must be a separate, operator-approved invocation, never one automated motion from proposal to committed record.
- First admitted `ContextSource` records (2026-07-17) live in `shared_context/context_provenance_preview/` and stay there until the future gate-implementation task creates the canonical `shared_context/context_provenance/` home and migrates them — the review task did not create the canonical directory because the gate spec reserves that for implementation. Step 7 review may be performed under explicit operator delegation via a task instruction, with the delegation recorded verbatim in `reviewed_by`; private machine-specific items are never admitted under delegation alone.

