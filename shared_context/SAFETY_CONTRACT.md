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

**Update (2026-07-27): the Operator has selected Model A** — a temporary,
static-phase-only policy, recorded verbatim in `shared_context/DECISIONS.md`
and detailed in full in `shared_context/PROJECT_STATE.md`'s "Production
Deployment Authorization — Model A Contract (Temporary, Static-Phase Only)".
Under Model A: each individually approved pull-request merge into `main`
also authorizes only the automatic Production publication that specific
merge causes — this is **not** blanket, standing, batch, or future
authorization; every merge-authorization request must explicitly warn that
merging into `main` immediately updates the public Production host; no
agent may merge on its own initiative; and nine canonical, blocking
migration triggers require Model B reconsideration before any affected
implementation or merge proceeds. Model A creates no branch protection,
ruleset, environment protection, or other technical deployment gate —
enforcement remains procedural, resting on per-merge Operator approval.

