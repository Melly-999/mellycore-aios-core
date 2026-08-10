# MellyCore AIOS — Commercial Showcase Homepage Specification

**Canonical owner:** MELLYCORE-HOMEPAGE-SPEC-001
**Reconciled by:** MELLYCORE-CINEMATIC-HOMEPAGE-SPEC-RECONCILIATION-001
**Version:** 2.0
**Status:** Complete specification; implementation not claimed
**Implementation foundation:** Existing static HTML/CSS/JavaScript under site/

---

## 1. Page purpose

The homepage is the first client-ready MellyCore commercial showcase. It must
let a visitor understand the product, see credible product surfaces, verify
the honesty of the preview, and choose a useful next action within roughly
15–30 seconds.

The page is product-led. It is not a personal CV, a generic AI agency page, a
runtime console, or evidence that planned capabilities are active.

The first-view questions are:

1. What is MellyCore?
2. Why is it different?
3. What can I see?
4. Why should I trust it?
5. What should I click next?

## 2. Audience

Primary audiences are B2B clients, founders, recruiters, technical
collaborators, and AI engineers. The page must balance commercial clarity with
enough architectural evidence to withstand technical scrutiny.

The default reading path must work for a scanning visitor. Deeper technical
detail belongs behind progressive disclosure or in linked documentation.

## 3. Product thesis and product structure

The homepage must derive its story from the canonical Product Vision:

> MellyCore is a local-first, operator-controlled **AI Operating System**.
>
> Its Command Center presents a cinematic AI Operations Observatory and
> visually compelling AI Workspaces, while its runtime, provider, tool,
> context, persistence, evidence, governance and safety planes remain
> vendor-neutral, explicit, provenance-bearing and fail-closed.

The page must preserve those terms. They are product requirements, not generic
marketing adjectives.

The product has exactly two top-level layers:

1. **Command Center** — the product and navigation manifestation of the
   accepted Control Plane / AI Operations Observatory. It projects canonical
   context, routing, runtime, evidence, governance, and safety state; it does
   not own replacement truth.
2. **AI Workspaces** — a planned ecosystem of exactly ten product workspaces.
   Visual presence on the homepage does not establish implementation,
   connection, execution, or authorization.

The controlled improvement loop may appear as supporting proof:

**observe → analyze → recommend → approve → implement → validate → record**

The primary story must not be centered on a gateway, model name, vendor list,
or another MellyGenix product family.

## 4. Page information architecture

The required M2 narrative is:

1. **Hero / product thesis**
2. **Command Center preview**
3. **Knowledge & Operations Graph preview**
4. **Runtime Constellation preview**
5. **AI Workspaces ecosystem**
6. **Governance, evidence, and safety proof**
7. **Commercial next action**
8. **Honest project-status footer**

This sequence is a hierarchy, not a requirement to make every Command Center
surface a full homepage section. Existing context, routing, tooling, roadmap,
and Source Arena material may be reused inside the appropriate preview or
linked as secondary detail. M2 must avoid a long catalogue of equal-weight
technical sections.

## 5. Hero structure

### Required composition

The hero must remain valid regardless of a later hero-direction decision:

1. identity kicker;
2. strong H1;
3. one-line commercial proposition;
4. concise supporting description;
5. visible static-preview disclosure;
6. selected factual safety or provenance badges;
7. primary and secondary CTA;
8. optional supporting visual stage.

The hero must not contain a giant explanatory paragraph. Supporting copy
should normally remain within two short sentences and approximately 45 words.

### Preferred production-spec copy

- **Kicker:** MellyCore AIOS / Local-first AI Operating System
- **H1:** One command center. Every AI plane under operator control.
- **One-line proposition:** Explore models, agents, tools, context, and
  workspaces through one cinematic, provenance-bearing AI operations
  experience.
- **Supporting copy:** MellyCore keeps provider and runtime choices
  vendor-neutral while evidence, approvals, and safety boundaries stay
  explicit. This showcase is a static product preview, not a live control
  surface.
- **Primary CTA:** Explore Command Center
- **Secondary CTA:** Explore AI Workspaces

Approved alternative H1:

- **A local-first AI operating system for serious, supervised work.**

The copy must not use an OmniRouter-centered thesis, “many models at the
center,” or shared-coordination-layer wording tied to MellyGenix.

### Honesty treatment

A non-dismissable StaticPreviewNotice must appear before or adjacent to the
first CTA:

**Static product preview — no live telemetry, provider calls, or execution.**

Up to three SafetyBadges may reinforce supportable facts such as
**Static preview**, **Operator-controlled**, and **Local-first**. A badge must
not claim that a future capability is verified, connected, or available.

### Structural requirements and allowed visual variation

