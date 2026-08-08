# Cross-Agent Context

Canonical cross-agent bootstrap and navigation packet for MellyCore AIOS.
Established by `MELLYCORE-CROSS-AGENT-CONTEXT-PACK-002`. This file **replaces
and supersedes** the prior minimal version of this same document — no
sibling or competing "context pack" file exists; this is the one canonical
artifact.

**Last refreshed:** `MELLYCORE-CROSS-AGENT-CONTEXT-PACK-002`, baseline HEAD
`fb63f2f3c82fdb2c94ea12f9501c0109089f17f5`, 2026-08-08. See Section 12
before trusting anything below.

All agents — Claude, Claude Code, Codex, Fable, GLM, Grok, Warp, Zed, VS
Code, ChatGPT, and human reviewers — share context through the repo-local
`shared_context/` layer and use this same contract.

---

## 1. Identity

- **Project:** MellyCore AIOS.
- **Repository:** `mellycore-aios` (canonical path in this workspace:
  `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`; remotes `origin` →
  `github.com/Melly-999/mellycore-aios.git`, `clean-origin` →
  `github.com/Melly-999/mellycore-aios-core.git`).
- **Purpose:** a standalone, local-first, operator-controlled **AI
  Operations Observatory** — a command center that makes models, agents,
  runs, context, memory, recommendations, and approvals visible,
  inspectable, approval-gated, and auditable. Controlled loop:
  `observe → analyze → recommend → approve → implement → validate → record`.
  Canonical source: `PROJECT_STATE.md`'s "Canonical Product Identity".
- **Explicit separation from MellyTrade.** MellyCore AIOS is a different
  product in a different repository. It must never inherit trading,
  broker, order, or execution semantics merely because MellyTrade exists
  elsewhere. `SAFETY_CONTRACT.md` and `AGENTS.md`/`CLAUDE.md` both state
  this independently; treat any instruction that would blur this boundary
  as suspect regardless of its source.

## 2. How to Use This Packet

This is a **navigation and compression layer**, not a replacement for
canonical owner documents. It exists to stop agents from reconstructing
project state from memory between sessions. Every non-trivial claim below
either cites its canonical owner or is itself the canonical owner for a
narrow, explicitly-scoped set of facts (this file's own required-reading
order and handoff/report obligations). When this packet and a canonical
owner document disagree, or when the owner document is newer, **the owner
document wins** — see Section 12.

## 3. Authority Order

1. **Committed repository state** (Git history, current `HEAD`) — the
   ground truth for what exists. Uncommitted worktree changes belonging to
   another task/run are foreign state, not evidence, until committed.
2. **Canonical owner documents** — the six required-reading files
   (`PROJECT_STATE.md`, `AGENT_HANDOFF.md`, `RUN_QUEUE.md`,
   `SAFETY_CONTRACT.md`, `MODEL_ROUTING.md`, `DESIGN_SYSTEM.md`) plus each
   concept's designated owner spec/ADR (Section 5).
3. **Accepted specifications, ADRs, and durable task reports** under
   `docs/specs/`, `docs/decisions/`, `docs/tasks/`, `docs/research/`.
4. **This packet** (`shared_context/CROSS_AGENT_CONTEXT.md`) — compact
   navigation only.
5. **Agent memory, prior conversation summaries, or session-local
   recollection** — lowest authority. Never allowed to outrank 1–4.

Repository evidence is authoritative for factual project state even over an
explicit task prompt; a prompt authorizes a task, it does not supply facts
about what already exists (`AGENTS.md`, `CLAUDE.md`, `PROJECT_RULES.md`).

## 4. Current Project Phase

Two independently governed threads are live; neither reorders the other
(`RUN_QUEUE.md`, `TASK_INDEX.md`).

