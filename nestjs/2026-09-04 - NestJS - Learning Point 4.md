---
title: "2026-09-04 - NestJS - Learning Point 4"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# Guards, Interceptors, and Pipes — The Request Pipeline

Guards check permissions before the handler runs (like a bouncer). Interceptors wrap the response (for logging, caching, transformation). Pipes validate and transform input data. These three layers let you add cross-cutting concerns without polluting your business logic.

## Key Takeaway
NestJS's middleware pipeline (Guards, Interceptors, Pipes) provides hooks for authentication, logging, and validation that don't touch business logic.

## Related Concepts
- Middleware
- Request Pipeline
- Cross-Cutting Concerns
