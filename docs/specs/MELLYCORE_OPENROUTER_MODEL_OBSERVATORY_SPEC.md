# MellyCore OpenRouter Model/Cost Observatory Spec

**Task ID:** `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-001`
**Version:** 1.0
**Status:** `SPEC_ONLY` · `STATIC_SNAPSHOT_PLANNED` ·
`LIVE_API_NOT_AUTHORIZED` · `ACCOUNT_USAGE_NOT_AUTHORIZED` · `NO_API_KEYS` ·
`NO_BACKEND` · `NO_MODEL_CALLS` · `NO_DEPLOY`

This document is a product, UX, routing, and static-data contract. It creates no
fixture, UI, provider connection, account integration, model call, backend, or
deployment.

## 1. Purpose

The OpenRouter Model/Cost Observatory gives a MellyCore operator a legible,
pre-run view of model fit, representative cost, capability trade-offs, and
fallback paths. It turns model selection from an opaque provider choice into an
inspectable planning decision while preserving MellyCore's controlled loop:

`observe → analyze → recommend → approve → implement → validate → record`

The Observatory complements Source Arena. Source Arena makes evidence and model
perspectives inspectable; the Observatory explains which model lane should be
considered before a future agent run. It does not route, call, or bill models.

## 2. Product Promise

> A cockpit for choosing the right model at the right cost before an agent run
> begins.

## 3. User Stories

- As an operator, I can identify a cheap routine worker for drafting or bounded
  iteration without implying it is suitable for final safety decisions.
- As a product designer, I can find the premium visual/product-judge lane and
  see Fable 5's unavailable status plus its defined fallback.
- As an architect, I can choose an Opus-class security/architecture review lane
  and see when a second model or operator review is required.
- As an operator, I can see GPT-5.6 Sol as a high-effort fallback when Fable 5
  is unavailable, without treating that fallback as an automatic model call.
- As a budget owner, I can enter token assumptions and receive an approximate
  static estimate, a cheaper compatible alternative, and a "worth premium
  model?" signal.
- As a visitor, I can distinguish representative pricing from live pricing and
  static snapshot data from account usage at every relevant panel.

## 4. Information Architecture

Desktop uses a command-cockpit composition, not a catalogue grid. The first
viewport answers three questions in order: "Which lane?", "Why this model?",
and "What might this run cost?"

### 4.1 Model Constellation

- Orbital, selectable model nodes grouped by routing lane around a restrained
  router core.
- Node size may encode capability breadth; ring position may encode lane; a
  text badge always communicates cost class and status.
- Selection updates Route Advisor, Budget Estimator, Capability Matrix, and
  Fallback Chain locally.
- The constellation is a visual index, not evidence of connectivity,
  availability, ranking, or live routing.

### 4.2 Cost Radar

- A compact radial or segmented HUD summarizing the selected model's static
  input/output price points, cost class, context window, and snapshot date.
- Missing price data renders `UNKNOWN` and suppresses computed cost.
- No "best value", savings, or price-trend claim without explicit static
  fixture evidence.

### 4.3 Route Advisor

- Leads with run type and recommended lane, then explains fit, cautions, and
  required capabilities.
- Advice is deterministic local policy derived from the fixture and the policy
  in Section 8.
- It never launches a run, chooses on the operator's behalf, or presents a
  recommendation as approval.

### 4.4 Budget Estimator

- Accepts the inputs and produces the outputs in Section 9.
- Shows formula assumptions, snapshot date, currency, and missing-data state.
- Is a planning instrument only; it has no account or billing connection.

### 4.5 Capability Matrix

- Compares only reviewed fixture fields such as reasoning, coding, vision,
  long-context, documentation, architecture review, and cost sensitivity.
- Defaults to the selected lane plus adjacent alternatives rather than a dense
  all-provider mega-table.
- Supports a semantic table-equivalent presentation.

### 4.6 Fallback Chain

- Displays ordered local policy steps: preferred model, first fallback, second
  fallback, and operator-escalation condition.
