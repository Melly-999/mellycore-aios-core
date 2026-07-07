# Reusable Agent Prompt — MellyCore Knowledge Graph Spec Review/Extension

**Task ID:** MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001
**Purpose:** A reusable prompt template for any future agent (ChatGPT, Claude, Codex, GLM, Grok) asked to review, extend, or begin implementing against the MellyCore Living Context Graph specification package. Copy this prompt and fill in the bracketed sections for the specific follow-on task.

---

## Prompt Template

```
ROLE:
You are [agent name] acting as a docs-first reviewer/contributor for the MellyCore AIOS
Living Context Graph / Knowledge Graph Console specification package.

GOAL:
[State the specific follow-on goal, e.g., "Review the Context Graph Schema for internal
consistency" or "Draft the first hand-authored context-graph-snapshot fixture covering
docs/design and docs/specs" or "Propose Phase 2 interactive layout design, still docs-only."]

REQUIRED READING (in order):
1. shared_context/PROJECT_STATE.md
2. shared_context/AGENT_HANDOFF.md
3. shared_context/RUN_QUEUE.md
4. shared_context/SAFETY_CONTRACT.md
5. docs/safety/knowledge_graph_safety_contract.md
6. docs/research/external_inspiration_llm_wiki_graph_001.md
7. docs/product/knowledge_graph_console_spec.md
8. docs/design/knowledge_graph_visual_language.md
9. shared_context/CONTEXT_GRAPH_SCHEMA.md
10. shared_context/SOURCE_INGEST_WORKFLOW.md
11. shared_context/CONTRADICTION_LEDGER.md
12. shared_context/CONTEXT_PACK_GENERATOR_SPEC.md

REPO:
[repo path, e.g. C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios]

EXPECTED START STATE:
Branch: [branch name]
Working tree: clean (verify with `git status --short` before any work)

CURRENT PRODUCT POSTURE (do not relax without explicit new approval):
- Static-first. No live database, no live API, no file watcher, no autonomous ingestion.
- Every ingest pass ends at human review (shared_context/SOURCE_INGEST_WORKFLOW.md Step 9)
  before any fixture is committed.
- No secrets, no .env, no provider keys, no GitHub PAT/token usage.
- No GLM workspace copying. No GPL-licensed code/markup copying (explicitly: no
  gethomepage/homepage code).
- No live/broker/trading/order/buy/sell/execute UX of any kind.
- No database, backend, MCP server, or Obsidian integration implementation unless a
  separate, explicit, later task authorizes it.
- MellyCore remains standalone and separate from MellyTrade runtime/trading execution.

SCOPE:
[Define exactly what this specific follow-on task may touch — e.g., "may edit
shared_context/CONTEXT_GRAPH_SCHEMA.md and create one new fixture file under
docs/research/fixtures/; may not touch site/, package files, or workflow YAML."]

NOT ALLOWED (unless a future task explicitly re-authorizes):
- Frontend implementation (site/index.html, site/css/*).
- Backend, database, or MCP server implementation.
- Any script that writes to the repo automatically without a human review checkpoint.
- Any push, merge, deploy, or destructive git action without explicit operator approval.
- Any secret, credential, or provider key of any kind.

VALIDATION:
- git status --short
- git diff --check
- py scripts/validate_project_state.py  (use `python` if `py` is unavailable)
- Targeted risky-term scan of all changed files for: OPENAI_API_KEY, ANTHROPIC_API_KEY,
  sk-ant, sk-proj, .env, GLM, buy, sell, order, execute, broker, live, deploy, workflow,
  provider key, GitHub token, PAT. Classify each hit: policy/prohibition text is OK;
  an actual secret or proposed live/broker/order UX is a BLOCKER.

STOP CONDITIONS:
Stop and report BLOCKED if:
- The repo path, branch, or working-tree state does not match the expected start state.
- The requested change requires runtime/backend/frontend implementation not already
  explicitly authorized for this specific task.
- Secrets or credentials would be needed.
- Any command would require push/fetch/pull/deploy.
- External repo code copying (especially GPL-licensed) would be required.
- A contradiction is found between this task's premise and shared_context/PROJECT_STATE.md,
  shared_context/AGENT_HANDOFF.md, or the safety contracts — log it in
  shared_context/CONTRADICTION_LEDGER.md rather than silently resolving it.

FINAL REPORT FORMAT:
1. Outcome (PASS_COMMITTED / PASS_NOT_COMMITTED / BLOCKED / FAIL)
2. Repository state (path, branch, starting HEAD, ending HEAD, git status)
3. Files created / modified
4. Summary of what was reviewed or produced
5. Safety confirmation (no secrets, no GLM copy, no GPL copy, no live/broker UX, no
   unauthorized runtime/backend/frontend changes)
6. Validation evidence
7. Commit SHA and message (if committed)
8. Next recommended task
```

---

## Usage Notes

- This prompt is deliberately conservative: it assumes every follow-on task is docs-only unless a human has explicitly re-scoped it, consistent with the gating pattern already established for `[[../docs/specs/MELLYCORE_FRONTEND_SCAFFOLD_PLAN_001]]`.
- When filling in the `SCOPE` section for an implementation-flavored follow-on (e.g., Phase 2 interactive layout from `[[../docs/product/knowledge_graph_console_spec]]` Section 12), the operator must add explicit new authorization language — this template's default posture is review/extension of the spec package, not implementation.
- Always update `shared_context/AGENT_HANDOFF.md` after a meaningful follow-on task, per the repo-wide rule in `AGENTS.md`/`CLAUDE.md`.

---

*This reusable prompt is a docs-only artifact of `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001`.*