The copy, disclosure, and CTA hierarchy are fixed structural requirements.
The supporting stage may use a Source Arena-led, orbital Command Center-led,
hybrid, or instrument/calibration treatment. It must remain subordinate to
the message, work without animation, and preserve the same truth labels.

The future hero bake-off is not an M2 dependency. No direction may block the
first commercial showcase.

## 6. Command Center preview

The homepage needs one legible, high-impact preview of the Command Center,
not the complete M3 shell.

The composition may use:

- **Left:** context management and routing;
- **Center:** Knowledge & Operations Graph;
- **Right:** agents, runtimes, observability, and approvals;
- **Bottom evidence rail:** context → routing → runtime → tools → approval →
  execution → evidence.

Required behavior:

- communicate that the Command Center is a projection over accepted canonical
  owners;
- make operator gates and evidence visible;
- prefer a few readable panels over dense dashboard chrome;
- label fixture, snapshot, simulated, and planned content at point of use;
- expose no operational controls that imply execution;
- keep major content visible in semantic HTML without JavaScript.

Source Arena may appear as a flagship proof surface or linked exploration. It
must not collapse the full product identity into a single provider or routing
story.

## 7. Knowledge & Operations Graph preview

The graph is a derived product visualization. It is not canonical truth and
must not be presented as one.

The preview may show relationships among context, documents, systems,
runtimes, agents, tools, runs, and evidence. Every relationship that is not
observed from accepted current evidence must be explicitly labeled as a
fixture, example, simulation, or planned projection.

Required content:

- a readable text summary outside the visual;
- visible provenance or DataOrigin treatment;
- a representative evidence/source strip;
- a legend that explains relationship types and status in text;
- a clear statement that the graph projects source records and does not own
  them.

On mobile, replace the dense graph with a simplified relationship path,
cluster summary, or ordered evidence list. Do not shrink desktop labels into
unreadable decoration.

## 8. Runtime Constellation preview

Runtime Constellation is a product projection, not a runtime owner or an
inventory assertion.

The preview may demonstrate how frameworks, agents, models, tools, and local
execution could be understood together, but a displayed name must never imply
that it is installed, supported, connected, running, or authorized.

Required behavior:

- show status with text and semantic treatment;
- pair the visual with a StaticPreviewNotice when misinterpretation is
  plausible;
- reserve motion for explaining relationships, never for fake activity;
- avoid pulsing “online” nodes or animated traffic;
- collapse to a compact, ordered list or relationship diagram on mobile;
- keep provider/framework examples subordinate to the vendor-neutral product
  contract.

## 9. Ten AI Workspaces presentation

The homepage must present one ecosystem with hierarchy, not ten identical
feature cards. Recommended treatment: a strong Wave 1 feature cluster, a
compact Wave 2 rail, and a restrained Wave 3/local-AI grouping. Each entry
uses existing planned/static-demo vocabulary and includes a short outcome,
not a fabricated operational state.

The canonical enumeration is exactly:

| # | Workspace | Activation wave | M2 presentation |
|---:|---|---:|---|
| 1 | Deep Research | 1 | Featured planned workflow |
| 2 | Compare Arena | 1 | Featured planned workflow |
| 3 | Multi-Agent Crew | 1 | Featured planned workflow |
| 4 | Email AI | 2 | Compact planned preview |
| 5 | Voice | 2 | Compact planned preview |
| 6 | Video Intelligence | 2 | Compact planned preview |
| 7 | Image Studio | 3 | Compact planned preview |
| 8 | Model Downloader | 3 | Local-AI planned preview |
| 9 | Ollama Manager | 3 | Local-AI planned preview |
| 10 | Coding / Runtime Studio | 1 | Featured planned workflow |

No other homepage concept is a workspace. In particular, graph, routing,
runtime, context, arena, hub, and mission-control concepts remain Command
Center surfaces or presentation groupings.

All ten remain planned at the pinned baseline. The page must state that
workspace visuals do not imply active backends, provider access, sends,
downloads, synchronization, or execution.

## 10. Governance, evidence, and safety proof

Trust must be demonstrated before the final CTA with a concise proof block,
not a wall of policy copy.

Required proof:

- local-first and operator-controlled posture;
- consequential actions require explicit approval;
- provenance and evidence remain visible;
- vendor and runtime choices remain explicit and replaceable;
- static and planned surfaces are labeled;
- fail-closed boundaries are described in plain language;
- no secrets, credential inputs, provider controls, or execution controls on
  the homepage.

The block may visualize the controlled improvement loop and link to
architecture or safety documentation. It must distinguish design claims from
current implementation evidence.

## 11. Prototype honesty system

These distinctions are mandatory:

**visual ≠ implemented; planned ≠ implemented; implemented ≠ tested; tested ≠
connected; connected ≠ authorized; static demo ≠ live telemetry; supported ≠
connected.**

