# Decisions

- MellyCore AIOS is a separate standalone project, not a MellyTrade runtime repo.
- The GLM/Z.ai workspace is reference only and must not be copied wholesale.
- Runtime app code is deferred until a later explicitly scoped run.
- Provider API keys stay outside the repository.
- Milestone B ("One Brain") starts with a provenance-and-sensitivity spec before any ingestion gate, database, or runtime is built — `secret` and `regulated_high_risk` content is refused at admission by default, not merely restricted in display.
- The ingestion gate's outcomes are validation verdicts, never admissions: `ACCEPT` still requires human review before any record is admitted, `REFUSE` is machine-binding, and the gate operates in no-write preview mode by default — a future apply mode must be a separate, operator-approved invocation, never one automated motion from proposal to committed record.
- First admitted `ContextSource` records (2026-07-17) live in `shared_context/context_provenance_preview/` and stay there until the future gate-implementation task creates the canonical `shared_context/context_provenance/` home and migrates them — the review task did not create the canonical directory because the gate spec reserves that for implementation. Step 7 review may be performed under explicit operator delegation via a task instruction, with the delegation recorded verbatim in `reviewed_by`; private machine-specific items are never admitted under delegation alone.
- Context Gate Phase I1 keeps contradiction/staleness evaluation deterministic and provider-free: optional manifest-only `subject`, `claim_dimension`, `contradicts`, `depends_on`, and `supersedes` controls make comparisons explicit and are never copied into `ContextSource` record bytes. Different claim dimensions are not treated as contradictions (the project-health loops-vs-runs near-miss is the regression case). The gate does not call a model to infer semantic conflict.
- The C8 machine-specific repository-path candidate is declined (2026-07-17) per the operator's `MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001` instruction and the implementation spec's recommendation. `PROJECT_STATE.md` already serves the operational reasoning need; the durable canonical rejection record intentionally does not duplicate the private path value. The six admitted preview records moved to the canonical store in the same task, with hash-verified identity evidence and the preview location retired.
- **Production deployment authorization model — Operator decision (2026-07-27,
  `MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-IMPLEMENTATION-001`).**
  Decision authority: **Operator** (sole decision authority; only the
  Operator could select between Model A and Model B per
  `MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-MODEL-DECISION-001`).
  Selected model: **Model A — combined static-site authorization**, scoped
  strictly to the current static-showcase, non-sensitive, non-runtime phase.
  Operator authorization statement, recorded verbatim:

  > I explicitly select Model A for the current static-showcase phase.
  > For each individually approved pull-request merge into canonical `main`,
  > my merge approval also authorizes the automatic Vercel Production
  > publication caused by that specific merge.
  > This is not blanket authorization for future merges.
  > Every merge still requires separate explicit operator approval and must
  > clearly warn that it immediately affects the public Production host.
  > Model A is limited to the static, non-sensitive, non-runtime phase.
  > Model A must be reconsidered before backend, authentication, stored
  > data, secrets, provider integration, agent execution, external write
  > capability, financial functionality, delegated merge authority, or
  > multiple active maintainers are introduced.
  > This authorization does not approve any current merge, deployment,
  > push, PR creation, PR mutation, Vercel change, GitHub settings change,
  > or implementation work.

  This decision does **not** create blanket, standing, batch, inferred, or
  future merge authorization — each individual PR merge still requires its
  own separate, explicit Operator approval, and every such approval request
  must explicitly warn that merging into `main` immediately updates the
  public Production host. No agent may merge on its own initiative. Full
  contract detail (per-merge rule, Production-impact warning, post-merge
  verification, rollback boundary, the nine blocking migration triggers,
  branch-protection boundary, PR #28 boundary):
  `shared_context/PROJECT_STATE.md`'s "Production Deployment Authorization —
  Model A Contract (Temporary, Static-Phase Only)". This decision does not
  authorize any current merge, deployment, push, PR creation, PR mutation,
  Vercel/GitHub configuration change, or implementation work, and does not
  affect PR #28's paused state or physical Android Chromium Gate B.
