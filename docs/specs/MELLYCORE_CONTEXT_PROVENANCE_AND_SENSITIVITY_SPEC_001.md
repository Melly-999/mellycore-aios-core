# Context Provenance and Sensitivity Spec

**Task ID:** MELLYCORE-CONTEXT-PROVENANCE-AND-SENSITIVITY-SPEC-001
**Version:** 1.0
**Status:** Draft specification (docs-only)
**Scope:** Foundation model for Milestone B ("One Brain") — how any piece of context earns the right to be trusted, reused, displayed, or cited by MellyCore AIOS

---

## 1. Purpose

Milestone A proved MellyCore can run a capability for real, persist honest evidence, and survive its own review without silent drift — but everything admitted so far (`shared_context/*.md`, the loop registry, run ledgers) has been trusted implicitly, by virtue of being a file a human wrote or an agent produced under direct supervision. Milestone B ("One Brain") widens the aperture: more sources, more agents, more reuse across tasks, and eventually an ingestion gate and a Context Pack Generator that pull content in with less direct human line-of-sight per item.

This document defines the **provenance and sensitivity model** every piece of admitted context must carry before it can be trusted, reused, or displayed. It is the foundation everything else in Milestone B depends on: the ingestion gate needs something to gate on; contradiction handling needs to know which source outranks which; the Context Pack Generator needs to know what is safe to include; the Living Context Graph's `SafetyDisplayState` (`[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]` Section 2.5) needs an upstream source of truth for what visibility a node is even allowed to have.

**This document authorizes no implementation.** No ingestion gate, database, MCP server, backend, or dashboard code is created by this task. It is a specification for future, separately approved coding tasks, following this project's established spec-before-code pattern (Loop Operations Foundation → persistence review → persistence implementation; Knowledge Graph spec package → static UI implementation).

---

## 2. Relationship to Existing Docs

This spec generalizes and sits **above** two existing, narrower specs rather than replacing them:

- `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]`'s `SourceRef` and `SafetyDisplayState` entities are scoped specifically to Living Context Graph fixtures. The model below is the general-purpose version — any admitted context, not just graph nodes, carries a provenance/sensitivity record. A future task may formally derive `SafetyDisplayState.visibility` from this spec's `sensitivity_level` (see Section 5's mapping table) so the two specs stay in lockstep, but that reconciliation is out of scope here — this spec does not edit `CONTEXT_GRAPH_SCHEMA.md`.
- `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]`'s ten steps remain the authoritative human-gated process for turning a source into a graph fixture. Section 6 below extends that same shape (classify → detect contradictions → human review → publish) to admission into "One Brain" generally, rather than defining a second, competing workflow.
- `[[../../shared_context/CONTRADICTION_LEDGER]]` remains the durable record of detected conflicts. Section 7 below adds precedence *guidance* for human reviewers using this spec's trust/provenance fields — it does not change the ledger's own rule that only a human may set `status: resolved`.
- `[[../../shared_context/CONTEXT_PACK_GENERATOR_SPEC]]`'s file allowlist/blocklist is a coarse, path-based filter. This spec's sensitivity model is finer-grained (per-item, not per-file) and applies after a context pack is generated, at the point an item is proposed for admission.

---

## 3. The `ContextSource` Record

Every piece of context admitted into One Brain — a fact, a claim, a document, a generated summary — is represented by one `ContextSource` record with the following required fields.

| Field | Type | Required | Description |
|---|---|---|---|
| `source_id` | string | yes | Stable unique identifier, e.g. `ctx-2026-07-17-roadmap-milestone-a-status`. |
| `source_identity` | string | yes | Human-readable description of exactly where this came from — a file path, a person's name/role, a task ID, a URL class (never the URL itself if it requires auth). |
| `source_type` | enum (Section 4) | yes | One of the four provenance labels: `user_provided`, `repo_derived`, `generated`, `externally_sourced`. |
| `verification_state` | enum | yes | `verified` or `unverified` (Section 4). |
| `trust_level` | enum | yes | `high`, `medium`, or `low` (Section 4.3). Defaulted from `source_type` × `verification_state`, human-overridable with a stated `trust_level_rationale`. |
| `sensitivity_level` | enum (Section 5) | yes | One of `public`, `internal`, `private`, `secret`, `regulated_high_risk`. |
| `allowed_use` | enum (Section 5.2) | yes | Derived from `sensitivity_level` by default; may be set stricter but never looser without a stated `allowed_use_override_rationale`. |
| `captured_at` | date (YYYY-MM-DD) | yes | Date this content was captured/read/generated. |
| `staleness_policy` | enum (Section 6) | yes | `immutable_historical`, `volatile`, or `periodic_review`. |
| `review_after` | date (YYYY-MM-DD) | conditional | Required if `staleness_policy` is `volatile` or `periodic_review`. |
| `proposed_by` | string | yes | Agent/task ID that proposed this record for admission. |
| `reviewed_by` | string \| null | yes | Human reviewer identity. `null` until reviewed — no record is admitted unreviewed. |
| `decision` | enum | yes | `admitted`, `rejected`, or `deferred`. |
| `decision_at` | date (YYYY-MM-DD) \| null | conditional | Required once `decision` is not pending. |
| `decision_rationale` | string | yes | Why this decision was made — required even for an obvious `admitted` decision, so a future reader never has to re-derive the reasoning. |
| `superseded_by` | string (`source_id`) \| null | no | If set, this record is historical; the referenced record is current. |
| `notes` | string \| null | no | Must never contain secrets, credentials, `.env` values, or account identifiers — same field-level rule as `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]` Section 6. |

**Immutability rule:** once `decision` is set, a `ContextSource` record is never edited in place except to set `superseded_by`. A changed or re-reviewed source gets a **new** `source_id`; the old record stays as history. This is the same write-once pattern already proven by the loop run-evidence system (`shared_context/loops/runs/**`) — deliberately reused here rather than inventing a second immutability convention.

---

## 4. Provenance Labels

Provenance answers *where did this come from and has anyone checked it*. Two independent axes.

### 4.1 `source_type` (where it came from)

| Label | Meaning | Example |
|---|---|---|
| `user_provided` | A human operator stated it directly, in this conversation or a prior one. | "The canonical repo is `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`." |
| `repo_derived` | Read directly from a file/commit already in this repository — the closest thing to primary source this project has. | The actual content of `shared_context/ROADMAP.md`, a `git log` result. |
| `generated` | Produced by an agent (summary, inference, synthesis) rather than copied from a primary source. | An agent's one-paragraph summary of a source, per `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` Step 2. |
| `externally_sourced` | From outside this repository and outside direct operator statement — a fetched page, an external doc, a third-party reference. | The Karpathy LLM Wiki / Gitingest inspiration summaries already cited across `docs/research/`. |

### 4.2 `verification_state` (has it been checked)

| Label | Meaning |
|---|---|
| `verified` | An independent check confirmed the claim — a human confirmed it, or a second, independent source corroborates it, or (for `repo_derived`) the content was read directly from the repository at the time of the claim rather than recalled from memory. |
| `unverified` | Asserted but not independently checked. Default for anything not yet reviewed. |

### 4.3 `trust_level` Default Lookup

`trust_level` is computed from `source_type` × `verification_state` at proposal time, then may be overridden by the human reviewer with a stated rationale (never silently).

| `source_type` | `verified` | `unverified` |
|---|---|---|
| `user_provided` | `high` | `medium` |
| `repo_derived` | `high` | `medium` |
| `generated` | `medium` | `low` |
| `externally_sourced` | `medium` | `low` |

Rationale: primary sources (what a human said, what a file actually contains) start higher than derived or external content, because they are closer to ground truth and carry less transformation risk. `generated` content — even when later verified — is capped at `medium`, never `high`, because an agent's synthesis can be fluent and wrong in ways a direct file read cannot; a human reviewer may raise this with a stated rationale, but the default deliberately does not auto-grant `high` trust to AI-generated claims.

---

## 5. Sensitivity Labels

Sensitivity answers *who is allowed to see or use this, and under what conditions*.

| Label | Meaning | Examples in this project's context |
|---|---|---|
| `public` | Safe to show in a hosted showcase, a public repo, a portfolio artifact. | The static `site/index.html` architectural copy; README content. |
| `internal` | Safe within this project's working context (dashboard, agent reasoning, shared_context files) but not intended for a public audience. | Task docs under `docs/tasks/`, internal design rationale. |
| `private` | Personal or operator-specific information that must stay local and must not be summarized externally, even internally-facing displays. | Local file paths containing a username, machine-specific configuration. |
| `secret` | Credentials, API keys, tokens, `.env` values, account identifiers — anything the repo-wide `[[../../shared_context/SAFETY_CONTRACT]]` already forbids from ever being committed. | Provider API keys, passwords. |
| `regulated_high_risk` | Financial, trading, health, legal, or PII-adjacent content subject to compliance obligations beyond this project's own safety contract — most relevant here because of MellyCore's proximity to the separate MellyTrade project. | Anything resembling brokerage account data, trade history, personally identifiable customer information. |

### 5.1 Hard Rule: `secret` and `regulated_high_risk`

- **`secret` content is refused at admission, always.** It is never assigned `allowed_use`; the correct `decision` is `rejected`, logged with `decision_rationale` explaining what category of secret was detected (never the secret value itself), matching `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` Step 1's existing safety gate.
- **`regulated_high_risk` content defaults to `rejected` on first contact.** It may only ever be admitted through a separate, explicitly-scoped and explicitly-approved review process outside the normal admission workflow described in Section 6 — this spec does not define that process, and none exists yet. Until it does, the only correct `decision` for `regulated_high_risk` content is `rejected` or `deferred`.
- Both rules exist specifically because of the `**/MellyTrade/**` / `**/mellytrade/**` boundary already enforced by `shared_context/loops/LOOP_REGISTRY.json`'s `global_forbidden_paths` — this spec extends that same boundary from "forbidden loop read scope" to "forbidden context admission," so the rule is enforced consistently at every layer, not just the loop system.

### 5.2 `allowed_use` Default Matrix

| `sensitivity_level` | Default `allowed_use` | May a human loosen it? |
|---|---|---|
| `public` | `public_display` — may appear in the dashboard, a static page, or a portfolio artifact. | N/A, already broadest. |
| `internal` | `internal_summary_display` — may appear in the dashboard or internal docs as a reviewed summary; never in a public-facing artifact. | No — loosening to `public_display` requires re-classifying `sensitivity_level` itself, not overriding `allowed_use`. |
| `private` | `internal_reasoning_only` — usable by an agent to reason about a task; must never be displayed, summarized, or quoted anywhere, including the dashboard. | No. |
| `secret` | `must_not_be_ingested` — refused outright (Section 5.1). | Never. |
| `regulated_high_risk` | `must_not_be_ingested` — refused outright pending a separate approval process (Section 5.1). | Never, by this spec alone. |

A human reviewer may always set a **stricter** `allowed_use` than the default (e.g., mark a nominally `public` item `internal_summary_display` because of context-specific caution) with a stated `allowed_use_override_rationale`. Loosening beyond the default is never permitted through this field — it requires re-examining `sensitivity_level` itself, keeping the two concerns separable and auditable.

---

## 6. Staleness and Expiry

Motivation is not theoretical: `MELLYCORE-OPERATIONAL-TRUST-REVIEW-001` found and fixed the same class of bug twice in three tasks — `shared_context/PROJECT_STATE.md`'s "Current HEAD" line going stale, and a "next task" claim contradicted by a later entry in the same file. Every `ContextSource` record must declare how it can go stale, so this stops being caught only by manual review.

| `staleness_policy` | Meaning | Example |
|---|---|---|
| `immutable_historical` | Describes a completed, dated event. Never goes stale — the record is true forever as a historical fact, even if current state has since changed. | "`MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001` was committed as `87077b9`." |
| `volatile` | Describes current, mutable state that changes as the project moves. Requires `review_after`; treat as suspect once that date passes. | "Current HEAD is `d59db8a`." "The next recommended task is X." |
| `periodic_review` | Describes something that doesn't change often but should be re-confirmed on a cadence regardless (policy text, safety rules, role definitions). Requires `review_after`. | The contents of `[[../../shared_context/SAFETY_CONTRACT]]`. |

A record whose `review_after` date has passed is not automatically deleted or hidden — it is flagged (see Section 8's "stale items" dashboard field) so a human can re-verify or explicitly re-date it. This mirrors the loop system's own philosophy: unmeasured is not the same as zero, and stale is not the same as false — both must be represented honestly, not silently collapsed into a misleading state.

---

## 7. Contradiction Behavior

When two `ContextSource` records make conflicting claims about the same subject, the resolution path is **always** `[[../../shared_context/CONTRADICTION_LEDGER]]` — this spec adds no shortcut that bypasses human review. What it adds is precedence *guidance* to help a reviewer decide faster, never an automatic resolution:

1. Higher `trust_level` is weighed first, but is a signal, not a verdict — a reviewer may still find the lower-trust claim correct and must say why.
2. For two records with equal `trust_level`, an `immutable_historical` record about a past, dated fact outranks a `volatile` record about current state, since the former cannot itself go stale.
3. For two `volatile` records at equal `trust_level`, the more recent `captured_at` is weighted higher — but only as a tiebreaker, since a newer claim being wrong is exactly as possible as an older one being right.
4. `repo_derived` generally outranks `generated` at equal `trust_level`, since it is closer to primary source.
5. **No contradiction is ever silently resolved by these rules alone.** Every contradiction still gets a `[[../../shared_context/CONTRADICTION_LEDGER]]` entry, `status: open` until a human sets `resolution_decision` and `status: resolved`, exactly as that document already requires. This spec's precedence guidance may be cited *inside* a `resolution_decision` field as the stated reasoning, but the decision itself remains human-made.

---

## 8. Admission Workflow (Extends the Existing Ingest Workflow)

This is the general form of `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]`'s ten steps, applicable to any content proposed for One Brain admission, not only Living Context Graph fixtures. It reuses that workflow's shape rather than replacing it.

1. **Collect** — identify the source; refuse at this step, per Section 5.1, if it is `secret` or `regulated_high_risk`-shaped (matching the existing `.env`/credential/`db/*.db` refusal already specified in `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` Step 1).
2. **Classify provenance** — assign `source_type` and `verification_state` (Section 4).
3. **Classify sensitivity** — assign `sensitivity_level` and derive `allowed_use` (Section 5). Anything landing on `secret` or `regulated_high_risk` exits here as `rejected`.
4. **Classify staleness** — assign `staleness_policy` and, if applicable, `review_after` (Section 6).
5. **Compute default `trust_level`** from the Section 4.3 lookup table.
6. **Detect contradictions** against already-admitted `ContextSource` records and other items in the same batch, exactly as `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` Step 7 already does for graph fixtures — logging any conflict to `[[../../shared_context/CONTRADICTION_LEDGER]]` per Section 7 above.
7. **Human review** — a human confirms or overrides `trust_level`/`allowed_use` (with stated rationale for any override), resolves or defers each contradiction found, and sets `decision` (`admitted` / `rejected` / `deferred`) with `decision_rationale`. No record may reach `admitted` without this step, matching `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` Step 9's "no ingest pass may skip this step" rule.
8. **Publish** — an `admitted` record is committed as a static, docs-only artifact (its eventual on-disk home — e.g. a future `shared_context/context_provenance/` directory — is not created by this spec; that is implementation, out of scope here). Never a live database write, never an auto-commit without the human decision from Step 7 having already happened.

### What this workflow does not authorize

Same constraints as `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` Section 3, restated for this broader scope: no autonomous loop repeating these steps without a human at Step 7 for each pass; no file watcher or continuous ingestion trigger; no database, API, or MCP implementation; no authenticated fetch of external sources; no modification of files outside `docs/`, `shared_context/`, and `agent_prompts/` by this workflow itself.

---

## 9. Future Dashboard Fields (Specification Only — No Code Written)

Once `ContextSource` records exist for real (they do not yet — this task creates none), a future task may add a "Context" tab to `site/dashboard.html`, following the dashboard's existing pattern: real data read live from committed files, mock data explicitly labeled, no provider calls. That future task would need to design its own data-loading and rendering code; this section only specifies *what* it should show, not how.

| Field | Meaning | Data source (once it exists) |
|---|---|---|
| **Source count** | Total admitted `ContextSource` records, broken down by `source_type`. | Count of files/entries under the future provenance-record location. |
| **Stale items** | Count of records whose `review_after` date has passed and have not been re-verified. | Computed by comparing each `volatile`/`periodic_review` record's `review_after` against the current date. |
| **Contradiction count** | Open vs. resolved entries in `[[../../shared_context/CONTRADICTION_LEDGER]]`. | Parsed live from that file, same pattern already used for `ROADMAP.md`/`RUN_QUEUE.md` on the existing dashboard. |
| **Sensitive items blocked** | Count of admission attempts that resulted in `decision: rejected` for `secret` or `regulated_high_risk` reasons. | Aggregate count only — **never** the item's `source_identity`, `notes`, or any content, matching Section 5.1's rule that even the fact of a blocked secret must not leak *what* it was. |
| **Latest accepted context pack** | Most recent `[[../../shared_context/CONTEXT_PACK_GENERATOR_SPEC]]` output that was reviewed and admitted, with its date and reported token estimate. | The most recently dated context-pack artifact file, once that generator is implemented (it is not yet — see that spec's own "authorizes no implementation" note). |

None of this exists today. The dashboard's current tabs (Overview, Loops, Models, Evidence, Roadmap, Live) are unchanged by this task.

---

## 10. What Remains Intentionally Unimplemented

- No `ContextSource` record has been created. This spec defines the shape; it populates nothing.
- No ingestion gate exists. This spec is explicitly the prerequisite Milestone B lists before that item — the gate's actual validation logic is a separate, future task.
- No code, script, or CLI implements any part of Section 8's workflow. It is a process specification, exactly like `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` before it.
- No dashboard tab, panel, or field from Section 9 has been built.
- No approval process for `regulated_high_risk` content has been defined (Section 5.1 explicitly flags this as a future, separately-scoped gap — the safe default in the meantime is refusal).
- No reconciliation between this spec's `sensitivity_level` and `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]`'s `SafetyDisplayState.visibility` has been made — they are conceptually aligned (Section 2) but not yet formally unified.

---

## 11. Safety Notes

- Every rule in `[[../../shared_context/SAFETY_CONTRACT]]` applies to this spec's model without exception — nothing here loosens any existing constraint.
- `notes` and `decision_rationale` fields must never contain secrets, credentials, `.env` values, or account identifiers, matching the field-level rule already established in `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]` Section 6.
- The `secret` and `regulated_high_risk` refusal rules (Section 5.1) are hard constraints, not defaults a future task may quietly relax — relaxing either requires a new, explicitly-scoped and explicitly-approved spec of its own, not an implementation detail of the ingestion gate.

---

*This specification is a docs-only artifact of `MELLYCORE-CONTEXT-PROVENANCE-AND-SENSITIVITY-SPEC-001`. It authorizes no ingestion gate, database, API, MCP, dashboard, or runtime implementation — every admission remains a human-reviewed, docs-only action until a separate, explicitly approved task changes that.*
