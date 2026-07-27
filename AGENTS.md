# AGENTS.md

Codex and other coding agents must treat this file as the repo entrypoint.

Before work, read these files in order:

1. `shared_context/PROJECT_STATE.md`
2. `shared_context/AGENT_HANDOFF.md`
3. `shared_context/RUN_QUEUE.md`
4. `shared_context/SAFETY_CONTRACT.md`
5. `shared_context/MODEL_ROUTING.md`
6. `shared_context/DESIGN_SYSTEM.md`

Rules:

- MellyCore AIOS is separate from MellyTrade.
- Do not add secrets, real API keys, provider tokens, account IDs, `.env` values, local databases, or runtime state.
- Do not run destructive git commands such as reset, clean, rebase, force push, or branch deletion without explicit approval.
- Do not push, merge, deploy, or create remote resources without explicit approval.
- Keep work docs-first until a later run explicitly requests runtime app code.
- Update `shared_context/AGENT_HANDOFF.md` after every meaningful task.
- **Interim operating rule (unresolved as of
  `MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REVIEW-001`,
  2026-07-27):** merging into canonical `main` currently causes the Vercel
  Git integration to create a public Production deployment automatically,
  with no separate human deployment-approval step and no technical
  enforcement (`main` has no branch protection, the repository has no
  rulesets, the Production environment has no protection rules). Treat every
  proposed merge into `main` as an immediate public-publication request; do
  not recommend or perform a merge unless immediate public publication is
  acceptable. Do not describe merge and Production deployment as
  independently gated until
  `MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-MODEL-DECISION-001`
  resolves the target authorization model. This does not authorize merge or
  deployment, and does not establish that merge approval has become
  permanent deployment approval.

Final reports must include outcome, repo path, branch, files changed, validation results, safety confirmation, and next recommended task.

