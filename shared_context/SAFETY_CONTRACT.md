# Safety Contract

- No secrets.
- No real API keys.
- No provider tokens.
- No `.env` values.
- No account IDs.
- No destructive git without explicit approval.
- No deploy without explicit approval.
- No push or merge without explicit approval.
- No workflow YAML changes without explicit approval.
- No runtime, provider, or MCP/tool integration or activation without
  explicit approval.
- No MellyTrade mutation.
- No broker/trading execution, and no order/buy/sell/execute/connect-live
  UX — ever. MellyCore AIOS is a separate product from MellyTrade and must
  never inherit trading/broker/execution semantics merely because
  MellyTrade exists elsewhere.
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
confined to a fixed production root derived from the Windows Local AppData
Known Folder at `<LocalAppData>\MellyCore\batch\authorizations`. Callers,
CLI arguments, environment variables, configuration, and authorization
artifacts cannot select that root; repository paths, repository ancestors,
children, `.git`, and worktree administrative paths are excluded. The
root-taking helper is private and test-only. Symlinks, junctions, marker
links, and other Windows reparse points remain rejected, and the marker is
created exclusively relative to the validated root handle. Stage B preflight
never creates or consumes such a marker. Stage C and the `USD 0.01` spend
remain unauthorized, and migration trigger #5 remains uncrossed.

## Agent Operating Discipline v1 — Safety Hardening (`MELLYCORE-SAFETY-CONTRACT-HARDENING-001`)

Additive to the rules above and to `AGENTS.md`, which remains the shared
multi-agent policy owner (`AGENTS.md`'s Authority hierarchy places this
file above `AGENTS.md` itself as the non-negotiable safety floor).
`shared_context/CROSS_AGENT_CONTEXT.md` Section 7 already summarized
several of the rules below as "compressed from `SAFETY_CONTRACT.md`"
before this file actually stated them — that gap is what this hardening
closes. This section does not authorize anything; it only tightens
existing boundaries.

### Fake-live and validator-honesty prohibitions

- No fake telemetry: no fake or simulated active agents, live provider
  health, live telemetry, cost/spend-rate, or token/minute metrics
  presented as real.
- No fake email/calendar/tool execution, fake Obsidian sync, or fake
  model download/installed state.
- No unsupported validator claims. `AGENTS.md`'s "Validation honesty"
  section is the canonical rule (report only validators actually run,
  with their actual output; "not run" / "unavailable" / "failed" /
  "passed" are four distinct outcomes) — restated here because it is a
  safety floor, not merely a reporting style.
- Do not launder prior chat/session claims, agent memory, or an external
  reference report into canonical repository truth. Per `AGENTS.md`'s
  Authority hierarchy (item 7) and `CROSS_AGENT_CONTEXT.md`'s Authority
  Order (item 5), those are the *lowest*-authority inputs — never
  sufficient on their own to assert a fact about current project state.

### Status and provenance semantics

Use this repository's own existing vocabulary; do not invent a competing
one. The ten-value `truthful_state` glossary
(`shared_context/operations/TRUTHFUL_STATE_LABELS.md`, canonically owned
by `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` §1.9) is
the required vocabulary for any UI or data surface — e.g. a
static/cinematic UI element must be labeled `SIMULATED` or `PLANNED`,
never presented unlabeled as `IMPLEMENTED`. Beyond that glossary, these
binary distinctions are safety floors, not stylistic preferences, and
apply to every task report, handoff entry, and durable spec in this
repository: visual presence != implemented; planned != implemented;
implemented != tested; tested != verified; verified != connected;
connected != authorized; static demo != live telemetry; fixture data !=
production data; local commit != push; local branch != production;
review pass != merge authorization; workflow milestone closed != product
implementation authorization.

### Branch, worktree, and remote verification

`MELLYCORE-AGENT-WORKFLOW-LANDING-MERGE-001` found, by direct repository
evidence, that this repository's local `main` branch and its `origin`
remote's `main` share **no merge-base at all** with this repository's real
development history — both are disconnected, effectively decoy refs —
while the `clean-origin` remote's `main` is the true ancestor. No future
task may assume any branch, including one literally named `main`, is the
canonical baseline without checking: the actual repository root and
worktree (`git worktree list` — see `.claude/commands/plan-task.md`); the
current branch and HEAD; `git remote -v`; and, before any merge, push, or
deploy is even proposed, `git merge-base`/`--is-ancestor` (or equivalent)
against every candidate baseline, not just the one literally named `main`.
A branch is canonical only when repository evidence — not its name —
supports that; if evidence and name conflict, say so and stop rather than
guess.

### Task-class safety defaults

`docs/specs/MELLYCORE_TASK_PROMPT_STANDARD_SPEC_001.md` §4 defines the
task-mode table (planning-only, read-only review, docs-only mutation,
implementation, external research). This contract adds one safety default
on top of it: within Mode D (Implementation), any task touching
`runtime/**`, `providers/**`, `integrations/**`, MCP/tool activation with
external side effects, or any deployment/release action defaults to
**BLOCKED** pending its own separate, explicit Operator authorization —
none of these are unlocked merely because a docs/spec/workflow-hardening
milestone closed. Frontend/static-only implementation work remains
governed by Mode D's ordinary rules.

