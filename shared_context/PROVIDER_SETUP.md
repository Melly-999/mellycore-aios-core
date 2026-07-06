# Provider Setup

Use placeholders only. Put real values in local secret stores or ignored local `.env` files, never in git.

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
ZAI_API_KEY=
XAI_API_KEY=
OPENROUTER_API_KEY=
OMNIROUTER_BASE_URL=
OMNIROUTER_API_KEY=
```

Provider notes:

- OpenAI: ChatGPT strategy and Codex implementation workflows.
- Anthropic: Claude architecture, reasoning, docs, and review.
- Z.ai / GLM 5.2: low-cost dynamic worker and design/reference iteration.
- xAI / Grok: critique and second opinion.
- OpenRouter: optional external model routing layer.
- OmniRouter local gateway: preferred local provider hub when available.

