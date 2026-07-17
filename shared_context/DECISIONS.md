# Decisions

- MellyCore AIOS is a separate standalone project, not a MellyTrade runtime repo.
- The GLM/Z.ai workspace is reference only and must not be copied wholesale.
- Runtime app code is deferred until a later explicitly scoped run.
- Provider API keys stay outside the repository.
- Milestone B ("One Brain") starts with a provenance-and-sensitivity spec before any ingestion gate, database, or runtime is built — `secret` and `regulated_high_risk` content is refused at admission by default, not merely restricted in display.
- The ingestion gate's outcomes are validation verdicts, never admissions: `ACCEPT` still requires human review before any record is admitted, `REFUSE` is machine-binding, and the gate operates in no-write preview mode by default — a future apply mode must be a separate, operator-approved invocation, never one automated motion from proposal to committed record.

