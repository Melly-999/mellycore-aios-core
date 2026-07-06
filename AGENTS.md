# AGENTS.md

Codex and other coding agents must treat this file as the repo entrypoint.

Before work, read these files in order:

1. `shared_context/PROJECT_STATE.md`
2. `shared_context/AGENT_HANDOFF.md`
3. `shared_context/RUN_QUEUE.md`
4. `shared_context/SAFETY_CONTRACT.md`
5. `shared_context/MODEL_ROUTING.md`
6. `shared_context/DESIGN_SYSTEM.md`

Rules:

- MellyCore AIOS is separate from MellyTrade.
- Do not add secrets, real API keys, provider tokens, account IDs, `.env` values, local databases, or runtime state.
- Do not run destructive git commands such as reset, clean, rebase, force push, or branch deletion without explicit approval.
- Do not push, merge, deploy, or create remote resources without explicit approval.
- Keep work docs-first until a later run explicitly requests runtime app code.
- Update `shared_context/AGENT_HANDOFF.md` after every meaningful task.

Final reports must include outcome, repo path, branch, files changed, validation results, safety confirmation, and next recommended task.