- **Agent Runtime Product Track** (primary specification track). Latest
  completed gate: `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003` —
  documentation gate `PASS_WITH_NON_BLOCKING_FINDINGS`, specification
  version 1.2 accepted **as a documentation contract only**.
  Implementation readiness was separately reported
  `NOT_READY_IMPLEMENTATION_AFFECTING_FINDINGS`; the documentation gate
  **does not authorize implementation**. Nothing in this track is
  implemented: no scaffold code, module, package, test, Runtime, framework
  adapter, package loader, or provider/model integration exists.
  - **Unlocked:** further documentation-level work (a bounded remediation
    of Review 003's five new findings is `PLANNED` in `TASK_INDEX.md`, no
    task ID minted yet, requires explicit Operator authorization).
  - **Not unlocked:** Agent Runtime Scaffold implementation itself
    (`BLOCKED` — a plain-name item with no task ID minted by any gate so
    far; requires its blocking finding resolved, separate explicit
    Operator authorization, and its own exact file allowlist) and
    everything downstream of it — Scaffold Implementation Review, First
    Agent Package, Cross-Agent Smoke (inert modes only —
    `MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001`, still `deferred`, **do not
    confuse with this packet or with this packet's own task,
    `MELLYCORE-CROSS-AGENT-CONTEXT-PACK-002`**), and Integration Review.
- **OpenAI Batch governance/publication reconciliation** — `RUN_QUEUE.md`'s
  own "Current" heading. This thread moves faster than this packet; treat
  `RUN_QUEUE.md` as authoritative for its exact live status, not this
  summary. The independently governed global pointer
  `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains
  `IN_PROGRESS` and is not reordered by the Agent Runtime track. Live Batch
  execution (Stage C) remains unauthorized; migration trigger #5 (first
  live provider connection) remains uncrossed.

## 5. Canonical Source Map

| Topic | Canonical file(s) | Notes |
| --- | --- | --- |
| Project state (durable, fast-moving) | `shared_context/PROJECT_STATE.md` | Largest, most current single source; sections are append-ordered by task. |
| Run queue / active gate | `shared_context/RUN_QUEUE.md` | Its own "Current" heading is authoritative for what's active right now. |
| Handoff log | `shared_context/AGENT_HANDOFF.md` | Newest entry first ("Latest Update"). Must be updated after every meaningful task. |
| Safety | `shared_context/SAFETY_CONTRACT.md` | Hard constraints; production-deployment enforcement state; Batch API activation controls. |
| Model routing (roles) | `shared_context/MODEL_ROUTING.md` | Who does what; not a runtime router. |
| Design system | `shared_context/DESIGN_SYSTEM.md` | Source Arena visual metaphor, Observatory surfaces, color/interaction rules. |
| Task identifiers / status | `shared_context/TASK_INDEX.md` | Canonical status vocabulary (Section 13); does not itself authorize anything. |
| Roadmap narrative | `shared_context/ROADMAP.md` | Full narrative detail; do not read indiscriminately — prefer `PROJECT_STATE.md`/`TASK_INDEX.md` first. |
| Decisions log | `shared_context/DECISIONS.md` | Operator decisions recorded verbatim (e.g. Model A deployment contract). |
| Contradiction ledger | `shared_context/CONTRADICTION_LEDGER.md` | Template + process for tracking source disagreements; check before asserting a disputed fact. |
| Branch inventory | `shared_context/BRANCH_INVENTORY_001.md` | Historical branch-classification report; not a live index. |
| Validation | `shared_context/VALIDATION.md` | Baseline validator commands (`scripts/validate_project_state.py`). |
| Tooling / provider setup | `shared_context/TOOLING.md`, `shared_context/PROVIDER_SETUP.md` | No real keys anywhere in this repo. |
| Agent Runtime architecture | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`, `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` | §37 of the Architecture spec is the sole owner of the inert v1 boundary; the Scaffold spec consumes it, never duplicates it. |
| Agent Runtime scaffold | `docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md` | **Foreign dirty state as of this packet's baseline — see Section 12.** Version 1.2 at last committed read. |
| Agent Package contract | `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` | v1.1, documentation contract only. |
| Framework bridge | `docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` | v1.0, documentation contract only; no adapter/SDK exists. |
| Shared Context Bridge | `docs/specs/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001.md` | v1.0, documentation contract only; no bridge/storage/memory-service exists. |
| Provider registry extension | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | Specification exists; exact gate/acceptance status not reproduced here — read the file and its `docs/tasks/`/`docs/research/` chain directly. |
| Integration gateway security | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | Same caveat as above. |
| Context admission | `docs/specs/MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001.md`, `MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001.md`, `MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md` | Context Gate I1–I4 is the one **implemented** admission mechanism (Section 6). |
| Context Pack **Generator** (different concept) | `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md` | **Not this document.** That spec defines a future, unimplemented, bounded read-only tool for turning external repo content into an ingestible context pack for the Context Gate. This file is the cross-agent bootstrap/navigation packet. Do not conflate the two. |
| Deployment state | `shared_context/PROJECT_STATE.md` ("Vercel Static Showcase", "Production Deployment Authorization — Model A Contract") | Model A is temporary and static-phase-only; nine migration triggers force reconsideration. |
| Safety posture, deep detail | `shared_context/SAFETY_CONTRACT.md` | See Section 7 for the compressed version. |

