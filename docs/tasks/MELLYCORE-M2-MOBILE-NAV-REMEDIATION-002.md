# MELLYCORE-M2-MOBILE-NAV-REMEDIATION-002

## RESULT

**PASS**

`M2-ACCEPT-02` is resolved by a range-safe CSS-only focus-containment rule for
the existing mobile horizontal header rail. This remediation does not accept the
Showcase, mark M2 complete, publish, merge, deploy, or activate any provider,
runtime, workspace backend, or external operation.

## OBSERVED

- Source baseline:
  `c3493c501158a10240d6ab7c099a763c3e7eb78d`
  (`docs: record M2 showcase rerun rejection`).
- Parent:
  `24312daa8f9c204faa42f9d5ca357834c1b10e81`.
- Source branch/worktree:
  `review/mellycore-m2-showcase-acceptance-002` at
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-m2-showcase-acceptance-002`.
- Task branch/worktree:
  `fix/mellycore-m2-mobile-nav-remediation-002` at
  `C:\AI\MellyCore_Workspace\02_Worktrees\mellycore-m2-mobile-nav-remediation-002`.
- The source worktree was verified clean and was not modified. The target
  branch and worktree path were absent before creation.
- The existing implementation was a compact horizontal mobile rail in
  `site/css/sections.css`, with `overflow-x: auto`, `padding-right: 32px`, and
  `scroll-padding-inline-end: 32px`.

## VERIFIED BEFORE EDITING

Fresh Chromium evidence reproduced the reported range behavior from a clean
page load using ordinary Tab traversal:

| Width | Focused scrollLeft | Max scroll | Final link bounds | Rail bounds | Focus visible |
| --- | ---: | ---: | --- | --- | --- |
| 360 | 125 | 125 | x=200.59..303.80 | x=24..336 | YES |
| 375 | 110 | 110 | x=215.59..318.80 | x=24..351 | YES |
| 390 | 0 | 95 | x=325.59..428.80 | x=24..366 | NO |
| 430 | 0 | 55 | x=325.59..428.80 | x=24..406 | NO |

At each width, document client width equaled document scroll width. The defect
was local focus-driven rail containment, not document overflow, missing scroll
range, or navigation semantics.

## ROOT CAUSE

Observed: Chromium's native focus scroll advanced the rail only where the final
anchor crossed its focus-scroll threshold. At 360 and 375 px it scrolled to the
available end range. At 390 and 430 px it treated the focused anchor border box
as sufficiently visible for the nearest-scroll calculation and left the rail at
`scrollLeft = 0`, even though the 2 px outline plus 2 px offset remained clipped
and manual end-scroll fully contained it.

Inferred: `scroll-padding-inline-end` alone defines an optimal viewing region
for scroll operations that consult scroll padding, but Chromium's keyboard focus
path did not consistently use that end padding or the focus outline geometry for
the partially visible anchor across the mobile range. Adding only
`scroll-margin-inline-end` did not change this behavior.

Actual CSS mechanism used: the rail now has proximity horizontal scroll snap,
anchors are snap areas with a 32 px inline-end snap margin matching the existing
end safety space, and the currently focused anchor snaps to the inline end.
This makes the browser's own focus-driven scroll choose the valid end-scroll
state without JavaScript or width-specific breakpoints.

## UPDATED

- `site/css/sections.css`: added `scroll-snap-type: x proximity` to the mobile
  `.command-bar nav` rule; added `scroll-margin-inline-end: 32px` and
  `scroll-snap-align: start` to mobile nav anchors; added a focused-anchor rule
  with `scroll-snap-align: end`.
- `shared_context/AGENT_HANDOFF.md`: updated because repository rules require a
  handoff after meaningful work.

## VERIFIED AFTER EDITING

Fresh Chromium evidence after the file edit:

| Width | Focused scrollLeft | Max scroll | Final link bounds | Rail bounds | Focus visible |
| --- | ---: | ---: | --- | --- | --- |
| 320 | 165 | 165 | x=160.59..263.80 | x=24..296 | YES |
| 360 | 125 | 125 | x=200.59..303.80 | x=24..336 | YES |
| 375 | 110 | 110 | x=215.59..318.80 | x=24..351 | YES |
| 390 | 95 | 95 | x=230.59..333.80 | x=24..366 | YES |
| 430 | 55 | 55 | x=270.59..373.80 | x=24..406 | YES |

Additional range-safety trials using temporary CSS before the file edit showed
the same mechanism passing at 340, 380, 400, 412, and 420 px.

Keyboard:

- Tab order: Skip to content, Command Center, Product evidence, Safety, Static
  dashboard.
- Shift+Tab from `Static dashboard` returns to Safety.
- Tabbing onward from `Static dashboard` reaches the hero CTA
  `Explore Command Center`.
- No focus trap or hidden focused element was observed.

Responsive checks:

- 720 CSS px reflow approximation: no document overflow, zero scripts, H1
  unchanged, sections contained.
- 768, 1024, 1440 px: no document overflow, zero scripts, H1 unchanged,
  sections contained.
- Reduced-motion emulation matched the media query, produced zero active
  animations, and kept root scrolling automatic.

Technical and product checks:

- H1 remains:
  `One command center. Every AI plane under operator control.`
- Exactly ten workspace records remain, in waves 4 / 3 / 3.
- Workspace names remain:
  Coding / Runtime Studio; Deep Research; Compare Arena; Multi-Agent Crew;
  Email AI; Video Intelligence; Voice; Image Studio; Model Downloader; Ollama
  Manager.
- Duplicate IDs: 0.
- Fragment links: all resolve.
- Authored local links: all returned HTTP 200 when served from repository root.
- Scripts: 0.
- Buttons/forms/inputs: 0.
- Page-owned requests: local HTML and CSS only.
- Known favicon 404 remains inherited and non-blocking.

## NOT CHANGED

- `shared_context/PROJECT_STATE.md`
- `shared_context/ROADMAP.md`
- `shared_context/TASK_INDEX.md`
- `shared_context/RUN_QUEUE.md`
- Product copy, Product Vision, accepted surfaces, runtime/provider/agent/MCP
  implementation, deployment, dependencies, assets, fonts, credentials, and
  public release state.
- Tablet Shared Context orphan, unused `.card-grid--4`, favicon 404, skip-link
  DOM focus transfer, mobile page length, MVP demo terminology, graph/runtime
  polish, and general visual polish.

## VALIDATION

- Browser reproduction before editing:
  `360 PASS`, `375 PASS`, `390 FAIL`, `430 FAIL`.
- Temporary CSS trials:
  `scroll-margin-inline-end` alone failed at 390/400/412/420/430; trailing
  content-space relocation failed at 390/400/412/420/430; larger scroll padding
  failed at 420/430; focus-end scroll snap with a 32 px end margin passed the
  tested mobile interval.
- Browser validation after editing:
  `320 PASS`, `360 PASS`, `375 PASS`, `390 PASS`, `430 PASS`, plus 720, 768,
  1024, and 1440 px regression checks.
- `py -3.9 scripts/validate_project_state.py`: PASS.
- `git diff --check`: PASS.
- `git diff --cached --check`: PASS.

## REMAINING

- M2 remains incomplete.
- Showcase Acceptance remains not accepted until a fresh independent acceptance
  rerun passes.
- No push, merge, deployment, provider/runtime activation, workspace backend
  activation, or public release occurred.

Recommended next task:

`MELLYCORE-M2-SHOWCASE-ACCEPTANCE-003`
