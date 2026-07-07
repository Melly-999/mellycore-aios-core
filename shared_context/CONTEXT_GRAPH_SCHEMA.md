# Context Graph Schema

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Version:** 1.0
**Status:** Draft schema specification (docs-only)
**Scope:** Data model for the MellyCore Living Context Graph static fixtures

---

## 1. Purpose

This document defines the entity and relation schema used by any static fixture produced for the Knowledge Graph Console (`[[../docs/product/knowledge_graph_console_spec]]`). It is a **schema specification only** — it defines shapes, not a database, API, or running service. Any future fixture (JSON or Markdown table) must conform to this schema.

All fixtures produced against this schema are static files committed to the repository after human review (`[[SOURCE_INGEST_WORKFLOW]]`). No fixture may be generated and published without that review step.

---

## 2. Entities

### 2.1 `ContextNode`

Represents one addressable thing in MellyCore's knowledge — an agent, a doc, a decision, etc.

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable unique identifier, kebab-case, e.g. `node-safety-contract`. |
| `type` | enum (Section 4) | yes | One of the node types listed below. |
| `label` | string | yes | Short human-readable name, 2-6 words. |
| `summary` | string | yes | One-sentence description of the node. |
| `cluster_id` | string | yes | References a `ContextCluster.id`. |
| `source_refs` | string[] | yes | List of `SourceRef.id` values this node is derived from. Must be non-empty — every node must trace to at least one source. |
| `safety_display_state_id` | string | yes | References a `SafetyDisplayState.id` governing what may be shown for this node. |
| `created_at` | date (YYYY-MM-DD) | yes | Date the node was first added to a fixture. |
| `superseded_by` | string (node id) | no | If set, this node is historical; the referenced node is current. |
| `notes` | string | no | Optional free-text clarification. Must not contain secrets (see safety contract). |

### 2.2 `ContextEdge`

Represents a directed relation between two nodes.

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable unique identifier, e.g. `edge-0001`. |
| `from_node_id` | string | yes | Source `ContextNode.id`. |
| `to_node_id` | string | yes | Target `ContextNode.id`. |
| `relation` | enum (Section 5) | yes | One of the relation types listed below. |
| `source_refs` | string[] | yes | List of `SourceRef.id` values supporting this edge's existence. |
| `created_at` | date (YYYY-MM-DD) | yes | Date the edge was first added to a fixture. |
| `notes` | string | no | Optional free-text clarification. |

### 2.3 `ContextCluster`

Represents a named grouping of nodes for the sidebar cluster filter (`[[../docs/product/knowledge_graph_console_spec]]` Section 6).

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable unique identifier, e.g. `cluster-safety`. |
| `label` | string | yes | Short display name, e.g. "Safety". |
| `accent` | enum | yes | One of: `orbital-violet`, `plasma-blue`, `signal-cyan`, `muted-lavender` (must map 1:1 to existing design-system color tokens — no new colors). |
| `description` | string | yes | One-sentence description of what belongs in this cluster. |

### 2.4 `SourceRef`

Represents an immutable reference to a real, already-existing artifact (a repo file, a dated external inspiration summary, a human decision record). `SourceRef` entries are the "raw sources as immutable truth" pattern adopted from the Karpathy LLM Wiki inspiration (`[[../docs/research/external_inspiration_llm_wiki_graph_001]]`).

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable unique identifier, e.g. `source-safety-contract-md`. |
| `kind` | enum | yes | One of: `repo_file`, `human_decision`, `external_summary`. |
| `locator` | string | yes | For `repo_file`: a repo-relative path. For `human_decision`: a reference to a `shared_context/DECISIONS.md` entry. For `external_summary`: a reference to the dated section in `[[../docs/research/external_inspiration_llm_wiki_graph_001]]`. Never a live URL requiring credentials; never a `.env` or secret file path. |
| `retrieved_at` | date (YYYY-MM-DD) | yes | Date this source was captured/reviewed. |
| `immutable` | boolean | yes | Always `true` for a committed `SourceRef` — once referenced by an edge/node, a `SourceRef` is not edited; a changed source gets a new `SourceRef.id` and the old one is marked superseded via the referencing nodes/edges. |

### 2.5 `SafetyDisplayState`

