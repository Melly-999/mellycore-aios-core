# MellyCore AIOS — M2 Homepage UI Sections Brief

**Canonical behavior owner:** docs/specs/MELLYCORE_HOMEPAGE_SPEC_001.md
**Reconciled by:** MELLYCORE-CINEMATIC-HOMEPAGE-SPEC-RECONCILIATION-001
**Version:** 2.0
**Status:** Implementation brief; no frontend implementation claimed
**Target:** Existing static HTML/CSS/JavaScript under site/

---

## 1. Ownership and implementation posture

This brief projects the canonical Homepage Specification into bounded static
sections. If wording here conflicts with that specification, the Homepage
Specification wins.

M2 evolves the current site. It does not authorize a framework rewrite,
generated JSX architecture, provider/runtime integration, a backend, or a
deployment.

Every section follows four rules:

1. critical content is semantic HTML and visible without JavaScript;
2. fixture, snapshot, simulated, and planned content is labeled at point of use;
3. status uses text plus semantic color;
4. motion is optional and never establishes meaning or visibility.

## 2. M2 section registry

### hero-command-center

| Field | Requirement |
|---|---|
| Priority | P0 — first viewport |
| Purpose | Establish local-first AIOS identity, concise commercial value, honest preview state, and the first navigation choice. |
| Required content | Kicker, H1, one-line proposition, short support copy, StaticPreviewNotice, up to three factual badges, primary and secondary anchors. |
| Existing foundation | Current hero markup, CTA group, safety badges, static notice, responsive grid, and decorative stage may be evolved. |
| Allowed variation | Source-led, orbital Command Center-led, hybrid, or instrument stage, provided the canonical hierarchy and disclosure remain intact. |
| Blocked | Gateway-centered thesis, vendor list as identity, mandatory animated reveal, fake-live signals, credential or execution CTA. |
| Mobile | Copy-first single column; decorative stage simplified or removed; full-width touch targets. |
| Validation | First-view comprehension, no-JS visibility, focus order, static disclosure before action, no horizontal overflow. |

### command-center-preview

| Field | Requirement |
|---|---|
| Priority | P0 |
| Purpose | Preview the product manifestation of context, routing, runtime, observability, approvals, and evidence without attempting the full M3 shell. |
| Required content | Legible context/routing area, central product visualization, agents/runtime/approval area, compact evidence rail, point-of-use status and provenance. |
| Existing foundation | Current static panels, constellation/router cards, context metadata, and reusable glass/HUD primitives may be consolidated rather than duplicated. |
| Blocked | Complete M3 dashboard, operational toggles, live health, provider selection, execution controls, dense gaming HUD. |
| Mobile | Ordered proof cards; reduced HUD density; center visualization becomes a readable summary. |
| Validation | Projection ownership explicit; no panel implies canonical ownership or active operation. |

### knowledge-operations-graph

| Field | Requirement |
|---|---|
| Priority | P0 |
| Purpose | Show a derived, provenance-bearing view across knowledge, system, and operations domains. |
| Required content | Text summary, representative clusters/relationships, source strip, relationship legend, DataOrigin, ownership disclaimer. |
| Existing foundation | Evolve the current living-context-graph markup and CSS; preserve fixture honesty and text fallback. |
| Anchor strategy | The existing living-context-graph anchor may remain as a compatibility alias until a coordinated implementation changes navigation. |
| Blocked | Live topology claim, database or ingestion assumption, invented production relationships, graph-only meaning. |
| Mobile | Replace the dense canvas with a simplified path, cluster summary, or ordered evidence list. |
| Validation | Fixture/example labeling, readable alternative, keyboard-independent comprehension, no false canonical-owner claim. |

### runtime-constellation

| Field | Requirement |
|---|---|
| Priority | P1 |
| Purpose | Explain the vendor-neutral runtime/framework ecosystem as a product projection. |
| Required content | Small relationship view, textual state labels, StaticPreviewNotice where needed, explicit displayed-does-not-mean-installed copy. |
| Existing foundation | Current constellation and router visual primitives may be reframed; their old central-gateway story must not survive. |
| Blocked | Online dots, animated traffic, support/install/connect/run claims without evidence, provider names as primary product identity. |
| Mobile | Ordered relationship list or compact diagram with equivalent text. |
| Validation | Every state is textual; no name implies installed, supported, connected, running, or authorized. |

