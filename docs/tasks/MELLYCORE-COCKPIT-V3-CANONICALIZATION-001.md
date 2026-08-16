# MELLYCORE-COCKPIT-V3-CANONICALIZATION-001

**Type:** Docs / spec / canonical-state reconciliation
**Status:** `COMPLETE` — `PASS_WITH_LIMITATIONS`
**Scope:** documentation and canonical state only. No `site/**`, runtime,
provider, integration, workflow, or deployment change.
**Baseline:** `clean-origin/main` @ `034962f3aab8ebdade6e84e054b2b2ef863db645`
**Branch:** `docs/mellycore-cockpit-v3-canonicalization-001`

---

## 1. Purpose

`MELLYCORE-COCKPIT-V3-IMPLEMENTATION-001` preflight returned
`BLOCKED_BY_CANONICAL_DOCS_SPEC_GATE`. This task reconciles the Operator's
accepted **MellyCore Cockpit V3.1** direction with canonical state and
establishes the smallest truthful remaining gate to frontend implementation.

## 2. Prior design-task evidence

Searched: all local refs, all `clean-origin` refs, all 60+ registered
worktrees, `docs/tasks/` across every ref, and full commit history
(`git log --all --grep`, per-ref `git cat-file -e`, per-ref `TASK_INDEX`
status grep).

| Task | Classification | Evidence |
|---|---|---|
| `MELLYCORE-CLAUDE-DESIGN-HANDOFF-REVIEW-001` | **D. NOT_EXECUTED** | No `docs/tasks/` record on any ref. No commit references it. Not `COMPLETE` in any ref's `TASK_INDEX.md`. |
| `MELLYCORE-HERO-DIRECTION-DECISION-001` | **D. NOT_EXECUTED** | Same searches; no record, no commit, no completion on any ref. |
| `MELLYCORE-DESIGN-SYSTEM-CINEMATIC-AMENDMENT-001` | **D. NOT_EXECUTED** | Same searches; no record, no commit, no completion on any ref. |
| `MELLYCORE-DOCS-INTEGRATION-REVIEW-001` | **D. NOT_EXECUTED** | Only incidental mention in `97ecbe2` ("docs: close renderer remediation chain") as a then-next-task pointer, later superseded. No task record, no review output. |

No durably completed design work was found to reuse. Nothing was marked
`COMPLETE` on the strength of conversation text or untracked files.

## 3. P1 finding — canonical description of the design handoff is factually wrong

**Finding ID:** `CV3-CANON-001`
**Severity:** P1 (canonical truth drift)
**Status:** corrected by this task

Canonical `TASK_INDEX.md` described `MELLYCORE-CLAUDE-DESIGN-HANDOFF-REVIEW-001`
as reviewing:

> the externally generated Claude Design System handoff (tokens, components,
> site/cockpit UI kits, `SKILL.md`) currently observed as untracked/foreign
> state (`.agents/`, `.claude/skills/`, `skills-lock.json`) on
> `design/mellycore-claude-design-sync-001`

A fresh read-only snapshot of those exact paths was taken on
`design/mellycore-claude-design-sync-001` @ `55bb5e9`. The actual contents are:

- `.agents/skills/` — eight **third-party Higgsfield AI** skill packages:
  `higgsfield-brandkit`, `-generate`, `-marketplace-cards`,
  `-product-photoshoot`, `-soul-id`, `-video-explainer`, `-websites`,
  `-youtube-thumbnail`. These are marketing/media-generation tooling (logo
  generation, product photoshoots, YouTube thumbnails).
- `.claude/skills/` — contains **only symlinks** to those same eight
  Higgsfield packages. No independent content.
- `skills-lock.json` — a lockfile pinning those eight skills from GitHub
  `higgsfield-ai/skills`.

A content search for MellyCore design material across `.agents/` returned a
single incidental match: `higgsfield-websites/references/design-taste-frontend.md`,
a generic third-party frontend reference.

**There are no MellyCore design tokens, components, UI kits, or cockpit
`SKILL.md` in those paths.** The canonical row's subject matter does not exist
as described. The same worktree also carries
`.claude/settings.local.json.backup-before-higgsfield-remove`, indicating this
third-party tooling was being removed rather than adopted.

**Consequence:** `MELLYCORE-CLAUDE-DESIGN-HANDOFF-REVIEW-001` could not be
executed as written, because its stated review target is unrelated third-party
agent tooling. The row is corrected rather than marked complete.

## 4. Design-input review actually performed

The genuine V3.1 design input lives **outside the repository**, on the
Operator's Desktop. A read-only inspection of
`MellyCore Cockpit V3.1 (standalone).html` (594,037 bytes, 406 lines, bundled,
`<title>Bundled Page</title>`) was performed.

### 4.1 Truthfulness audit of the artifact — PASS

| Term | Occurrences | Assessment |
|---|---|---|
| `STATIC PREVIEW` | 2 | correct disclosure |
| `SUPERVISED` | 2 | correct disclosure |
| `NO LIVE PROVIDERS` | 1 | correct disclosure |
| `EXECUTION` | 5 | locked-execution semantics |
| `LIVE` | 8 | **all eight are negations** — `NO LIVE PROVIDERS`, `TOPOLOGY DERIVED FROM REPOSITORY · NOT LIVE RUNTIME`, `FROZEN · NOT LIVE` |
| `tokens/min`, `cost/hour`, `ACTIVE REQUESTS`, `Error Rate`, `Healthy`, `Operational`, `Running` | **0 each** | no fake telemetry present |

