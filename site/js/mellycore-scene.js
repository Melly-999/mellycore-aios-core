/*
 * MellyCore 3D scene foundation.
 *
 * Progressive enhancement only: the semantic summary and CSS/DOM source map
 * render first and remain authoritative. This module performs no network,
 * provider, model, routing, persistence, or execution work.
 */

import {
  SCENE_NODES,
  resolveSceneQualityProfile,
} from "./mellycore-scene-config.js";

const REDUCED_MOTION_QUERY = window.matchMedia("(prefers-reduced-motion: reduce)");
const REDUCED_DATA_QUERY = window.matchMedia("(prefers-reduced-data: reduce)");
const FORCED_COLORS_QUERY = window.matchMedia("(forced-colors: active)");
const FINE_POINTER_QUERY = window.matchMedia("(pointer: fine)");
const SOURCE_ARENA_TAB = "source-arena";

function sceneEnvironment() {
  const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  return {
    width: window.innerWidth,
    forcedStatic: new URLSearchParams(window.location.search).get("scene") === "css",
    forcedColors: FORCED_COLORS_QUERY.matches,
    reducedMotion: REDUCED_MOTION_QUERY.matches,
    reducedData: REDUCED_DATA_QUERY.matches,
    saveData: Boolean(connection && connection.saveData),
    deviceMemory: Number(navigator.deviceMemory),
    hardwareConcurrency: Number(navigator.hardwareConcurrency),
  };
}

function seededRandomFactory(seed) {
  let value = seed >>> 0;
  return function seededRandom() {
    value = (value * 1664525 + 1013904223) >>> 0;
    return value / 4294967296;
  };
}

function createRendererCanvas() {
  const canvas = document.createElement("canvas");
  canvas.className = "mellycore-scene-canvas";
  canvas.setAttribute("aria-hidden", "true");
  canvas.setAttribute("tabindex", "-1");
  return canvas;
}

function createWebGLContext(canvas) {
  const attributes = {
    alpha: true,
    antialias: true,
    depth: true,
    powerPreference: "high-performance",
    premultipliedAlpha: true,
    preserveDrawingBuffer: false,
    failIfMajorPerformanceCaveat: true,
  };

  try {
    return (
      canvas.getContext("webgl2", attributes) ||
      canvas.getContext("webgl", attributes)
    );
  } catch (_error) {
    return null;
  }
}

class MellyCoreSceneInstance {
  constructor(host, profile) {
    this.host = host;
    this.panel = host.closest('[role="tabpanel"]');
    this.profile = profile;
    this.canvas = createRendererCanvas();
    this.context = null;
    this.renderer = null;
    this.scene = null;
    this.camera = null;
    this.routingCore = null;
    this.orbitAssembly = null;
    this.routeParticleAttribute = null;
    this.routePoints = null;
    this.resources = { geometries: new Set(), materials: new Set() };
    this.resizeObserver = null;
    this.intersectionObserver = null;
    this.rafId = 0;
    this.disposed = false;
    this.ready = false;
    this.inViewport = false;
    this.panelActive = !this.panel || !this.panel.hidden;
    this.contextLossCount = 0;
    this.permanentFallback = false;
    this.animationTime = 0;
    this.lastTimestamp = 0;
    this.lastRenderedAt = 0;
    this.pointerTarget = { x: 0, y: 0 };
    this.handleFrame = this.handleFrame.bind(this);
    this.handleResize = this.handleResize.bind(this);
    this.handlePointerMove = this.handlePointerMove.bind(this);
    this.handleContextLost = this.handleContextLost.bind(this);
    this.handleContextRestored = this.handleContextRestored.bind(this);
  }