### DataOrigin

DataOrigin is a UI provenance projection, not a new universal product status
enum. Allowed M2 labels include:

- **Committed local data**
- **Audit snapshot**
- **Simulated**

Planned content uses an explicit planned-state treatment separate from
DataOrigin. A provenance label must appear next to the data or visual it
qualifies.

### StatusChip

StatusChip always combines text with semantic visual treatment. Color alone
is insufficient. Labels must use current repository vocabulary and must not
invent a universal enum.

### StaticPreviewNotice

StaticPreviewNotice is visible in the hero and within any telemetry-like,
graph, constellation, workspace, or dashboard preview that could reasonably
be mistaken for live operation. It is non-dismissable and not relegated to
the footer.

### SafetyBadge

SafetyBadge communicates only concise, factual claims supported at the
baseline. It cannot turn a policy aspiration into verified runtime state.

### Prohibited implications

The page must not imply live providers, model calls, runtime execution,
fixture telemetry, active synchronization, email sending, model downloads,
implemented workspace backends, or autonomous action.

## 12. CTA strategy

CTA priority is:

1. **Explore Command Center** — primary product-exploration anchor.
2. **Explore AI Workspaces** — secondary ecosystem anchor.
3. **View Architecture** — supporting technical-documentation link.
4. **Discuss an AI Project** — commercial conversion only when a real,
   reviewed destination exists; do not add a non-functional form.

The page must not behave like a freelancer profile. Commercial conversion is
framed around the product and its architecture.

Forbidden CTA families include connect, execute, deploy, send, download,
activate, add credentials, or any action that implies a backend or provider
capability not present.

## 13. Visual direction and semantic color

The direction is cinematic, premium, technical, spatial, AI-native, and
operator-controlled. Use near-black/deep-navy foundations, restrained violet
and cobalt structure, cyan signal accents, deliberate whitespace, structured
panels, and purposeful depth.

Semantic color rules:

| Color family | Meaning |
|---|---|
| Violet | Primary structure and identity |
| Blue / cyan | Data, signal, and routing accents |
| Magenta | Interaction emphasis only |
| Amber | Safety, approval, and caution |
| Green | Verified real/current state only |
| Red | Blocked or error |

Color is never the only status carrier. Green must not be used as generic
decorative success.

Avoid generic SaaS composition, random particles, glowing borders on every
surface, excessive glass blur, gaming-HUD density, ubiquitous purple
gradients, repeated identical cards, meaningless graphs, and unreadable
sci-fi labels.

## 14. Typography delivery

The visual family direction may reference Inter and JetBrains Mono, but M2
must not require Google Fonts or another external font CDN.

The implementation baseline is local-first:

- body: Segoe UI, system-ui, sans-serif;
- technical text: Cascadia Mono, Consolas, monospace.

Existing token stacks may retain preferred family names only as optional
first choices when those fonts are already installed locally; the page must
remain intentional and metrically robust with system fallbacks.

Self-hosted licensed font assets are a non-blocking later decision. This task
adds no font files and authorizes no download.

## 15. Motion

Motion is progressive enhancement:

- all critical content is visible without JavaScript;
- no content starts hidden behind entry-animation opacity;
- no animation is required for comprehension or navigation;
- no fake pulsing live indicators;
- reduced-motion mode removes non-essential motion;
- relationship motion, if later added, must clarify hierarchy and stop
  cleanly without changing meaning.

If a timeline or script stalls, the complete static reading state must remain
visible. The static state is the acceptance baseline.

## 16. Responsive behavior

Mobile is an intentional composition, not compressed desktop.

| Surface | Desktop / wide | Mobile / narrow |
|---|---|---|
| Hero | Copy plus optional visual stage | Copy-first stack; decorative stage simplified or removed |
| Command Center | Structured multi-panel preview | Ordered proof cards with lower HUD density |
| Graph | Spatial clusters and evidence rail | Simplified path, cluster summary, or evidence list |
| Constellation | Spatial relationships | Compact ordered relationship list |
| Workspaces | Hierarchical feature cluster and rails | One-column prioritized groups; no accidental horizontal scroll |
| Governance / CTA | Side-by-side proof and actions where space permits | Proof before full-width touch targets |

Touch targets must be comfortably operable, body text remains legible, and
horizontal rails are used only when deliberate, discoverable, and keyboard
accessible.

## 17. Accessibility requirements

The future implementation must provide:

- semantic landmarks and heading hierarchy;
- a usable skip link;
- keyboard-operable links and controls;
- visible focus;
- sufficient tested contrast;
- text labels for every status;
- reduced-motion support;
- meaningful text alternatives and summaries for complex visuals;
- no critical information only on hover;
- readable minimum typography and resilient 200% zoom;
- decorative visuals hidden from assistive technology where appropriate.

