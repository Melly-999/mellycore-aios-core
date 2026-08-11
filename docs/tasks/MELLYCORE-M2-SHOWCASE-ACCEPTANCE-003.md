# MELLYCORE-M2-SHOWCASE-ACCEPTANCE-003

## 1. RESULT

`ACCEPTED_WITH_NON_BLOCKING_LIMITATIONS`

This is an independent rendered acceptance rerun. No `site/**` repair was
made by this task.

## 2. CANDIDATE BASELINE

- Candidate commit: `8264d29712396fa71101aedb578f5d5a13f33d8d`
- Subject: `fix: make M2 mobile nav focus range-safe`
- Parent: `c3493c501158a10240d6ab7c099a763c3e7eb78d`
- Review branch/worktree: `review/mellycore-m2-showcase-acceptance-003` at
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-m2-showcase-acceptance-003`
- Initial status: clean; the expected remediation worktree was also clean.
- Existing worktrees modified: `NO`.

## 3. ACCEPTANCE CONTRACT

Canonical sources were `shared_context/PROJECT_STATE.md`, `ROADMAP.md`,
`TASK_INDEX.md`, `RUN_QUEUE.md`, `DESIGN_SYSTEM.md`, and `SAFETY_CONTRACT.md`,
plus `docs/specs/MELLYCORE_HOMEPAGE_SPEC_001.md` and the two prior acceptance
and remediation records. Criteria were the existing M2 static-showcase
contract only: truthful two-layer product model, ten-workspace 4 / 3 / 3
inventory, commercial responsive composition, keyboard-visible focus,
reduced-motion, local/static posture, and no false-live implication. No M3,
runtime, provider, integration, workspace backend, 3D, telemetry, Obsidian,
or deployment requirement was added.

## 4. M2-ACCEPT-01

375: `RESOLVED: YES`.

From a fresh load the fifth Tab reached `Static dashboard`, advanced the rail
from `scrollLeft=0` to `125` of `125`, and contained the target
`x=200.59..303.80` plus its 2 px outline and 2 px offset inside the rail
`x=24..336`. Document and body client/scroll widths were each `360` CSS px
(the emulated 375 px browser viewport reserves a visible scrollbar).

## 5. M2-ACCEPT-02

390: `RESOLVED: YES`. Fresh ordinary fifth-Tab focus advanced the rail from
`0` to its `110` px maximum; the target was `x=215.59..318.80` inside the
`x=24..351` rail with the complete focus treatment contained.

430: `RESOLVED: YES`. The same fresh traversal advanced from `0` to its `70`
px maximum; the target was `x=255.59..358.80` inside the `x=24..391` rail
with the complete focus treatment contained.

## 6. MOBILE NAVIGATION MATRIX

All five primary widths used a fresh load with no manual rail scrolling. Tab
order was `Skip to content` → `Command Center` → `Product evidence` →
`Safety` → `Static dashboard`; the subsequent Tab reached `Explore Command
Center`, and Shift+Tab returned to `Static dashboard`.

| Device width | Rail x bounds | client / scroll width | initial / focused / max scrollLeft | final-link x bounds | Focus containment |
| --- | --- | --- | --- | --- | --- |
| 320 | 24..281 | 257 / 437 | 0 / 180 / 180 | 145.59..248.80 | YES |
| 360 | 24..321 | 297 / 437 | 0 / 125 / 140 | 200.59..303.80 | YES |
| 375 | 24..336 | 312 / 437 | 0 / 125 / 125 | 200.59..303.80 | YES |
| 390 | 24..351 | 327 / 437 | 0 / 110 / 110 | 215.59..318.80 | YES |
| 430 | 24..391 | 367 / 437 | 0 / 70 / 70 | 255.59..358.80 | YES |

At 380, 400, 412, and 420 px, ordinary focus likewise contained the final
link: respectively `120/120`, `100/100`, `88/88`, and `80/80` focused/max
scroll positions. Local horizontal mouse-wheel scrolling at 390 remained
possible (`scrollLeft=110` of `110`), focus snapped to the intended final
item, and 768 px desktop navigation had no scroll range. No sticky, wrong-item,
or Shift+Tab regression was observed.

## 7. RESPONSIVE ACCEPTANCE

Fresh full-page rendered inspection at 1440, 1024, 768, 720, 430, 390, 375,
360, and 320 found the Hero, Source Arena, Command Center, Calibration,
Routing Invariants, Runtime Constellation, Workspaces, Shared Context, Graph,
Roadmap, Safety, Tooling, Operator Channel, and footer present, contained,
and readable. The 720 CSS-pixel check is the established 200% reflow
approximation, not OS/browser zoom certification. The cinematic 1440
composition remains commercially credible; mobile preserves a coherent,
readable single-column story and usable CTA.

At every checked width document client width equalled document scroll width:
1425/1425, 1009/1009, 753/753, 705/705, 415/415, 375/375, 360/360, 345/345,
and 305/305 respectively. Intentional local nav scrolling is the only
horizontal overflow.

## 8. KEYBOARD / ACCESSIBILITY

- Tab: `PASS`; primary widths follow the required order and continue into hero
  content.
- Shift+Tab: `PASS`; returns naturally, with no trap.
- Visible focus: `PASS`; final-link 2 px outline plus 2 px offset is fully
  visible at every primary width.
- Skip link: visible and targets `#main-content`; its existing DOM
  focus-transfer limitation remains recorded below.