## 6. Accepted Architecture

Status vocabulary below is the repository's own — not invented here (see
Section 13). Only concepts with strong, directly-read evidence are
classified; everything else is left to its own canonical source rather than
asserted from memory.

| Concept | Status | Evidence |
| --- | --- | --- |
| Context Gate (admission) I1–I4 | **IMPLEMENTED** | `PROJECT_STATE.md` "Durable Implemented State": guarded admission, 7 validated canonical records, content-free index, computed audit, read-only dashboard Context surface. |
| Agent Runtime Architecture | **SPECIFIED, not implemented** | Accepted with non-blocking findings across two reviews; §37 owns the inert v1 boundary. |
| Agent Runtime Scaffold | **SPECIFIED, not implemented, v1.2** | `PASS_WITH_NON_BLOCKING_FINDINGS` (doc gate) + `NOT_READY_IMPLEMENTATION_AFFECTING_FINDINGS` (implementation readiness). No code exists. |
| Agent Package Contract | **SPECIFIED, not implemented, v1.1** | `PASS_WITH_NON_BLOCKING_FINDINGS`. |
| Framework Bridge Contract | **SPECIFIED, not implemented, v1.0** | `PASS_WITH_NON_BLOCKING_FINDINGS`; no adapter/SDK exists. |
| Shared Context Bridge Contract | **SPECIFIED, not implemented, v1.0** | `PASS_WITH_NON_BLOCKING_FINDINGS`; no bridge/storage/memory-service exists. |
| AI Operations Intelligence | **SPECIFIED, not implemented** | Integrated into canonical `main` via PR #7; modules remain `SPECIFIED`. |
| Operations Data Contract | **SPECIFIED (schema/fixture only)** | Integrated into canonical `main` via PR #13; documentation/schema/fixture scope only, no adapter or runtime consumption. |
| Source Arena renderer (CSS/DOM) | **IMPLEMENTED (static slice)** | Merged into canonical `main` via PR #17; WebGL/Three.js path remains unmerged (paused PR #28, blocked Gate B). |
| OpenRouter Model Observatory | **IMPLEMENTED (static snapshot only)** | Merged into canonical `main` via PR #21; `NO_API_KEYS`, `NO_BACKEND`, `NO_MODEL_CALLS`, `NO_DEPLOY` beyond the static fixture. |
| Cockpit / UI (Design System) | **ACCEPTED (specification), partially implemented** | Static homepage + Live Cockpit V2 prototype implemented; Mission Control, Agent Activity, Context Pulse, Model Router, Unified Run Ledger, Approval Queue, Memory & Recommendation Ledger, AI Estate Inventory, Skill Gap Detector, Memory Freshness Monitor are **planned surfaces**, not built. |
| Production deployment model (Model A) | **ACCEPTED (temporary, static-phase-only)** | Operator decision 2026-07-27; per-merge authorization only, no technical enforcement gate; nine migration triggers force Model B reconsideration. |
| Provider Registry extension, Integration Gateway Security, Cybersecurity/Marketing provider packs | **SPECIFIED — status not independently re-verified here** | Read the file and its own review chain directly rather than trusting this row. |
| Control Plane, Model Router (as a runtime surface) | **PLANNED / NOT_IMPLEMENTED** | Named across specs and the Design System as a future Observatory surface; no runtime router exists. |