This specification does not claim WCAG conformance. Conformance requires
implementation-level validation.

## 18. Static implementation constraints

M2 evolves the existing site/ HTML/CSS/JavaScript foundation. It does not
authorize a framework rewrite or generated JSX architecture.

Requirements:

- semantic content renders without JavaScript;
- JavaScript is limited to progressive enhancement;
- no provider SDK, API request, credential field, database, backend, serverless
  route, runtime adapter, or execution path;
- reuse current tokens, responsive primitives, focus treatment, reduced-motion
  handling, and static honesty components where they remain compatible;
- preserve or migrate stable section anchors deliberately so existing local
  navigation does not fail silently;
- fixture data is committed, inspectable, and labeled at point of use;
- no required external network dependency for fonts or critical content.

## 19. M2 implementation slices

These are scope boundaries, not newly minted task identifiers:

1. **Foundation and first viewport** — reconcile navigation, hero, copy,
   disclosure, CTA hierarchy, and Command Center preview shell.
2. **Technical product proof** — evolve the existing context graph into the
   Knowledge & Operations Graph preview and add the Runtime Constellation
   preview with point-of-use provenance.
3. **Ecosystem and conversion** — add the hierarchical ten-workspace
   presentation, governance/evidence proof, commercial CTA, and honest footer.
4. **Acceptance pass** — responsive, keyboard/focus, contrast, reduced-motion,
   no-JS visibility, truthfulness, performance, and exact-workspace-count
   validation.

Each slice requires its own authorization and review scope. No slice requires
the hero bake-off, full cinematic Design System amendment, provider
integration, runtime integration, or backend work.

## 20. Explicitly out of scope

- homepage HTML, CSS, or JavaScript implementation;
- changes under site/;
- Hero Bake-off or final hero metaphor selection;
- full Design System Cinematic Amendment;
- changes to the older design-system document;
- providers, runtimes, models, tools, MCP servers, credentials, or live calls;
- Obsidian or workspace backend integration;
- graph schema or canonical architecture ownership changes;
- framework migration or generated JSX adoption;
- font downloads or binaries;
- push, merge, deployment, or production-state claims.

The future hero decision and full Design System amendment are non-blocking
follow-ups, not M2 prerequisites.

## 21. M2 acceptance criteria

These criteria apply to future implementation and are not claims about the
current site:

- [ ] Existing static site architecture is retained unless separately changed.
- [ ] The first viewport communicates the product within roughly 15–30 seconds.
- [ ] The two-layer product structure is clear.
- [ ] The workspace ecosystem contains exactly the canonical count.
- [ ] No visual or copy implies fake-live capability.
- [ ] Provenance labels appear at point of use where needed.
- [ ] Static/demo and planned surfaces are explicit.
- [ ] The page feels cinematic, premium, technical, and commercially relevant.
- [ ] Command Center, graph, runtime, and workspace previews form one story.
- [ ] Mobile is intentionally composed and has no accidental horizontal scroll.
- [ ] Keyboard and visible-focus paths are viable.
- [ ] Reduced motion is supported.
- [ ] Critical content remains visible without JavaScript or animation.
- [ ] A product-led commercial CTA is present and functional.
- [ ] No external font CDN is required.
- [ ] Primary positioning contains no stale MellyGenix or gateway-centered story.
- [ ] No unauthorized provider, runtime, tool, workspace, or data integration exists.
- [ ] Complex visuals provide equivalent readable text.
- [ ] Status and provenance never rely on color alone.

## 22. Canonical ownership and reconciliation record

This file is the canonical homepage behavior and content specification.
docs/specs/MELLYCORE_UI_SECTIONS.md is its subordinate implementation
projection and must not create conflicting product truth.

Still-valid prior decisions retained:

- static-first delivery;
- prototype honesty before action;
- semantic status labels;
- safety as visible product proof;
- cinematic deep-space restraint;
- mobile transformations rather than desktop compression;
- anchor/documentation navigation until a real destination exists.

Superseded assumptions:

- OmniRouter as homepage identity or hero center;
- provider/model-name lists as the product thesis;
- MellyGenix coordination-layer positioning;
- the orbital cube as a mandatory hero;
- nine equal legacy sections as the M2 narrative;
- roadmap and tooling catalogues as primary commercial-story sections;
- a documentation-only CTA hierarchy;
- footer claims that predate the current static implementation state.

Where older design narrative conflicts, authority is:

**PROJECT_STATE → ROADMAP / TASK_INDEX → shared DESIGN_SYSTEM → older design
documentation.**

The full cinematic Design System amendment and hero-direction decision remain
future work and do not block this specification or M2.