- Every step includes a reason and any capability loss or cost change.
- A fallback chain is guidance, not automatic failover.

### 4.7 Safety Boundary Strip

A persistent strip remains visible near the Observatory heading and estimator:

`STATIC SNAPSHOT` · `NO API KEY` · `NO MODEL CALLS` · `NO ACCOUNT USAGE` ·
`NOT LIVE PRICING` · `FUTURE-GATED LIVE CATALOG`

## 5. Visual Direction

The Observatory should feel like a premium JARVIS-like AI command cockpit:

- black-space foundation with purple, blue, cyan, and restrained magenta neon;
- an orbital model constellation used as navigational structure;
- crisp HUD cards, glassmorphism, fine grid lines, and controlled depth;
- violet as primary structure, cyan as secondary data accent, magenta for
  interaction, amber for caution/gates, and green only for verified state;
- generous negative space and a clear command hierarchy.

It must not feel like:

- a spreadsheet or pricing table;
- a crypto dashboard or market ticker;
- a provider catalogue dump;
- a retail or institutional trading terminal;
- a wall of equal-weight cards.

Atmosphere never outranks labels, provenance, cost assumptions, or keyboard
focus. No WebGL, Three.js, or Canvas renderer is required or authorized for the
static snapshot slice; the orbital composition must be achievable with
HTML/CSS/DOM.

## 6. Static Data Schema

The next implementation task may create a local fixture that conforms to this
contract. No fixture is created by this spec.

```yaml
schema_version:
model_id:
display_name:
provider:
routing_lane:
cost_class:
input_cost_per_million:
output_cost_per_million:
cache_read_cost_per_million:
currency:
context_window:
capabilities:
best_for:
avoid_for:
fallbacks:
status:
snapshot_date:
source_note:
safety_note:
```

Field rules:

- `model_id` is a reviewed fixture identifier, not proof that a provider
  currently exposes that identifier.
- `routing_lane` must be one Section 7 lane.
- `cost_class` is one of `FREE_EXPERIMENTAL`, `LOW`, `MEDIUM`, `HIGH`,
  `PREMIUM`, or `UNKNOWN`.
- Cost fields are non-negative numbers or `null`, expressed per one million
  tokens in `currency`. Unknown is `null`, never zero.
- `cache_read_cost_per_million` is optional/nullable. The estimator behavior
  for a missing cache rate is defined in Section 9.
- `context_window` is a positive integer or `null`; it is never guessed.
- `capabilities`, `best_for`, `avoid_for`, and `fallbacks` are arrays.
  Fallback entries include `model_ref`, `reason`, and `tradeoff`.
- `status` is one of `REPRESENTATIVE_SNAPSHOT`, `PLANNED_ALIAS`,
  `UNAVAILABLE`, `UNKNOWN`, or `DEPRECATED_IN_SNAPSHOT`.
- `snapshot_date` is an ISO date for fixture review, not a freshness guarantee.
- `source_note` describes the human-reviewed basis for representative pricing
  and capability copy. It must include `not live pricing`.
- `safety_note` must include the applicable static/no-call/no-account boundary.

The fixture as a whole must carry an `example_notice` stating that it is a
static snapshot, contains representative pricing, is not live pricing, and is
not account-backed. Model aliases such as "Opus-class" or "Tera" must use
`PLANNED_ALIAS` unless the implementation task records a reviewed exact
identifier. No provider logos or availability badges may imply endorsement or
connectivity.

## 7. Model Lanes

