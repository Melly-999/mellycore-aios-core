# Model Routing

OmniRouter / OmniRoute is the preferred provider gateway when available. Provider API keys stay outside the repo.

Routing roles:

- ChatGPT: strategy, context synthesis, prompt generation, planning, memory.
- Claude / Claude Code: architecture, reasoning, documentation, review.
- Codex: implementation, validation, PR preparation.
- GLM 5.2 / Z.ai: cheap/dynamic worker for drafting, iteration, exploration, and secondary implementation ideas.
- Grok / xAI: critique, second opinion, adversarial review, risk review.
- OmniRouter / OmniRoute: local gateway and provider/model routing layer.
- Warp: command workflows, safe operator prompts, repeatable local runbooks.
- Zed: editor-agent workspace and local coding ergonomics.
- VS Code: editor workspace, settings examples, extension-compatible docs.
- GitHub: remote source control, issues, PRs, project history, review evidence.

Provider API keys remain local-only and must not be committed.

