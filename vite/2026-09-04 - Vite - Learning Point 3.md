---
title: "2026-09-04 - Vite - Learning Point 3"
tags:
  - learning
  - vite
created: 2026-09-04
---

# esbuild Pre-Bundling Makes Dependencies Lightning Fast

Vite uses esbuild (written in Go) to pre-bundle dependencies. Go is 10-100x faster than JavaScript for parsing tasks. Your thousands of node_modules get processed at build speed, not dev-server speed. Production builds then use Rollup for optimal code splitting.

## Key Takeaway
Writing the dependency bundler in Go gives Vite a 10-100x speed advantage over JavaScript-based bundlers for initial processing.

## Related Concepts
- esbuild
- Go Language
- Code Splitting