## 7. Current Safety Posture

Compressed from `shared_context/SAFETY_CONTRACT.md`, `AGENTS.md`,
`CLAUDE.md` — read those for full detail, this list does not replace them:

- No secrets, real API keys, provider tokens, `.env` values, or account
  identifiers anywhere in the repository.
- No wholesale import of the GLM/Z.ai workspace; no `.git` import from
  reference workspaces; no database files or local runtime state committed.
- No destructive Git (`reset --hard`, `clean`, force push, branch deletion)
  without explicit approval.
- No deploy, push, merge, or PR without explicit, per-action Operator
  approval — never blanket or inferred. Under the temporary Model A
  contract, one merge approval authorizes only the automatic Production
  publication that specific merge causes.
- No workflow YAML changes unless explicitly approved.
- MellyCore AIOS is separate from MellyTrade: no broker/trading execution,
  no order/buy/sell/execute/connect-live UX, ever.
- Validator results must be reported honestly. An unavailable validator is
  reported `NOT RUN / UNAVAILABLE` — **never** silently converted to a pass.
  (`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-002`'s own report
  notes validator success is not treated as evidence of correctness on its
  own; findings were independently re-derived, not accepted from claims.)
- Live provider connections remain hard-blocked
  (`LIVE_PROVIDER_CONNECTION_BLOCKED_BY_MIGRATION_TRIGGER_5`, exit code
  `78`) until a separate, explicit authorization crosses that trigger.

## 8. Agent Preflight Contract

Before any mutation, every agent must:

1. Confirm repository identity (this is MellyCore AIOS, not MellyTrade —
   check README.md self-description and `docs/tasks/` naming, not remote
   URL alone).
2. Inspect current branch, current `HEAD`, and current worktree status.
3. Identify any pre-existing dirty/uncommitted state and treat it as
   foreign unless it is this agent's own uncommitted work from earlier in
   the same task.
4. Read the six required files, in order:
   `PROJECT_STATE.md` → `AGENT_HANDOFF.md` → `RUN_QUEUE.md` →
   `SAFETY_CONTRACT.md` → `MODEL_ROUTING.md` → `DESIGN_SYSTEM.md`
   (`AGENTS.md`, `CLAUDE.md`, `PROJECT_RULES.md`).
5. Read the current task's own task record if one exists under
   `docs/tasks/`.
6. Determine the exact authorized file scope before writing anything.
7. Stop on any ownership or baseline conflict rather than resolving it
   unilaterally (see Section 9).

## 9. Mutation Contract

- Keep scope narrow; touch only explicitly authorized files.
- Preserve foreign dirty/uncommitted state exactly as found — do not edit,
  stage, stash, reset, or discard it, and never infer that its uncommitted
  content is canonical.
- No opportunistic refactors or unrelated cleanup riding on a task's commit.
- Never silently reconcile two canonical documents that disagree — log the
  disagreement (`CONTRADICTION_LEDGER.md`) or stop and report it.
- Never promote `PLANNED`/`SPECIFIED` state to `IMPLEMENTED`/`COMPLETE`
  without durable evidence a human or independent reviewer can reproduce.
- An LLM's own decision is never its own authorization. Explicit Operator
  approval is required for anything in the "explicit permission" tier
  (push, deploy, PR, merge, destructive Git, secrets, account changes).
- Stage explicit file paths only — never `git add -A` / `git add .`.

## 10. Validation Contract

- Run only the validators that actually exist and apply
  (`python scripts/validate_project_state.py`, `git diff --check`,
  `git status --short` — see `VALIDATION.md`).
- Report exact commands and their exact output/exit codes, not paraphrases.
- An unavailable or not-run validator is reported as such, never as a pass.
- Inspect diff scope explicitly; confirm no file outside the authorized
  scope changed; scan new/changed content for secrets, API keys, `.env`
  values, or provider credentials before considering a task done.