| Lane | Intended work | Admission rule | Typical caution |
| --- | --- | --- | --- |
| Free / Experimental | Exploration, disposable ideation, capability probes | No safety-critical or final output | Availability and quality may be unstable |
| Cheap Worker | Drafting, extraction, formatting, high-volume bounded tasks | Human review before promotion | Avoid sole architecture or security judgment |
| Balanced Daily | Routine docs, synthesis, moderate reasoning, review | Default when capability fit is sufficient | Confirm long-context and vision needs |
| Premium Reasoning | Complex planning, ambiguity, high-stakes reasoning | Justify premium with run type or risk | High output-token cost |
| Visual/Product Judge | Visual hierarchy, product taste, acceptance review | Requires visual/product capability | Do not spend on mechanical work |
| Security/Architecture Review | Threat boundaries, system architecture, adversarial review | Prefer independent review for consequential decisions | Premium spend does not replace evidence |
| Long Context | Large specs, repositories, cross-document consistency | Context need must exceed balanced lane | Large prompts can dominate cost |
| Coding / Refactor | Implementation, deterministic refactor, tests, validation | Scope and safety constraints must be explicit | Review generated changes and validators |
| Fallback / Emergency | Continuity when preferred model is unavailable or unsuitable | Preserve capability floor; disclose tradeoff | Never silently downgrade |

Lane selection is policy guidance. It neither verifies model availability nor
authorizes a call.

## 8. Model-Routing Policy

All entries below are example routing policy for a static snapshot. Exact
provider model IDs, capabilities, context windows, and representative prices
must come from the reviewed local fixture. "Fallback" means local advice only.

| Model or family | Best use | Avoid use | Cost caution | Fallback |
| --- | --- | --- | --- | --- |
| Fable 5 | Premium visual/product judgment, cinematic UX hierarchy, final visual acceptance | Routine drafting, mechanical edits, any assumption that it is available | Treat as premium/unknown; unavailable in the current task context | GPT-5.6 Sol for product architecture; Opus-class for safety ambiguity |
| Opus-class / Opus 4.x | Security boundaries, architecture, adversarial reasoning, future-live gate review | Cheap high-volume work or cosmetic-only edits | Premium; long outputs require explicit budget review | GPT-5.6 Sol, then Claude Sonnet with independent review |
| GPT-5.6 Sol | High-effort product architecture, routing strategy, complex implementation/reasoning; Fable 5 fallback | Low-value bulk drafting where a cheaper lane meets requirements | Premium; justify by complexity, risk, or cross-domain scope | Opus-class for ambiguous safety/future-live boundaries; Claude Sonnet for docs consistency |
| GPT-5.5 | Strong general reasoning, synthesis, and balanced-to-premium daily work | Assuming specialist visual judgment or the cheapest batch route | Medium/high representative class; verify fixture before estimating | Claude Sonnet, then Tera |
| Claude Sonnet | Documentation consistency, architecture synthesis, bounded reviews, daily high-quality work | Acting as the only reviewer for an ambiguous security or live-account gate | Medium representative class; long context may increase spend | GPT-5.5 for general reasoning; Opus-class for escalated review |
| Tera | Cost-aware daily implementation, iteration, and fallback work under an explicit reviewed alias | Final security, account-usage, or ambiguous safety decisions | Low/medium representative class; alias and price may be unknown | GLM/cheaper model for routine work; Claude Sonnet for higher assurance |
| GLM / cheaper models | Cheap Worker lane: drafting, formatting, extraction, exploration, secondary implementation ideas | Sole source for architecture, security, visual acceptance, or consequential approval | Low or free/experimental; do not equate low cost with fit | Tera, then Claude Sonnet |
| Codex | Scoped coding/refactor work, tests, validation, implementation review, deterministic repository changes | Unbounded product strategy or treating generated code as validated | Underlying model cost must be represented explicitly; no generic Codex price assumption | GPT-5.6 Sol for complex implementation reasoning; Claude Sonnet for docs/architecture review |

Routing precedence:

1. Reject any option that lacks a required capability or has `UNAVAILABLE`,
   `UNKNOWN`, or unreviewed-alias status for that requirement.
2. Route safety/future-live/account ambiguity to
   Security/Architecture Review and require operator review.
3. Prefer the lowest-cost lane that meets the capability and assurance floor.
4. Use premium lanes when risk, visual judgment, architectural ambiguity, or
   cross-domain complexity justifies them.
