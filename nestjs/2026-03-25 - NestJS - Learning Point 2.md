---
title: "2026-03-25 - NestJS - Learning Point 2"
tags:
  - learning
  - nestjs
created: 2026-03-25
---

# Dependency Injection and the IoC Container

NestJS uses a custom Inversion of Control (IoC) container to manage dependencies. When NestJS bootstraps, it reads your module declarations, constructs a dependency graph, and instantiates providers in the correct order. When a controller or provider needs another service, you declare it in the constructor (`constructor(private readonly userService: UserService)`), and NestJS resolves it from the container — either as a singleton (shared across all requests) or a request-scoped instance (new per request, useful for per-request context like database transactions).

## Key Takeaway
NestJS's IoC container means you never `new` up services manually — the framework wires everything together, making swapping implementations (e.g., mock databases in tests) effortless.

## Related Concepts
- Constructor injection pattern
- Request-scoped providers
- Custom providers and factory functions
