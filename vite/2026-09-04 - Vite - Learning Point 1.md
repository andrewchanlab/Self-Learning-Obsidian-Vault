---
title: "2026-09-04 - Vite - Learning Point 1"
tags:
  - learning
  - vite
created: 2026-09-04
---

# Vite Skips Bundling During Development for Instant Start

Traditional bundlers (Webpack, Rollup) must scan and bundle your entire dependency tree before serving the first page. Vite serves native ES modules directly to the browser — no bundling step needed. Dev server starts in ~100ms regardless of project size.

## Key Takeaway
Vite's esbuild-powered dependency pre-bundling eliminates the startup wait, making dev servers feel instantaneous even in large projects.

## Related Concepts
- ES Modules
- Build Tooling
- Dev Server
