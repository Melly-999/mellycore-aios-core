---
name: docs-portfolio-asset-sync
description: Capture authoritative production screenshots and sync portfolio evidence to a docs branch.
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [documentation, screenshots, portfolio, production, assets]
    related_skills: [github-pr-workflow, github-repo-management]
---

# Portfolio Asset Sync Skill

Capture authoritative screenshots from a live production deployment and
synchronize portfolio evidence to a repository docs branch.

## When to Use

- A public production deployment has passed QA and needs authoritative screenshots captured
- Portfolio, showcase, or case-study assets need to be refreshed from live evidence
- A previous task marked `PORTFOLIO_RELEASE_READY: YES` and the next task needs input packs
- Screenshots are needed for Useme, Upwork, LinkedIn, or GitHub case studies

Do NOT use when:
- Redesigning the frontend (scope violation)
- Publishing directly to external platforms in this task
- The production URL is unavailable or returns non-acceptance content

## Prerequisites

- `playwright` Python package installed and functional
- Chrome or Chromium available (headless)
- `sha256sum` or equivalent for hash computation
- Public production URL verified (HTTP 200)
- Canonical repository established (see Procedure)

## Quick Reference

| Step | Command |
|------|---------|
| Identify canonical remote | `git remote -v` — look for the primary push/fetch remote |
| Verify production SHA | `git ls-tree canonical/main` or `git rev-parse canonical/main` |
| List existing assets | `find docs -name "*.png" -o -name "*.jpg"` |
| Capture viewport | playwright `page.goto()` + `page.screenshot()` at each viewport |
| Compute hash | `sha256sum file.png` |
| Verify PNG | `file file.png` |

## Procedure

### Step 1 — Preflight: Establish Canonical Remote

Before any mutation, identify the authoritative remote:

```bash
cd /path/to/repo
git remote -v
```

If multiple remotes exist, identify the canonical one (the primary
`Melly-999/mellycore-aios-core` style canonical repo, not a personal fork).
Record the canonical remote name (e.g. `clean-origin`) and its main branch
SHA. Verify the production commit is reachable from canonical main:

```bash
git rev-parse canonical/main
git fetch canonical
git log canonical/main --oneline -3
```

### Step 2 — Preflight: Verify Production URL

```bash
curl -sI "https://production-url.vercel.app/dashboard.html" | head -5
```

Confirm HTTP 200 and expected page title before proceeding.

### Step 3 — Preflight: Inventory Existing Assets

```bash
find docs/screenshots docs/design docs/showcase -type f \( -name "*.png" -o -name "*.jpg" \) 2>/dev/null
file docs/screenshots/*.png
stat --printf="%n %s %Y\n" docs/screenshots/*.png
```

Classify each asset:
- **CURRENT_PRODUCTION** — authoritative deployed evidence
- **PREVIOUS_PRODUCTION** — prior deployment, historical
- **DESIGN_REFERENCE** — mockup or design artifact
- **DEVELOPMENT_EVIDENCE** — acceptance/test evidence
- **OBSOLETE** — no longer current
- **UNKNOWN** — requires review

Report which images must NOT be used as current portfolio evidence.

### Step 4 — Create Docs Branch

```bash
git fetch canonical
git checkout canonical/main
git checkout -b docs/mellycore-portfolio-assets-repo-sync-001
```

Use a task-id-style branch name matching the task label.

### Step 5 — Capture Screenshots

Use playwright with a script like:

```python
from playwright.sync_api import sync_playwright
import os, hashlib

VIEWPORTS = [
    ("1920x1080", 1920, 1080),
    ("1600x900", 1600, 900),
    ("1440x900", 1440, 900),
    ("390x844", 390, 844),
]

PROD_URL = "https://production-url.vercel.app"
DASHBOARD = f"{PROD_URL}/dashboard.html"
OUT_DIR = "docs/screenshots/mellycore-portfolio-assets"

def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    for name, w, h in VIEWPORTS:
        ctx = browser.new_context(viewport={"width": w, "height": h})
        page = ctx.new_page()
        page.goto(DASHBOARD, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(2000)
        title = page.title()
        # Verify correct page loaded
        assert "cockpit" in title.lower() or "command" in title.lower(), f"Wrong page: {title}"
        path = f"{OUT_DIR}/mellycore-cockpit-v3-production-{name}.png"
        page.screenshot(path=path, full_page=False)
        print(f"{name}: {page.viewport_size} -> {os.path.getsize(path)} bytes, SHA={sha256(path)}")
        ctx.close()
    browser.close()
```