  async initialize() {
    if (this.disposed || !this.host.isConnected) return;

    this.context = createWebGLContext(this.canvas);
    if (!this.context) {
      this.activateFallback("webgl-unavailable");
      return;
    }

    this.host.prepend(this.canvas);
    this.host.dataset.sceneProfile = this.profile.id;

    try {
      const THREE = await import("../vendor/three-r164.module.js");
      if (this.disposed || !this.host.isConnected) return;
      this.createScene(THREE);
      this.attachLifecycle();
      this.handleResize();
      this.renderer.render(this.scene, this.camera);
      this.recordFrameMetrics();
      this.ready = true;
      this.host.classList.add("scene-webgl-ready");
      this.host.dataset.sceneMode = "webgl-enhancement";
      this.syncAnimationState();
    } catch (_error) {
      console.warn("MellyCore scene enhancement unavailable; CSS fallback retained.");
      this.activateFallback("initialization-failed", true);
    }
  }

  createScene(THREE) {
    this.renderer = new THREE.WebGLRenderer({
      canvas: this.canvas,
      context: this.context,
      alpha: true,
      antialias: this.profile.id !== "tablet",
      powerPreference: "high-performance",
    });
    this.renderer.setClearColor(0x020106, 0);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, this.profile.pixelRatioCap));
    this.renderer.outputColorSpace = THREE.SRGBColorSpace;
    this.renderer.shadowMap.enabled = false;

    this.scene = new THREE.Scene();
    this.scene.fog = new THREE.FogExp2(0x020106, 0.052);
    this.camera = new THREE.PerspectiveCamera(38, 1, 0.1, 60);
    this.camera.position.set(0, 0.15, 10.5);

    this.scene.add(new THREE.AmbientLight(0x51417a, 0.72));
    const coreLight = new THREE.PointLight(0x7c3aed, 5.2, 15, 2);
    coreLight.position.set(0.4, 0.8, 2.7);
    this.scene.add(coreLight);
    const edgeLight = new THREE.PointLight(0x35d7f2, 2.4, 16, 2);
    edgeLight.position.set(-4, -2, 4);
    this.scene.add(edgeLight);

    this.createRoutingCore(THREE);
    this.createOrbitalNodes(THREE);
    this.createRoutingPaths(THREE);
    this.createStarField(THREE);
  }

  rememberGeometry(geometry) {
    this.resources.geometries.add(geometry);
    return geometry;
  }

  rememberMaterial(material) {
    this.resources.materials.add(material);
    return material;
  }

  createRoutingCore(THREE) {
    this.routingCore = new THREE.Group();
    this.routingCore.name = "routingCore";

    const coreGeometry = this.rememberGeometry(new THREE.IcosahedronGeometry(1.05, 1));
    const coreMaterial = this.rememberMaterial(new THREE.MeshStandardMaterial({
      color: 0x090713,
      emissive: 0x28105b,
      emissiveIntensity: 0.72,
      metalness: 0.58,
      roughness: 0.34,
      transparent: true,
      opacity: 0.98,
    }));
    const routingMass = new THREE.Mesh(coreGeometry, coreMaterial);
    routingMass.name = "routingCoreMass";

    const edgeGeometry = this.rememberGeometry(new THREE.EdgesGeometry(coreGeometry, 18));
    const edgeMaterial = this.rememberMaterial(new THREE.LineBasicMaterial({
      color: 0xa86cff,
      transparent: true,
      opacity: 0.78,
    }));
    const routingEdges = new THREE.LineSegments(edgeGeometry, edgeMaterial);
    routingEdges.name = "routingCoreEdges";

    const innerGeometry = this.rememberGeometry(new THREE.OctahedronGeometry(0.42, 0));
    const innerMaterial = this.rememberMaterial(new THREE.MeshBasicMaterial({
      color: 0x35d7f2,
      transparent: true,
      opacity: 0.22,
      wireframe: true,
    }));
    const policyKernel = new THREE.Mesh(innerGeometry, innerMaterial);
    policyKernel.name = "policyKernel";

    this.routingCore.add(routingMass, routingEdges, policyKernel);
    this.scene.add(this.routingCore);

    this.orbitAssembly = new THREE.Group();
    this.orbitAssembly.name = "routingOrbits";
    const ringGeometry = this.rememberGeometry(new THREE.TorusGeometry(2.15, 0.014, 5, 96));
    const ringMaterial = this.rememberMaterial(new THREE.MeshBasicMaterial({
      color: 0x6d5dfc,
      transparent: true,
      opacity: 0.32,
    }));
    const providerOrbit = new THREE.Mesh(ringGeometry, ringMaterial);
    providerOrbit.rotation.x = Math.PI / 2.45;
    providerOrbit.rotation.y = Math.PI / 8;
    const modelOrbit = new THREE.Mesh(ringGeometry, ringMaterial);
    modelOrbit.scale.setScalar(1.32);
    modelOrbit.rotation.x = Math.PI / 1.72;
    modelOrbit.rotation.z = Math.PI / 5;
    this.orbitAssembly.add(providerOrbit, modelOrbit);
    this.scene.add(this.orbitAssembly);
  }

  createOrbitalNodes(THREE) {
    const visibleNodes = SCENE_NODES.slice(0, this.profile.nodes);
    const geometry = this.rememberGeometry(new THREE.IcosahedronGeometry(0.19, 0));
    const material = this.rememberMaterial(new THREE.MeshStandardMaterial({
      color: 0x8467d7,
      emissive: 0x3a197b,
      emissiveIntensity: 0.92,
      metalness: 0.34,
      roughness: 0.42,
    }));
    const modelNodes = new THREE.InstancedMesh(geometry, material, visibleNodes.length);
    modelNodes.name = "staticDemonstrationNodes";
    modelNodes.frustumCulled = false;

    const matrixHelper = new THREE.Object3D();
    visibleNodes.forEach((node, index) => {
      matrixHelper.position.set(...node.position);
      matrixHelper.rotation.set(index * 0.28, index * 0.41, index * 0.19);
      matrixHelper.updateMatrix();
      modelNodes.setMatrixAt(index, matrixHelper.matrix);
    });
    modelNodes.instanceMatrix.needsUpdate = true;
    this.scene.add(modelNodes);
  }

  createRoutingPaths(THREE) {
    const visibleNodes = SCENE_NODES.slice(0, this.profile.nodes);
    const routePositions = new Float32Array(visibleNodes.length * 6);
    visibleNodes.forEach((node, index) => {
      routePositions.set(node.position, index * 6);
      routePositions.set([0, 0, 0], index * 6 + 3);
    });
    const routeGeometry = this.rememberGeometry(new THREE.BufferGeometry());
    routeGeometry.setAttribute("position", new THREE.BufferAttribute(routePositions, 3));
    const routeMaterial = this.rememberMaterial(new THREE.LineBasicMaterial({
      color: 0x4f8fe7,
      transparent: true,
      opacity: 0.2,
    }));
    const contextPaths = new THREE.LineSegments(routeGeometry, routeMaterial);
    contextPaths.name = "simulatedRoutingPaths";
    this.scene.add(contextPaths);

    this.routePoints = [
      SCENE_NODES[0].position,
      [0, 0, 0],
      SCENE_NODES[2].position,
    ];
    const particleGeometry = this.rememberGeometry(new THREE.BufferGeometry());
    const particlePositions = new Float32Array(9);
    this.routeParticleAttribute = new THREE.BufferAttribute(particlePositions, 3);
    particleGeometry.setAttribute("position", this.routeParticleAttribute);
    const particleMaterial = this.rememberMaterial(new THREE.PointsMaterial({
      color: 0x8bdcff,
      size: 0.07,
      sizeAttenuation: true,
      transparent: true,
      opacity: 0.72,
    }));
    const routeParticles = new THREE.Points(particleGeometry, particleMaterial);
    routeParticles.name = "simulatedRouteMarkers";
    this.scene.add(routeParticles);
    this.updateRouteParticles();
  }

  createStarField(THREE) {
    const random = seededRandomFactory(0x4d454c4c);
    const positions = new Float32Array(this.profile.stars * 3);
    for (let index = 0; index < this.profile.stars; index += 1) {
      const radius = 9 + random() * 19;
      const theta = random() * Math.PI * 2;
      const phi = Math.acos(2 * random() - 1);
      positions[index * 3] = radius * Math.sin(phi) * Math.cos(theta);
      positions[index * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
      positions[index * 3 + 2] = radius * Math.cos(phi) - 5;
    }
    const starGeometry = this.rememberGeometry(new THREE.BufferGeometry());
    starGeometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    const starMaterial = this.rememberMaterial(new THREE.PointsMaterial({
      color: 0xa9bff8,
      size: this.profile.id === "tablet" ? 0.035 : 0.045,
      sizeAttenuation: true,
      transparent: true,
      opacity: 0.48,
      depthWrite: false,
    }));
    const starField = new THREE.Points(starGeometry, starMaterial);
    starField.name = "proceduralStarField";
    this.scene.add(starField);
  }

  attachLifecycle() {
    this.canvas.addEventListener("webglcontextlost", this.handleContextLost);
    this.canvas.addEventListener("webglcontextrestored", this.handleContextRestored);

    this.resizeObserver = new ResizeObserver(this.handleResize);
    this.resizeObserver.observe(this.host);

    this.intersectionObserver = new IntersectionObserver(
      (entries) => {
        this.inViewport = Boolean(entries[0] && entries[0].isIntersecting);
        this.syncAnimationState();
      },
      { threshold: 0.05 },
    );
    this.intersectionObserver.observe(this.host);

    if (this.profile.pointerParallax && FINE_POINTER_QUERY.matches) {
      this.host.addEventListener("pointermove", this.handlePointerMove, { passive: true });
    }
  }

  handleResize() {
    if (!this.renderer || !this.camera || this.disposed) return;
    const width = Math.max(1, this.host.clientWidth);
    const height = Math.max(1, this.host.clientHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, this.profile.pixelRatioCap));
    this.renderer.setSize(width, height, false);
    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();
    if (!this.rafId) this.renderer.render(this.scene, this.camera);
  }

  recordFrameMetrics() {
    if (!this.renderer || !this.host) return;

    const { calls, triangles, points, lines } = this.renderer.info.render;
    this.host.dataset.sceneDrawCalls = String(calls);
    this.host.dataset.sceneTriangles = String(triangles);
    this.host.dataset.scenePoints = String(points);
    this.host.dataset.sceneLines = String(lines);
  }

  handlePointerMove(event) {
    const bounds = this.host.getBoundingClientRect();
    const relativeX = (event.clientX - bounds.left) / Math.max(1, bounds.width) - 0.5;
    const relativeY = (event.clientY - bounds.top) / Math.max(1, bounds.height) - 0.5;
    this.pointerTarget.x = Math.max(-0.24, Math.min(0.24, relativeX * 0.34));
    this.pointerTarget.y = Math.max(-0.16, Math.min(0.16, -relativeY * 0.22));
  }

  handleContextLost(event) {
    event.preventDefault();
    this.contextLossCount += 1;
    this.suspend();
    this.ready = false;
    this.host.classList.remove("scene-webgl-ready");
    this.host.dataset.sceneMode = "css-context-loss-fallback";
    if (this.contextLossCount > 1) {
      this.permanentFallback = true;
      this.activateFallback("repeated-context-loss", true);
    }
  }

  handleContextRestored() {
    if (this.disposed || this.permanentFallback || !this.renderer) return;
    try {
      this.renderer.resetState();
      this.handleResize();
      this.renderer.render(this.scene, this.camera);
      this.recordFrameMetrics();
      this.ready = true;
      this.host.classList.add("scene-webgl-ready");
      this.host.dataset.sceneMode = "webgl-enhancement";
      this.syncAnimationState();
    } catch (_error) {
      this.activateFallback("context-restore-failed", true);
    }
  }

  setPanelActive(active) {
    this.panelActive = active;
    this.syncAnimationState();
  }

  shouldAnimate() {
    return (
      this.ready &&
      !this.disposed &&
      !this.permanentFallback &&
      !document.hidden &&
      this.panelActive &&
      this.inViewport
    );
  }

  syncAnimationState() {
    if (this.shouldAnimate()) this.resume();
    else this.suspend();
  }

  resume() {
    if (this.rafId || !this.shouldAnimate()) return;
    this.lastTimestamp = 0;
    this.rafId = window.requestAnimationFrame(this.handleFrame);
  }

  suspend() {
    if (this.rafId) window.cancelAnimationFrame(this.rafId);
    this.rafId = 0;
    this.lastTimestamp = 0;
  }

  handleFrame(timestamp) {
    this.rafId = 0;
    if (!this.shouldAnimate()) return;

    if (
      this.profile.frameInterval &&
      timestamp - this.lastRenderedAt < this.profile.frameInterval
    ) {
      this.rafId = window.requestAnimationFrame(this.handleFrame);
      return;
    }

    const delta = this.lastTimestamp ? Math.min(50, timestamp - this.lastTimestamp) : 0;
    this.lastTimestamp = timestamp;
    this.lastRenderedAt = timestamp;
    this.animationTime += delta;

    this.routingCore.rotation.x = Math.sin(this.animationTime * 0.00013) * 0.11;
    this.routingCore.rotation.y += delta * 0.000075;
    this.orbitAssembly.rotation.z += delta * 0.000018;
    this.camera.position.x += (this.pointerTarget.x - this.camera.position.x) * 0.025;
    this.camera.position.y += (0.15 + this.pointerTarget.y - this.camera.position.y) * 0.025;
    this.camera.lookAt(0, 0, 0);
    this.updateRouteParticles();
    this.renderer.render(this.scene, this.camera);
    this.rafId = window.requestAnimationFrame(this.handleFrame);
  }

  updateRouteParticles() {
    if (!this.routeParticleAttribute || !this.routePoints) return;
    const positions = this.routeParticleAttribute.array;
    for (let index = 0; index < 3; index += 1) {
      const phase = (this.animationTime * 0.000018 + index / 3) % 1;
      const firstLeg = phase < 0.5;
      const amount = firstLeg ? phase * 2 : (phase - 0.5) * 2;
      const from = firstLeg ? this.routePoints[0] : this.routePoints[1];
      const to = firstLeg ? this.routePoints[1] : this.routePoints[2];
      positions[index * 3] = from[0] + (to[0] - from[0]) * amount;
      positions[index * 3 + 1] = from[1] + (to[1] - from[1]) * amount;
      positions[index * 3 + 2] = from[2] + (to[2] - from[2]) * amount;
    }
    this.routeParticleAttribute.needsUpdate = true;
  }

  activateFallback(reason, removeCanvas = false) {
    this.suspend();
    this.ready = false;
    this.host.classList.remove("scene-webgl-ready");
    this.host.dataset.sceneProfile = "fallback";
    this.host.dataset.sceneMode = "css-fallback";
    this.host.dataset.sceneFallbackReason = reason;
    if (removeCanvas) {
      this.disposeRenderer();
      this.canvas.remove();
    }
  }

  disposeRenderer() {
    this.resources.geometries.forEach((geometry) => geometry.dispose());
    this.resources.materials.forEach((material) => material.dispose());
    this.resources.geometries.clear();
    this.resources.materials.clear();
    if (this.renderer) this.renderer.dispose();
    this.renderer = null;
    this.scene = null;
    this.camera = null;
  }

  dispose() {
    if (this.disposed) return;
    this.disposed = true;
    this.suspend();
    this.resizeObserver?.disconnect();
    this.intersectionObserver?.disconnect();
    this.host.removeEventListener("pointermove", this.handlePointerMove);
    this.canvas.removeEventListener("webglcontextlost", this.handleContextLost);
    this.canvas.removeEventListener("webglcontextrestored", this.handleContextRestored);
    this.disposeRenderer();
    this.canvas.remove();
    this.host.classList.remove("scene-webgl-ready");
  }
}

