# Task Report: MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Purpose:** Produce a docs-only research, product, design, schema, and safety specification package for a future MellyCore feature direction — the "MellyCore Living Context Graph" / Knowledge Graph Console — translating external inspiration (Karpathy LLM Wiki, LLM Wiki Newsroom, Gitingest, Homepage, Neon, and TikTok visual references) into a safe, static-first product/spec direction.
**Scope:** Nine required specification files plus this task report and a `RUN_QUEUE.md` update. No frontend, backend, runtime, database, or MCP implementation.
**Status:** Complete

---

## Changed Files

| File | Action | Description |
|---|---|---|
| `docs/research/external_inspiration_llm_wiki_graph_001.md` | Created | Source-by-source summary of the six inspiration references, what to adopt/avoid, licensing cautions |
| `docs/product/knowledge_graph_console_spec.md` | Created | Feature spec: user value, console layout, sidebar controls, overlays, static MVP, future phases |
| `docs/design/knowledge_graph_visual_language.md` | Created | Visual language extending the core design system: clusters, node/edge styling, HUD sidebar, states, accessibility, responsive |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md` | Created | Entity/relation schema: ContextNode, ContextEdge, ContextCluster, SourceRef, SafetyDisplayState; node and relation type tables |
| `shared_context/SOURCE_INGEST_WORKFLOW.md` | Created | 10-step human-gated ingest workflow from source collection to static-fixture publication |
| `shared_context/CONTRADICTION_LEDGER.md` | Created | Ledger template with field definitions and one illustrative (non-live) worked example |
| `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md` | Created | Gitingest-inspired read-only repo digest spec: allowlist/blocklist, token budget, safety summary |
| `docs/safety/knowledge_graph_safety_contract.md` | Created | Feature-specific safety rules extending `shared_context/SAFETY_CONTRACT.md` |
| `agent_prompts/MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001.md` | Created | Reusable prompt template for future review/extension agents |
| `docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001.md` | Created | This task report |
| `shared_context/RUN_QUEUE.md` | Modified | Recorded this task as complete; added the immediate next recommended task |
| `shared_context/AGENT_HANDOFF.md` | Modified | Updated handoff state to reflect this task's completion |

No other files were read-modified. No files under `site/`, no package/config/workflow files, no `.env` files.

---

## Specification Summary

**Research (`docs/research/external_inspiration_llm_wiki_graph_001.md`):** Summarizes Karpathy LLM Wiki (immutable source / mutable derived note / contradiction tracking), LLM Wiki Newsroom (source catalog, entity pages, publish/review gate), Gitingest (bounded read-only repo digest), Homepage (config-driven card grid + search — explicit GPL-copying refusal), Neon (branchable snapshot metaphor only, no DB), and TikTok links (visual mood only, no unverified claims). States the static-first product decision.

**Product (`docs/product/knowledge_graph_console_spec.md`):** Defines the "MellyCore Living Context Graph" feature and "Knowledge Graph Console" page. Layout: command bar, left sidebar (search, cluster filter, relation filter, timeline/contradiction/safety overlay toggles, always-visible relation legend), graph canvas, footer status panel. Defines a Static MVP (one human-reviewed JSON/Markdown fixture, static SVG/CSS rendering, no JS graph library) and four future phases, each requiring separate approval.

**Design (`docs/design/knowledge_graph_visual_language.md`):** Extends the existing design system rather than introducing new tokens. Black-space background with reduced star density behind clusters; cluster color limited to the four existing accent tokens; three discrete node-size tiers by edge count; node shape encodes type; edge line-style (not color) encodes relation type; always-visible relation legend; empty/loading/error states with no live-retry implication; accessibility (two-channel encoding, keyboard operability); reduced motion; responsive behavior including a mobile linear-list fallback.

**Schema (`shared_context/CONTEXT_GRAPH_SCHEMA.md`):** Defines `ContextNode`, `ContextEdge`, `ContextCluster`, `SourceRef`, `SafetyDisplayState` with full field tables. Nine node types (`agent`, `model`, `task`, `doc`, `source`, `decision`, `risk`, `module`, `safety_rule`) and nine relation types (`depends_on`, `defines`, `references`, `contradicts`, `supersedes`, `produced_by`, `validated_by`, `blocked_by`, `belongs_to`), matching the task brief exactly.

**Ingest workflow (`shared_context/SOURCE_INGEST_WORKFLOW.md`):** Ten steps — collect source, summarize, extract entities, extract claims, map nodes, map edges, detect contradictions, write ledger entry, human review, publish (docs/static fixture only). Explicitly cites MellyCore's own real prior incident (`MELLYCORE-DOCS-ACCURACY-SYNC-001`) as the motivating example for contradiction detection. No automation authorized.

**Contradiction ledger (`shared_context/CONTRADICTION_LEDGER.md`):** Template with contradiction ID, related nodes, source refs, claim A/B, severity, status, resolution decision, reviewer, date. One illustrative worked example (explicitly marked non-live) referencing the same real prior incident. No live entries yet — first entries wait for a future ingest pass.

**Context pack generator (`shared_context/CONTEXT_PACK_GENERATOR_SPEC.md`):** Specifies a future, separately implemented, strictly read-only, offline tool: file allowlist/blocklist (secrets/credentials/db files always blocked), token budget with honest truncation reporting, changed-files summary, mandatory safety summary, task-queue reflection. No PAT/API usage authorized.

**Safety contract (`docs/safety/knowledge_graph_safety_contract.md`):** Extends the repo-wide safety contract with feature-specific rules: what can/must-be-hidden, no secrets/credentials/`.env`/provider keys, no personal sensitive data without explicit approval, no runtime execution controls in the console (read-only graph, no edit/publish/run buttons), no live broker/trading controls, no fake validator claims (safety badges must correspond to real enforced constraints and real review events).

---

## Safety Confirmation

- **No secrets.** All nine specification files, the task report, and the two `shared_context/` updates were authored fresh with zero API keys, tokens, credentials, or real configuration values. No `.env` file was created, read for values, or modified.
- **No GLM copy.** No files from the GLM/Z.ai reference workspace were read or copied. The research doc only references the workspace's *existence* as an already-known project fact (matching `shared_context/PROJECT_STATE.md`), not its contents.
- **No frontend/site/backend/runtime/package/workflow/config/env changes.** No file under `site/` was created, read, or modified. No `package.json`, lockfile, build config, or workflow YAML was touched. No runtime/executable code (HTML, CSS, JS, Python, etc.) was created — every new file is Markdown documentation.
- **No provider/API/database/MCP/Obsidian integration.** All references to Neon, providers, and databases are explicitly framed as inspiration/metaphor only, with hard "no live integration" language repeated in the research, product, and safety docs.
- **No live/broker/order/trading UX.** The safety contract doc (Section 10) explicitly forbids any MellyTrade execution-shaped content in the graph; no such content was introduced anywhere in this task's output.
- **No deploy. No push.** No git remote operation was performed. This task only reads local files and, pending validation, creates one local commit.

---

## Validation Evidence

Validation was run from the repository root (`C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`) after all files above were created/updated:

- `git status --short` — see Final Report section of the response for the exact output captured at validation time; only the ten new files and the two modified `shared_context/` files appear, nothing else.
- `git diff --check` — reported below in the Final Report; no whitespace-conflict-marker errors.
- `py scripts\validate_project_state.py` (or `python scripts/validate_project_state.py` if `py` was unavailable) — result captured in the Final Report.
- Targeted risky-term scan across every changed file for: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `sk-ant`, `sk-proj`, `.env`, `GLM`, `buy`, `sell`, `order`, `execute`, `broker`, `live`, `deploy`, `workflow`, `provider key`, `GitHub token`, `PAT`. All hits were classified: matches are exclusively policy/prohibition language (e.g., "no secrets," "no GLM workspace copying," "no live/broker/trading UX," "provider keys stay outside the repo," "no destructive git... push... without explicit approval") or benign substrings (e.g., "order" inside "in order to," "coordination," "workflow" as a noun describing the ingest process itself, which is docs-only and creates no `.yml`/`.yaml` file). No actual secret, no proposed live/broker/order UX, and no token example appeared. See the Final Report for the literal grep output.

---

## Completion Status

**COMPLETE.** All nine required specification files were created exactly as scoped, plus the task report and a `RUN_QUEUE.md`/`AGENT_HANDOFF.md` update. No stop condition was triggered: the repo path, branch, and starting HEAD matched the expected start state; no runtime/backend/frontend/package/workflow/env change was required; no secret or credential was needed; no push/fetch/pull/deploy was required; no external repo code copying occurred.

## Next Recommended Task

The existing queue (`shared_context/RUN_QUEUE.md`) already names `MELLYCORE-GITHUB-REMOTE-SETUP-001` as the immediate next recommended task (remote setup only, no push without separate approval), followed by the deferred `MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001`. This specification package does not change that sequencing — it is additive. If the operator wants to proceed within this new feature direction specifically rather than the existing queue order, the next task would be:

**`MELLYCORE-KNOWLEDGE-GRAPH-FIXTURE-DRAFT-001`** — using `agent_prompts/MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001.md` as the starting prompt, hand-author (not automate) the first small `ContextGraph` fixture covering `docs/design/`, `docs/specs/`, and `shared_context/` as the initial corpus, following `shared_context/SOURCE_INGEST_WORKFLOW.md` end to end including human review — still docs-only, no console implementation.