5. Show the ordered fallback chain and tradeoffs; never fail over silently.
6. Never infer quality, safety, or availability from price alone.

## 9. Budget Estimator Behavior

### 9.1 Inputs

- selected model;
- input tokens, non-negative integer;
- output tokens, non-negative integer;
- optional cache-read tokens, non-negative integer not exceeding input tokens;
- run type, one of `routine`, `drafting`, `coding_refactor`,
  `long_context`, `visual_product_review`, `security_architecture_review`, or
  `fallback_emergency`.

### 9.2 Calculation

With all required representative rates present:

```text
uncached_input_tokens = input_tokens - cache_read_tokens
input_estimate = uncached_input_tokens / 1_000_000 * input_rate
cache_estimate = cache_read_tokens / 1_000_000 * cache_read_rate
output_estimate = output_tokens / 1_000_000 * output_rate
estimated_cost = input_estimate + cache_estimate + output_estimate
```

- If cache-read tokens are omitted, they are zero.
- If cache-read tokens are supplied but the cache rate is `null`, use the
  regular input rate as a conservative planning assumption and show
  `CACHE_RATE_UNKNOWN_ASSUMED_INPUT_RATE`.
- If an input or output rate is `null`, `estimated_cost` is `null` and the UI
  shows `INSUFFICIENT PRICING DATA`; it must not invent a number.
- Round only for display; retain enough local precision to avoid cumulative
  rounding error. Currency comes from the selected fixture entry.
- No tax, provider fee, retry, tool-call, image, audio, or account-specific
  adjustment may be implied unless the future fixture explicitly models it.

### 9.3 Outputs

- estimated cost or `null`;
- cost class;
- a cheaper alternative that meets the same required capability floor, or
  `NO REVIEWED CHEAPER ALTERNATIVE`;
- "worth premium model?" signal:
  `RECOMMENDED`, `OPTIONAL`, `NOT_JUSTIFIED`, or `INSUFFICIENT_DATA`;
- assumptions and snapshot date.

The premium signal is deterministic policy:

- `RECOMMENDED` for visual/product or security/architecture work when the
  selected premium lane meets capabilities and a cheaper reviewed option does
  not meet the assurance floor;
- `OPTIONAL` when both premium and cheaper options meet the floor but premium
  may reduce review risk;
- `NOT_JUSTIFIED` for routine/drafting work when a reviewed cheaper option
  meets the same floor;
- `INSUFFICIENT_DATA` when pricing, capability, status, or alias data is
  unknown.

Every output must say: `Static approximate estimate — not account billing`.

## 10. Safety Labels

The exact labels below are mandatory and must not be paraphrased away:

- `STATIC SNAPSHOT`
- `NO API KEY`
- `NO MODEL CALLS`
- `NO ACCOUNT USAGE`
- `NOT LIVE PRICING`
- `FUTURE-GATED LIVE CATALOG`

The complete strip appears at the Observatory entry and estimator. Compact
cards may show a relevant subset only when the complete strip remains visible
on the same screen. `representative pricing`, `example routing lanes`, and
`future-gated live catalog` are preferred explanatory phrases.

## 11. Interactions for Future Implementation

The static snapshot slice permits only local, deterministic interactions:

- model selection updates the local detail panels;
- run type highlights a recommended lane;
- estimator inputs update calculations locally;
- fallback chain updates locally;
- capability filters operate locally;
- keyboard focus and selection update the same state as pointer input.

There are no network calls, fetches, provider clients, account requests,
telemetry posts, or model calls. Selection is not execution. No control may be
named Run, Call, Connect, Sync Account, or similar.

## 12. Mobile Behavior

- Stack cards in reading order: Safety Boundary Strip, lane selector, Route
  Advisor, selected model, simplified estimator, fallback chain, matrix.
- Put the lane selector first after the safety strip.
- Make the Capability Matrix collapsible with a semantic table-equivalent
  fallback.