V3.1 is truthfulness-clean. The fake telemetry that appears in the earlier
"Reference A" cockpit target image (uptime %, active requests, tokens/min,
error rate, cost/hour, per-agent running percentages) is **absent from V3.1**.
Adopting V3.1 strengthens rather than strains the safety posture.

### 4.2 Palette extracted from the artifact

Consistent with the cockpit-scoped colour rule now recorded in
`shared_context/DESIGN_SYSTEM.md`:

- near-black canvas: `#05070c`, `#06090f`, `#080b12`, `#0b0f17`
- cyan/blue (core, routing, architecture): `#38bdf8`, `#7dd3fc`, `#22d3ee`, `#2dd4bf`
- violet (governance, identity): `#a78bfa`, `#c084fc`
- amber (context, attention): `#f59e0b`, `#fbbf24`
- green/lime (verified capability): `#a3e635`, `#4ade9c`, `#34d399`, `#10b981`
- slate text ramp: `#64748b` → `#94a3b8` → `#cbd5e1` → `#e2e8f0` → `#eef2f8`

No red appears in the artifact's thirty most-frequent colours, consistent with
"red = critical only".

### 4.3 Surfaces confirmed present in the artifact

Context Management, Model Routing, Operations Graph, AI Agents / Loop Registry,
Architecture Snapshot, Attention Queue, AI Operations Workflow, MellyCore Core,
and compact navigation (Dashboard, Operations, Agents, Models, Tools, Context,
Policies, Audit). "Source Arena" does not appear — consistent with the cockpit
being a distinct surface from the hero.

### 4.4 Component-level disposition

| Element | Disposition |
|---|---|
| Semantic subsystem colours | **ADOPT** (cockpit-scoped) |
| Cockpit density: 8–12px gaps, 12–16px padding, small radii, 1px borders | **ADOPT** |
| Near-black technical canvas | **ADOPT** |
| Central graph dominance, MellyCore Core emphasis | **ADOPT** |
| Static-preview / execution-locked / no-live-providers semantics | **ADOPT** |
| `FROZEN · NOT LIVE`, `TOPOLOGY DERIVED FROM REPOSITORY` disclosures | **ADOPT** |
| Seven-stage workflow with constrained Execution stage | **ADOPT** |
| Compact technical navigation | **ADAPT** — destinations named, secondary pages not authorized |
| Typography direction | **ADAPT** — readability and layout fidelity over font imitation; no remote font dependency |
| Graph interactions | **ADAPT** — hover/focus/select/filter/fit only; no physics, no live simulation |
| Bundled HTML, bundler runtime, generated component architecture | **REJECT** — must not enter `site/` |
| Higgsfield third-party skill packages | **REJECT** — unrelated to MellyCore design; not adopted |
| Full M3 surface set beyond the cockpit | **DEFER** — separate specs required |

## 5. Decisions recorded

1. **V3.1 = ADOPT** as the primary Command Center visual direction, on Operator
   direction, scoped to `site/dashboard.html`.
2. **Source Arena retained**, scoped to the homepage/hero surface. No
   either/or decision was forced; the two occupy different product roles.
3. **New canonical spec owner created:**
   `docs/specs/MELLYCORE_COMMAND_CENTER_COCKPIT_SPEC_001.md`. Verified that no
   existing spec owned `site/dashboard.html`; the homepage spec explicitly
   disclaims being a runtime console, and `MELLYCORE_UI_SECTIONS.md` scopes
   `command-center-preview` to a preview "without attempting the full M3 shell".
4. **Knowledge graph semantics reused, not duplicated** — deferred to
   `docs/product/knowledge_graph_console_spec.md`.
5. **Design System delta is minimal and surface-scoped.** No global rule was
   deleted; the homepage lead-image constraint was scoped to its own surface.

## 6. Limitations

1. **The V3.1 design artifacts are not under version control.** They exist only
   on the Operator's Desktop (`MellyCore Cockpit V3.1 (standalone).html`,
   `MellyCore AIOS Cockpit Redesign.zip`, `MellyCore AIOS Design System-handoff.zip`).
   This task mitigates the durability risk by making
   `MELLYCORE_COMMAND_CENTER_COCKPIT_SPEC_001.md` the canonical source of truth,
   so implementation depends on the specification rather than on an
   unversioned file. Whether to archive the binaries into the repository is an
   Operator decision and was not performed here.
2. `MellyCore Cockpit (standalone) (1).html` on the Desktop has a byte count
   identical to the V3.1 file (594,037). Which is authoritative was not
   determined; the file explicitly named V3.1 was used.
3. The two Desktop `.zip` archives were not opened.
4. `MELLYCORE-DOCS-INTEGRATION-REVIEW-001` remains `NOT_EXECUTED`. Its scope
   (docs/spec coherence across the Cinematic AIOS lock, the design handoff
   outcome, and the reconciled homepage spec) is **not** a prerequisite for
   cockpit implementation and is not treated as one.
5. No WCAG conformance is claimed.

## 7. Safety confirmation

No secrets, `.env` values, API keys, or provider tokens were read, printed, or
committed. No `site/**`, runtime, provider, agent, integration, workflow,
deployment, or MellyTrade change. No push, merge, deploy, or destructive Git
operation. Execution remains locked; no provider is connected.