- Reduced motion: `PASS`; `prefers-reduced-motion: reduce` matched, no active
  animations were reported, non-zero transitions were `0.00001s`, root scroll
  was `auto`, and navigation remained usable.
- Reflow approximation: `PASS` at 720 CSS px.
- Text alternatives: reasonable, including the graph textual alternative.
- WCAG certification claimed: `NO`.

## 9. PRODUCT MODEL

- Top-level layers: `2` — Command Center and AI Workspaces.
- Workspace count: `10`.
- Wave structure: `4 / 3 / 3`.
- 11th workspace: `NONE`; Local AI Hub remains a presentation grouping only.

## 10. HERO / SOURCE ARENA / COMMAND CENTER

The accepted H1 remains `One command center. Every AI plane under operator
control.` The Hero is clear, commercially composed, mobile-readable, and
explicitly static. Source Arena labels its representative/simulated origin,
operator approval, provenance, fail-closed safety, and no-live provider/runtime
state. System Calibration and Routing Invariants remain static/source-backed,
show provider `Not connected`, execution `No live activity`, and state that
the flow is not routing or telemetry.

## 11. KNOWLEDGE & OPERATIONS GRAPH

The graph remains a derived representative fixture with visible committed-source
references, provenance labels, no-live-ingestion safeguards, and an
understandable textual mobile fallback. It expressly disclaims ownership of
canonical truth and live ingestion.

## 12. RUNTIME CONSTELLATION

The Constellation remains a reference/planned projection. Its displayed
framework names do not imply installed, connected, running, or authorized
state; the point-of-use statement retains all of those distinctions. Mobile
fallback remains understandable and introduces no runtime activity claim.

## 13. AI WORKSPACES

All ten named workspaces render in the required waves. Email distinguishes
READ/DRAFT from `SEND / approval required`; Voice disclaims authority and a
microphone; Video disclaims media/inference; Image Studio disclaims generation;
Model Downloader disclaims downloads; Ollama Manager disclaims installed local
models/hardware; Coding / Runtime Studio disclaims editor, terminal, and
execution control. The presentation is commercially clear without representing
active applications.

## 14. SHARED CONTEXT / ROADMAP / SAFETY / TOOLING

Shared Context is a static metadata projection, not live monitoring or a
completeness claim. The Roadmap remains manually updated and its current,
planned, and approval-gated labels are not contradictory. Safety and Tooling
remain reference-only, approval-bound, and non-executing.

## 15. OPERATOR CHANNEL

The local documentation and dashboard links are authored local targets and
exist. The channel correctly states that no inquiry/onboarding endpoint is
configured and that links do not cause communication or execution. No fake
contact functionality was found.

## 16. PRODUCT / DESIGN DRIFT

