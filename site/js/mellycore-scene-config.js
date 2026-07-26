/*
 * Deterministic static scene configuration for
 * MELLYCORE-3D-SCENE-FOUNDATION-001.
 *
 * These records are visual fixtures only. They do not describe provider
 * availability, runtime activity, model execution, or a live route.
 */

export const SCENE_NODES = Object.freeze([
  Object.freeze({ id: "provider", label: "Provider", position: [-3.2, 1.4, -0.5] }),
  Object.freeze({ id: "model", label: "Model", position: [-2.4, -1.8, 0.25] }),
  Object.freeze({ id: "agent", label: "Agent", position: [2.75, -1.5, -0.35] }),
  Object.freeze({ id: "context", label: "Context", position: [-0.8, 2.55, -0.9] }),
  Object.freeze({ id: "policy", label: "Policy", position: [2.55, 1.55, 0.4] }),
  Object.freeze({ id: "artifact", label: "Artifact", position: [0.85, -2.7, -0.75] }),
]);

export const SCENE_QUALITY_PROFILES = Object.freeze({
  cinematic: Object.freeze({
    id: "cinematic",
    enabled: true,
    stars: 360,
    nodes: 6,
    pixelRatioCap: 2,
    frameInterval: 0,
    pointerParallax: true,
  }),
  standard: Object.freeze({
    id: "standard",
    enabled: true,
    stars: 240,
    nodes: 6,
    pixelRatioCap: 1.75,
    frameInterval: 0,
    pointerParallax: true,
  }),
  tablet: Object.freeze({
    id: "tablet",
    enabled: true,
    stars: 120,
    nodes: 4,
    pixelRatioCap: 1.5,
    frameInterval: 1000 / 30,
    pointerParallax: false,
  }),
  fallback: Object.freeze({
    id: "fallback",
    enabled: false,
    stars: 0,
    nodes: 0,
    pixelRatioCap: 1,
    frameInterval: 0,
    pointerParallax: false,
  }),
});

export function resolveSceneQualityProfile(environment) {
  if (environment.forcedStatic) {
    return { ...SCENE_QUALITY_PROFILES.fallback, reason: "forced-static" };
  }

  if (environment.forcedColors) {
    return { ...SCENE_QUALITY_PROFILES.fallback, reason: "forced-colors-static" };
  }

  if (environment.reducedMotion) {
    return { ...SCENE_QUALITY_PROFILES.fallback, reason: "reduced-motion" };
  }

  if (environment.width <= 760) {
    return { ...SCENE_QUALITY_PROFILES.fallback, reason: "mobile-static" };
  }

  const constrainedDevice =
    environment.reducedData ||
    environment.saveData ||
    (Number.isFinite(environment.deviceMemory) && environment.deviceMemory <= 4) ||
    (Number.isFinite(environment.hardwareConcurrency) && environment.hardwareConcurrency <= 4);

  if (constrainedDevice) {
    return { ...SCENE_QUALITY_PROFILES.fallback, reason: "low-power-static" };
  }

  if (environment.width < 1180) return SCENE_QUALITY_PROFILES.tablet;
  if (environment.width < 1600) return SCENE_QUALITY_PROFILES.standard;
  return SCENE_QUALITY_PROFILES.cinematic;
}
