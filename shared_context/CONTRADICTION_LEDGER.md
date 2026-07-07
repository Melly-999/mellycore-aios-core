# Contradiction Ledger

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Version:** 1.0
**Status:** Draft ledger template (docs-only)
**Scope:** Durable record of detected contradictions between sources referenced by the Living Context Graph

---

## 1. Purpose

This ledger is the durable record of contradictions detected during `[[SOURCE_INGEST_WORKFLOW]]` Step 7, and of any contradiction discovered through other project work (manual review, QA passes, agent handoff corrections). It exists so that disagreements between sources are tracked as first-class, reviewable objects instead of being silently overwritten — the pattern adopted from the Karpathy LLM Wiki / LLM Wiki Newsroom inspiration (`[[../docs/research/external_inspiration_llm_wiki_graph_001]]`).

This is a template and process document. It does not itself contain any real contradiction entries yet — the first entries are created by a future, separately run ingest pass or by manually logging a known discrepancy.

---

## 2. Entry Template

Copy this block for each new contradiction:

```
### CL-XXXX

- **Contradiction ID:** CL-XXXX
- **Related nodes:** [ContextNode id(s) involved, e.g. node-cross-agent-smoke-status]
- **Source refs:** [SourceRef id(s) for claim A and claim B]
- **Claim A:** [What the first source states, in plain language]
- **Claim B:** [What the second source states, in plain language]
- **Severity:** [low | medium | high]
- **Status:** [open | resolved]
- **Resolution decision:** [Blank until resolved. When resolved, state which claim is correct and why, or how both are reconciled.]
- **Reviewer:** [Name/handle of the human who reviewed this entry. Blank until reviewed.]
- **Date:** [YYYY-MM-DD — date the contradiction was logged]
```

**Field notes:**
- `Contradiction ID` uses a stable `CL-` prefix with a zero-padded sequence number (`CL-0001`, `CL-0002`, ...), assigned in the order entries are added — never reused.
- `Severity` guidance: `high` = a safety-relevant or user-facing factual conflict (e.g., a false "complete" claim about a safety-relevant task); `medium` = a project-state discrepancy with no safety impact; `low` = a minor wording/detail mismatch.
- `Status` starts as `open` and only a human reviewer may set it to `resolved` (per `[[SOURCE_INGEST_WORKFLOW]]` Step 9). No entry may be deleted once logged — a resolved entry remains in the ledger as history, consistent with the "immutable source, tracked history" pattern.
- `Resolution decision` must state the reasoning, not just the outcome, so a future reader understands why one claim won (or how both were reconciled) without re-deriving it.

---

## 3. Worked Example (Illustrative Only — Not a Live Entry)

The example below illustrates the template using MellyCore's own real, already-resolved history (`MELLYCORE-DOCS-ACCURACY-SYNC-001`, referenced in `shared_context/PROJECT_STATE.md`) as a worked reference. It is shown here for format clarity; a real ledger entry for this specific historical item may be logged verbatim by a future ingest pass if desired.

```
### CL-EXAMPLE (illustrative — not a numbered live entry)

- **Contradiction ID:** CL-EXAMPLE
- **Related nodes:** node-cross-agent-smoke-status, node-agent-handoff-doc
- **Source refs:** source-agent-handoff-md, source-project-state-md
- **Claim A:** shared_context/AGENT_HANDOFF.md implied cross-agent smoke testing was complete.
- **Claim B:** shared_context/PROJECT_STATE.md and shared_context/RUN_QUEUE.md show cross-agent smoke testing (MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001) as deferred/pending, not complete.
- **Severity:** high
- **Status:** resolved
- **Resolution decision:** Claim B was correct. MELLYCORE-DOCS-ACCURACY-SYNC-001 corrected the false completion claim in the handoff file and clarified that cross-agent smoke testing remains deferred, to be run from a clean main worktree per shared_context/BRANCH_INVENTORY_001.md.
- **Reviewer:** (operator, per project history)
- **Date:** (date of MELLYCORE-DOCS-ACCURACY-SYNC-001; see shared_context/RUN_QUEUE.md for commit reference)
```

---

## 4. Live Entries

_No live entries yet. Entries are added here by a future, separately run ingest pass (`[[SOURCE_INGEST_WORKFLOW]]`) or by manual logging of a newly discovered discrepancy, always following the template in Section 2._

---

## 5. Safety Notes

- Ledger entries must never contain secrets, credentials, `.env` values, or account identifiers in any field.
- Ledger entries must never propose or describe live/broker/trading UX as a "resolution" — if a contradiction somehow involves such content, the correct resolution is to exclude that content from the graph entirely (mark related nodes `hidden` per `[[CONTEXT_GRAPH_SCHEMA]]` Section 2.5), not to display it.
- This ledger is additive/append-mostly: existing entries are updated only to change `status`, `resolution_decision`, `reviewer`, or add a dated addendum — never deleted, preserving an honest history of what was disputed and how it was resolved.

---

*This contradiction ledger template is a docs-only artifact of `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`. It authorizes no automation — all entries are logged and resolved through human-reviewed process.*
