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
- **Production deployment rule — Model A selected (Operator decision,
  2026-07-27, temporary, static-phase-only):** merging into canonical `main`
  causes the Vercel Git integration to create a public Production deployment
  automatically, with no technical enforcement (`main` has no branch
  protection, the repository has no rulesets, the Production environment
  has no protection rules). The Operator has selected Model A — see
  `shared_context/PROJECT_STATE.md`'s "Production Deployment Authorization —
  Model A Contract" for the full contract. Every individual PR merge still
  requires its own separate, explicit Operator approval — **never** a
  blanket, standing, batch, inferred, or future authorization — and every
  merge-authorization request an agent prepares must explicitly warn that
  merging into `main` immediately updates the public Production host. No
  agent may merge on its own initiative under any circumstance. Nine
  canonical, blocking migration triggers (first backend, authentication,
  stored user data, runtime secret, live provider connection,
  execution-capable agent, external write-capable integration,
  financial/trading action, or delegated merge authority/multiple
  maintainers) require Model B reconsideration before any affected
  implementation or merge proceeds — agents must treat these as blocking,
  not optional. This rule does not itself authorize any current merge or
  deployment.

Final reports must include outcome, repo path, branch, files changed, validation results, safety confirmation, and next recommended task.