let activeScene = null;
let pendingHost = null;
let idleHandle = 0;
let resizeTimer = 0;

function cancelPendingMount() {
  if (!idleHandle) return;
  if ("cancelIdleCallback" in window) window.cancelIdleCallback(idleHandle);
  else window.clearTimeout(idleHandle);
  idleHandle = 0;
}

function runWhenIdle(callback) {
  if ("requestIdleCallback" in window) {
    idleHandle = window.requestIdleCallback(callback, { timeout: 700 });
  } else {
    idleHandle = window.setTimeout(callback, 32);
  }
}

function scheduleSceneMount(host) {
  if (!(host instanceof HTMLElement)) return;
  pendingHost = host;
  cancelPendingMount();

  const profile = resolveSceneQualityProfile(sceneEnvironment());
  if (activeScene) {
    const sameHostAndProfile =
      activeScene.host === host &&
      activeScene.profile.id === profile.id &&
      profile.enabled;
    if (sameHostAndProfile) {
      activeScene.handleResize();
      return;
    }
    activeScene.dispose();
    activeScene = null;
  }

  host.dataset.sceneProfile = profile.id;
  host.dataset.sceneMode = profile.enabled ? "pending-enhancement" : "css-fallback";
  if (!profile.enabled) {
    host.dataset.sceneFallbackReason = profile.reason;
    if (activeScene) {
      activeScene.dispose();
      activeScene = null;
    }
    return;
  }

  runWhenIdle(async () => {
    idleHandle = 0;
    if (host !== pendingHost || !host.isConnected) return;
    const currentProfile = resolveSceneQualityProfile(sceneEnvironment());
    if (!currentProfile.enabled) {
      host.dataset.sceneMode = "css-fallback";
      host.dataset.sceneFallbackReason = currentProfile.reason;
      return;
    }
    activeScene = new MellyCoreSceneInstance(host, currentProfile);
    await activeScene.initialize();
  });
}

