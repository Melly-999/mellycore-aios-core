/*
 * MellyCore AIOS — Live Cockpit V2 (social source arena).
 *
 * Local committed data is fetched read-only from shared_context/**.
 * The Source Arena tab renders a small, deterministic local Source Archive —
 * no external request, no API key, zero network dependency. Model-lens text
 * is deterministic local mock copy and is labeled SIMULATED MODEL OUTPUT
 * wherever it appears. Social action counts are deterministic demo numbers,
 * labeled as such. No provider model is called and nothing is written or
 * published.
 */

(function () {
  "use strict";

  const ARCHIVE_CATEGORIES = {
    context: { label: "Context" },
    workflow: { label: "Workflow" },
    safety: { label: "Safety" },
    observability: { label: "Observability" },
    model: { label: "Model" },
    routing: { label: "Routing" },
    memory: { label: "Memory" },
    orchestration: { label: "Orchestration" },
  };

  /* Deterministic local showcase records — no external request, no remote
   * image URL. Each record summarizes an already-documented, verifiable
   * piece of this repository's own committed state. */
  const ARCHIVE_RECORDS = [
    {
      id: "context-gate",
      title: "Context Gate — Admission Ledger",
      category: "context",
      description: "Guarded admission pipeline (through Increment 4): validates, scores trust, and computes a content-free provenance index.",
      tags: ["context", "provenance", "audit"],
      status: "Implemented through I4",
    },
    {
      id: "loop-registry",
      title: "Loop Operations Registry",
      category: "workflow",
      description: "Nine registered loops define the controlled observe -> analyze -> recommend -> approve -> implement -> validate -> record cycle. Report-only; no production-enabled loop.",
      tags: ["workflow", "loops", "governance"],
      status: "Report-only",
    },
    {
      id: "safety-contract",
      title: "Safety Contract",
      category: "safety",
      description: "Committed operator-approval rules: no autonomous merges, deploys, or trades, and no self-modifying safety rules.",
      tags: ["safety", "approval", "governance"],
      status: "Committed",
    },
    {
      id: "project-health",
      title: "Project-Health Evidence Ledger",
      category: "observability",
      description: "Immutable run ledger recording guard decisions, budget checks, and outcomes for human-invoked project-health runs.",
      tags: ["observability", "evidence", "ledger"],
      status: "2 recorded runs",
    },
    {
      id: "ai-ops-intel",
      title: "AI Operations Intelligence Spec",
      category: "model",
      description: "Logical contract for the AI Estate Inventory, Unified Run Ledger, Skill Gap Detector, and Memory Freshness Monitor. Specification only.",
      tags: ["model", "specification", "router"],
      status: "Specified, not implemented",
    },
    {
      id: "operations-data-contract",
      title: "Operations Data Contract",
      category: "routing",
      description: "Fixture and schema artifacts translating the logical contract into validated shapes for a future adapter layer.",
      tags: ["routing", "schema", "fixture"],
      status: "Integrated (schema/fixture only)",
    },
    {
      id: "memory-freshness",
      title: "Memory Freshness Monitor",
      category: "memory",
      description: "Planned detection of stale, conflicting, or superseded context records.",
      tags: ["memory", "freshness", "planned"],
      status: "Planned",
    },
    {
      id: "source-arena-renderer",
      title: "Source Arena Hybrid Renderer",
      category: "orchestration",
      description: "Accepted decision for a WebGL-enhanced renderer with a mandatory CSS/DOM fallback. Decision level only; not yet implemented.",
      tags: ["orchestration", "renderer", "planned"],
      status: "Accepted (spec only)",
    },
  ];

  const MODEL_DEFS = [
    { id: "fable", name: "Fable 5", color: "#a86cff" },
    { id: "opus", name: "Opus", color: "#35d7f2" },
    { id: "gpt", name: "GPT", color: "#58e68a" },
    { id: "glm", name: "GLM", color: "#ffc34d" },
  ];

  const MODEL_COPY = {
    context: {
      fable: "Story lens: frame why context provenance matters before any record reaches the surface. Scripted interface sample, not generated analysis.",
      opus: "Architecture lens: separate admitted records from rejected or reasoning-only entries before drawing conclusions. Mock response only.",
      gpt: "Context synthesis lens: connect the visible context metrics to the underlying admission pipeline. Simulated output.",
      glm: "Fast exploration lens: suggest adjacent context records worth auditing next. No provider request was sent.",
    },
    workflow: {
      fable: "Story lens: frame the nine registered loops as a single controlled improvement cycle. Scripted mock copy.",
      opus: "Architecture lens: separate report-only loops from any production-enabled path before interpreting status. Simulated output.",
      gpt: "Synthesis lens: connect loop tiers to the observe-to-approve-to-implement cycle. Mock response only.",
      glm: "Exploration lens: branch toward loop tiering and cadence questions. No model was called.",
    },
    safety: {
      fable: "Story lens: frame operator approval as the boundary every consequential action must cross. Deterministic mock output.",
      opus: "Scientific caution lens: do not infer an approval decision from this summary alone. Simulated response.",
      gpt: "Context lens: place the safety contract beside the loop registry without claiming enforcement beyond what is committed. Mock response only.",
      glm: "Discovery lens: suggest which safety clauses deserve a closer audit. No provider connection exists.",
    },
    observability: {
      fable: "Story lens: frame the evidence ledger as the record of what actually happened, not a projection. Scripted sample.",
      opus: "Source lens: distinguish measured tokens from null/unmeasured fields before interpretation. Simulated output.",
      gpt: "Educational lens: relate guard decisions and budget checks to run outcomes. Mock response only.",
      glm: "Exploration lens: branch toward run-history and budget-guard follow-ups. No request was sent.",
    },
    model: {
      fable: "Story lens: frame the AI Operations Intelligence spec as a contract, not a running system. Deterministic mock output.",
      opus: "Mission lens: identify which modules remain specified versus implemented before asserting capability. Simulated response.",
      gpt: "Context lens: connect the spec's logical contracts to the controlled improvement loop. Mock response only.",
      glm: "Discovery lens: propose adapter, router, and ledger follow-ups. No model was called.",
    },
    routing: {
      fable: "Story lens: frame the Operations Data Contract as schema/fixture scope, not runtime routing. Scripted mock copy.",
      opus: "Architecture lens: separate integrated documentation scope from any adapter or provider routing. Simulated output.",
      gpt: "Synthesis lens: connect fixture shapes to the future routing surface they are meant to validate. Mock response only.",
      glm: "Exploration lens: branch toward adapter and provider routing questions. No provider request was sent.",
    },
    memory: {
      fable: "Story lens: frame memory freshness as a planned safeguard against stale or superseded context. Deterministic mock output.",
      opus: "Evidence lens: separate 'planned' from 'implemented' before treating this as an active monitor. Simulated output.",
      gpt: "Synthesis lens: connect freshness monitoring to the existing context-audit aggregates. Mock response only.",
      glm: "Exploration lens: branch toward conflict-detection and supersession questions. No model was called.",
    },
    orchestration: {
      fable: "Story lens: frame the accepted Hybrid renderer decision as a specification, not a shipped scene. Scripted sample.",
      opus: "Source lens: distinguish the accepted decision record from any vendored dependency or renderer code. Simulated output.",
      gpt: "Context lens: place the renderer decision beside the CSS/DOM fallback requirement it is paired with. Mock response only.",
      glm: "Exploration lens: branch toward fallback-accessibility and performance-QA follow-ups. No request was sent.",
    },
  };

  /* ------------------------------------------------------------------
   * OpenRouter Model Observatory — static snapshot slice.
   * Local fixture only. No fetch, no API key, no model call, no account
   * usage. Conforms to docs/specs/MELLYCORE_OPENROUTER_MODEL_OBSERVATORY_SPEC.md
   * §6 (static data schema), §7 (lanes), §8 (routing policy), §9 (estimator).
   * ------------------------------------------------------------------ */

  const OBS_SAFETY_LABELS = [
    "STATIC SNAPSHOT",
    "NO API KEY",
    "NO MODEL CALLS",
    "NO ACCOUNT USAGE",
    "NOT LIVE PRICING",
    "FUTURE-GATED LIVE CATALOG",
  ];

  const OBS_LANES = {
    free_experimental: "Free / Experimental",
    cheap_worker: "Cheap Worker",
    balanced_daily: "Balanced Daily",
    premium_reasoning: "Premium Reasoning",
    visual_product_judge: "Visual/Product Judge",
    security_architecture_review: "Security/Architecture Review",
    long_context: "Long Context",
    coding_refactor: "Coding / Refactor",
    fallback_emergency: "Fallback / Emergency",
  };

  const OBS_RUN_TYPES = {
    routine: { label: "Routine", lane: "cheap_worker", primaryCapability: "cheap_routine" },
    drafting: { label: "Drafting", lane: "cheap_worker", primaryCapability: "cheap_routine" },
    coding_refactor: { label: "Coding / Refactor", lane: "coding_refactor", primaryCapability: "coding" },
    long_context: { label: "Long Context", lane: "long_context", primaryCapability: "long_context" },
    visual_product_review: { label: "Visual/Product Review", lane: "visual_product_judge", primaryCapability: "visual_product" },
    security_architecture_review: { label: "Security/Architecture Review", lane: "security_architecture_review", primaryCapability: "security_review" },
    fallback_emergency: { label: "Fallback / Emergency", lane: "fallback_emergency", primaryCapability: "cheap_routine" },
  };

  const OBS_CAPABILITY_FIELDS = [
    ["coding", "Coding"],
    ["reasoning", "Reasoning"],
    ["visual_product", "Visual/Product"],
    ["security_review", "Security/Review"],
    ["long_context", "Long Context"],
    ["cheap_routine", "Cheap/Routine"],
  ];

  const OBS_COST_CLASS_RANK = { FREE_EXPERIMENTAL: 0, LOW: 1, MEDIUM: 2, HIGH: 3, PREMIUM: 4 };

  const OBS_FIXTURE_NOTICE = "This Observatory fixture is a static snapshot of representative example entries only. It is not live pricing, not account-backed, and not a claim about current OpenRouter catalog availability. Cost and context-window fields are null unless a reviewed source is on file.";

  /* Every model record conforms 1:1 to spec §6. cost/context fields are
   * null wherever this fixture has no reviewed source — this is the
   * correct, expected state per §9.2, not a bug. cost_class and lane
   * fit are carried over from the reviewed routing table already
   * committed at docs/specs/MELLYCORE_OPENROUTER_MODEL_OBSERVATORY_SPEC.md §8. */
  const OBS_MODEL_FIXTURE = {
    schema_version: "1.0",
    example_notice: OBS_FIXTURE_NOTICE,
    models: [
      {
        model_id: "fable-5",
        display_name: "Fable 5",
        provider: "PLANNED_ALIAS — no verified provider binding",
        routing_lane: "visual_product_judge",
        cost_class: "UNKNOWN",
        input_cost_per_million: null,
        output_cost_per_million: null,
        cache_read_cost_per_million: null,
        currency: "USD",
        context_window: null,
        capabilities: { coding: 0, reasoning: 2, visual_product: 3, security_review: 1, long_context: 1, cheap_routine: 0 },
        best_for: ["Final visual/product acceptance review", "Cinematic UX hierarchy judgment"],
        avoid_for: ["Routine drafting", "Mechanical edits", "Any run assuming availability"],
        fallbacks: [
          { model_ref: "gpt-5-6-sol", reason: "Premium reasoning fallback for product architecture", tradeoff: "Loses dedicated visual/product judgment specialization" },
          { model_ref: "opus-class", reason: "Fallback for safety/architecture ambiguity", tradeoff: "Different specialization, not a visual judge" },
        ],
        status: "UNAVAILABLE",
        snapshot_date: "2026-07-23",
        source_note: "Representative example entry only — not live pricing. Fable 5 is unavailable in this task context; no provider connection exists.",
        safety_note: "STATIC SNAPSHOT · NO API KEY · NO MODEL CALLS · NO ACCOUNT USAGE",
      },
      {
        model_id: "opus-class",
        display_name: "Opus-class",
        provider: "PLANNED_ALIAS — Opus-class family, no exact reviewed identifier",
        routing_lane: "security_architecture_review",
        cost_class: "PREMIUM",
        input_cost_per_million: null,
        output_cost_per_million: null,
        cache_read_cost_per_million: null,
        currency: "USD",
        context_window: null,
        capabilities: { coding: 2, reasoning: 3, visual_product: 0, security_review: 3, long_context: 2, cheap_routine: 0 },
        best_for: ["Security boundaries", "Architecture and adversarial reasoning", "Future-live gate review"],
        avoid_for: ["Cheap high-volume work", "Cosmetic-only edits"],
        fallbacks: [
          { model_ref: "gpt-5-6-sol", reason: "High-effort reasoning fallback", tradeoff: "Less specialized for adversarial security review" },
          { model_ref: "claude-sonnet", reason: "Independent review for docs/architecture consistency", tradeoff: "Lower assurance floor for adversarial security review" },
        ],
        status: "PLANNED_ALIAS",
        snapshot_date: "2026-07-23",
        source_note: "Representative example entry only — not live pricing. No reviewed exact provider identifier is on file for this alias.",
        safety_note: "STATIC SNAPSHOT · NO API KEY · NO MODEL CALLS · NO ACCOUNT USAGE",
      },
      {
        model_id: "gpt-5-6-sol",
        display_name: "GPT-5.6 Sol",
        provider: "PLANNED_ALIAS — no verified provider binding",
        routing_lane: "premium_reasoning",
        cost_class: "PREMIUM",
        input_cost_per_million: null,
        output_cost_per_million: null,
        cache_read_cost_per_million: null,
        currency: "USD",
        context_window: null,
        capabilities: { coding: 3, reasoning: 3, visual_product: 1, security_review: 2, long_context: 2, cheap_routine: 0 },
        best_for: ["High-effort product architecture", "Routing strategy", "Complex implementation/reasoning", "Fable 5 fallback"],
        avoid_for: ["Low-value bulk drafting where a cheaper lane meets requirements"],
        fallbacks: [
          { model_ref: "opus-class", reason: "Ambiguous safety/future-live boundary escalation", tradeoff: "Different reasoning emphasis" },
          { model_ref: "claude-sonnet", reason: "Documentation consistency fallback", tradeoff: "Lower architecture-reasoning depth" },
        ],
        status: "PLANNED_ALIAS",
        snapshot_date: "2026-07-23",
        source_note: "Representative example entry only — not live pricing. No reviewed exact provider identifier is on file for this alias.",
        safety_note: "STATIC SNAPSHOT · NO API KEY · NO MODEL CALLS · NO ACCOUNT USAGE",
      },
      {
        model_id: "gpt-5-5",
        display_name: "GPT-5.5",
        provider: "UNKNOWN — no reviewed provider identifier on file",
        routing_lane: "long_context",
        cost_class: "MEDIUM",
        input_cost_per_million: null,
        output_cost_per_million: null,
        cache_read_cost_per_million: null,
        currency: "USD",
        context_window: null,
        capabilities: { coding: 2, reasoning: 3, visual_product: 1, security_review: 1, long_context: 2, cheap_routine: 1 },
        best_for: ["Strong general reasoning", "Synthesis", "Balanced-to-premium daily work"],
        avoid_for: ["Assuming specialist visual judgment", "The cheapest batch route"],
        fallbacks: [
          { model_ref: "claude-sonnet", reason: "Documentation and synthesis fallback", tradeoff: "Slightly different reasoning style" },
          { model_ref: "tera", reason: "Cost-aware fallback", tradeoff: "Lower assurance and unreviewed alias pricing" },
        ],
        status: "UNKNOWN",
        snapshot_date: "2026-07-23",
        source_note: "Representative example entry only — not live pricing. No reviewed provider price is on file for this model in this fixture.",
        safety_note: "STATIC SNAPSHOT · NO API KEY · NO MODEL CALLS · NO ACCOUNT USAGE",
      },
      {
        model_id: "claude-sonnet",
        display_name: "Claude Sonnet",
        provider: "UNKNOWN — no reviewed provider identifier on file",
        routing_lane: "balanced_daily",
        cost_class: "MEDIUM",
        input_cost_per_million: null,
        output_cost_per_million: null,
        cache_read_cost_per_million: null,
        currency: "USD",
        context_window: null,
        capabilities: { coding: 2, reasoning: 2, visual_product: 1, security_review: 2, long_context: 3, cheap_routine: 2 },
        best_for: ["Documentation consistency", "Architecture synthesis", "Bounded reviews", "Daily high-quality work"],
        avoid_for: ["Acting as the only reviewer for an ambiguous security or live-account gate"],
        fallbacks: [
          { model_ref: "gpt-5-5", reason: "General reasoning fallback", tradeoff: "Different documentation-consistency emphasis" },
          { model_ref: "opus-class", reason: "Escalated review fallback", tradeoff: "Higher premium cost class" },
        ],
        status: "UNKNOWN",
        snapshot_date: "2026-07-23",
        source_note: "Representative example entry only — not live pricing. No reviewed provider price is on file for this model in this fixture.",
        safety_note: "STATIC SNAPSHOT · NO API KEY · NO MODEL CALLS · NO ACCOUNT USAGE",
      },
      {
        model_id: "tera",
        display_name: "Tera",
        provider: "PLANNED_ALIAS — reviewed alias, no confirmed provider identifier",
        routing_lane: "fallback_emergency",
        cost_class: "LOW",
        input_cost_per_million: null,
        output_cost_per_million: null,
        cache_read_cost_per_million: null,
        currency: "USD",
        context_window: null,
        capabilities: { coding: 2, reasoning: 1, visual_product: 0, security_review: 0, long_context: 1, cheap_routine: 3 },
        best_for: ["Cost-aware daily implementation", "Iteration", "Fallback work under an explicit reviewed alias"],
        avoid_for: ["Final security, account-usage, or ambiguous safety decisions"],
        fallbacks: [
          { model_ref: "glm-cheap", reason: "Cheaper routine-work fallback", tradeoff: "Lower reasoning ceiling" },
          { model_ref: "claude-sonnet", reason: "Higher-assurance fallback", tradeoff: "Higher cost class" },
        ],
        status: "PLANNED_ALIAS",
        snapshot_date: "2026-07-23",
        source_note: "Representative example entry only — not live pricing. Alias and price are unreviewed for this fixture.",
        safety_note: "STATIC SNAPSHOT · NO API KEY · NO MODEL CALLS · NO ACCOUNT USAGE",
      },
      {
        model_id: "glm-cheap",
        display_name: "GLM / cheap model",
        provider: "PLANNED_ALIAS — generic cheap-tier descriptor, no exact identifier",
        routing_lane: "cheap_worker",
        cost_class: "LOW",
        input_cost_per_million: null,
        output_cost_per_million: null,
        cache_read_cost_per_million: null,
        currency: "USD",
        context_window: null,
        capabilities: { coding: 1, reasoning: 1, visual_product: 0, security_review: 0, long_context: 0, cheap_routine: 3 },
        best_for: ["Drafting", "Formatting", "Extraction", "Exploration", "Secondary implementation ideas"],
        avoid_for: ["Sole source for architecture, security, visual acceptance, or consequential approval"],
        fallbacks: [
          { model_ref: "tera", reason: "Slightly higher-assurance fallback", tradeoff: "Alias/price still unreviewed" },
          { model_ref: "claude-sonnet", reason: "Higher-assurance escalation", tradeoff: "Higher cost class" },
        ],
        status: "PLANNED_ALIAS",
        snapshot_date: "2026-07-23",
        source_note: "Representative example entry only — not live pricing. Generic cheap-tier descriptor; do not equate low cost with fit.",
        safety_note: "STATIC SNAPSHOT · NO API KEY · NO MODEL CALLS · NO ACCOUNT USAGE",
      },
      {
        model_id: "codex",
        display_name: "Codex",
        provider: "UNKNOWN — no generic Codex price assumption is authorized",
        routing_lane: "coding_refactor",
        cost_class: "UNKNOWN",
        input_cost_per_million: null,
        output_cost_per_million: null,
        cache_read_cost_per_million: null,
        currency: "USD",
        context_window: null,
        capabilities: { coding: 3, reasoning: 2, visual_product: 0, security_review: 1, long_context: 1, cheap_routine: 1 },
        best_for: ["Scoped coding/refactor work", "Tests", "Validation", "Implementation review", "Deterministic repository changes"],
        avoid_for: ["Unbounded product strategy", "Treating generated code as already validated"],
        fallbacks: [
          { model_ref: "gpt-5-6-sol", reason: "Complex implementation reasoning fallback", tradeoff: "Higher premium cost class" },
          { model_ref: "claude-sonnet", reason: "Docs/architecture review fallback", tradeoff: "Different coding-specific tuning" },
        ],
        status: "UNKNOWN",
        snapshot_date: "2026-07-23",
        source_note: "Representative example entry only — not live pricing. The underlying model cost is not represented; no generic Codex price assumption is made.",
        safety_note: "STATIC SNAPSHOT · NO API KEY · NO MODEL CALLS · NO ACCOUNT USAGE",
      },
    ],
  };

  const OBS_LANE_PRIMARY = {
    cheap_worker: { primary: "glm-cheap", alt: "tera" },
    balanced_daily: { primary: "claude-sonnet", alt: "gpt-5-5" },
    premium_reasoning: { primary: "gpt-5-6-sol", alt: "opus-class" },
    visual_product_judge: { primary: "fable-5", alt: "gpt-5-6-sol" },
    security_architecture_review: { primary: "opus-class", alt: "claude-sonnet" },
    long_context: { primary: "gpt-5-5", alt: "claude-sonnet" },
    coding_refactor: { primary: "codex", alt: "gpt-5-6-sol" },
    fallback_emergency: { primary: "tera", alt: "glm-cheap" },
  };

  function obsFindModel(modelId) {
    return OBS_MODEL_FIXTURE.models.find((model) => model.model_id === modelId) || null;
  }

  function obsCapabilityLabel(level) {
    if (level >= 3) return { label: "Strong", cls: "obs-cap--strong" };
    if (level === 2) return { label: "Partial", cls: "obs-cap--partial" };
    if (level === 1) return { label: "Limited", cls: "obs-cap--limited" };
    return { label: "None", cls: "obs-cap--none" };
  }

  const state = {
    roadmapText: "",
    runQueueText: "",
    safetyContractText: "",
    registry: null,
    projectHealthState: null,
    evidence: null,
    snapshot: null,
    contextIndex: null,
    contextAuditSnapshot: null,
    archiveItems: [],
    archiveSelected: 0,
    activeCategory: "context",
    feedRunning: true,
    feedTimer: null,
    feedPulseIndex: 0,
    obsActiveLane: "",
    obsSelectedModelId: "glm-cheap",
    obsRunType: "routine",
  };

  /* All visible dates/times/numbers are pinned to en-US or ISO-style output. */
  function pad2(value) {
    return String(value).padStart(2, "0");
  }

  function clockLabel(date) {
    return `${pad2(date.getHours())}:${pad2(date.getMinutes())}:${pad2(date.getSeconds())}`;
  }

  function formatInt(value) {
    return Number(value).toLocaleString("en-US");
  }

  /* Curated hue per category's procedural swatch — local, no image.
     Fixed mapping (not hash-derived) so hues stay distinct and inside the
     MellyCore violet/blue/cyan/magenta family, clear of the reserved
     semantic colors (green=verified, amber=caution, red=danger). */
  const CATEGORY_SWATCH_HUE = {
    context: 182,
    workflow: 200,
    safety: 218,
    observability: 236,
    model: 255,
    routing: 275,
    memory: 294,
    orchestration: 312,
  };
  function hueForCategory(category) {
    const hue = CATEGORY_SWATCH_HUE[category];
    return hue === undefined ? 260 : hue;
  }

  function escapeHTML(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  async function getText(path, options) {
    const response = await fetch(path, options);
    if (!response.ok) throw new Error(`GET ${path} → ${response.status}`);
    return response.text();
  }

  async function getJSON(path, options) {
    const response = await fetch(path, options);
    if (!response.ok) {
      let detail = "";
      try {
        const payload = await response.json();
        detail = payload.reason ? `: ${payload.reason}` : "";
      } catch (_error) {
        detail = "";
      }
      throw new Error(`GET ${path} → ${response.status}${detail}`);
    }
    return response.json();
  }

  async function findLatestEvidenceFile(loopId) {
    const directory = `/shared_context/loops/runs/${encodeURIComponent(loopId)}/`;
    const listing = await getText(directory);
    const files = Array.from(listing.matchAll(/href="([^"]+\.json)"/g)).map((match) => decodeURIComponent(match[1]));
    files.sort();
    return files.length ? directory + files[files.length - 1] : null;
  }

  function parseBulletList(markdown) {
    return markdown.split("\n").filter((line) => line.trim().startsWith("- ")).map((line) => line.trim().slice(2).trim());
  }

  function parseRunQueueTail(markdown, count) {
    return markdown.split("\n").filter((line) => /^\d+\.\s/.test(line.trim())).slice(-count).map((line) => line.trim());
  }

  function parseMilestone(markdown, name) {
    const heading = `### ${name}`;
    const start = markdown.indexOf(heading);
    if (start === -1) return [];
    const remaining = markdown.slice(start);
    const nextHeading = remaining.indexOf("\n### ", 1);
    const block = nextHeading === -1 ? remaining : remaining.slice(0, nextHeading);
    return parseBulletList(block);
  }

  const COMPLETED_BULLET_PATTERN = /\*\*completed|\*\*complete\b|\bcomplete\s*\(|\bcompleted\s*\(|\bcomplete\s+locally|\bcompleted\s+locally/i;

  function isCompletedRoadmapBullet(item) {
    return COMPLETED_BULLET_PATTERN.test(item);
  }

  function findRecommendedNextTask(runQueueText) {
    const matches = Array.from((runQueueText || "").matchAll(/Recommended next:\s*`([^`]+)`/g));
    return matches.length ? matches[matches.length - 1][1].trim() : null;
  }

  function activateTab(tabName, focus) {
    document.querySelectorAll(".dash-tab-btn").forEach((button) => {
      const selected = button.dataset.tab === tabName;
      button.setAttribute("aria-selected", String(selected));
      button.tabIndex = selected ? 0 : -1;
      if (selected && focus) button.focus();
    });
    document.querySelectorAll(".dash-panel").forEach((panel) => {
      panel.hidden = panel.id !== `tab-${tabName}`;
    });
    window.history.replaceState(null, "", `#${tabName}`);
  }

  function initTabs() {
    const buttons = Array.from(document.querySelectorAll(".dash-tab-btn"));
    buttons.forEach((button, index) => {
      button.addEventListener("click", () => activateTab(button.dataset.tab, false));
      button.addEventListener("keydown", (event) => {
        if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
        event.preventDefault();
        const direction = event.key === "ArrowRight" ? 1 : -1;
        const next = buttons[(index + direction + buttons.length) % buttons.length];
        activateTab(next.dataset.tab, true);
      });
    });
    const requested = window.location.hash.slice(1);
    activateTab(buttons.some((button) => button.dataset.tab === requested) ? requested : "source-arena", false);
  }

  function initClock() {
    const clock = document.getElementById("dash-clock");
    const tick = () => { clock.textContent = clockLabel(new Date()); };
    tick();
    window.setInterval(tick, 1000);
  }

  function contextAudit() {
    return state.contextAuditSnapshot ? (state.contextAuditSnapshot.audit || state.contextAuditSnapshot) : null;
  }

  function metricHTML(value, label, tone) {
    return `<div class="metric-cell metric-cell--${tone}"><strong>${escapeHTML(value)}</strong><span>${escapeHTML(label)}</span></div>`;
  }

  function contextMetricMarkup(audit) {
    if (!audit) return metricHTML("—", "audit", "warning");
    const counts = audit.counts || {};
    return [
      metricHTML((counts.valid_records || 0), "valid", "good"),
      metricHTML(((counts.by_decision || {}).admitted || 0), "admitted", "cyan"),
      metricHTML(((counts.by_decision || {}).rejected || 0), "rejected", "danger"),
      metricHTML(((counts.by_freshness || {}).expiring || 0), "expiring", "warning"),
      metricHTML(((counts.by_freshness || {}).stale || 0), "stale", "good"),
      metricHTML((audit.refusal_entries || 0), "refusals", "accent"),
      metricHTML((audit.finding_count || 0), "findings", "cyan"),
    ].join("");
  }

  function renderOverview() {
    const milestoneB = parseMilestone(state.roadmapText, "Milestone B — One Brain");
    document.getElementById("ov-milestone").textContent = "Milestone B — One Brain";

    const recommendedNext = findRecommendedNextTask(state.runQueueText);
    const pendingMilestoneBullet = milestoneB.find(
      (item) => /next|dashboard|cockpit/i.test(item) && !isCompletedRoadmapBullet(item)
    );
    const nextTaskText = recommendedNext
      ? `Recommended next: \`${recommendedNext}\``
      : pendingMilestoneBullet;
    document.getElementById("ov-next-task").textContent = nextTaskText
      ? nextTaskText.replace(/\*\*/g, "")
      : "No queued task — ready for review.";

    document.getElementById("ov-context-metrics").innerHTML = contextMetricMarkup(contextAudit());
    const audit = contextAudit();
    if (audit) {
      document.getElementById("mission-context-health").textContent = `${audit.counts.valid_records} valid · ${audit.finding_count} findings`;
    }

    const nodes = document.getElementById("ov-systemmap-nodes");
    nodes.innerHTML = state.registry.loops.map((loop) => {
      const disabled = loop.status === "DISABLED";
      return `<div class="loop-node${disabled ? " loop-node--disabled" : ""}"><strong>${escapeHTML(loop.title)}</strong><span>${disabled ? "disabled" : "validated"}</span></div>`;
    }).join("");

    const tests = state.snapshot.commands.tests;
    document.getElementById("ov-test-status").textContent = `${tests.passed} loop tests passed · captured ${state.snapshot.captured_at}`;
    document.getElementById("ov-safety-list").innerHTML = parseBulletList(state.safetyContractText).slice(0, 7).map((item) => `<li>${escapeHTML(item)}</li>`).join("");

    const history = state.projectHealthState.run_history || [];
    const latest = history[history.length - 1];
    document.getElementById("ov-evidence").innerHTML = latest
      ? `<strong>${escapeHTML(latest.run_id)}</strong> · ${escapeHTML(latest.outcome)} · finished ${escapeHTML(latest.finished_at)}`
      : "No persisted run evidence found.";
  }

  function freshnessForRecord(record, audit) {
    if (record.superseded_by) return { label: "superseded", cls: "freshness-tag" };
    if (!record.review_after) return { label: "immutable", cls: "freshness-tag freshness-tag--immutable" };
    const reviewDate = new Date(`${record.review_after}T00:00:00Z`);
    const asOf = new Date(`${audit.as_of}T00:00:00Z`);
    const days = Math.ceil((reviewDate - asOf) / 86400000);
    if (days < 0) return { label: "stale", cls: "freshness-tag freshness-tag--stale" };
    if (days <= (audit.expiring_window_days || 30)) return { label: "expiring", cls: "freshness-tag freshness-tag--expiring" };
    return { label: "fresh", cls: "freshness-tag freshness-tag--fresh" };
  }

  function renderContext() {
    const audit = contextAudit();
    const index = state.contextIndex;
    document.getElementById("context-metrics").innerHTML = contextMetricMarkup(audit);
    document.getElementById("context-index-state").textContent = `${escapeHTML(audit.index_status)} index · ${index.record_count} records`;
    const captured = state.contextAuditSnapshot.captured_at || audit.as_of;
    document.getElementById("context-audit-captured").textContent = `Audit snapshot · ${captured}`;

    const visibleRecords = index.records.filter((record) =>
      record.decision === "admitted" && ["public_display", "internal_summary_display"].includes(record.allowed_use)
    );
    document.getElementById("context-visible-count").textContent = `${visibleRecords.length} visible`;
    document.getElementById("context-records").innerHTML = visibleRecords.map((record) => {
      const freshness = freshnessForRecord(record, audit);
      return `<tr>
        <td>${escapeHTML(record.source_id)}</td>
        <td>${escapeHTML(record.source_type)}</td>
        <td><span class="trust-tag">${escapeHTML(record.trust_level)}</span></td>
        <td><span class="${freshness.cls}">${escapeHTML(freshness.label)}</span></td>
        <td><span class="decision-tag decision-tag--admitted">admitted</span></td>
      </tr>`;
    }).join("");

    const useCounts = index.records.reduce((counts, record) => {
      counts[record.allowed_use] = (counts[record.allowed_use] || 0) + 1;
      return counts;
    }, {});
    document.getElementById("context-use-counts").innerHTML = [
      ["public display", useCounts.public_display || 0],
      ["internal summary", useCounts.internal_summary_display || 0],
      ["reasoning only (counted)", useCounts.internal_reasoning_only || 0],
    ].map(([label, value]) => `<div><dt>${escapeHTML(label)}</dt><dd>${escapeHTML(value)}</dd></div>`).join("");

    const refusalEntries = Object.entries(audit.refusal_counts || {});
    document.getElementById("context-refusals").innerHTML = refusalEntries.length
      ? refusalEntries.map(([reason, count]) => `<li><span>${escapeHTML(reason)}</span><strong>${escapeHTML(count)}</strong></li>`).join("")
      : "<li>None recorded</li>";
  }

  function tierForLoop(loopId, loop) {
    if (loop.status === "DISABLED") return { label: "disabled", cls: "loop-tier loop-tier--disabled" };
    const tiers = state.snapshot.commands.audit.loop_tiers || [];
    const match = tiers.find((row) => row.loop_id === loopId);
    return { label: match ? match.highest_earned_tier : "configured", cls: "loop-tier" };
  }

  function renderLoops() {
    document.getElementById("loops-list").innerHTML = state.registry.loops.map((loop) => {
      const tier = tierForLoop(loop.id, loop);
      return `<details class="dash-details"><summary><span><strong>${escapeHTML(loop.title)}</strong><code>${escapeHTML(loop.id)}</code></span><span class="${tier.cls}">${escapeHTML(tier.label)}</span></summary><div class="dash-details-body"><p>${escapeHTML(loop.purpose)}</p><dl><dt>Level</dt><dd>${escapeHTML(loop.level)}</dd><dt>Status</dt><dd>${escapeHTML(loop.status)}</dd><dt>Trigger</dt><dd>${escapeHTML(loop.trigger_type)} · ${escapeHTML(loop.suggested_cadence)}</dd><dt>Read scope</dt><dd>${loop.read_scope.map(escapeHTML).join(", ")}</dd><dt>Write scope</dt><dd>${loop.allowed_write_scope.length ? loop.allowed_write_scope.map(escapeHTML).join(", ") : "none"}</dd><dt>Human gates</dt><dd>${loop.human_gates.map(escapeHTML).join(", ")}</dd></dl></div></details>`;
    }).join("");
  }

  function renderEvidence() {
    const target = document.getElementById("evidence-body");
    if (!state.evidence) {
      target.innerHTML = '<p class="dash-error-note">No persisted project-health evidence was found.</p>';
      return;
    }
    const ledger = state.evidence.ledger;
    const guard = state.evidence.guard_evaluation;
    const firstIteration = ledger.iterations[0];
    target.innerHTML = `<dl class="evidence-grid"><dt>Run ID</dt><dd><code>${escapeHTML(ledger.run_id)}</code></dd><dt>Outcome</dt><dd>${escapeHTML(ledger.outcome)}</dd><dt>Started / completed</dt><dd>${escapeHTML(ledger.started_at)} → ${escapeHTML(ledger.completed_at)}</dd><dt>Branch / HEAD</dt><dd>${escapeHTML(ledger.branch)} @ <code>${escapeHTML((ledger.head_sha || "").slice(0, 12))}</code></dd><dt>Guard decision</dt><dd>${escapeHTML(guard.decision)}</dd><dt>Budget checks</dt><dd>${escapeHTML(guard.checks.per_run_budget)} / ${escapeHTML(guard.checks.daily_budget)}</dd><dt>Tokens</dt><dd>${firstIteration && firstIteration.tokens.measured ? escapeHTML(firstIteration.tokens.total) : "null · unmeasured"}</dd><dt>Repository mutations</dt><dd>${escapeHTML(ledger.repository_mutation_count)}</dd><dt>Remote actions</dt><dd>${escapeHTML(ledger.remote_action_count)}</dd></dl>`;
  }

  function clampListItem(text) {
    const safe = escapeHTML(text);
    if (text.length <= 200) return `<li><div class="clamp-wrap"><span class="clamp-text">${safe}</span></div></li>`;
    return `<li><div class="clamp-wrap"><span class="clamp-text is-clamped">${safe}</span><button type="button" class="clamp-toggle" aria-expanded="false">Show more</button></div></li>`;
  }

  function initClampToggles(listId) {
    document.getElementById(listId).addEventListener("click", (event) => {
      const toggle = event.target.closest(".clamp-toggle");
      if (!toggle) return;
      const textNode = toggle.parentElement.querySelector(".clamp-text");
      const expanded = toggle.getAttribute("aria-expanded") === "true";
      textNode.classList.toggle("is-clamped", expanded);
      toggle.setAttribute("aria-expanded", String(!expanded));
      toggle.textContent = expanded ? "Show more" : "Show less";
    });
  }

  function renderRoadmap() {
    const milestone = parseMilestone(state.roadmapText, "Milestone B — One Brain");
    document.getElementById("roadmap-milestone").innerHTML = milestone.map((item) => clampListItem(item.replace(/\*\*/g, ""))).join("");
    document.getElementById("roadmap-queue").innerHTML = parseRunQueueTail(state.runQueueText, 8).map((item) => clampListItem(item)).join("");
  }

  function readArchiveForm() {
    const queryEl = document.getElementById("source-arena-query");
    const categoryEl = document.getElementById("source-arena-category");
    return {
      query: queryEl ? queryEl.value.trim() : "",
      category: categoryEl ? categoryEl.value : "",
    };
  }

  function filterArchiveRecords(values) {
    const query = (values.query || "").toLowerCase();
    const category = values.category || "";
    return ARCHIVE_RECORDS.filter((record) => {
      if (category && record.category !== category) return false;
      if (!query) return true;
      const haystack = `${record.title} ${record.description} ${record.category} ${(record.tags || []).join(" ")}`.toLowerCase();
      return haystack.includes(query);
    });
  }

  function renderArchiveEmpty(message) {
    const stage = document.getElementById("source-arena-stage");
    if (stage) stage.innerHTML = `<div class="media-stage-error"><strong>No records found</strong><span>${escapeHTML(message)}</span></div>`;
    const queue = document.getElementById("source-arena-queue");
    if (queue) queue.innerHTML = "";
    const dots = document.getElementById("source-arena-stage-dots");
    if (dots) dots.innerHTML = "";
    renderCompareSource();
  }

  function renderArchiveQueue() {
    const queue = document.getElementById("source-arena-queue");
    if (!queue) return;
    queue.innerHTML = state.archiveItems.map((item, index) => `<li class="source-arena-queue-item"><button type="button" class="source-arena-queue-button" data-arena-index="${index}" aria-current="${index === state.archiveSelected}"><span class="source-arena-queue-thumb" style="--swatch-hue:${hueForCategory(item.category)}" aria-hidden="true">${escapeHTML((item.category || "").slice(0, 2).toUpperCase())}</span><span class="source-arena-queue-copy"><strong>${escapeHTML(item.title)}</strong><span>${escapeHTML(item.category)} · ${escapeHTML(item.status)}</span></span></button></li>`).join("");
    queue.querySelectorAll("[data-arena-index]").forEach((button) => button.addEventListener("click", () => selectArchiveItem(Number(button.dataset.arenaIndex))));
  }

  function renderArchiveDots() {
    const dots = document.getElementById("source-arena-stage-dots");
    if (!dots) return;
    const limit = Math.min(state.archiveItems.length, 8);
    const buttons = Array.from({ length: limit }, (_value, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "stage-dot";
      button.dataset.stageIndex = String(index);
      button.setAttribute("aria-label", `Show source node ${index + 1}`);
      button.setAttribute("aria-current", String(index === state.archiveSelected));
      button.addEventListener("click", () => selectArchiveItem(index));
      return button;
    });
    dots.replaceChildren(...buttons);
  }

  /* Static holographic source map — a command-stage layout, not a feed.
     Each filtered local record is a source node orbiting a central core;
     the active node feeds a fixed inspector panel. Selection is by node,
     queue, dot, or stepper — never swipe-to-next-feed. All data is the
     local, deterministic Source Archive; no network, no engagement.
     Built via DOM APIs (not innerHTML): setAttribute/textContent never
     parse their input as markup, so record fields need no HTML-escaping
     here. */
  function buildArenaNodes(items, selected) {
    const total = items.length;
    const fragment = document.createDocumentFragment();
    items.forEach((item, index) => {
      const angle = total > 1 ? Math.round((index / total) * 360) : 0;
      const isActive = index === selected;
      const glyph = (item.category || "").slice(0, 2).toUpperCase();

      const button = document.createElement("button");
      button.type = "button";
      button.className = isActive ? "arena-node is-active" : "arena-node";
      button.dataset.arenaNode = String(index);
      button.style.setProperty("--node-angle", `${angle}deg`);
      button.style.setProperty("--swatch-hue", String(hueForCategory(item.category)));
      button.setAttribute("aria-pressed", String(isActive));
      button.setAttribute("aria-label", `Select source node ${index + 1} of ${total}: ${item.title}, ${item.category}`);
      button.addEventListener("click", () => selectArchiveItem(index));

      const dot = document.createElement("span");
      dot.className = "arena-node-dot";
      dot.setAttribute("aria-hidden", "true");
      dot.textContent = glyph;

      const tag = document.createElement("span");
      tag.className = "arena-node-tag";
      tag.textContent = item.category;

      button.append(dot, tag);
      fragment.append(button);
    });
    return fragment;
  }

  function buildArenaInspector(item, total) {
    const nodeWord = total === 1 ? "node" : "nodes";

    const root = document.createElement("div");
    root.className = "arena-inspector";

    const head = document.createElement("div");
    head.className = "arena-inspector-head";
    const origin = document.createElement("span");
    origin.className = "data-origin data-origin--local";
    origin.textContent = "Local source fixture";
    const mapLabel = document.createElement("span");
    mapLabel.className = "arena-inspector-map";
    mapLabel.textContent = `Static source map · ${total} ${nodeWord} · no network`;
    head.append(origin, mapLabel);

    const title = document.createElement("h2");
    title.className = "arena-inspector-title";
    title.textContent = item.title;

    const desc = document.createElement("p");
    desc.className = "arena-inspector-desc";
    desc.textContent = item.description;

    const tagsWrap = document.createElement("div");
    tagsWrap.className = "arena-inspector-tags";
    tagsWrap.setAttribute("aria-label", "Record tags");
    (item.tags || []).forEach((tag) => {
      const tagEl = document.createElement("span");
      tagEl.className = "arena-tag";
      tagEl.textContent = tag;
      tagsWrap.append(tagEl);
    });

    const fine = document.createElement("p");
    fine.className = "arena-inspector-fine";
    fine.textContent = `${item.category} · ${item.status} · source id ${item.id}`;

    root.append(head, title, desc, tagsWrap, fine);
    return root;
  }

  function renderArchiveStage() {
    const items = state.archiveItems;
    const item = items[state.archiveSelected];
    if (!item) return;
    const stage = document.getElementById("source-arena-stage");
    if (!stage) return;
    const total = items.length;
    const activeAngle = total > 1 ? Math.round((state.archiveSelected / total) * 360) : 0;
    const coreGlyph = (item.category || "").slice(0, 2).toUpperCase();

    const map = document.createElement("div");
    map.className = "arena-map";
    map.setAttribute("role", "group");
    map.setAttribute("aria-label", "Holographic source stage — static local source map");

    const scene = document.createElement("div");
    scene.className = "arena-map-scene";

    const orbit = document.createElement("span");
    orbit.className = "arena-orbit";
    orbit.setAttribute("aria-hidden", "true");

    const link = document.createElement("span");
    link.className = "arena-link";
    link.style.setProperty("--node-angle", `${activeAngle}deg`);
    link.setAttribute("aria-hidden", "true");

    const nodes = document.createElement("div");
    nodes.className = "arena-nodes";
    nodes.append(buildArenaNodes(items, state.archiveSelected));

    const core = document.createElement("div");
    core.className = "arena-core";
    core.style.setProperty("--swatch-hue", String(hueForCategory(item.category)));
    core.setAttribute("aria-hidden", "true");
    const coreRing = document.createElement("span");
    coreRing.className = "arena-core-ring";
    const coreGlyphEl = document.createElement("span");
    coreGlyphEl.className = "arena-core-glyph";
    coreGlyphEl.textContent = coreGlyph;
    core.append(coreRing, coreGlyphEl);

    scene.append(orbit, link, nodes, core);
    map.append(scene);

    stage.replaceChildren(map, buildArenaInspector(item, total));
    renderCompareSource();
    renderModelOutputs();
  }

  function renderCompareSource() {
    const target = document.getElementById("compare-source-card");
    if (!target) return;
    const item = state.archiveItems[state.archiveSelected];
    if (!item) {
      target.innerHTML = '<div class="compare-source-empty">No local record selected yet. Filter the Source Arena.</div>';
      return;
    }
    target.innerHTML = `<span class="compare-source-thumb compare-source-thumb--procedural" style="--swatch-hue:${hueForCategory(item.category)}" aria-hidden="true">${escapeHTML((item.category || "").slice(0, 2).toUpperCase())}</span>
      <div class="compare-source-copy">
        <div class="stage-meta-labels"><span class="data-origin data-origin--local">Local source fixture</span></div>
        <strong>${escapeHTML(item.title)}</strong>
        <span>${escapeHTML(item.category)} · ${escapeHTML(item.status)} · source id ${escapeHTML(item.id)}</span>
      </div>`;
  }

  function selectArchiveItem(index, options) {
    if (!state.archiveItems.length) return;
    const normalized = (index + state.archiveItems.length) % state.archiveItems.length;
    state.archiveSelected = normalized;
    if (!(options && options.skipQueueRender)) renderArchiveQueue();
    renderArchiveDots();
    renderArchiveStage();
  }

  function renderArchiveResults(options) {
    const opts = options || {};
    const errorEl = document.getElementById("source-arena-form-error");
    if (errorEl) errorEl.textContent = "";

    const values = readArchiveForm();
    state.archiveItems = filterArchiveRecords(values);
    state.archiveSelected = 0;
    renderArchiveQueue();
    renderArchiveDots();
    if (state.archiveItems.length) {
      selectArchiveItem(0, { skipQueueRender: true });
    } else {
      renderArchiveEmpty("No local records matched that filter. Try a broader query or clear the category.");
    }

    const resultCountEl = document.getElementById("source-arena-result-count");
    if (resultCountEl) resultCountEl.textContent = `${formatInt(state.archiveItems.length)} records`;
    const footerEl = document.getElementById("footer-system-state");
    if (footerEl) footerEl.innerHTML = "<i></i> Source Archive ready";
    if (!opts.preserveCategory) updateCategoryFromQuery(values.query);
  }

  function updateCategoryFromQuery(query) {
    const lower = (query || "").toLowerCase();
    if (!lower) return;
    const match = Object.entries(ARCHIVE_CATEGORIES).find(([id, category]) => lower.includes(id) || lower.includes(category.label.toLowerCase()));
    if (match) setActiveCategory(match[0], false);
  }

  function setActiveCategory(categoryId, runFilter) {
    if (!ARCHIVE_CATEGORIES[categoryId]) return;
    state.activeCategory = categoryId;
    document.querySelectorAll("[data-category]").forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.category === categoryId)));
    renderCompareCategorySelector();
    renderModelOutputs();
    if (runFilter) {
      const category = ARCHIVE_CATEGORIES[categoryId];
      const searchInput = document.getElementById("arena-search-input");
      if (searchInput) searchInput.value = category.label;
      const queryEl = document.getElementById("source-arena-query");
      const categoryEl = document.getElementById("source-arena-category");
      if (queryEl) queryEl.value = "";
      if (categoryEl) categoryEl.value = categoryId;
      renderArchiveResults({ preserveCategory: true });
    }
  }

  function modelCardMarkup(model) {
    const item = state.archiveItems[state.archiveSelected];
    const title = item ? item.title : `${ARCHIVE_CATEGORIES[state.activeCategory].label} records`;
    const text = MODEL_COPY[state.activeCategory][model.id];
    const timestamp = clockLabel(new Date());
    return `<article class="model-output-card" data-model-id="${model.id}" style="--model-accent:${model.color}"><div class="model-output-head"><strong>${model.name}</strong><span>Simulated model output</span></div><p>${escapeHTML(text)}</p><div class="model-output-foot"><span>Input label: ${escapeHTML(title)}</span><time>${escapeHTML(timestamp)}</time></div></article>`;
  }

  function renderModelOutputs() {
    const markup = MODEL_DEFS.map(modelCardMarkup).join("");
    document.getElementById("model-feed").innerHTML = markup;
    document.getElementById("compare-grid").innerHTML = markup;
    pulseModelCard();
  }

  function pulseModelCard() {
    document.querySelectorAll(".model-output-card").forEach((card) => card.classList.toggle("is-pulsing", card.dataset.modelId === MODEL_DEFS[state.feedPulseIndex].id));
  }

  function setFeedRunning(running) {
    state.feedRunning = running;
    document.getElementById("feed-toggle").textContent = running ? "Pause feed" : "Resume feed";
    document.getElementById("feed-toggle").setAttribute("aria-pressed", String(running));
    document.getElementById("compare-feed-toggle").textContent = running ? "Pause simulated feed" : "Resume simulated feed";
    document.getElementById("compare-feed-toggle").setAttribute("aria-pressed", String(running));
    document.getElementById("feed-state-label").textContent = running ? "Simulated feed active" : "Simulated feed paused";
    window.clearInterval(state.feedTimer);
    if (running) {
      state.feedTimer = window.setInterval(() => {
        state.feedPulseIndex = (state.feedPulseIndex + 1) % MODEL_DEFS.length;
        renderModelOutputs();
      }, 4200);
    }
  }

  function renderCompareCategorySelector() {
    const target = document.getElementById("compare-task-selector");
    if (!target) return;
    target.innerHTML = Object.entries(ARCHIVE_CATEGORIES).map(([id, category], index) => `<button type="button" class="task-button" data-category="${id}" aria-pressed="${id === state.activeCategory}"><span>0${index + 1}</span>${escapeHTML(category.label)}</button>`).join("");
    target.querySelectorAll("[data-category]").forEach((button) => button.addEventListener("click", () => setActiveCategory(button.dataset.category, true)));
  }

  function initArchiveInteractions() {
    const searchForm = document.getElementById("source-arena-search-form");
    if (searchForm) searchForm.addEventListener("submit", (event) => { event.preventDefault(); renderArchiveResults(); });

    const arenaForm = document.getElementById("arena-search-form");
    if (arenaForm) arenaForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const input = document.getElementById("arena-search-input");
      const query = input ? input.value.trim() : "";
      if (!query) return;
      const queryEl = document.getElementById("source-arena-query");
      const categoryEl = document.getElementById("source-arena-category");
      if (queryEl) queryEl.value = query;
      if (categoryEl) categoryEl.value = "";
      renderArchiveResults();
    });

    document.querySelectorAll(".mission-rail [data-category]").forEach((button) => button.addEventListener("click", () => setActiveCategory(button.dataset.category, true)));

    // Secondary stepper through source nodes (keyboard/pointer). Node clicks,
    // the queue, and the dot selector remain the primary selection paths —
    // there is deliberately no swipe/wheel "next feed" interaction.
    const prevItem = document.getElementById("source-arena-prev-item");
    if (prevItem) prevItem.addEventListener("click", () => selectArchiveItem(state.archiveSelected - 1));
    const nextItem = document.getElementById("source-arena-next-item");
    if (nextItem) nextItem.addEventListener("click", () => selectArchiveItem(state.archiveSelected + 1));
    document.getElementById("feed-toggle").addEventListener("click", () => setFeedRunning(!state.feedRunning));
    document.getElementById("compare-feed-toggle").addEventListener("click", () => setFeedRunning(!state.feedRunning));
  }

  function obsSafetyStripMarkup() {
    return OBS_SAFETY_LABELS.map((label) => `<span class="obs-safety-chip">${escapeHTML(label)}</span>`).join("");
  }

  function renderObsSafetyStrip() {
    const top = document.getElementById("obs-safety-strip-top");
    const estimator = document.getElementById("obs-safety-strip-estimator");
    const markup = obsSafetyStripMarkup();
    if (top) top.innerHTML = markup;
    if (estimator) estimator.innerHTML = markup;
  }

  function renderObsLaneFilter() {
    const target = document.getElementById("obs-lane-filter");
    if (!target) return;
    const lanesInUse = Array.from(new Set(OBS_MODEL_FIXTURE.models.map((model) => model.routing_lane)));
    const chips = ["", ...lanesInUse].map((laneId, index) => {
      const label = laneId ? OBS_LANES[laneId] : "All lanes";
      const pressed = state.obsActiveLane === laneId;
      return `<button type="button" class="task-button" data-obs-lane="${escapeHTML(laneId)}" aria-pressed="${pressed}"><span>${String(index).padStart(2, "0")}</span>${escapeHTML(label)}</button>`;
    }).join("");
    target.innerHTML = chips;
    target.querySelectorAll("[data-obs-lane]").forEach((button) => {
      button.addEventListener("click", () => setObsLaneFilter(button.dataset.obsLane));
    });
  }

  function setObsLaneFilter(laneId) {
    state.obsActiveLane = laneId || "";
    renderObsLaneFilter();
    renderObsModelGrid();
  }

  function obsModelCardMarkup(model) {
    const selected = model.model_id === state.obsSelectedModelId;
    const statusCls = model.status === "UNAVAILABLE" ? "obs-status--unavailable" : model.status === "PLANNED_ALIAS" ? "obs-status--alias" : "obs-status--unknown";
    const lane = OBS_LANES[model.routing_lane] || model.routing_lane;
    const label = `${model.display_name}, ${lane} lane, cost class ${model.cost_class}, status ${model.status}${selected ? ", selected" : ""}`;
    return `<button type="button" class="obs-model-card${selected ? " is-selected" : ""}" data-obs-model="${escapeHTML(model.model_id)}" aria-pressed="${selected}" aria-label="${escapeHTML(label)}">
        <span class="obs-model-card-head">
          <strong>${escapeHTML(model.display_name)}</strong>
          <span class="obs-cost-chip obs-cost-chip--${escapeHTML(model.cost_class)}">${escapeHTML(model.cost_class)}</span>
        </span>
        <span class="obs-model-lane">${escapeHTML(lane)}</span>
        <span class="obs-status-chip ${statusCls}">${escapeHTML(model.status)}</span>
      </button>`;
  }

  function renderObsModelGrid() {
    const target = document.getElementById("obs-model-grid");
    if (!target) return;
    const models = OBS_MODEL_FIXTURE.models.filter((model) => !state.obsActiveLane || model.routing_lane === state.obsActiveLane);
    target.innerHTML = models.length
      ? models.map(obsModelCardMarkup).join("")
      : '<p class="dash-source-note">No fixture model is assigned to this lane yet.</p>';
    target.querySelectorAll("[data-obs-model]").forEach((button) => {
      button.addEventListener("click", () => selectObsModel(button.dataset.obsModel));
    });
  }

  function selectObsModel(modelId) {
    if (!obsFindModel(modelId)) return;
    state.obsSelectedModelId = modelId;
    renderObsModelGrid();
    renderObsCostRadar();
    renderObsSelectedDetail();
    renderObsFallbackChain();
    renderObsRouteAdvisor();
    renderObsEstimatorResult();
    renderObsMatrix();
  }

  function obsRateLabel(rate, currency) {
    return rate == null ? "UNKNOWN" : `${rate.toLocaleString("en-US")} ${escapeHTML(currency || "USD")}/M`;
  }

  function renderObsCostRadar() {
    const target = document.getElementById("obs-cost-radar");
    if (!target) return;
    const model = obsFindModel(state.obsSelectedModelId);
    if (!model) { target.innerHTML = ""; return; }
    target.innerHTML = [
      metricHTML(model.cost_class, "cost class", model.cost_class === "UNKNOWN" ? "warning" : "accent"),
      metricHTML(obsRateLabel(model.input_cost_per_million, model.currency), "input rate", "cyan"),
      metricHTML(obsRateLabel(model.output_cost_per_million, model.currency), "output rate", "cyan"),
      metricHTML(model.context_window == null ? "UNKNOWN" : formatInt(model.context_window), "context window", "warning"),
      metricHTML(model.snapshot_date, "snapshot date", "good"),
    ].join("");
  }

  function renderObsSelectedDetail() {
    const target = document.getElementById("obs-selected-detail");
    if (!target) return;
    const model = obsFindModel(state.obsSelectedModelId);
    if (!model) { target.innerHTML = "<p class=\"dash-muted\">No model selected.</p>"; return; }
    target.innerHTML = `
      <h3 class="obs-selected-title">${escapeHTML(model.display_name)}</h3>
      <p class="obs-selected-provider">${escapeHTML(model.provider)}</p>
      <dl class="context-rule-list obs-selected-facts">
        <div><dt>Lane</dt><dd>${escapeHTML(OBS_LANES[model.routing_lane] || model.routing_lane)}</dd></div>
        <div><dt>Status</dt><dd>${escapeHTML(model.status)}</dd></div>
        <div><dt>Cost class</dt><dd>${escapeHTML(model.cost_class)}</dd></div>
      </dl>
      <p class="obs-selected-label">Best for</p>
      <ul class="dash-line-list">${model.best_for.map((item) => `<li>${escapeHTML(item)}</li>`).join("")}</ul>
      <p class="obs-selected-label">Avoid for</p>
      <ul class="dash-line-list">${model.avoid_for.map((item) => `<li>${escapeHTML(item)}</li>`).join("")}</ul>
      <p class="obs-source-note">${escapeHTML(model.source_note)}</p>
      <p class="obs-safety-note">${escapeHTML(model.safety_note)}</p>`;
  }

  function renderObsFallbackChain() {
    const target = document.getElementById("obs-fallback-chain");
    if (!target) return;
    const model = obsFindModel(state.obsSelectedModelId);
    if (!model) { target.innerHTML = ""; return; }
    const steps = [{ model_ref: model.model_id, reason: "Preferred model for the selected lane.", tradeoff: "None — this is the primary selection." }].concat(model.fallbacks || []);
    target.innerHTML = steps.map((step, index) => {
      const stepModel = obsFindModel(step.model_ref);
      const name = stepModel ? stepModel.display_name : step.model_ref;
      return `<li class="obs-fallback-step"><span class="obs-fallback-index">${index === 0 ? "Selected" : `Fallback ${index}`}</span><strong>${escapeHTML(name)}</strong><span class="obs-fallback-reason">${escapeHTML(step.reason)}</span>${index > 0 ? `<span class="obs-fallback-tradeoff">Trade-off: ${escapeHTML(step.tradeoff)}</span>` : ""}</li>`;
    }).join("");
  }

  function renderObsRunTypeSelector() {
    const target = document.getElementById("obs-runtype-selector");
    if (!target) return;
    target.innerHTML = Object.entries(OBS_RUN_TYPES).map(([id, runType], index) => {
      const pressed = state.obsRunType === id;
      return `<button type="button" class="task-button" data-obs-runtype="${id}" aria-pressed="${pressed}"><span>${String(index + 1).padStart(2, "0")}</span>${escapeHTML(runType.label)}</button>`;
    }).join("");
    target.querySelectorAll("[data-obs-runtype]").forEach((button) => {
      button.addEventListener("click", () => setObsRunType(button.dataset.obsRuntype));
    });
  }

  function setObsRunType(runType) {
    if (!OBS_RUN_TYPES[runType]) return;
    state.obsRunType = runType;
    renderObsRunTypeSelector();
    renderObsRouteAdvisor();
    renderObsEstimatorResult();
  }

  function obsCostRankOf(model) {
    return model && Object.prototype.hasOwnProperty.call(OBS_COST_CLASS_RANK, model.cost_class) ? OBS_COST_CLASS_RANK[model.cost_class] : null;
  }

  function obsFindCheaperAlternative(runType, model) {
    const rt = OBS_RUN_TYPES[runType];
    const selfRank = obsCostRankOf(model);
    if (selfRank == null) return null;
    const candidates = OBS_MODEL_FIXTURE.models.filter((candidate) => {
      if (candidate.model_id === model.model_id) return false;
      if (candidate.status === "UNAVAILABLE") return false;
      const rank = obsCostRankOf(candidate);
      if (rank == null || rank >= selfRank) return false;
      return (candidate.capabilities[rt.primaryCapability] || 0) >= 1;
    }).sort((left, right) => obsCostRankOf(left) - obsCostRankOf(right));
    return candidates[0] || null;
  }

  function obsPremiumSignal(runType, model) {
    if (!model) return "INSUFFICIENT_DATA";
    if (["UNKNOWN", "UNAVAILABLE", "PLANNED_ALIAS"].includes(model.status)) return "INSUFFICIENT_DATA";
    const rt = OBS_RUN_TYPES[runType];
    const cheaper = obsFindCheaperAlternative(runType, model);
    if (rt.lane === "visual_product_judge" || rt.lane === "security_architecture_review") {
      return cheaper ? "OPTIONAL" : "RECOMMENDED";
    }
    if (runType === "routine" || runType === "drafting") {
      return cheaper ? "NOT_JUSTIFIED" : "OPTIONAL";
    }
    return "OPTIONAL";
  }

  function renderObsRouteAdvisor() {
    const target = document.getElementById("obs-route-result");
    if (!target) return;
    const rt = OBS_RUN_TYPES[state.obsRunType];
    const laneModels = OBS_LANE_PRIMARY[rt.lane];
    const primary = laneModels ? obsFindModel(laneModels.primary) : null;
    const alt = laneModels ? obsFindModel(laneModels.alt) : null;
    if (!primary) {
      target.innerHTML = `<p class="dash-source-note">No fixture model owns the ${escapeHTML(OBS_LANES[rt.lane])} lane yet. Consult the fallback chain for a currently selected model.</p>`;
      return;
    }
    const caution = primary.status === "UNAVAILABLE"
      ? `<p class="obs-advisor-caution"><strong>Caution:</strong> ${escapeHTML(primary.display_name)} is currently <code>UNAVAILABLE</code>. Use the fallback chain instead of assuming this model can be called.</p>`
      : `<p class="obs-advisor-caution">Status: <code>${escapeHTML(primary.status)}</code> — treat as a reviewed fixture entry, not proof of live availability.</p>`;
    target.innerHTML = `
      <p class="obs-advisor-lane">Recommended lane: <strong>${escapeHTML(OBS_LANES[rt.lane])}</strong></p>
      <p class="obs-advisor-model">Recommended model: <strong>${escapeHTML(primary.display_name)}</strong>${alt ? ` · fallback: <strong>${escapeHTML(alt.display_name)}</strong>` : ""}</p>
      ${caution}
      <p class="dash-source-note">This is local policy guidance only. It never launches a run, chooses on your behalf, or represents approval.</p>
      <button type="button" class="cockpit-button cockpit-button--secondary obs-advisor-select" data-obs-model="${escapeHTML(primary.model_id)}">Inspect ${escapeHTML(primary.display_name)} below</button>`;
    const selectBtn = target.querySelector(".obs-advisor-select");
    if (selectBtn) selectBtn.addEventListener("click", () => selectObsModel(selectBtn.dataset.obsModel));
  }

  function readObsEstimatorForm() {
    const inputEl = document.getElementById("obs-input-tokens");
    const outputEl = document.getElementById("obs-output-tokens");
    const cacheEl = document.getElementById("obs-cache-tokens");
    const toNonNegativeInt = (el) => {
      const value = Math.trunc(Number(el && el.value));
      return Number.isFinite(value) && value >= 0 ? value : 0;
    };
    return {
      inputTokens: toNonNegativeInt(inputEl),
      outputTokens: toNonNegativeInt(outputEl),
      cacheTokens: toNonNegativeInt(cacheEl),
    };
  }

  /* Static approximate estimate only — spec §9.2. Never invents a rate;
     null input/output rate always yields a null estimate. */
  function computeObsEstimate(model, tokens) {
    const cacheTokens = Math.min(tokens.cacheTokens, tokens.inputTokens);
    const uncachedInput = tokens.inputTokens - cacheTokens;
    if (model.input_cost_per_million == null || model.output_cost_per_million == null) {
      return { estimatedCost: null, note: "INSUFFICIENT PRICING DATA" };
    }
    let cacheNote = null;
    let cacheRate = model.cache_read_cost_per_million;
    if (cacheTokens > 0 && cacheRate == null) {
      cacheRate = model.input_cost_per_million;
      cacheNote = "CACHE_RATE_UNKNOWN_ASSUMED_INPUT_RATE";
    }
    const inputEstimate = (uncachedInput / 1000000) * model.input_cost_per_million;
    const cacheEstimate = cacheRate == null ? 0 : (cacheTokens / 1000000) * cacheRate;
    const outputEstimate = (tokens.outputTokens / 1000000) * model.output_cost_per_million;
    return { estimatedCost: inputEstimate + cacheEstimate + outputEstimate, note: cacheNote };
  }

  function renderObsEstimatorResult() {
    const target = document.getElementById("obs-estimator-result");
    if (!target) return;
    const model = obsFindModel(state.obsSelectedModelId);
    if (!model) { target.innerHTML = ""; return; }
    const tokens = readObsEstimatorForm();
    const estimate = computeObsEstimate(model, tokens);
    const cheaper = obsFindCheaperAlternative(state.obsRunType, model);
    const signal = obsPremiumSignal(state.obsRunType, model);
    const costLine = estimate.estimatedCost == null
      ? `<strong class="obs-estimate-unknown">INSUFFICIENT PRICING DATA</strong>`
      : `<strong class="obs-estimate-value">${estimate.estimatedCost.toFixed(4)} ${escapeHTML(model.currency || "USD")}</strong>`;
    target.innerHTML = `
      <div class="obs-estimate-line">${costLine}${estimate.note ? `<span class="obs-estimate-note">${escapeHTML(estimate.note)}</span>` : ""}</div>
      <dl class="context-rule-list obs-estimate-facts">
        <div><dt>Cheaper alternative</dt><dd>${cheaper ? escapeHTML(cheaper.display_name) : "NO REVIEWED CHEAPER ALTERNATIVE"}</dd></div>
        <div><dt>Worth premium model?</dt><dd><span class="obs-signal-chip obs-signal--${signal}">${escapeHTML(signal)}</span></dd></div>
        <div><dt>Snapshot date</dt><dd>${escapeHTML(model.snapshot_date)}</dd></div>
      </dl>
      <p class="obs-estimate-fine">Static approximate estimate — not account billing. Assumptions: representative per-million-token rates from the local fixture only; no tax, provider fee, retry, tool-call, image, or audio adjustment is modeled.</p>`;
  }

  function obsMatrixRowMarkup(model) {
    return `<tr>
      <th scope="row">${escapeHTML(model.display_name)}</th>
      ${OBS_CAPABILITY_FIELDS.map(([field]) => {
        const level = obsCapabilityLabel(model.capabilities[field] || 0);
        return `<td><span class="obs-cap-chip ${level.cls}">${escapeHTML(level.label)}</span></td>`;
      }).join("")}
    </tr>`;
  }

  function renderObsMatrix() {
    const target = document.getElementById("obs-matrix-body");
    if (!target) return;
    const selected = obsFindModel(state.obsSelectedModelId);
    const lane = selected ? selected.routing_lane : null;
    const rows = OBS_MODEL_FIXTURE.models.filter((model) => !lane || model.routing_lane === lane || model.model_id === state.obsSelectedModelId);
    target.innerHTML = rows.map(obsMatrixRowMarkup).join("");
  }

  function initObsInteractions() {
    const form = document.getElementById("obs-estimator-form");
    if (form) form.addEventListener("input", () => renderObsEstimatorResult());
  }

  function renderObservatory() {
    renderObsSafetyStrip();
    renderObsLaneFilter();
    renderObsModelGrid();
    renderObsCostRadar();
    renderObsSelectedDetail();
    renderObsRunTypeSelector();
    renderObsRouteAdvisor();
    renderObsEstimatorResult();
    renderObsMatrix();
    renderObsFallbackChain();
  }

  async function loadLocalData() {
    const [roadmapText, runQueueText, safetyContractText, registry, projectHealthState, snapshot, contextIndex, contextAuditSnapshot] = await Promise.all([
      getText("/shared_context/ROADMAP.md"),
      getText("/shared_context/RUN_QUEUE.md"),
      getText("/shared_context/SAFETY_CONTRACT.md"),
      getJSON("/shared_context/loops/LOOP_REGISTRY.json"),
      getJSON("/shared_context/loops/states/project-health.state.json"),
      getJSON("/site/data/dashboard_snapshot.json"),
      getJSON("/shared_context/context_provenance/INDEX.json"),
      getJSON("/site/data/context_audit_snapshot.json"),
    ]);
    Object.assign(state, { roadmapText, runQueueText, safetyContractText, registry, projectHealthState, snapshot, contextIndex, contextAuditSnapshot });
    try {
      const evidencePath = await findLatestEvidenceFile("project-health");
      state.evidence = evidencePath ? await getJSON(evidencePath) : null;
    } catch (error) {
      console.warn("Evidence read unavailable:", error);
      state.evidence = null;
    }
  }

  async function boot() {
    initTabs();
    initClock();
    initArchiveInteractions();
    renderCompareCategorySelector();
    renderModelOutputs();
    setFeedRunning(true);

    initObsInteractions();
    renderObservatory();

    initClampToggles("roadmap-milestone");
    initClampToggles("roadmap-queue");

    try {
      await loadLocalData();
      renderOverview();
      renderContext();
      renderLoops();
      renderEvidence();
      renderRoadmap();
    } catch (error) {
      console.error(error);
      document.getElementById("dash-main").insertAdjacentHTML("afterbegin", `<p class="dash-error-note">Local cockpit data failed to load: ${escapeHTML(error.message)}. Serve this page from the repository root at 127.0.0.1.</p>`);
    }

    renderArchiveResults({ preserveCategory: true });
  }

  document.addEventListener("DOMContentLoaded", boot);
})();