- Product Drift introduced: `NO`.
- Design Drift introduced: `NO`.

Candidate source changes are the existing mobile rail's scroll-snap and
focus-snap declarations only, plus remediation/handoff documentation. Product
model, workspace inventory, semantic colors, component species, copy, and
signature surfaces are unchanged from the rejection parent.

## 17. VISUAL REGRESSION

Hero, Graph, Runtime, Workspaces, governance surfaces, and the responsive
composition show no material regression. The 390 px focused mobile rail was
visually inspected after ordinary keyboard focus and shows the complete target
and outline. The 1440 hero/Source Arena remains strong and contained.

## 18. TECHNICAL VALIDATION

- Console: no application exception or log error in the rendered local-file
  pass. The inherited favicon 404 was not recreated under file protocol and
  remains non-blocking/unmodified by the candidate.
- Network: no scripts, external dependencies, or external URLs in the page
  surface; local-file rendering produced no resource requests. A first
  loopback-server attempt failed from a local harness memory error before a
  page rendered and is not used as acceptance evidence.
- Scripts: `0`; external dependencies: `none` observed.
- Duplicate IDs: `0`; all six fragment anchors resolved.
- Authored local links: all five unique repository targets exist.
- Document overflow: none at every required width.

## 19. NON-BLOCKING DEBT

| Item | State |
| --- | --- |
| Tablet Shared Context orphan | UNCHANGED |
| Unused `.card-grid--4` | UNCHANGED |
| Favicon | UNCHANGED |
| Skip link DOM focus transfer | UNCHANGED |
| Mobile depth | UNCHANGED |
| `MVP demo — Planned` terminology | UNCHANGED |

The candidate implementation delta is confined to mobile nav CSS, so none of
these inherited items is worsened.

## 20. FORMAL SHOWCASE VERDICT

`SHOWCASE_ACCEPTED_WITH_NON_BLOCKING_LIMITATIONS`

## 21. SHOWCASE READY

`YES`

## 22. M2 STATUS

`COMPLETE` for this local candidate lineage. `RUN_QUEUE.md` assigned formal
Showcase Acceptance authority to decide whether M2 may be marked complete, and
`TASK_INDEX.md` permits `COMPLETE` when durable evidence exists. This record
is that evidence. Completion does not claim a push, merge, production state,
provider/runtime activation, or public release.

## 23. GOVERNANCE FILES CHANGED

- `docs/tasks/MELLYCORE-M2-SHOWCASE-ACCEPTANCE-003.md` — durable independent
  decision and evidence.
- `shared_context/AGENT_HANDOFF.md` — required post-task handoff.
- `shared_context/PROJECT_STATE.md`, `TASK_INDEX.md`, and `RUN_QUEUE.md` —
  narrowly advance the accepted local M2/showcase state under their existing
  owner rules.
- `site/**`: `UNCHANGED`.

## 24. VALIDATION PERFORMED

- Candidate object/subject/parent, expected branch/worktree, clean candidate,
  review path/branch absence, and all worktrees were independently verified.
- Chromium headless rendered fresh local-file loads at 1440, 1024, 768, 720,
  430, 390, 375, 360, and 320; primary keyboard trials at 320, 360, 375, 390,
  and 430 plus 380, 400, 412, and 420 range checks; reduced-motion at 390.
- Source/DOM checks verified 0 scripts, 0 duplicate IDs, six resolving
  fragments, five local targets, no external dependency surface, exact H1,
  ten workspaces, and 4 / 3 / 3 waves.
- `py -3.9 scripts/validate_project_state.py`: `PASS` before governance
  mutation.

## 25. COMMIT

One local governance commit is required after final scope, consistency, and
validator checks. It is not pushed, merged, or deployed.

## 26. FINAL STATE

- Review branch: `review/mellycore-m2-showcase-acceptance-003`.
- Push: `NO`.
- Merge: `NO`.
- Deploy: `NO`.

## 27. NEXT CANONICAL TASK

Recommend `MELLYCORE-M2-PUBLIC-SHOWCASE-RELEASE-001` as a separately
authorized public-release task. It is not executed or authorized by this
acceptance record.
