# Task Report: MELLYCORE-GITHUB-PAGES-OR-STATIC-PREVIEW-DECISION-001

**Task ID:** MELLYCORE-GITHUB-PAGES-OR-STATIC-PREVIEW-DECISION-001
**Purpose:** Decide how the published MellyCore AIOS static site should be previewed and, later if approved, published.
**Scope:** Decision report only. No GitHub Pages enablement, no workflow YAML, no site moves, no deploy.
**Status:** Complete

---

## 1. Outcome

**PASS_DECISION_COMMITTED_NO_PUSH** — the repository should keep the current `site/` source of truth and use local static preview plus screenshot evidence as the canonical path for now.

## 2. Current Repository / Static Site State

- Current repo path: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`
- Current branch: `publish/mellycore-main-001`
- Current HEAD: `7dca340ac46fba3c052be281fe55a87be65965f8`
- Canonical clean remote: `clean-origin https://github.com/Melly-999/mellycore-aios-core.git`
- Canonical clean remote main: `clean-origin/main = 7dca340ac46fba3c052be281fe55a87be65965f8`
- Static site source of truth: `site/index.html` and `site/css/`
- Current posture: static-first, safety-first, docs/spec foundation, no runtime/provider integrations, no secrets

## 3. GitHub Pages Constraint

GitHub Pages branch deployment only supports publishing from `/` or `/docs` on the selected branch. The current static site lives under `site/`, so branch-based GitHub Pages cannot publish the site as-is without either moving/copying the site, restructuring the repository root, or adding a GitHub Actions workflow. Those implementation paths are intentionally deferred.

## 4. Decision Options

- **A. Local preview only**: keep `site/` as source of truth and preview locally. This is the best immediate default.
- **B. GitHub Pages from `/docs`**: would require moving/copying deployable content into `/docs`, which would conflict with the current docs structure and needs a separate implementation task later.
- **C. GitHub Pages from repository root `/`**: would require root-level site restructuring and a separate implementation task later.
- **D. GitHub Pages with GitHub Actions**: can publish `site/`, but requires workflow YAML and explicit approval that is not granted in this task.
- **E. External static preview**: possible later via a provider such as Vercel, Netlify, or Cloudflare Pages, but not now.
- **F. Screenshot/evidence-only preview**: keep using QA screenshots and visual evidence as public-facing proof until a hosting decision is approved.

## 5. Recommended Decision

**Recommended now: A + F.**

Keep local static preview as the canonical preview path and continue using screenshot/QA evidence as the public-facing proof while the site remains static and unhosted. This preserves the current repository structure, avoids deployment or workflow changes, and keeps the site honest about its prototype status.

## 6. Why No Deploy Now

- The site already has a verified local static implementation and visual QA evidence.
- GitHub Pages branch publishing does not fit the current `site/` layout without repo restructuring.
- Adding GitHub Actions would introduce workflow YAML, which is explicitly out of scope here.
- The clean canonical repository is already published and verified; the remaining question is preview policy, not build correctness.

## 7. Future Implementation Tasks

- `MELLYCORE-GITHUB-PAGES-IMPLEMENTATION-001` if branch-based Pages is ever chosen later.
- `MELLYCORE-GITHUB-ACTIONS-PAGES-SETUP-001` if workflow-based deployment is approved later.
- `MELLYCORE-STATIC-PREVIEW-EVIDENCE-PACK-001` to package screenshots and local preview instructions for review or portfolio use.

## 8. Explicit Non-Actions

- No GitHub Pages enablement.
- No workflow YAML.
- No deploy.
- No site move or copy.
- No root-level restructuring.
- No push.
- No runtime/backend/provider integration.
- No secrets or `.env`.
- No live trading, broker, order, buy, sell, execute, or connect-live UX.

## 9. Validation Evidence

- `git diff --check` passed.
- `py scripts\validate_project_state.py` passed.
- Static preview constraint was confirmed from `site/index.html` and the existing QA report.
- GitHub Pages branch constraint was confirmed: `/` and `/docs` are the only branch-deploy paths that apply here.

---

*This decision report is docs-only. It records the static preview policy without changing hosting, workflow, or site structure.*
