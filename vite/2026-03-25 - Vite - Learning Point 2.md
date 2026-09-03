---
title: "2026-03-25 - Vite - Learning Point 2"
tags:
  - learning
  - vite
created: 2026-03-25
---

# Rollup-Based Production Bundling

When it's time to build for production, Vite switches strategies — it uses Rollup (which it sponsors and helps maintain) to bundle the entire application. Rollup performs tree-shaking: it analyzes the ES module dependency graph and removes unused code, so if you import a 1MB library but only use one function, that function is all that ends up in your bundle. Vite also splits chunks intelligently, separating vendor libraries from application code so that when your app code changes, users don't need to re-download the vendor chunk.

## Key Takeaway
Vite pairs the best dev experience (native ESM) with the best production output (Rollup's tree-shaking and code splitting) — best of both worlds.

## Related Concepts
- Tree-shaking dead code elimination
- Code splitting and chunking strategies
- Rollup vs Webpack bundling philosophy
