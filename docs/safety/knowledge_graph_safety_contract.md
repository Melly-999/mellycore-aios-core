# Knowledge Graph Safety Contract

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Version:** 1.0
**Status:** Draft safety specification (docs-only)
**Scope:** Safety rules specific to the Living Context Graph / Knowledge Graph Console feature direction

---

## 1. Relationship to the Repo-Wide Safety Contract

This document extends `[[../../shared_context/SAFETY_CONTRACT]]`. It does not replace or relax any rule there — every rule in the repo-wide contract applies fully to this feature direction. This document adds rules specific to graph nodes, edges, fixtures, and the console UI.

---

## 2. What Can Be Displayed

- Node/edge metadata as defined in `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]`: `id`, `type`, `label`, `summary`, `cluster_id`, `source_refs`, `created_at`, `notes` (subject to Section 3 below), and relation type on edges.
- Aggregate/structural information: cluster membership, edge counts, node tier (size), timeline position, contradiction-ledger status (open/resolved), safety-rule linkage.
- Human-authored summaries of source content (never verbatim reproduction of large source blocks, and never verbatim reproduction of any third-party GPL-licensed code or markup — see `[[../research/external_inspiration_llm_wiki_graph_001]]` Section 2.4).
- References to repo-relative file paths and task IDs already present in this repository's own docs (these are not secrets — they are the project's own documentation structure).

---

## 3. What Must Be Hidden

- Any node/edge whose only available source content is secret-shaped (see Section 4) must be excluded entirely from any committed fixture — not merely UI-hidden. A `SafetyDisplayState.visibility = hidden` (per `[[../../shared_context/CONTEXT_GRAPH_SCHEMA]]` Section 2.5) is a signal to exclude at authoring time, and existence of such a case must itself be raised to the human reviewer during `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` Step 9.
- Raw file contents of any source file must never be embedded wholesale into a node's `summary` or `notes` field — only human-written, reviewed summaries.
- Any personally identifiable or sensitive personal data about an individual must not be displayed unless explicitly approved by the operator for that specific case; by default, no such data may appear.

---

## 4. No Secrets

The following must never appear in any `ContextNode`, `ContextEdge`, `SourceRef`, or `ContradictionLedger` field, in any fixture, in any UI copy, or in any generated context pack:

- Real API keys or provider tokens of any kind (examples of shapes to refuse: `OPENAI_API_KEY=`, `ANTHROPIC_API_KEY=`, `sk-ant-...`, `sk-proj-...`).
- `.env` file contents or `.env` values quoted out of context.
- GitHub personal access tokens (PATs) or any other authentication token.
- Account IDs, broker account numbers, or any MellyTrade runtime credential.
- Passwords, private keys, certificates, or connection strings.

If an ingest pass ever encounters one of these shapes in a candidate source, the correct action is to log a `risk` node describing that the exposure was found and remediated (e.g., "an .env-shaped file was found at `<path>` during ingest and excluded"), never to quote the secret itself anywhere, including in the risk node's `notes`.

---

## 5. No Credentials

Same treatment as Section 4: no database connection credentials, no service-account JSON, no SSH keys, no signing keys. This applies to Neon-metaphor "snapshot" fixtures too (`[[../product/knowledge_graph_console_spec]]` Section 11-12) — a snapshot is a plain static file, never a database credential or connection object.

---

## 6. No Raw `.env`

- No `.env` or `.env.*` file may be referenced as a `SourceRef.locator`, included in a context pack (`[[../../shared_context/CONTEXT_PACK_GENERATOR_SPEC]]` blocklist, Section 3), or quoted in any node/edge field.

---

## 7. No Provider Keys

- No provider API key, whether real, placeholder-that-looks-real, or example-format, may appear in any graph fixture, console UI copy, or ingest artifact. If a routing/provider concept needs to be represented (e.g., "OmniRouter routes to Claude"), represent it as a `model`/`agent` node with a role label only — never with a key, token, or connection example, consistent with the existing `[[../specs/MELLYCORE_HOMEPAGE_SPEC_001]]` "no provider-key forms" rule.

---

## 8. No Personal Sensitive Data Unless Explicitly Approved

- Names of individuals (beyond the operator's own already-public project role) must not be added as graph content by default.
- If a future task explicitly requires representing a named individual (e.g., a reviewer field in the contradiction ledger), that is limited to the minimal identifier the operator already uses in this repo (e.g., "operator," a handle already used in existing docs) — never expanded scope (email, phone, address, etc.) without separate explicit approval.

---

## 9. No Runtime Execution Controls

- The Knowledge Graph Console displays a **read-only** graph. It must never include: an "edit node" form that writes back to a fixture from the browser, a "run ingest" button, a "publish" button, or any control that triggers a backend process. All authoring happens through the human-gated `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` outside the console UI.
- No live polling, no auto-refresh implying a running backend, no WebSocket/SSE connection.

---

## 10. No Live Broker/Trading Controls

- No node type, edge type, or UI element in this feature may represent, imply, or link to MellyTrade broker execution, order placement, buy/sell controls, live account balances, or PnL — consistent with `[[../../README.md]]` and `[[../design/MELLYCORE_DESIGN_SYSTEM_001]]` Section 20 (Forbidden Design Patterns). If MellyTrade needs to be represented in the graph at all, it is only as a `module` node with a summary description ("MellyTrade — separate trading intelligence product coordinated through MellyCore"), never with any execution-shaped content.

---

## 11. No Fake Validator Claims

- Any "validated_by" edge or safety-overlay badge in the console must correspond to an actual, real human review event or an actual passing validation command (e.g., `scripts/validate_project_state.py` output), never an aspirational or assumed validation.
- The Safety Overlay's persistent confirmation text (`[[../product/knowledge_graph_console_spec]]` Section 10) must state that it reflects "the last human-reviewed static fixture" — never imply continuous or real-time validation, matching this repo's existing "no fake live status indicators" discipline (`[[../design/MELLYCORE_DESIGN_SYSTEM_001]]` Section 5, Section 20).
- No safety badge may be rendered for a constraint that is not actually enforced, mirroring the exact rule already stated for `SafetyBadge` in the core design system.

---

## 12. Enforcement

- Every ingest pass must pass through `[[../../shared_context/SOURCE_INGEST_WORKFLOW]]` Step 9 (Human Review) before publication, which explicitly includes a safety-contract check against this document.
- This safety contract must be re-read alongside `[[../../shared_context/SAFETY_CONTRACT]]` before any future implementation task in this feature area begins, per the repo-wide instruction to read shared context first (`[[../../README.md]]`, `[[../../AGENTS.md]]`, `[[../../CLAUDE.md]]`).

---

*This safety contract is a docs-only artifact of `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`. It authorizes no implementation and adds constraints on top of, never in place of, the existing repo-wide safety contract.*