For every required viewport: set viewport, fresh page load, verify content,
capture. Do NOT resize one already-rendered page.

### Step 6 — Validate Screenshots

```bash
file docs/screenshots/mellycore-portfolio-assets/*.png
sha256sum docs/screenshots/mellycore-portfolio-assets/*.png
```

Verify:
- All PNGs valid format
- Dimensions match requested viewports
- SHA-256 computed and recorded
- Page title verified during capture
- No loading artifacts (check `file` output shows proper PNG)

### Step 7 — Create Asset Manifest

Create `docs/screenshots/mellycore-portfolio-assets/PORTFOLIO_ASSET_MANIFEST.md` with:
- Capture date, production URL, production SHA, deployment ID
- Table: filename | viewport | dimensions | size | SHA-256 | status
- Per-screenshot detail blocks
- Verified portfolio facts (from repository evidence only)
- Truthfulness limitations (what NOT to claim)

Also create `docs/screenshots/ASSET_INVENTORY_001.md` with full classification.

### Step 8 — Create Next-Task Input Pack

Create `docs/tasks/<TASK-NAME>-INPUT-PACK.md` with:
- Production source details (URL, SHA, deployment)
- Authoritative screenshot paths + hashes
- Project identity (title, URL, repo)
- Factual technical summary (no marketing)
- Verified technology list (from repo evidence only)
- Truthfulness limitations
- Explicit "do not publish externally" instruction

### Step 9 — Commit

```bash
git add docs/screenshots/mellycore-portfolio-assets/
git add docs/screenshots/ASSET_INVENTORY_001.md
git add docs/tasks/<TASK-NAME>-INPUT-PACK.md
git commit -m "docs: sync MellyCore production portfolio assets"
```

Do NOT push, merge, or deploy.

### Step 10 — Final Validation

```bash
# No forbidden files changed
git diff --stat canonical/main -- site/dashboard.html site/css/ site/js/

# git clean
git diff --check

# Production still accessible
curl -sI "https://production-url.vercel.app/dashboard.html" | grep "HTTP"

# Secret scan
grep -rE "(api_key|token|secret|password)" docs/screenshots/mellycore-portfolio-assets/ || echo "clean"
```

## Pitfalls

1. **Browser remote debugging not configured.** If Chrome requires manual
   `--remote-debugging-port` setup, use playwright's headless launch directly.
   Do not block on CDP setup — playwright's built-in browser management works.

2. **Multi-remote repos.** Some repos have `origin` + `clean-origin` or similar
   dual remotes. Always identify the canonical remote before branching or
   computing SHA reachability.

3. **Worktree path on Windows.** Git worktrees created with Windows-style
   absolute paths can confuse the repo's git operations when run from inside
   the worktree. Prefer a plain branch (detached HEAD → new branch) over
   worktrees on Windows hosts.

4. **Graph geometry is deterministic on page load.** The Knowledge & Operations
   Graph computes presentation on page load. Resizing the browser after load
   does not recompute layout. Always do a fresh page load per viewport.

5. **Vision analysis credits.** If vision API credits are exhausted, validate
   screenshots through technical signals (file format, dimensions, SHA-256,
   page title) rather than abandoning the capture.

6. **Existing asset confusion.** Repos often have `Dashboard tapeta.png`,
   `live dashboard.png`, or `RAG .png` from prior work. Classify these as
   OBSOLETE and explicitly report they must NOT be presented as current evidence.

7. **Forbidden files.** Never change `site/dashboard.html`, `site/css/`,
   `site/js/`, runtime, providers, backend, `.env`, or deployment configs
   during an asset sync task.

## Verification

- [ ] All screenshots captured at required viewports
- [ ] All PNGs valid (verified with `file`)
- [ ] All dimensions exact
- [ ] SHA-256 computed for every file
- [ ] Manifest references all real files
- [ ] git diff --check passes
- [ ] No forbidden files changed
- [ ] Production URL still returns HTTP 200
- [ ] Commit created locally (not pushed)
- [ ] Next-task input pack created