Represents what may be shown for a node, keeping the safety contract enforceable at the data level, not just by convention. Adopted directly for the console's Safety Overlay (`[[../docs/product/knowledge_graph_console_spec]]` Section 10).

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable unique identifier, e.g. `safety-display-public-metadata-only`. |
| `visibility` | enum | yes | One of: `public_metadata_only` (name/summary/type only, no content body), `internal_summary_only` (a reviewed summary, never raw file contents), `hidden` (node may exist in the schema for graph completeness but must not be rendered — used only if a future ingest pass discovers something that must never surface, e.g. accidentally-referenced secret-shaped content; such a node must be flagged in the contradiction/safety review and excluded from any committed fixture, not merely hidden in the UI). |
| `rationale` | string | yes | Why this visibility level applies. |

---

## 3. Relationships Between Entities

```
SourceRef  --(derives)-->  ContextNode  --(belongs_to)-->  ContextCluster
ContextNode --(safety_display_state_id)--> SafetyDisplayState
ContextNode --(from/to)--> ContextEdge --(relation)--> ContextNode
```

Every `ContextNode` must belong to exactly one `ContextCluster`, must reference at least one `SourceRef`, and must reference exactly one `SafetyDisplayState`. Every `ContextEdge` must reference at least one `SourceRef` justifying the relation.

---

## 4. Node Types

| Type | Meaning | Example |
|---|---|---|
| `agent` | An AI agent or tool in MellyCore's coordination roster | ChatGPT, Claude Code, Codex |
| `model` | An underlying model/provider referenced by routing docs | Claude, GLM 5.2 |
| `task` | A tracked unit of work (task ID) | `MELLYCORE-HOMEPAGE-SPEC-001` |
| `doc` | A documentation file | `MELLYCORE_DESIGN_SYSTEM_001.md` |
| `source` | An external inspiration or reference source | "Gitingest concept summary" |
| `decision` | A recorded project decision | An entry in `shared_context/DECISIONS.md` |
| `risk` | A named risk or open concern | "GLM workspace wholesale-copy risk" |
| `module` | A structural repo area/component grouping | "Design System", "Homepage Spec" |
| `safety_rule` | A specific rule from the safety contract | "No secrets committed" |

## 5. Relation Types

| Relation | Meaning | Direction convention |
|---|---|---|
| `depends_on` | The `from` node requires the `to` node to be valid/complete | task → doc, doc → doc |
| `defines` | The `from` node authoritatively defines the `to` node's shape/rules | doc → module, doc → safety_rule |
| `references` | The `from` node mentions/cites the `to` node without a dependency | doc → source |
| `contradicts` | The `from` node's claim conflicts with the `to` node's claim | doc → doc, decision → doc |
| `supersedes` | The `from` node replaces the `to` node as current truth | doc → doc (new spec version → old) |
| `produced_by` | The `from` node (a doc/task output) was produced by the `to` node (an agent/task) | doc → agent, doc → task |
| `validated_by` | The `from` node's claim was checked/confirmed by the `to` node (a task, a review) | doc → task |
| `blocked_by` | The `from` node cannot proceed until the `to` node (a risk, a decision, a task) resolves | task → risk, task → decision |
| `belongs_to` | The `from` node is a structural member of the `to` node (typically a cluster) | node → cluster (structural, not semantic) |

---

## 6. Safety Notes Specific to This Schema

- `notes` fields on `ContextNode` and `ContextEdge` must never contain secrets, API keys, tokens, `.env` values, or account identifiers — this is enforced by the same repo-wide safety contract (`[[SAFETY_CONTRACT]]`), applied at the field level here.
- `SourceRef.locator` must never be a URL requiring authentication, a PAT-gated API endpoint, or a path inside `db/` or any local runtime-state directory.
- A `SafetyDisplayState` of `hidden` is a signal to exclude the node from any committed fixture entirely, not a UI-only hide — nothing sensitive should ship in the fixture file at all, visible or not.
- This schema defines shape only. It does not define, authorize, or imply any storage engine, query language, API, or UI beyond the static fixture + static rendering described in `[[../docs/product/knowledge_graph_console_spec]]`.

---

*This schema specification is a docs-only artifact of `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`. It authorizes no database, API, or runtime implementation.*
