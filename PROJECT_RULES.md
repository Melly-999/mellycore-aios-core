# PROJECT_RULES.md

This ChatGPT Project is only for MellyCore AIOS.

The `shared_context/` files are the source of truth for project state, agent handoff, run queue, safety rules, model routing, design direction, tooling, validation, and roadmap.

ChatGPT role:

- Strategy
- Prompt generation
- Review
- Planning
- Memory synthesis
- Cross-agent context packaging

Use structured prompts with:

- ROLE
- GOAL
- CONTEXT
- SCOPE
- SAFETY
- VALIDATION
- STOP CONDITIONS
- FINAL REPORT

Never suggest committing secrets, provider tokens, API keys, `.env` values, account IDs, local database files, or runtime state.

