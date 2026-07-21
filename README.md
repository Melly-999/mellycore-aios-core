# MellyCore AIOS

MellyCore AIOS is a **local-first, operator-controlled AI Operations
Observatory**. Its purpose is to make models, agents, runs, context, memory,
recommendations, and approvals visible, inspectable, approval-gated, and
auditable.

The operating loop is deliberately controlled:

> observe → analyze → recommend → approve → implement → validate → record

Consequential actions remain human-approved. MellyCore does not autonomously
change its safety rules, merge or deploy changes, execute recommendations, or
store provider credentials in this repository.

[Open the local cockpit](site/dashboard.html) · [Review the current roadmap](shared_context/ROADMAP.md) · [Inspect project state](shared_context/PROJECT_STATE.md) · [Open the canonical repository](https://github.com/Melly-999/mellycore-aios-core)

## Product Direction

The Observatory direction brings several operational views into one coherent
cockpit:

- **Mission Control** — current objectives, gates, blockers, and operator choices.
- **Agent Activity** — visible work state and evidence without uncontrolled tool use.
- **Context Pulse** — provenance, sensitivity, freshness, and contradiction signals.
- **Model Router** — explicit model roles and later evidence-backed routing decisions.
- **Unified Run Ledger** — one inspectable history for validated runs and outcomes.
- **Approval Queue** — consequential recommendations waiting for operator decision.
- **Memory & Recommendation Ledger** — durable, reviewable recommendations and their disposition.
- **AI Estate Inventory** — the local models, agents, skills, tools, and governed surfaces in scope.
- **Skill Gap Detector** — planned analysis of missing or weak operational capabilities.
- **Memory Freshness Monitor** — planned detection of stale, conflicting, or superseded context.

These are roadmap domains, not claims that the complete Observatory already
exists. The AI Operations Intelligence specification
(`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001`) is **integrated into canonical
`main` via PR #7**; it defines the detailed logical contract for these domains
without authorizing implementation — its modules remain `SPECIFIED`, not
runtime-implemented. The next roadmap task,
`MELLYCORE-OPERATIONS-DATA-CONTRACT-001`, translates that contract into
fixture/schema artifacts and is **integrated into canonical `main` via PR
#13** (merge commit `e0db28f06613d29028df96a2d651b6dfdf2f2aa8`). Integration
is documentation/schema/fixture scope only: no adapter, backend execution,
runtime-consumed schema, or provider integration was implemented or
authorized by this merge.

## What Exists Today

| Area | Status | Truthful boundary |
| --- | --- | --- |
| Repository documentation and static homepage | Implemented | Local, reviewable source; no hosted runtime is claimed. |
| Loop Operations Foundation | Implemented, report-only | Nine registered loops; no production-enabled or unattended loop. |
| Context Gate | Implemented through I4 | Guarded CLI, immutable records, content-free index, read-only audit/dashboard surface. |
| Project-health evidence | Implemented | Two human-invoked persisted runs; no scheduler. |
| Live Cockpit V2 / Social Source Arena | Implemented legacy prototype | Local vanilla HTML/CSS/JS surface; not the completed Observatory. NASA runtime retirement (see "NASA Images Disposition" below) is implemented on a separate branch/draft PR, pending review and merge — canonical `main` as described here reflects the pre-retirement state until that PR lands. |
| Model comparison copy | Simulated | Deterministic local text, not live model responses. |
| Holographic Source Arena | Accepted specification | The 390×844 model-lens hero and 3D treatment are not implemented. |
| Source Arena Hybrid renderer decision | Accepted (decision/specification level only, 2026-07-20) | `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` records an accepted WebGL-enhanced, CSS-complete-fallback renderer decision; no WebGL code or vendored dependency exists in the repository yet — implementation requires its own separately-authorized task. |
| Observatory modules and real adapters | Planned | Detailed specification and guarded implementation remain future work. |

The repository also contains a hand-authored Living Context Graph fixture with
8 clusters, 45 nodes, and 66 edges. It is useful historical prototype evidence,
not a live telemetry or memory system.

## Source Arena Visual Direction

Source Arena remains the leading holographic visual metaphor: a 390×844
mobile-first model-lens composition that puts the operator's selected evidence,
model perspectives, provenance, recommendations, and approval state into one
inspectable feed. It is the intended hero experience.

The accepted visual contract is in
[`MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md`](docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md).
That specification does not mean the holographic UI, 3D treatment, model-lens
feed, or real-data adapters are already implemented. Overview's core/orbit/hull
composition remains supporting imagery only.

An accepted Hybrid renderer decision —
[`MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`](docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md)
(status: **ACCEPTED**, 2026-07-20, decision/specification level only) —
narrowly permits a WebGL-enhanced renderer for Source Arena's central stage,
backed by one pinned, vendored Three.js module, always paired with a complete
CSS/DOM fallback. Zero build step and zero external runtime network requests
remain preserved under this decision. No WebGL code, no vendored dependency,
and no such renderer exist in this repository as of this note — implementing
any of it requires its own separately-authorized task.

## NASA Images Disposition

NASA Images was never a current product pillar, roadmap module, or intended
core integration. Historical task reports and `v0.2.0` release evidence
describing the earlier NASA-backed prototype remain untouched in the
repository as the historical record of why it existed.

`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001` (implemented on branch
`fix/mellycore-source-arena-nasa-runtime-retirement-001`, draft PR open,
pending review) removes the executable NASA Images API code from
`site/dashboard.html` / `site/js/dashboard.js` and replaces it with a local,
deterministic Source Archive dataset: zero external requests, no API key, no
boot-time network call. This status is accurate for that branch/PR; canonical
`main` reflects it only once the PR is reviewed and merged.

`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` (**ACCEPTED**,
2026-07-20, decision/specification level only) recorded the decision
authorizing this retirement. The retirement task itself implements no
adapter, backend, runtime-consumed schema, provider integration, renderer, or
CSS fallback — those remain separately gated, not-yet-implemented future
work.

## Safety and Non-Goals

MellyCore AIOS is not:

- a NASA image browser or generic space-media application;
- a trading terminal or part of MellyTrade;
- an autonomous self-modifying system;
- an autonomous merge, deployment, or recommendation-execution agent;
- a provider-key or secret store;
- a production backend that already executes approvals;
- a system permitted to modify its own safety rules.

Provider keys, tokens, account identifiers, and private runtime state stay
outside the repository. Real adapters, runtime execution, and guarded operations
remain later milestones requiring explicit specifications, reviews, operator
approval, and validation.

## Architecture and Evidence Flow

```text
Repository evidence and local operational state
                    |
                    v
       Guarded context and run records
                    |
                    v
       Read-only observability surfaces
                    |
                    v
     Operator review and explicit approval
                    |
                    v
 Separately authorized implementation/validation
```

The static graph fixture, Context Gate, loop evidence, cockpit prototype, and
future Observatory modules are distinct layers. Planned views must not be
presented as implemented merely because a specification names them.

## Local Setup

No package installation or build step is required for the current local preview.

1. Clone the canonical repository.
2. Serve the repository using the verified localhost instructions in
   [`MELLYCORE_LOCALHOST_QUICKSTART.md`](docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md).
3. Bind only to `127.0.0.1`.
4. Open [`site/index.html`](site/index.html) or [`site/dashboard.html`](site/dashboard.html).

The current dashboard includes legacy prototype behavior. A local preview is not
a public deployment or proof that planned Observatory capabilities exist.

## Validation

Run from the repository root:

```powershell
py -3.9 -B -m scripts.context_gate audit --json
py -3.9 -B -m scripts.loop_ops validate
py -3.9 -B scripts/validate_project_state.py
py -3.9 -B -m unittest discover
```

The repository-specific checks validate the context index/audit, loop registry,
project structure, safety-sensitive patterns, and standard-library test suite.

## Repository Structure

```text
site/             Static homepage and legacy local cockpit prototype
shared_context/   Concise operational state, queue, handoff, safety, and evidence
docs/             Product, design, architecture, evidence, specifications, and task reports
agent_prompts/    Repository-specific guidance for supported agent workflows
scripts/          Project validation, Context Gate, and Loop Operations utilities
tests/            Standard-library tests for the implemented guarded tooling
```

## Author and Related Work

**Mateusz Ozimkiewicz**

Full-Stack Developer | React · TypeScript · FastAPI · AI Tools

- [GitHub profile](https://github.com/Melly-999)
- [Canonical MellyCore AIOS repository](https://github.com/Melly-999/mellycore-aios-core)
- [MellyTrade](https://github.com/Melly-999/alpha_data_scraper_ai) — a separate safety-first, read-only AI trading workstation project

<!-- PORTFOLIO_URL_PENDING -->
