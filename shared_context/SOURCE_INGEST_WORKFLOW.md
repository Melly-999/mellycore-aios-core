# Source Ingest Workflow

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Version:** 1.0
**Status:** Draft workflow specification (docs-only)
**Scope:** Safe, human-gated workflow for turning a source into Context Graph fixture entries

---

## 1. Purpose

This document defines the workflow an agent follows to safely propose additions to the Living Context Graph (`[[CONTEXT_GRAPH_SCHEMA]]`). It is a **process specification**, not automation — no script, cron job, or agent loop is created or authorized by this document. Every ingest pass ends at a human review checkpoint before anything is committed.

This workflow directly implements the "publish/review gate" pattern adopted from the LLM Wiki Newsroom inspiration (`[[../docs/research/external_inspiration_llm_wiki_graph_001]]`, Section 2.2) and the "raw sources as immutable truth" pattern from the Karpathy LLM Wiki inspiration (Section 2.1).

---

## 2. Workflow Steps

### Step 1 — Collect Source

- Identify the candidate source: a repo file, a human decision, or a dated external-summary entry.
- Record it as a `SourceRef` (`[[CONTEXT_GRAPH_SCHEMA]]` Section 2.4) with `kind`, `locator`, and `retrieved_at`.
- **Safety gate:** refuse any source whose locator is a `.env` file, a credential/token file, a `db/*.db` file, or any path already excluded by `[[CONTEXT_PACK_GENERATOR_SPEC]]`'s blocklist. Do not create a `SourceRef` for such a path — log it instead as a `risk` node if its existence itself is noteworthy (e.g., "an .env file was found where it should not be" is a `risk`, not a `source`).

### Step 2 — Summarize Source

- Write a one-paragraph, human-readable summary of what the source says, in the agent's own words. Never paste large verbatim blocks of the source, and never paste code/config from a third-party GPL-licensed project (see licensing caution in `[[../docs/research/external_inspiration_llm_wiki_graph_001]]` Section 2.4).
- The summary is a draft artifact only — it does not become a fixture until Steps 3-9 complete and a human approves it.

### Step 3 — Extract Entities

- From the summary, identify candidate `ContextNode` entries: what agents, tasks, docs, sources, decisions, risks, modules, or safety rules does this source describe or affect?
- Draft each candidate node with `type`, `label`, `summary`, proposed `cluster_id`, and `source_refs` pointing back to the `SourceRef` from Step 1.

### Step 4 — Extract Claims

- List the discrete factual claims the source makes (e.g., "the homepage scaffold is complete," "cross-agent smoke has not been run"). Claims are the raw material for both edges and contradiction detection — write them down explicitly rather than skipping straight to edges.

### Step 5 — Map Nodes

- Finalize the candidate `ContextNode` list from Step 3, assigning each a stable `id`, a `cluster_id` (creating a new `ContextCluster` only if no existing cluster fits), and a `safety_display_state_id` (default to `public_metadata_only` unless a reason exists to restrict further).

### Step 6 — Map Edges

- For each claim from Step 4 that describes a relationship between two nodes, draft a `ContextEdge` using the relation types in `[[CONTEXT_GRAPH_SCHEMA]]` Section 5. Every edge must cite the `SourceRef`(s) supporting it.
- Do not invent a relation that isn't supported by an actual claim in a source — no speculative edges.

### Step 7 — Detect Contradictions

- Compare the new claims (Step 4) against existing fixture claims already committed to the graph (and against other sources being ingested in the same pass).
- If two claims about the same subject conflict (e.g., one source says a task is "complete" and another says it is "pending"), do not silently pick one. Proceed to Step 8.
- This step mirrors MellyCore's own prior real incident: `MELLYCORE-DOCS-ACCURACY-SYNC-001` corrected a false "complete" claim about cross-agent smoke testing found in `shared_context/AGENT_HANDOFF.md` against the actual (pending) state recorded elsewhere. That kind of discrepancy is exactly what this step is designed to catch going forward.

### Step 8 — Write Contradiction Ledger Entry

- For every contradiction found in Step 7, create an entry in `[[CONTRADICTION_LEDGER]]` using its template: contradiction id, related nodes, source refs, claim A, claim B, severity, status (`open`), reviewer (blank until Step 9), date.
- Do not resolve the contradiction unilaterally in this step — record it and hand it to human review.

### Step 9 — Human Review

- Present the full draft package to a human operator: proposed nodes, proposed edges, proposed cluster assignments, and any new contradiction ledger entries.
- The human reviewer:
  - Confirms no safety-contract violation exists in any proposed node/edge/notes field (no secrets, no credentials, no live/broker/trading content, no GPL-derived text).
  - Confirms every proposed node/edge cites a real, defensible `SourceRef`.
  - Resolves or defers each contradiction ledger entry (sets `status` to `resolved` with a `resolution_decision` and `reviewer`, or leaves `open` for later).
  - Approves, edits, or rejects the draft package.
- **No ingest pass may skip this step.** An agent may prepare the draft; only a human may approve it for publication.

### Step 10 — Publish (Docs/Static Fixture Only)

- Once approved, the agent commits the new/updated fixture file(s) (e.g., an updated `context-graph-snapshot-<date>.json` or equivalent Markdown table, per `[[CONTEXT_PACK_GENERATOR_SPEC]]` naming) and any updated `CONTRADICTION_LEDGER.md` entries as a docs-only commit.
- "Publish" here means exactly that: a committed static file in this repository. It never means deploying a live site, calling an external API, or writing to any database.
- No automatic republishing, no scheduled/cron ingestion, no agent-triggered commit without the human approval from Step 9 having already happened for that specific content.

---

## 3. What This Workflow Does Not Authorize

- No autonomous agent loop that repeats Steps 1-10 without a human present at Step 9 for each pass.
- No file watcher or continuous ingestion trigger.
- No database write, no API endpoint, no MCP server implementation.
- No use of a GitHub PAT or any authenticated API to fetch external sources.
- No modification of files outside `docs/`, `shared_context/`, and `agent_prompts/` as part of this workflow.

---

*This workflow specification is a docs-only artifact of `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`. It authorizes no automation, runtime, or backend implementation — every ingest pass ends at human review before publication.*
