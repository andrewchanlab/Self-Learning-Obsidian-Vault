---
title: "2026-09-04 - Vite - Learning Point 2"
tags:
  - learning
  - vite
created: 2026-09-04
---

# Hot Module Replacement Updates Only What Changed

When you edit a file, Vite doesn't reload the whole page — it swaps just that module in the browser. Your app state (form inputs, scroll position) survives. This is like replacing one Lego block without dismantling the entire structure.

## Key Takeaway
Vite's HMR preserves application state while instantly updating changed modules — the fastest possible feedback loop during development.

## Related Concepts
- Hot Module Replacement
- State Preservation
- Fast Refresh
