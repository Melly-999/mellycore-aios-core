/*
 * MellyCore AIOS — Live Cockpit V2.
 *
 * Local committed data is fetched read-only from shared_context/**.
 * NASA media is fetched from the public, keyless Images API.
 * Model comparison text is deterministic local mock copy and is labeled
 * SIMULATED MODEL OUTPUT wherever it appears. No provider is called.
 */

(function () {
  "use strict";

  const NASA_API_ROOT = "https://images-api.nasa.gov";
  const TASKS = {
    apollo: { label: "Apollo", q: "Apollo 11", mediaType: "image", yearStart: "1968", yearEnd: "1972" },
    asteroid: { label: "Asteroid", q: "asteroid", mediaType: "image", yearStart: "", yearEnd: "" },
    "solar-flare": { label: "Solar flare", q: "solar flare", mediaType: "image", yearStart: "", yearEnd: "" },
    aurora: { label: "Aurora", q: "aurora", mediaType: "image", yearStart: "", yearEnd: "" },
    mars: { label: "Mars", q: "Mars", mediaType: "image", yearStart: "", yearEnd: "" },
  };

  const MODEL_DEFS = [
    { id: "fable", name: "Fable 5", color: "#a86cff" },
    { id: "opus", name: "Opus", color: "#35d7f2" },
    { id: "gpt", name: "GPT", color: "#58e68a" },
    { id: "glm", name: "GLM", color: "#ffc34d" },
  ];

  const MODEL_COPY = {
    apollo: {
      fable: "Cinematic mission framing: lunar exploration, human scale, and the texture of an archival moment. This is a scripted interface sample, not generated analysis.",
      opus: "Architecture lens: identify mission, capture date, NASA center, and media type before interpreting the selected asset. Mock response only.",
      gpt: "Context synthesis lens: connect the selected Apollo artifact to the broader mission while preserving the NASA record as the source of truth. Simulated output.",
      glm: "Fast exploration lens: summarize the visible mission theme and propose adjacent NASA searches. No provider request was sent.",
    },
    asteroid: {
      fable: "Story lens: frame scale, motion, and uncertainty without turning scientific imagery into spectacle. Scripted mock copy.",
      opus: "Evidence lens: separate observed media metadata from any inference about asteroid composition or trajectory. Simulated output.",
      gpt: "Synthesis lens: explain why asteroid imagery may combine observations, models, or mission documentation. Mock response only.",
      glm: "Exploration lens: branch toward near-Earth objects, impact studies, and spacecraft encounters. No model was called.",
    },
    "solar-flare": {
      fable: "Visual lens: emphasize eruptive form and scale while keeping the NASA asset label primary. Deterministic mock output.",
      opus: "Scientific caution lens: do not infer event class, intensity, or terrestrial impact from an image alone. Simulated response.",
      gpt: "Context lens: place solar activity beside space-weather monitoring without claiming a live forecast. Mock response only.",
      glm: "Discovery lens: suggest coronal mass ejection and solar observatory searches. No provider connection exists.",
    },
    aurora: {
      fable: "Atmospheric story lens: color, motion, and the meeting point between solar activity and Earth. Scripted sample.",
      opus: "Source lens: distinguish orbital, ground, and illustration media before interpretation. Simulated output.",
      gpt: "Educational lens: relate auroral light to charged particles and the upper atmosphere, without treating mock copy as a NASA claim.",
      glm: "Exploration lens: branch toward ISS aurora, geomagnetic storms, and polar observations. No request was sent.",
    },
    mars: {
      fable: "Planetary story lens: terrain, distance, and exploration as a visual narrative. Deterministic mock output.",
      opus: "Mission lens: identify rover, orbiter, or archival source before asserting what the media depicts. Simulated response.",
      gpt: "Context lens: connect the selected asset to Mars exploration while preserving metadata boundaries. Mock response only.",
      glm: "Discovery lens: propose surface, atmosphere, rover, and orbital-imagery follow-ups. No model was called.",
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
    nasaItems: [],
    nasaTotal: 0,
    nasaSelected: 0,
    nasaManifestCache: new Map(),
    nasaRequest: null,
    activeTask: "apollo",
    feedRunning: true,
    feedTimer: null,
    feedPulseIndex: 0,
  };

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
    activateTab(buttons.some((button) => button.dataset.tab === requested) ? requested : "nasa", false);
  }

  function initClock() {
    const clock = document.getElementById("dash-clock");
    const tick = () => { clock.textContent = new Date().toLocaleTimeString([], { hour12: false }); };
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
    const next = milestoneB.find((item) => /next|dashboard|cockpit/i.test(item));
    const queue = parseRunQueueTail(state.runQueueText, 1)[0];
    document.getElementById("ov-next-task").textContent = (next || queue || "No queued task found.").replace(/\*\*/g, "");

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

  function renderRoadmap() {
    const milestone = parseMilestone(state.roadmapText, "Milestone B — One Brain");
    document.getElementById("roadmap-milestone").innerHTML = milestone.map((item) => `<li>${escapeHTML(item.replace(/\*\*/g, ""))}</li>`).join("");
    document.getElementById("roadmap-queue").innerHTML = parseRunQueueTail(state.runQueueText, 8).map((item) => `<li>${escapeHTML(item)}</li>`).join("");
  }

  function readNasaForm() {
    const q = document.getElementById("nasa-q").value.trim();
    const yearStart = document.getElementById("nasa-year-start").value.trim();
    const yearEnd = document.getElementById("nasa-year-end").value.trim();
    const page = Number(document.getElementById("nasa-page").value);
    const pageSize = Number(document.getElementById("nasa-page-size").value);
    if (!q) throw new Error("Enter a search term (q). NASA requires at least one search parameter.");
    if (yearStart && !/^\d{4}$/.test(yearStart)) throw new Error("year_start must use YYYY format.");
    if (yearEnd && !/^\d{4}$/.test(yearEnd)) throw new Error("year_end must use YYYY format.");
    if (yearStart && yearEnd && Number(yearStart) > Number(yearEnd)) throw new Error("year_start cannot be later than year_end.");
    if (!Number.isInteger(page) || page < 1) throw new Error("page must be 1 or greater.");
    if (![8, 12, 24, 48].includes(pageSize)) throw new Error("Choose a supported page_size.");
    return { q, mediaType: document.getElementById("nasa-media-type").value, yearStart, yearEnd, page, pageSize };
  }

  function buildNasaSearchURL(values) {
    const params = new URLSearchParams();
    params.set("q", values.q);
    params.set("media_type", values.mediaType);
    if (values.yearStart) params.set("year_start", values.yearStart);
    if (values.yearEnd) params.set("year_end", values.yearEnd);
    params.set("page", String(values.page));
    params.set("page_size", String(values.pageSize));
    return `${NASA_API_ROOT}/search?${params.toString()}`;
  }

  function normalizeNasaItem(item) {
    const data = (item.data || [])[0] || {};
    const previewLink = (item.links || []).find((link) => link.rel === "preview" || link.render === "image");
    return {
      nasaId: data.nasa_id || "unknown",
      title: data.title || "Untitled NASA media",
      description: data.description || "",
      dateCreated: data.date_created || "",
      mediaType: data.media_type || "unknown",
      center: data.center || "NASA",
      preview: previewLink ? previewLink.href : "",
      manifestHref: item.href || "",
      assetHref: "",
      manifestState: "pending",
    };
  }

  function dateLabel(value) {
    if (!value) return "Date unavailable";
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? value : date.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
  }

  async function searchNasa(options) {
    const opts = options || {};
    const error = document.getElementById("nasa-form-error");
    error.textContent = "";
    let values;
    try {
      values = readNasaForm();
    } catch (formError) {
      error.textContent = formError.message;
      return;
    }

    if (state.nasaRequest) state.nasaRequest.abort();
    const controller = new AbortController();
    state.nasaRequest = controller;
    document.getElementById("footer-system-state").innerHTML = "<i></i> NASA request active";
    document.getElementById("nasa-result-count").textContent = "Loading";
    document.getElementById("nasa-stage").innerHTML = '<div class="media-stage-loading"><span class="stage-scan" aria-hidden="true"></span><strong>Searching NASA Images API…</strong><span>Public request · no API key</span></div>';

    try {
      const payload = await getJSON(buildNasaSearchURL(values), { signal: controller.signal });
      const collection = payload.collection || {};
      state.nasaItems = (collection.items || []).map(normalizeNasaItem);
      state.nasaTotal = (collection.metadata || {}).total_hits || state.nasaItems.length;
      state.nasaSelected = 0;
      renderNasaQueue();
      renderNasaDots();
      if (state.nasaItems.length) {
        await selectNasaItem(0, { skipQueueRender: true });
      } else {
        renderNasaEmpty("NASA returned no matching media. Try a broader query or remove the year range.");
      }
      document.getElementById("nasa-result-count").textContent = `${state.nasaTotal.toLocaleString()} hits`;
      document.getElementById("nasa-page-label").textContent = `Page ${values.page}`;
      document.getElementById("nasa-prev-page").disabled = values.page <= 1;
      document.getElementById("nasa-next-page").disabled = state.nasaItems.length < values.pageSize;
      document.getElementById("footer-system-state").innerHTML = "<i></i> NASA data loaded";
      if (!opts.preserveTask) updateTaskFromQuery(values.q);
    } catch (requestError) {
      if (requestError.name === "AbortError") return;
      error.textContent = `NASA request unavailable: ${requestError.message}`;
      renderNasaEmpty("The public NASA service could not be reached. Local cockpit data remains available.", true);
      document.getElementById("nasa-result-count").textContent = "Unavailable";
      document.getElementById("footer-system-state").innerHTML = "<i></i> Local data ready";
    } finally {
      if (state.nasaRequest === controller) state.nasaRequest = null;
    }
  }

  function renderNasaEmpty(message, isError) {
    document.getElementById("nasa-stage").innerHTML = `<div class="media-stage-error"><strong>${isError ? "NASA feed unavailable" : "No media found"}</strong><span>${escapeHTML(message)}</span></div>`;
    document.getElementById("nasa-queue").innerHTML = "";
    document.getElementById("nasa-stage-dots").innerHTML = "";
  }

  function renderNasaQueue() {
    document.getElementById("nasa-queue").innerHTML = state.nasaItems.map((item, index) => `<li class="nasa-queue-item"><button type="button" class="nasa-queue-button" data-nasa-index="${index}" aria-current="${index === state.nasaSelected}">${item.preview ? `<img class="nasa-queue-thumb" src="${escapeHTML(item.preview)}" alt="" loading="lazy">` : '<span class="nasa-queue-thumb"></span>'}<span class="nasa-queue-copy"><strong>${escapeHTML(item.title)}</strong><span>${escapeHTML(item.mediaType)} · ${escapeHTML(dateLabel(item.dateCreated))}</span></span></button></li>`).join("");
    document.querySelectorAll("[data-nasa-index]").forEach((button) => button.addEventListener("click", () => selectNasaItem(Number(button.dataset.nasaIndex))));
  }

  function renderNasaDots() {
    const limit = Math.min(state.nasaItems.length, 8);
    document.getElementById("nasa-stage-dots").innerHTML = Array.from({ length: limit }, (_value, index) => `<button type="button" class="stage-dot" data-stage-index="${index}" aria-label="Show NASA result ${index + 1}" aria-current="${index === state.nasaSelected}"></button>`).join("");
    document.querySelectorAll("[data-stage-index]").forEach((button) => button.addEventListener("click", () => selectNasaItem(Number(button.dataset.stageIndex))));
  }

  function chooseManifestAsset(manifestItems, mediaType) {
    const hrefs = manifestItems.map((item) => item.href).filter(Boolean);
    const patterns = {
      image: [/~medium\.(jpg|jpeg|png|webp)$/i, /~large\.(jpg|jpeg|png|webp)$/i, /\.(jpg|jpeg|png|webp)$/i],
      video: [/~medium\.mp4$/i, /\.mp4$/i, /\.(webm|mov)$/i],
      audio: [/\.mp3$/i, /\.(m4a|wav|ogg)$/i],
    };
    const candidates = patterns[mediaType] || patterns.image;
    for (const pattern of candidates) {
      const match = hrefs.find((href) => pattern.test(href) && !/metadata\.json$/i.test(href));
      if (match) return match;
    }
    return "";
  }

  async function resolveManifest(item) {
    if (state.nasaManifestCache.has(item.nasaId)) return state.nasaManifestCache.get(item.nasaId);
    const url = `${NASA_API_ROOT}/asset/${encodeURIComponent(item.nasaId)}`;
    const payload = await getJSON(url);
    const href = chooseManifestAsset(((payload.collection || {}).items || []), item.mediaType);
    state.nasaManifestCache.set(item.nasaId, href);
    return href;
  }

  function stageMediaMarkup(item) {
    const source = item.assetHref || item.preview;
    if (item.mediaType === "video" && item.assetHref) {
      return `<video class="stage-media stage-media--video" src="${escapeHTML(item.assetHref)}" poster="${escapeHTML(item.preview)}" controls preload="metadata"></video>`;
    }
    if (item.mediaType === "audio" && item.assetHref) {
      const style = item.preview ? ` style="background-image:url('${escapeHTML(item.preview)}')"` : "";
      return `<div class="stage-audio"${style}><audio src="${escapeHTML(item.assetHref)}" controls preload="metadata"></audio></div>`;
    }
    if (source) return `<img class="stage-media" src="${escapeHTML(source)}" alt="${escapeHTML(item.title)}">`;
    return '<div class="media-stage-error"><strong>Preview unavailable</strong><span>The NASA manifest has no compatible browser media file.</span></div>';
  }

  function renderNasaStage() {
    const item = state.nasaItems[state.nasaSelected];
    if (!item) return;
    const manifestLabel = item.manifestState === "resolved" ? "manifest resolved" : item.manifestState === "failed" ? "preview fallback" : "resolving manifest";
    document.getElementById("nasa-stage").innerHTML = `${stageMediaMarkup(item)}<span class="stage-media-type">${escapeHTML(item.mediaType)}</span><div class="stage-meta"><span class="data-origin data-origin--nasa">Real NASA data <span class="stage-manifest-state">${escapeHTML(manifestLabel)}</span></span><h2>${escapeHTML(item.title)}</h2><p>${escapeHTML(item.center)} · ${escapeHTML(dateLabel(item.dateCreated))} · NASA ID ${escapeHTML(item.nasaId)}</p></div>`;
    document.getElementById("compare-source-title").textContent = item.title;
    renderModelOutputs();
  }

  async function selectNasaItem(index, options) {
    if (!state.nasaItems.length) return;
    const normalized = (index + state.nasaItems.length) % state.nasaItems.length;
    state.nasaSelected = normalized;
    if (!(options && options.skipQueueRender)) renderNasaQueue();
    renderNasaDots();
    const item = state.nasaItems[normalized];
    renderNasaStage();
    if (item.manifestState !== "pending") return;
    try {
      item.assetHref = await resolveManifest(item);
      item.manifestState = item.assetHref ? "resolved" : "failed";
    } catch (_error) {
      item.manifestState = "failed";
    }
    if (state.nasaItems[state.nasaSelected] === item) renderNasaStage();
  }

  function updateTaskFromQuery(query) {
    const lower = query.toLowerCase();
    const match = Object.entries(TASKS).find(([_id, task]) => lower.includes(task.q.toLowerCase()) || lower.includes(task.label.toLowerCase()));
    if (match) setActiveTask(match[0], false);
  }

  function setActiveTask(taskId, runSearch) {
    if (!TASKS[taskId]) return;
    state.activeTask = taskId;
    document.querySelectorAll("[data-task]").forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.task === taskId)));
    renderCompareTaskSelector();
    renderModelOutputs();
    if (runSearch) {
      const task = TASKS[taskId];
      document.getElementById("nasa-q").value = task.q;
      document.getElementById("nasa-media-type").value = task.mediaType;
      document.getElementById("nasa-year-start").value = task.yearStart;
      document.getElementById("nasa-year-end").value = task.yearEnd;
      document.getElementById("nasa-page").value = "1";
      searchNasa({ preserveTask: true });
    }
  }

  function modelCardMarkup(model) {
    const item = state.nasaItems[state.nasaSelected];
    const title = item ? item.title : `${TASKS[state.activeTask].label} search`;
    const text = MODEL_COPY[state.activeTask][model.id];
    const timestamp = new Date().toLocaleTimeString([], { hour12: false });
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

  function renderCompareTaskSelector() {
    document.getElementById("compare-task-selector").innerHTML = Object.entries(TASKS).map(([id, task], index) => `<button type="button" class="task-button" data-task="${id}" aria-pressed="${id === state.activeTask}"><span>0${index + 1}</span>${escapeHTML(task.label)}</button>`).join("");
    document.querySelectorAll("#compare-task-selector [data-task]").forEach((button) => button.addEventListener("click", () => setActiveTask(button.dataset.task, true)));
  }

  function changeNasaPage(delta) {
    const pageInput = document.getElementById("nasa-page");
    pageInput.value = String(Math.max(1, Number(pageInput.value) + delta));
    searchNasa({ preserveTask: true });
  }

  function initNasaInteractions() {
    document.getElementById("nasa-search-form").addEventListener("submit", (event) => { event.preventDefault(); searchNasa(); });
    document.querySelectorAll(".mission-rail [data-task]").forEach((button) => button.addEventListener("click", () => setActiveTask(button.dataset.task, true)));
    document.getElementById("nasa-prev-page").addEventListener("click", () => changeNasaPage(-1));
    document.getElementById("nasa-next-page").addEventListener("click", () => changeNasaPage(1));
    document.getElementById("nasa-prev-item").addEventListener("click", () => selectNasaItem(state.nasaSelected - 1));
    document.getElementById("nasa-next-item").addEventListener("click", () => selectNasaItem(state.nasaSelected + 1));
    document.getElementById("feed-toggle").addEventListener("click", () => setFeedRunning(!state.feedRunning));
    document.getElementById("compare-feed-toggle").addEventListener("click", () => setFeedRunning(!state.feedRunning));

    const stage = document.getElementById("nasa-stage");
    let wheelLocked = false;
    stage.addEventListener("wheel", (event) => {
      if (Math.abs(event.deltaY) < 18 || wheelLocked) return;
      event.preventDefault();
      wheelLocked = true;
      selectNasaItem(state.nasaSelected + (event.deltaY > 0 ? 1 : -1));
      window.setTimeout(() => { wheelLocked = false; }, 450);
    }, { passive: false });

    let touchY = null;
    stage.addEventListener("touchstart", (event) => { touchY = event.changedTouches[0].clientY; }, { passive: true });
    stage.addEventListener("touchend", (event) => {
      if (touchY == null) return;
      const delta = touchY - event.changedTouches[0].clientY;
      if (Math.abs(delta) > 44) selectNasaItem(state.nasaSelected + (delta > 0 ? 1 : -1));
      touchY = null;
    }, { passive: true });
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
    initNasaInteractions();
    renderCompareTaskSelector();
    renderModelOutputs();
    setFeedRunning(true);

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

    await searchNasa({ preserveTask: true });
  }

  document.addEventListener("DOMContentLoaded", boot);
})();
