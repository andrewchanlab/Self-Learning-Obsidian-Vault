---
title: "2026-03-25 - Vite - Learning Point 3"
tags:
  - learning
  - vite
created: 2026-03-25
---

# Plugin Ecosystem: Extending Vite's Build Pipeline

Vite's plugin API is compatible with Rollup's, meaning most Rollup plugins work directly in Vite. Beyond that, Vite adds its own plugin hooks specifically for the dev server (like `configureServer` for adding custom middleware) and HMR (like `handleHotUpdate` for controlling what triggers a reload). This means you can add Vue, React, or Svelte support via community plugins, integrate with backend frameworks like SvelteKit or Remix, and even process custom file types — all through the same unified plugin interface.

## Key Takeaway
Vite's dual nature as both a dev server and a bundler is unified through a plugin system that works across both modes, giving you one config to rule development and production.

## Related Concepts
- Vite plugin vs Rollup plugin differences
- esbuild for fast TypeScript/JSX transformation
- Framework-specific Vite plugins (Vue, React)