- Simplify the estimator to essential inputs and one assumptions disclosure.
- Provide no hover-only interaction; selected/focus states are explicit.
- Do not render a dense mega-table or force horizontal page scrolling.
- The constellation may flatten into a lane-grouped list while preserving the
  same selection state and labels.

## 13. Accessibility

- Use semantic buttons for model and lane selection with `aria-pressed` or an
  equivalent selected-state contract.
- Preserve logical keyboard order, visible focus, and arrow-key behavior only
  where a standard composite-widget pattern is implemented correctly.
- Honor `prefers-reduced-motion`; orbital motion becomes a stable pose.
- Never communicate cost class, availability, or safety state by color alone.
- Provide a text alternative for the constellation that lists model, lane,
  cost class, status, and selected state.
- Provide a semantic table-equivalent fallback for the Capability Matrix.
- Maintain readable contrast over actual glass-panel backgrounds and preserve
  forced-colors usability.
- Minimum pointer targets are 44×44 CSS pixels.

## 14. Non-Goals

This spec and the next static snapshot slice explicitly exclude:

- live OpenRouter catalog access;
- account usage or account-backed cost data;
- API keys, tokens, credentials, or `.env` values;
- a backend, proxy, database, authentication service, or secrets manager;
- model calls, automatic routing, or automatic fallback;
- billing synchronization or invoice reconciliation;
- deployment or release;
- a WebGL, Three.js, or Canvas renderer;
- changes to MellyTrade or any trading/broker/execution surface.

## 15. Acceptance Criteria for Static Snapshot Slice

The next implementation task is acceptable only when all items pass:

- [ ] Uses a local fixture only; every entry carries snapshot/source/safety
      notes.
- [ ] Makes no API or other network request.
- [ ] Adds no key, credential, account identifier, `.env`, backend, or proxy.
- [ ] Makes no model call and implies no automatic routing.
- [ ] Implements desktop and mobile states, including a flattened mobile
      constellation/list.
- [ ] Shows all six exact safety labels at the Observatory entry and estimator.
- [ ] Uses `null`/unknown states instead of invented prices, capabilities,
      context windows, or availability.
- [ ] Labels all costs as representative, static, approximate, not live
      pricing, and not account billing.
- [ ] Provides local model, lane, run-type, filter, estimator, and fallback
      interactions with keyboard parity.
- [ ] Provides reduced-motion, text-alternative, and table-equivalent states.
- [ ] Does not use WebGL, Three.js, Canvas, or new runtime dependencies.
- [ ] Does not edit workflow YAML or deploy configuration.
- [ ] Repository validators, JavaScript syntax checks when applicable, browser
      smoke, desktop/mobile visual checks, and `git diff --check` pass.

## 16. Future Gates

These gates are future only. This spec does not authorize or start them.

### `MELLYCORE-OPENROUTER-PUBLIC-CATALOG-LIVE-READINESS-001`

Docs/security readiness review for a future public catalog: permitted fields,
provenance, cache/freshness policy, failure states, rate limits, privacy,
frontend-key prohibition, and truthful labels. It must decide whether a later
slice is allowed; it implements nothing and includes no account usage.

### `MELLYCORE-OPENROUTER-PUBLIC-CATALOG-LIVE-SLICE-001`

Potential read-only public-catalog implementation only after readiness passes
and the operator explicitly authorizes it. It requires visible freshness and
failure states, cache behavior, no account usage, no frontend secret, and
separate validation/deployment gates. It is not part of Option B's first static
snapshot.

### `MELLYCORE-OPENROUTER-ACCOUNT-USAGE-SECURITY-REVIEW-001`

Strict review before any account-backed usage or cost work. It must cover
backend architecture, secret storage, authentication/authorization, data
minimization, log redaction, retention, billing semantics, threat modeling,
deployment security, and explicit operator approval. No account feature may
begin without this gate and separately authorized follow-on tasks.

The exact next task after this spec's local commit is:
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-PUBLISH-001`.
