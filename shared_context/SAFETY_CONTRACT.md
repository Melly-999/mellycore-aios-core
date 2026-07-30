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
publication are **not** currently independent, separately gated actions.
Before the Operator selected temporary Model A on 2026-07-27, this document
required them to be treated as separately authorized. Under the current
Model A contract below, explicit approval of one specific merge also
authorizes only the automatic Production publication caused by that merge.

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

## OpenAI Batch API — Stage B Activation Controls (No Provider Secrets, Trigger #5 Uncrossed)

`scripts/mellycore_batch/activation.py` (Stage B, branch
`feat/mellycore-openai-batch-controlled-activation-001`) is a local-only
planning/validation layer, not a live provider integration. It never reads
or prints a credential *value* (only a boolean "present/absent" check,
delegated to `scripts/mellycore_batch/policy.py`'s existing
`credential_material_present()`), never imports the `openai` SDK on any
reachable path, and never opens a socket. Full details, including the
governing capability-research and pricing-evidence outcomes and the
Model B decision that authorized Stage B implementation only, are recorded
in `shared_context/PROJECT_STATE.md`'s "OpenAI Batch API — Stage B
Controlled Activation" section.

Consistent with the rest of this contract: GitHub Actions secrets and
Vercel environment variables carrying an OpenAI credential are prohibited
for this repository, and no backend or serverless route capable of making a
provider call exists or is authorized by Stage B. Live provider connections
remain hard-blocked by `scripts/mellycore_batch/policy.py`
(`live_provider_connections_allowed = false`,
`LIVE_PROVIDER_CONNECTION_BLOCKED_BY_MIGRATION_TRIGGER_5`, exit code `78`);
Stage B adds a second, independent, local activation-control layer on top of
that block, it does not replace or weaken it. This dormant Stage B merge
does **not** cross migration trigger #5 ("first live provider connection")
— that trigger is crossed only by an actual, successful, credentialed
connection to the OpenAI API, which no Stage B code path performs. A
separate, explicit authorization is required before any live Batch
execution (Stage C, `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`)
may proceed.

Pricing evidence is accepted only when both its SHA-256 integrity digest and
the complete hardcoded Python dual lock agree on every reviewed price,
source URL, timestamp, capability flag, and envelope field; the digest alone
is not an authority source. Any future one-time authorization consumption is
confined to a validated local directory handle: symlinks, junctions, marker
links, and other Windows reparse points are rejected, and the marker is
created exclusively relative to the validated handle. Stage B preflight
never creates or consumes such a marker.

