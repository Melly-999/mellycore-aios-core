/*
 * MellyCore AIOS — Live Dashboard Preview (local, read-only).
 *
 * Real data: fetched at load time from shared_context/**  files in this repo
 * (ROADMAP.md, RUN_QUEUE.md, LOOP_REGISTRY.json, project-health.state.json,
 * the persisted run ledger, MODEL_ROUTING.md, SAFETY_CONTRACT.md). Reload
 * the page after editing those files and the dashboard reflects the change.
 *
 * Frozen snapshot: site/data/dashboard_snapshot.json — captured by actually
 * running `scripts.loop_ops validate/audit` and the test suite once during
 * this task. Does not re-run itself; regenerate it to update.
 *
 * Mock: the Live tab's event stream and the "Pause/Resume" control. No
 * network call, provider, scheduler, or backend exists anywhere here.
 *
 * This file makes no writes anywhere — every fetch() call is a plain GET
 * against the local static file server.
 */

(function () {
  "use strict";

  const state = {
    roadmapText: null,
    runQueueText: null,
    modelRoutingText: null,
    safetyContractText: null,
    registry: null,
    projectHealthState: null,
    evidence: null,
    snapshot: null,
  };

  // ---------- fetch helpers ----------

  async function getText(path) {
    const res = await fetch(path);
    if (!res.ok) throw new Error(`GET ${path} -> ${res.status}`);
    return res.text();
  }

  async function getJSON(path) {
    const res = await fetch(path);
    if (!res.ok) throw new Error(`GET ${path} -> ${res.status}`);
    return res.json();
  }

  async function findLatestEvidenceFile(loopId) {
    const dirUrl = `/shared_context/loops/runs/${loopId}/`;
    const html = await getText(dirUrl);
    const hrefs = Array.from(html.matchAll(/href="([^"]+\.json)"/g)).map((m) =>
      decodeURIComponent(m[1])
    );
    if (hrefs.length === 0) return null;
    hrefs.sort();
    return dirUrl + hrefs[hrefs.length - 1];
  }

  // ---------- markdown-ish parsing (small, targeted, not a full parser) ----------

  function parseMilestoneA(md) {
    const start = md.indexOf("### Milestone A");
    if (start === -1) return [];
    const rest = md.slice(start);
    const nextHeading = rest.indexOf("\n### ", 1);
    const block = nextHeading === -1 ? rest : rest.slice(0, nextHeading);
    return block
      .split("\n")
      .filter((l) => l.trim().startsWith("- "))
      .map((l) => l.trim().slice(2).trim());
  }

  function parseRunQueueTail(md, n) {
    const lines = md.split("\n").filter((l) => /^\d+\.\s/.test(l.trim()));
    return lines.slice(-n).map((l) => l.trim());
  }

  function parseBulletList(md) {
    return md
      .split("\n")
      .filter((l) => l.trim().startsWith("- "))
      .map((l) => l.trim().slice(2).trim());
  }

  function parseModelRouting(md) {
    return parseBulletList(md)
      .map((line) => {
        const m = line.match(/^([^:]+):\s*(.+)$/);
        return m ? { name: m[1].trim(), role: m[2].trim() } : null;
      })
      .filter(Boolean);
  }

  // ---------- tier / badge logic ----------

  function tierForLoop(loopId, registryEntry, snapshot) {
    if (registryEntry.status === "DISABLED") {
      return { label: "Blocked", cls: "dash-badge--blocked" };
    }
    const tierRow = snapshot
      ? snapshot.commands.audit.loop_tiers.find((t) => t.loop_id === loopId)
      : null;
    const tier = tierRow ? tierRow.highest_earned_tier : "configured";
    if (tier === "exercised") return { label: "Exercised", cls: "dash-badge--exercised" };
    if (tier === "validated") return { label: "Ready", cls: "dash-badge--ready" };
    return { label: "Warning", cls: "dash-badge--warning" };
  }

  function badgeHTML(label, cls) {
    return `<span class="dash-badge ${cls}">${escapeHTML(label)}</span>`;
  }

  function escapeHTML(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  // ---------- tabs ----------

  function initTabs() {
    const buttons = Array.from(document.querySelectorAll(".dash-tab-btn"));
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const target = btn.dataset.tab;
        buttons.forEach((b) => b.setAttribute("aria-selected", String(b === btn)));
        document.querySelectorAll(".dash-panel").forEach((panel) => {
          panel.hidden = panel.id !== `tab-${target}`;
        });
      });
    });
  }

  // ---------- renderers ----------

  function renderOverview() {
    const { registry, snapshot, projectHealthState, roadmapText, runQueueText, safetyContractText, modelRoutingText } = state;

    const milestoneBullets = parseMilestoneA(roadmapText);
    document.getElementById("ov-milestone").textContent = "Milestone A — Operational Trust";

    const nextBullet = milestoneBullets.find((b) => b.includes("**next**"));
    document.getElementById("ov-next-task").textContent = nextBullet
      ? nextBullet.replace(/\*\*/g, "")
      : "No item marked **next** was found in ROADMAP.md.";

    const queueTail = parseRunQueueTail(runQueueText, 5);
    const queueEl = document.getElementById("ov-queue-tail");
    queueEl.innerHTML = queueTail
      .map((line) => `<li class="dash-roadmap-item"><span class="dash-roadmap-text">${escapeHTML(line)}</span></li>`)
      .join("");

    // System map nodes
    const nodesEl = document.getElementById("ov-systemmap-nodes");
    nodesEl.innerHTML = registry.loops
      .map((loop) => {
        const badge = tierForLoop(loop.id, loop, snapshot);
        return `<div class="dash-node">
          <span class="dash-node-title">${escapeHTML(loop.title)}</span>
          ${badgeHTML(badge.label, badge.cls)}
        </div>`;
      })
      .join("");

    // Test status
    const testInfo = snapshot.commands.tests;
    document.getElementById("ov-test-status").innerHTML =
      `${badgeHTML(testInfo.failed === 0 ? "Ready" : "Warning", testInfo.failed === 0 ? "dash-badge--ready" : "dash-badge--warning")} ` +
      `${testInfo.passed} passed, ${testInfo.failed} failed — captured ${escapeHTML(snapshot.captured_at)}`;

    // Safety list (first 6 bullets of SAFETY_CONTRACT.md)
    const safetyBullets = parseBulletList(safetyContractText).slice(0, 6);
    document.getElementById("ov-safety-list").innerHTML = safetyBullets
      .map((b) => `<li class="dash-roadmap-item"><span class="dash-roadmap-text">${escapeHTML(b)}</span></li>`)
      .join("");

    // Model preview (first 5 roles)
    const models = parseModelRouting(modelRoutingText).slice(0, 5);
    document.getElementById("ov-model-preview").innerHTML = models
      .map((m) => `<li class="dash-roadmap-item"><span class="dash-roadmap-text"><strong>${escapeHTML(m.name)}</strong> — ${escapeHTML(m.role)}</span></li>`)
      .join("");

    // Latest evidence
    const runHistory = projectHealthState.run_history || [];
    if (runHistory.length > 0) {
      const last = runHistory[runHistory.length - 1];
      document.getElementById("ov-evidence").innerHTML =
        `${badgeHTML(last.outcome === "success" ? "Ready" : "Warning", last.outcome === "success" ? "dash-badge--exercised" : "dash-badge--warning")} ` +
        `<code>${escapeHTML(last.run_id)}</code> — ${escapeHTML(last.outcome)}, finished ${escapeHTML(last.finished_at)}`;
    } else {
      document.getElementById("ov-evidence").innerHTML = `${badgeHTML("Warning", "dash-badge--warning")} No run recorded yet.`;
    }
  }

  function renderLoops() {
    const { registry, snapshot } = state;
    const el = document.getElementById("loops-list");
    el.innerHTML = registry.loops
      .map((loop) => {
        const badge = tierForLoop(loop.id, loop, snapshot);
        return `<details class="dash-details">
          <summary>
            <span>${escapeHTML(loop.title)} <code>${escapeHTML(loop.id)}</code></span>
            ${badgeHTML(badge.label, badge.cls)}
          </summary>
          <div class="dash-details-body">
            <p>${escapeHTML(loop.purpose)}</p>
            <dl>
              <dt>Level</dt><dd>${escapeHTML(loop.level)}</dd>
              <dt>Status</dt><dd>${escapeHTML(loop.status)}</dd>
              <dt>Trigger</dt><dd>${escapeHTML(loop.trigger_type)}, ${escapeHTML(loop.suggested_cadence)}</dd>
              <dt>Read scope</dt><dd>${loop.read_scope.map(escapeHTML).join(", ")}</dd>
              <dt>Write scope</dt><dd>${loop.allowed_write_scope.length ? loop.allowed_write_scope.map(escapeHTML).join(", ") : "none (empty)"}</dd>
              <dt>Human gates</dt><dd>${loop.human_gates.map(escapeHTML).join(", ")}</dd>
              <dt>Success condition</dt><dd>${escapeHTML(loop.success_condition)}</dd>
            </dl>
          </div>
        </details>`;
      })
      .join("");
  }

  function renderModels() {
    const models = parseModelRouting(state.modelRoutingText);
    const grid = document.getElementById("models-grid");
    const detail = document.getElementById("models-detail");

    grid.innerHTML = models
      .map(
        (m, i) => `<button type="button" class="dash-model-card" aria-pressed="false" data-index="${i}">
          <span class="dash-model-name">${escapeHTML(m.name)}</span>
          <span class="dash-model-role">${escapeHTML(m.role)}</span>
        </button>`
      )
      .join("");

    grid.querySelectorAll(".dash-model-card").forEach((card) => {
      card.addEventListener("click", () => {
        grid.querySelectorAll(".dash-model-card").forEach((c) => c.setAttribute("aria-pressed", "false"));
        card.setAttribute("aria-pressed", "true");
        const m = models[Number(card.dataset.index)];
        detail.hidden = false;
        detail.innerHTML = `
          <span class="dash-card-label">Selected route <span class="dash-mock-flag">preview only — no request sent</span></span>
          <h3>${escapeHTML(m.name)}</h3>
          <p>${escapeHTML(m.role)}</p>
          <p class="dash-source-note">This is a documented role from MODEL_ROUTING.md, not a live connection. No provider API key exists in this repository, and clicking this card does not contact any provider.</p>
        `;
      });
    });
  }

  function renderEvidence() {
    const el = document.getElementById("evidence-body");
    if (!state.evidence) {
      el.innerHTML = `<p class="dash-error-note">No persisted run evidence found under shared_context/loops/runs/project-health/.</p>`;
      return;
    }
    const ev = state.evidence;
    const ledger = ev.ledger;
    const guard = ev.guard_evaluation;
    el.innerHTML = `
      <dl class="dash-details-body" style="display:grid;grid-template-columns:max-content 1fr;gap:6px 16px;">
        <dt>Run ID</dt><dd><code>${escapeHTML(ledger.run_id)}</code></dd>
        <dt>Outcome</dt><dd>${escapeHTML(ledger.outcome)}</dd>
        <dt>Started / completed</dt><dd>${escapeHTML(ledger.started_at)} &rarr; ${escapeHTML(ledger.completed_at)}</dd>
        <dt>Branch / HEAD</dt><dd>${escapeHTML(ledger.branch)} @ <code>${escapeHTML((ledger.head_sha || "").slice(0, 12))}</code></dd>
        <dt>Guard decision</dt><dd>${badgeHTML(guard.decision === "CONTINUE" ? "Ready" : "Warning", guard.decision === "CONTINUE" ? "dash-badge--ready" : "dash-badge--warning")} ${escapeHTML(guard.decision)}</dd>
        <dt>Per-run budget</dt><dd>${escapeHTML(guard.checks.per_run_budget)}</dd>
        <dt>Daily budget</dt><dd>${escapeHTML(guard.checks.daily_budget)}</dd>
        <dt>Tokens (measured)</dt><dd>${ledger.iterations[0] && ledger.iterations[0].tokens.measured ? escapeHTML(String(ledger.iterations[0].tokens.total)) : "null (unmeasured — honest, not a fake zero)"}</dd>
        <dt>Repository mutations</dt><dd>${escapeHTML(String(ledger.repository_mutation_count))}</dd>
        <dt>Remote actions</dt><dd>${escapeHTML(String(ledger.remote_action_count))}</dd>
        <dt>Schema / semantic / redaction</dt><dd>${ev.validation.schema_valid ? "valid" : "INVALID"} / ${ev.validation.semantic_valid ? "valid" : "INVALID"} / ${ev.validation.redaction_clean ? "clean" : "FLAGGED"}</dd>
      </dl>
      <p class="dash-source-note" style="margin-top:12px;">${escapeHTML(ledger.notes || "")}</p>
    `;
  }

  function renderRoadmap() {
    const milestoneBullets = parseMilestoneA(state.roadmapText);
    document.getElementById("roadmap-milestone-a").innerHTML = milestoneBullets
      .map((b) => {
        const isNext = b.includes("**next**");
        const isComplete = b.includes("**completed");
        const badge = isNext
          ? badgeHTML("Next up", "dash-badge--warning")
          : isComplete
          ? badgeHTML("Complete", "dash-badge--exercised")
          : badgeHTML("Pending", "dash-badge--warning");
        return `<li class="dash-roadmap-item">${badge}<span class="dash-roadmap-text">${escapeHTML(b.replace(/\*\*/g, ""))}</span></li>`;
      })
      .join("");

    const queueTail = parseRunQueueTail(state.runQueueText, 8);
    document.getElementById("roadmap-queue").innerHTML = queueTail
      .map((line) => `<li class="dash-roadmap-item"><span class="dash-roadmap-text">${escapeHTML(line)}</span></li>`)
      .join("");
  }

  // ---------- Live tab: mock event stream ----------

  const MOCK_EVENTS = [
    "[MOCK] registry.validate() -> 9 loops, 0 findings",
    "[MOCK] readiness.audit() -> configured=9 validated=9 exercised=1",
    "[MOCK] guard.evaluate(project-health) -> CONTINUE (no limit reached)",
    "[MOCK] kill_switch check -> absent, not engaged",
    "[MOCK] worktree-hygiene -> DISABLED loops skipped (ci-sweeper, dependency-sweeper, post-merge-cleanup)",
    "[MOCK] safety-posture scan -> no secret-shaped strings found in read_scope",
    "[MOCK] context-drift -> 0 contradictions found (simulated)",
    "[MOCK] pr-review-monitor -> no open PR state to report (simulated)",
  ];

  function initLive() {
    const log = document.getElementById("live-eventlog");
    const toggle = document.getElementById("live-toggle");
    const badge = document.getElementById("live-status-badge");
    let running = true;
    let timer = null;

    function addEvent() {
      const text = MOCK_EVENTS[Math.floor(Math.random() * MOCK_EVENTS.length)];
      const li = document.createElement("li");
      li.className = "dash-event";
      const time = new Date().toLocaleTimeString();
      li.innerHTML = `<span class="dash-event-time">${time}</span><span class="dash-event-text">${escapeHTML(text)}</span>`;
      log.prepend(li);
      while (log.children.length > 40) {
        log.removeChild(log.lastChild);
      }
    }

    function start() {
      running = true;
      toggle.textContent = "Pause stream";
      toggle.setAttribute("aria-pressed", "true");
      badge.textContent = "Running";
      badge.className = "dash-badge dash-badge--running";
      timer = setInterval(addEvent, 3500);
    }

    function stop() {
      running = false;
      toggle.textContent = "Resume stream";
      toggle.setAttribute("aria-pressed", "false");
      badge.textContent = "Ready";
      badge.className = "dash-badge dash-badge--ready";
      clearInterval(timer);
    }

    toggle.addEventListener("click", () => (running ? stop() : start()));

    addEvent();
    start();
  }

  function initClock() {
    const el = document.getElementById("dash-clock");
    function tick() {
      el.textContent = new Date().toLocaleTimeString();
    }
    tick();
    setInterval(tick, 1000);
  }

  // ---------- boot ----------

  async function boot() {
    initTabs();
    initClock();
    initLive();

    try {
      const [roadmapText, runQueueText, modelRoutingText, safetyContractText, registry, projectHealthState, snapshot] =
        await Promise.all([
          getText("/shared_context/ROADMAP.md"),
          getText("/shared_context/RUN_QUEUE.md"),
          getText("/shared_context/MODEL_ROUTING.md"),
          getText("/shared_context/SAFETY_CONTRACT.md"),
          getJSON("/shared_context/loops/LOOP_REGISTRY.json"),
          getJSON("/shared_context/loops/states/project-health.state.json"),
          getJSON("/site/data/dashboard_snapshot.json"),
        ]);

      Object.assign(state, {
        roadmapText,
        runQueueText,
        modelRoutingText,
        safetyContractText,
        registry,
        projectHealthState,
        snapshot,
      });

      try {
        const evidencePath = await findLatestEvidenceFile("project-health");
        state.evidence = evidencePath ? await getJSON(evidencePath) : null;
      } catch (e) {
        state.evidence = null;
        console.warn("Evidence fetch failed:", e);
      }

      renderOverview();
      renderLoops();
      renderModels();
      renderEvidence();
      renderRoadmap();
    } catch (err) {
      console.error(err);
      document.getElementById("dash-main").insertAdjacentHTML(
        "afterbegin",
        `<div class="container"><p class="dash-error-note">Failed to load local project data: ${escapeHTML(err.message)}. Make sure this page is served from the repository root (e.g. python -m http.server --bind 127.0.0.1), not opened as a file:// URL.</p></div>`
      );
    }
  }

  document.addEventListener("DOMContentLoaded", boot);
})();