### ai-workspaces

| Field | Requirement |
|---|---|
| Priority | P0 |
| Purpose | Present the exact canonical ecosystem as a hierarchy with commercially legible outcomes. |
| Required content | The ten-row canonical enumeration from Homepage Specification §9, planned/static-demo labels, Wave 1 feature cluster, Wave 2 compact rail, Wave 3/local-AI grouping. |
| Blocked | Eleventh workspace, equal-card wall, invented status enum, backend/activation implication, horizontal rail without keyboard access. |
| Mobile | Prioritized single-column groups with all entries readable and no accidental overflow. |
| Validation | Mechanical exact-count check; every entry visibly planned or static/demo; no Command Center surface misclassified as a workspace. |

### governance-evidence

| Field | Requirement |
|---|---|
| Priority | P0 |
| Purpose | Turn local-first, operator control, provenance, approval, and fail-closed behavior into concise trust proof. |
| Required content | Controlled improvement loop or equivalent, evidence/provenance statement, approval boundary, vendor-neutral statement, honest current-state links. |
| Existing foundation | Reuse safety checklist, status chips, source/evidence strip, and safety badge primitives selectively. |
| Blocked | Unverified “safe,” “secure,” “live,” or “connected” claims; complete policy wall; decorative green success. |
| Mobile | Proof precedes action; concise stacked statements; status text never truncated. |
| Validation | Every badge and claim traceable to the baseline; color never sole carrier. |

### commercial-cta

| Field | Requirement |
|---|---|
| Priority | P0 |
| Purpose | Offer product exploration, technical depth, and a real commercial next step. |
| Required content | Explore Command Center, Explore AI Workspaces, View Architecture, and a commercial contact action only when its destination is real and reviewed. |
| Existing foundation | Reuse the current anchor CTA component and visible focus treatment. |
| Blocked | Non-functional form, external write, connect/execute/deploy/send/download/activate language, freelancer-profile framing. |
| Mobile | Full-width, comfortably sized anchors in narrative priority order. |
| Validation | All destinations resolve; CTA wording matches actual capability. |

### footer-status

| Field | Requirement |
|---|---|
| Priority | P1 |
| Purpose | Close with current project state and documentation links without carrying the full honesty burden. |
| Required content | Static showcase status, concise no-live-operation statement, factual links, product attribution. |
| Existing foundation | Current semantic footer and status styles. |
| Blocked | Stale phase claims, live Git/provider data fetching, stale product-family attribution, invented production state. |
| Mobile | Single-column reading and focus order. |
| Validation | Footer agrees with point-of-use disclosures and does not contradict canonical current state. |

## 3. Cross-section honesty primitives

### DataOrigin

Use only as a UI provenance projection:

- Committed local data
- Audit snapshot
- Simulated

Planned content receives a separate planned label. DataOrigin is not a
universal product status enum.

### StatusChip

Always text plus semantic visual treatment. Use repository vocabulary. Green
is reserved for verified real/current state; red for blocked/error; amber for
approval/caution; violet for structure; blue/cyan for data/signal; magenta for
interaction emphasis.

### StaticPreviewNotice

Required in the hero and within any telemetry-like graph, constellation,
workspace, or dashboard surface that could be mistaken for live operation.
It is visible and non-dismissable.

### SafetyBadge

Use only for concise baseline-supported facts. Visual presence never upgrades
planned or policy state into implementation evidence.

## 4. Responsive transformation contract

| Pattern | Wide layout | Narrow layout |
|---|---|---|
| Spatial stage | Copy plus bounded visual | Copy-first; simplify/remove decoration |
| Multi-panel cockpit | Structured columns | Ordered proof cards |
| Graph | Clusters and evidence rail | Relationship path or evidence list |
| Constellation | Spatial nodes | Ordered list |
| Ecosystem | Hierarchical clusters/rails | Prioritized stacked groups |
| Proof and CTA | May share a row | Proof first, actions second |