function syncCurrentHost() {
  const host = document.querySelector(".mellycore-scene-host");
  if (host) scheduleSceneMount(host);
}

document.addEventListener("mellycore:scenehost", (event) => {
  const host = event.detail && event.detail.host;
  if (host instanceof HTMLElement) {
    scheduleSceneMount(host);
    return;
  }
  pendingHost = null;
  cancelPendingMount();
  activeScene?.dispose();
  activeScene = null;
});

document.addEventListener("mellycore:tabchange", (event) => {
  activeScene?.setPanelActive(event.detail && event.detail.tabName === SOURCE_ARENA_TAB);
});

document.addEventListener("visibilitychange", () => activeScene?.syncAnimationState());
window.addEventListener("pagehide", () => activeScene?.dispose(), { once: true });

function handleEnvironmentChange() {
  const host = activeScene?.host || pendingHost || document.querySelector(".mellycore-scene-host");
  if (host) scheduleSceneMount(host);
}

REDUCED_MOTION_QUERY.addEventListener("change", handleEnvironmentChange);
REDUCED_DATA_QUERY.addEventListener("change", handleEnvironmentChange);
FORCED_COLORS_QUERY.addEventListener("change", handleEnvironmentChange);
window.addEventListener("resize", () => {
  window.clearTimeout(resizeTimer);
  resizeTimer = window.setTimeout(handleEnvironmentChange, 180);
}, { passive: true });

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => window.setTimeout(syncCurrentHost, 0), { once: true });
} else {
  window.setTimeout(syncCurrentHost, 0);
}
