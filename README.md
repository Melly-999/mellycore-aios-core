# MellyCore AIOS

MellyCore AIOS is a standalone project scaffold for a modular AI operating workspace that coordinates strategy, documentation, agent handoffs, model routing, design direction, and future implementation work across ChatGPT, Claude, Codex, GLM/Z.ai, Grok/xAI, OmniRouter, Warp, Zed, VS Code, and GitHub.

MellyCore AIOS is separate from MellyTrade. Do not import MellyTrade runtime code, broker workflows, credentials, account identifiers, or trading execution surfaces into this repository.

Current status: scaffold/bootstrap. Runtime app code has not been created yet.

Shared project context lives in `shared_context/`. Every agent should start by reading:

1. `shared_context/PROJECT_STATE.md`
2. `shared_context/AGENT_HANDOFF.md`
3. `shared_context/RUN_QUEUE.md`
4. `shared_context/SAFETY_CONTRACT.md`
5. `shared_context/MODEL_ROUTING.md`
6. `shared_context/DESIGN_SYSTEM.md`

Safety notice: never commit secrets, provider tokens, real API keys, `.env` values, account IDs, local databases, or runtime state.

