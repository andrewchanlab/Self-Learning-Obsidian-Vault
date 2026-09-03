---
title: "2026-09-04 - NestJS - Learning Point 2"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# Controllers Direct Traffic, Services Do the Work

Controllers receive HTTP requests, extract parameters, and call the right service methods. They never contain business logic — they delegate to services which know HOW to do things. This separation makes business logic reusable across different entry points (HTTP, WebSockets, gRPC).

## Key Takeaway
NestJS enforces a clean separation between routing (controllers) and business logic (services) — making logic reusable and testable.

## Related Concepts
- MVC Pattern
- Business Logic
- REST API
