# MellyCore AIOS

Static-first AI command center and living context graph foundation for coordinating agents, context, specs, and safety gates.

## Status

- Static prototype
- Safety-first
- Docs/spec foundation
- No runtime/provider integrations
- No secrets
- Public source repository available at `clean-origin`
- Live website URL not enabled yet

## What is included

- Static HTML/CSS homepage under `site/`
- Design system docs
- Homepage spec docs
- Shared context files
- Knowledge Graph / Living Context Graph specs
- Validation script: `scripts/validate_project_state.py`

## What is intentionally not included

- No live AI provider integration
- No backend runtime
- No database
- No deploy pipeline
- No secrets
- No trading, broker, order, buy, sell, or execute UX

## Project structure

- `site/` - static homepage implementation
- `docs/` - design, spec, research, safety, and task documentation
- `shared_context/` - project state, handoff, roadmap, routing, validation, and safety context
- `agent_prompts/` - reusable prompts for future agent tasks
- `scripts/` - repo validation utilities

## Local preview

Open `site/index.html` in a browser for the simplest static preview.

If you prefer a local static server, serve the `site/` directory with any standard static file server. No additional dependencies are required. See `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md` for the exact verified command.

The current public preview policy is local/static plus evidence-pack publishing. See `docs/showcase/static_preview_evidence_pack_001.md` for the verified local screenshot filenames, viewport coverage, and explicit non-deploy status. Any future live website or deploy decision is separate and not enabled in this repository.

## Validation

Run:

```powershell
py scripts\validate_project_state.py
```

## Safety posture

MellyCore AIOS is a standalone repository and remains separate from MellyTrade. Do not add secrets, `.env` values, provider keys, runtime state, broker credentials, or trading execution surfaces here. Do not introduce live provider integrations, backend services, deploy pipelines, or workflow YAML unless a separate task explicitly authorizes them.

## Roadmap

- README showcase polish
- Static preview or GitHub Pages decision
- Knowledge Graph fixture draft
- Obsidian-like 3D graph page later
- Cloud compute readiness docs later

Shared project context lives in `shared_context/`. Every agent should start by reading:

1. `shared_context/PROJECT_STATE.md`
2. `shared_context/AGENT_HANDOFF.md`
3. `shared_context/RUN_QUEUE.md`
4. `shared_context/SAFETY_CONTRACT.md`
5. `shared_context/MODEL_ROUTING.md`
6. `shared_context/DESIGN_SYSTEM.md`

Safety notice: never commit secrets, provider tokens, real API keys, `.env` values, account IDs, local databases, or runtime state.