At narrow widths, reduce HUD density, preserve body text size, avoid tiny
labels, and use horizontal rails only when intentional, discoverable, and
keyboard accessible.

## 5. Accessibility and motion contract

- semantic landmarks and heading order;
- skip link;
- keyboard-accessible targets and visible focus;
- tested contrast on every glass/gradient state;
- text labels for status and provenance;
- meaningful summaries for complex visuals;
- no information available only on hover;
- resilient layout at 200% zoom;
- no critical content hidden behind animation opacity;
- content complete with JavaScript disabled;
- prefers-reduced-motion removes non-essential motion;
- no animation required for comprehension.

This brief defines requirements. It does not claim WCAG conformance.

## 6. Typography delivery

M2 has no external font dependency. The required baseline is:

- Segoe UI, system-ui, sans-serif;
- Cascadia Mono, Consolas, monospace.

Preferred locally installed families may remain first in an existing fallback
stack, but the design must be intentional when they are absent. Google Fonts
or another remote font CDN is not required. Self-hosted font assets remain a
non-blocking later licensing and packaging decision.

## 7. Static implementation boundaries

Allowed:

- edits to existing static markup, styles, and progressive-enhancement scripts
  under a separately authorized implementation task;
- reuse of current tokens, panels, status primitives, anchors, focus styles,
  reduced-motion rules, and fixture patterns;
- committed and reviewable fixture content;
- deliberate anchor migration with compatibility handling.

Blocked:

- frontend framework migration;
- generated JSX as production architecture;
- provider SDK or fetch-based provider calls;
- backend, database, serverless route, credential UI, runtime adapter, or
  execution path;
- live telemetry, filesystem access, dynamic Git state, email send, model
  download, or external synchronization;
- required remote fonts or critical assets;
- any change under site/ by this specification task.

## 8. M2 implementation order

1. **Foundation and first viewport:** navigation, hero, disclosure, CTA
   hierarchy, Command Center preview shell.
2. **Technical product proof:** graph evolution and Runtime Constellation with
   provenance.
3. **Ecosystem and conversion:** workspace hierarchy, governance/evidence,
   commercial CTA, honest footer.
4. **Acceptance pass:** responsive, keyboard/focus, contrast, reduced motion,
   no-JS, truthfulness, performance, exact count, and destination checks.

These are boundaries, not task identifiers. Each future slice requires
separate authorization and review.

## 9. M2 visual QA checklist

- [ ] Product identity and first action are clear within approximately 15–30 seconds.
- [ ] Command Center and workspace ecosystem read as exactly two product layers.
- [ ] Mechanical workspace-count check passes against the canonical enumeration.
- [ ] No Command Center surface is presented as an additional workspace.
- [ ] Static/demo/planned labels appear at point of use.
- [ ] No live provider, runtime, telemetry, synchronization, send, download, or backend claim.
- [ ] Complex visuals have readable text equivalents.
- [ ] No content starts hidden behind animation.
- [ ] JavaScript-disabled content is complete.
- [ ] Reduced-motion behavior is complete.
- [ ] Keyboard order and visible focus are usable.
- [ ] Status and provenance never rely on color alone.
- [ ] Contrast is tested rather than inferred.
- [ ] Mobile composition is intentional and free of accidental horizontal scroll.
- [ ] Touch targets are comfortably operable.
- [ ] CTA destinations resolve and match their labels.
- [ ] No required external font CDN or critical network asset.
- [ ] No stale product-family or central-gateway positioning.
- [ ] Current static HTML/CSS/JavaScript architecture remains the target.
- [ ] No out-of-scope integration or implementation is introduced.

## 10. Non-blocking follow-ups

The future hero-direction decision and full cinematic Design System amendment
may refine visual language later. Neither is a prerequisite for M2.

The older design-system document contains useful visual primitives and stale
product-story material. Implementation may reuse only the compatible visual
guidance under the authority order recorded in the canonical Homepage
Specification.
