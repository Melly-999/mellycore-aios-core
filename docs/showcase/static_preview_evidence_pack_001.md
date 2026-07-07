# MellyCore Static Preview Evidence Pack 001

Task ID: `MELLYCORE-STATIC-PREVIEW-EVIDENCE-PACK-001`
Status: Complete
Date: 2026-07-07

## Outcome

`PASS_STATIC_PREVIEW_EVIDENCE_PACK`

MellyCore AIOS remains a local static preview with screenshot/evidence-only publishing as the public proof layer. The current recommended preview path is still A + F:

- A: local static preview only.
- F: screenshot/evidence-only publishing.

This pack does not enable GitHub Pages, deploy hosting, workflow YAML, or any site move/copy.

## Current Preview Decision

- Local preview is canonical for now.
- Screenshot/evidence-only publishing is the public proof layer.
- No GitHub Pages is enabled.
- No deploy is configured.
- No workflow YAML is added.
- No site move or copy was performed.

The decision source is `docs/tasks/MELLYCORE-GITHUB-PAGES-OR-STATIC-PREVIEW-DECISION-001.md`.

## Static Site Source

The static homepage source of truth remains:

- `site/index.html`
- `site/css/tokens.css`
- `site/css/base.css`
- `site/css/components.css`
- `site/css/sections.css`

No static site source files were modified by this evidence-pack task.

## Existing QA Evidence

The local visual QA evidence folder was re-verified by filename during this run:

`C:\AI\MellyCore_Workspace\04_QA_Evidence\MELLYCORE-STATIC-VISUAL-QA-001\`

Confirmed local screenshot files:

- `qa-375-mobile-full.png`
- `qa-768-tablet-full.png`
- `qa-1024-small-desktop-full.png`
- `qa-1280-desktop-full.png`
- `qa-1920-wide-full.png`

Screenshot binaries remain outside the repository and were not copied or committed.

## Viewports Previously Verified

The existing visual QA report records passing checks for:

- `375x812`
- `768x1024`
- `1024x768`
- `1280x900`
- `1920x1080`

See `docs/tasks/MELLYCORE-STATIC-VISUAL-QA-001.md` for the full QA record.

## Safety Checks

The showcase remains constrained to a static documentation/prototype posture:

- Static HTML/CSS only.
- No JavaScript runtime requirement.
- No API calls.
- No provider keys.
- No `.env` values.
- No backend.
- No database.
- No deploy.
- No workflow YAML.
- No live trading, broker, order, buy, sell, or execute UX.

## Local Preview Instructions

Open `site/index.html` directly in a browser.

If a local static server is already available, serve the `site/` directory with that existing tool. No new dependencies are required for this task.

## Public README Wording

README status should stay explicit:

- The public source repository is available at the canonical clean remote.
- A live website URL is not enabled yet.
- The current preview path is local/static plus this evidence pack.
- Any deploy decision is a separate future task.

This evidence pack does not add fake live links or production claims.

## Non-Actions

- No GitHub Pages enablement.
- No deploy.
- No workflow YAML.
- No site move or copy.
- No backend/runtime/provider/API/database/MCP/Obsidian integration.
- No package, config, or env changes.
- No secrets or tokens.
- No live trading, broker, order, buy, sell, execute, or connect-live UX.
