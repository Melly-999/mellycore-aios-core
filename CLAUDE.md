# CLAUDE.md

MellyCore AIOS is a standalone project and is separate from MellyTrade.

Claude Code must read the shared context before work:

- `shared_context/PROJECT_STATE.md`
- `shared_context/AGENT_HANDOFF.md`
- `shared_context/RUN_QUEUE.md`
- `shared_context/SAFETY_CONTRACT.md`
- `shared_context/MODEL_ROUTING.md`
- `shared_context/DESIGN_SYSTEM.md`

Use a docs-first workflow until a later run explicitly authorizes runtime app code. Do not mutate MellyTrade repositories unless the user explicitly requests that in a separate task. Do not add secrets, real API keys, provider tokens, `.env` values, local databases, or runtime state.

Do not push, merge, deploy, reset, rebase, clean, force push, or delete branches without explicit approval.

Update `shared_context/AGENT_HANDOFF.md` after meaningful work.

