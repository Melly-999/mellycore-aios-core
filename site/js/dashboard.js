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
    likedIds: new Set(),
    savedIds: new Set(),
    inspectOpen: false,
    shareState: "",
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

  /* Deterministic demo engagement numbers — clearly labeled, never real. */
  function demoCount(seed, base, spread) {
    let hash = 0;
    for (let i = 0; i < seed.length; i += 1) hash = (hash * 31 + seed.charCodeAt(i)) >>> 0;
    return base + (hash % spread);
  }

  /* Deterministic hue for a category's procedural swatch — local, no image. */
  function hueForCategory(category) {
    let hash = 0;
    const text = String(category || "");
    for (let i = 0; i < text.length; i += 1) hash = (hash * 31 + text.charCodeAt(i)) >>> 0;
    return hash % 360;
  }

  function shortCount(value) {
    return value >= 1000 ? `${(value / 1000).toFixed(1)}K` : String(value);
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
    dots.innerHTML = Array.from({ length: limit }, (_value, index) => `<button type="button" class="stage-dot" data-stage-index="${index}" aria-label="Show source result ${index + 1}" aria-current="${index === state.archiveSelected}"></button>`).join("");
    dots.querySelectorAll("[data-stage-index]").forEach((button) => button.addEventListener("click", () => selectArchiveItem(Number(button.dataset.stageIndex))));
  }

  function stageMediaMarkup(item) {
    const hue = hueForCategory(item.category);
    return `<div class="stage-media stage-media--procedural" style="--swatch-hue:${hue}" role="img" aria-label="${escapeHTML(item.category)} category swatch"><span class="stage-media-glyph">${escapeHTML((item.category || "").slice(0, 2).toUpperCase())}</span></div>`;
  }

  function stageActionsMarkup(item) {
    const liked = state.likedIds.has(item.id);
    const saved = state.savedIds.has(item.id);
    const likeCount = demoCount(`${item.id}:like`, 240, 8600) + (liked ? 1 : 0);
    const saveCount = demoCount(`${item.id}:save`, 30, 940) + (saved ? 1 : 0);
    const shareLabel = state.shareState === "copied" ? "Copied" : state.shareState === "failed" ? "Link" : "Share";
    return `<div class="stage-actions" aria-label="Arena actions — demo counts, not real engagement">
      <div class="stage-action-group"><button type="button" class="stage-action" data-stage-action="like" aria-pressed="${liked}" aria-label="Like (demo count)">♥</button><span>${shortCount(likeCount)}</span></div>
      <div class="stage-action-group"><button type="button" class="stage-action" data-stage-action="inspect" aria-pressed="${state.inspectOpen}" aria-label="Inspect source metadata">◉</button><span>Inspect</span></div>
      <div class="stage-action-group"><button type="button" class="stage-action" data-stage-action="save" aria-pressed="${saved}" aria-label="Save locally (demo count)">⬢</button><span>${shortCount(saveCount)}</span></div>
      <div class="stage-action-group"><button type="button" class="stage-action" data-stage-action="share" aria-pressed="false" aria-label="Copy local source link">➦</button><span>${escapeHTML(shareLabel)}</span></div>
      <span class="stage-actions-note">Demo counts</span>
    </div>`;
  }

  function stageCaptionMarkup(item) {
    const description = state.inspectOpen
      ? `<p class="stage-desc"><span class="stage-desc-label">Local record description</span>${escapeHTML(item.description)}</p>`
      : "";
    const shareNote = state.shareState === "failed" ? `<p class="stage-share-note">Local reference: #source-arena-${escapeHTML(item.id)}</p>` : "";
    const tags = (item.tags || []).map((tag) => `#${escapeHTML(tag)}`).join(" ");
    return `<div class="stage-meta">
      <div class="stage-meta-labels"><span class="data-origin data-origin--local">Local source fixture</span></div>
      <strong class="stage-handle">@mellycore-source-archive</strong>
      <h2>${escapeHTML(item.title)}</h2>
      <p class="stage-caption">${escapeHTML(item.description)}</p>
      ${description}${shareNote}
      <p class="stage-tags">${tags}</p>
      <p class="stage-fine">${escapeHTML(item.category)} · ${escapeHTML(item.status)} · source id ${escapeHTML(item.id)}</p>
    </div>`;
  }

  function handleStageAction(action, item) {
    if (action === "like") {
      state.likedIds.has(item.id) ? state.likedIds.delete(item.id) : state.likedIds.add(item.id);
    } else if (action === "save") {
      state.savedIds.has(item.id) ? state.savedIds.delete(item.id) : state.savedIds.add(item.id);
    } else if (action === "inspect") {
      state.inspectOpen = !state.inspectOpen;
    } else if (action === "share") {
      const localRef = `${window.location.origin}${window.location.pathname}#source-arena-${item.id}`;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(localRef).then(
          () => { state.shareState = "copied"; renderArchiveStage(); },
          () => { state.shareState = "failed"; renderArchiveStage(); }
        );
        return;
      }
      state.shareState = "failed";
    }
    renderArchiveStage();
  }

  function renderArchiveStage() {
    const item = state.archiveItems[state.archiveSelected];
    if (!item) return;
    const stage = document.getElementById("source-arena-stage");
    if (!stage) return;
    stage.innerHTML = `${stageMediaMarkup(item)}${stageActionsMarkup(item)}${stageCaptionMarkup(item)}`;
    stage.querySelectorAll("[data-stage-action]").forEach((button) => {
      button.addEventListener("click", (event) => {
        event.stopPropagation();
        handleStageAction(button.dataset.stageAction, item);
      });
    });
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
    if (normalized !== state.archiveSelected) state.shareState = "";
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

    const prevItem = document.getElementById("source-arena-prev-item");
    if (prevItem) prevItem.addEventListener("click", () => selectArchiveItem(state.archiveSelected - 1));
    const nextItem = document.getElementById("source-arena-next-item");
    if (nextItem) nextItem.addEventListener("click", () => selectArchiveItem(state.archiveSelected + 1));
    document.getElementById("feed-toggle").addEventListener("click", () => setFeedRunning(!state.feedRunning));
    document.getElementById("compare-feed-toggle").addEventListener("click", () => setFeedRunning(!state.feedRunning));

    const stage = document.getElementById("source-arena-stage");
    if (stage) {
      let wheelLocked = false;
      stage.addEventListener("wheel", (event) => {
        if (Math.abs(event.deltaY) < 18 || wheelLocked) return;
        event.preventDefault();
        wheelLocked = true;
        selectArchiveItem(state.archiveSelected + (event.deltaY > 0 ? 1 : -1));
        window.setTimeout(() => { wheelLocked = false; }, 450);
      }, { passive: false });

      let touchY = null;
      stage.addEventListener("touchstart", (event) => { touchY = event.changedTouches[0].clientY; }, { passive: true });
      stage.addEventListener("touchend", (event) => {
        if (touchY == null) return;
        const delta = touchY - event.changedTouches[0].clientY;
        if (Math.abs(delta) > 44) selectArchiveItem(state.archiveSelected + (delta > 0 ? 1 : -1));
        touchY = null;
      }, { passive: true });
    }
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