- Verify final Git state (branch, `HEAD`, staged files) matches what the
  final report claims.

## 11. Handoff Contract

After meaningful work, every agent must update
`shared_context/AGENT_HANDOFF.md` (prepend a new "Latest Update" entry —
newest first) and produce a final report that states, at minimum:

- Task ID and outcome.
- Baseline `HEAD` and final `HEAD` (if changed).
- Branch.
- Files changed (explicit list).
- Validation results (commands run and their real output).
- Safety confirmation (what was and was not touched: secrets, `.env`,
  provider integration, deploy, push, PR, merge, destructive Git, foreign
  dirty state).
- Next canonical task — **only if repository evidence establishes one**;
  otherwise state plainly that none is established. Do not begin it.

## 12. Freshness / Drift Rule

If this packet conflicts with a newer committed canonical owner document,
accepted task record, or repository state, **the newer canonical source
wins**. This packet is refreshed periodically, not continuously — treat
every fact above as potentially stale the moment a new task lands in
`AGENT_HANDOFF.md`, `PROJECT_STATE.md`, `RUN_QUEUE.md`, or `TASK_INDEX.md`.
Refresh this file rather than silently preserving stale context; do not
patch around a known drift without updating the source claim.

At the time this section was last written, the working tree carried one
piece of **foreign, uncommitted state** belonging to a different task:
`docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md` had local,
uncommitted edits not authored by, owned by, or evaluated as part of
establishing this packet. This packet's description of the Scaffold spec
(Sections 4–6) reflects the **last committed** version only. Do not treat
that fact as still true once the file is committed or the diff resolved —
re-read the file's committed state directly.

## 13. Status Vocabularies by Layer

MellyCore uses multiple status vocabularies for different layers. Do not
combine them into one enum.

### Task-level status

`TASK_INDEX.md` formally defines exactly these task-level statuses:

- **`COMPLETE`** — task finished; it may still be local and unpushed, so
  check the linked evidence.
- **`IN_PROGRESS`** — started, not complete.
- **`ELIGIBLE`** — a gate has cleared the task for Operator authorization;
  it has not been authorized or started.
- **`BLOCKED`** — not eligible; a prior gate, review, resolution, or
  Operator authorization is outstanding.
- **`PLANNED`** — named in the roadmap; no gate has run yet.

### Other project and architecture state terms

Other canonical owner documents use terms such as **`SPECIFIED`**,
**`IMPLEMENTED`**, **`ACCEPTED`**, and **`DEFERRED`** for architecture,
product, decision, queue, or narrative state. These terms are not
automatically members of `TASK_INDEX.md`'s task-status enum. Interpret each
term from the canonical owner document that uses it; in particular, never
read `SPECIFIED` or decision-level `ACCEPTED` as `IMPLEMENTED`.

This packet must never read like a roadmap or marketing summary of what
MellyCore AIOS will eventually do. Every claim in Sections 4 and 6 is
scoped to what repository evidence supports **right now**.

## 14. Current Next Action

Not established by this packet's own task. Two separately governed
next-actions exist in the repository, neither authorized or begun here:

- Agent Runtime track: a bounded remediation of
  `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003`'s five new findings is
  `PLANNED` in `TASK_INDEX.md`; **no task ID is minted**; requires explicit
  Operator authorization.
- Governance/publication track: `RUN_QUEUE.md`'s "Current" heading names
  its own exact next task; treat that heading as authoritative, not this
  line, since it changes faster than this packet.

Do not treat either of the above as authorized by this packet. This packet
authorizes nothing beyond its own creation.

---

*This file is the sole canonical cross-agent context packet for MellyCore
AIOS. It was created/expanded by `MELLYCORE-CROSS-AGENT-CONTEXT-PACK-002`;
see `docs/tasks/MELLYCORE-CROSS-AGENT-CONTEXT-PACK-002.md` for that task's
full baseline, scope, and validation record.*
