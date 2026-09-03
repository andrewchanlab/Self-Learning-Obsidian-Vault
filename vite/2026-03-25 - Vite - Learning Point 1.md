---
title: "2026-03-25 - Vite - Learning Point 1"
tags:
  - learning
  - vite
created: 2026-03-25
---

# Vite's Development Server: ES Modules and Native ESM

Unlike traditional bundlers (Webpack, Rollup) that bundle everything before serving, Vite takes advantage of the browser's native ES Module (ESM) support. In development, Vite serves files as raw ES modules — when you import a file, the browser requests it directly and Vite transforms it on-the-fly. This means cold start is near-instant regardless of project size, and Hot Module Replacement (HMR) updates only the exact module that changed, making dev feedback nearly instantaneous. For a large project, this is a night-and-day difference compared to waiting 30+ seconds for a full rebundle.

## Key Takeaway
Vite's trick is letting the browser do the bundling work during development — no bundler step means instant startup and fast HMR.

## Related Concepts
- Native ES Modules in browsers
- Hot Module Replacement (HMR)
- On-the-fly code transformation
