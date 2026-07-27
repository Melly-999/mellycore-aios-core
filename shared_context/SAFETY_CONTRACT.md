# Safety Contract

- No secrets.
- No real API keys.
- No provider tokens.
- No `.env` values.
- No account IDs.
- No destructive git without explicit approval.
- No deploy without explicit approval.
- No MellyTrade mutation.
- No wholesale import of the GLM workspace.
- No `.git` import from reference workspaces.
- No database files committed.
- No `db/custom.db` copied into this repo.
- No local runtime state committed.

## Production Deployment — Current Enforcement State

"No deploy without explicit approval" above states the required norm: an
agent or operator must never trigger, request, or recommend a deployment
without explicit approval, and merge into canonical `main` must never be
approved unless immediate public Production publication is acceptable.

As of `MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REVIEW-001`
(2026-07-27), this norm is **not currently separately technically enforced**
for the step after merge. Observed reality: the Vercel Git integration
watches canonical `main` and automatically creates a public Production
deployment within seconds of any merge, with no further human action. `main`
has no branch protection, the repository has no rulesets, and the Production
GitHub environment has no protection rules (all independently verified
read-only). The only human decision point in the current path is the
decision to approve the merge itself — merge approval and Production
publication are **not** currently independent, separately gated actions,
even though this document requires that they be treated as requiring
separate explicit authorization.

This is a recorded, unresolved **operational control mismatch**, not an
accepted permanent policy. Until an operator decision resolves it (see
`MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-MODEL-DECISION-001`), every
proposed merge into `main` must be treated as an immediate public-publication
request, and no agent may describe merge and Production deployment as
independently gated.

