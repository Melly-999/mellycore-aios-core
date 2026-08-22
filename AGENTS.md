# AGENTS.md

Codex and other coding agents must treat this file as the repo entrypoint.
This file is the canonical, shared multi-agent policy owner for MellyCore
AIOS — every tool-specific wrapper (for example `CLAUDE.md`) holds only its
own deltas and defers to this file for shared rules, the same
canonical-owner pattern `agent_prompts/loops/README.md` already proves for
loop skills.

## Authority hierarchy

1. An explicit operator instruction in the current turn — scoped to that
   instruction only, never a standing exception.
2. `shared_context/SAFETY_CONTRACT.md` — the non-negotiable safety floor.
3. Live canonical state: `shared_context/PROJECT_STATE.md`,
   `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md`.
4. This file.
5. A tool-specific wrapper (for example `CLAUDE.md`) — deltas only, never a
   restatement or contradiction of this file.
6. The current task prompt — may narrow scope, never loosen safety.
7. External reference reports and third-party guidance — persuasive input
   only; a useful external pattern is never MellyCore canonical truth on
   its own.

## Preflight

Before work, read these files in order:

1. `shared_context/PROJECT_STATE.md`
2. `shared_context/AGENT_HANDOFF.md`
3. `shared_context/RUN_QUEUE.md`
4. `shared_context/SAFETY_CONTRACT.md`
5. `shared_context/MODEL_ROUTING.md`
6. `shared_context/DESIGN_SYSTEM.md`

Then confirm branch, HEAD, and `git status` before any mutation, and leave
any unrelated dirty state untouched. See `.claude/commands/plan-task.md`
for the full procedure.

## Edit discipline

- Read a file before editing it.
- Make the minimum change the task requires; do not refactor, reformat, or
  otherwise touch code or prose you were not asked to change.
- Every changed line should trace to the current task.

## Rules

- MellyCore AIOS is separate from MellyTrade. Do not mutate MellyTrade
  repositories unless the user explicitly requests that in a separate task.
- Do not add secrets, real API keys, provider tokens, account IDs, `.env`
  values, local databases, or runtime state. If a suspected secret turns up
  while investigating, report only its file, line, and category — never
  its value.
- Do not run destructive git commands such as reset, clean, rebase, force
  push, or branch deletion without explicit approval.
- Do not push, merge, deploy, or create remote resources without explicit
  approval.
- Keep work docs-first until a later run explicitly requests runtime app
  code.
- Update `shared_context/AGENT_HANDOFF.md` after every meaningful task. A
  separate, single-purpose commit for that update is acceptable, and often
  preferable to folding it into the deliverable commit.
- **Production deployment rule — Model A selected (Operator decision,
  2026-07-27, temporary, static-phase-only):** merging into canonical `main`
  causes the Vercel Git integration to create a public Production deployment
  automatically, with no technical enforcement (`main` has no branch
  protection, the repository has no rulesets, the Production environment
  has no protection rules). The Operator has selected Model A — see
  `shared_context/PROJECT_STATE.md`'s "Production Deployment Authorization —
  Model A Contract" for the full contract. Every individual PR merge still
  requires its own separate, explicit Operator approval — **never** a
  blanket, standing, batch, inferred, or future authorization — and every
  merge-authorization request an agent prepares must explicitly warn that
  merging into `main` immediately updates the public Production host. No
  agent may merge on its own initiative under any circumstance. Nine
  canonical, blocking migration triggers (first backend, authentication,
  stored user data, runtime secret, live provider connection,
  execution-capable agent, external write-capable integration,
  financial/trading action, or delegated merge authority/multiple
  maintainers) require Model B reconsideration before any affected
  implementation or merge proceeds — agents must treat these as blocking,
  not optional. This rule does not itself authorize any current merge or
  deployment.

## Validation honesty

Report only validators actually run, with their actual output. "Not run",
"unavailable", "failed", and "passed" are four different outcomes — do not
round one up to another. `planned != implemented`, `implemented != tested`,
`tested != verified`, `configured != exercised`: say which one applies. If
a claim cannot be traced to a file, line, or command output you observed
yourself, do not make the claim.

## Review principles

An independent review does not inherit the result of the work it reviews,
and the reviewer must not be that work's own author. The default verdict is
REJECT until evidence you personally observed supports every claim under
review. A review reports findings; it does not fix them unless separately
asked to, as a distinct later step. See `.claude/commands/review.md`.

## Stop conditions

Stop and report, rather than proceed, when required files are missing or
conflict in a way this file does not resolve, when a task would need a
safety exception this file does not already grant, or when a suspected real
secret or credential appears. Concluding that an exception is *necessary*
does not make it permitted — that conclusion is itself the escalation.

Final reports must include outcome, repo path, branch, files changed, validation results, safety confirmation, and next recommended task.
