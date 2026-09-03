---
title: "2026-03-25 - NestJS - Learning Point 3"
tags:
  - learning
  - nestjs
created: 2026-03-25
---

# Guards, Interceptors, and Pipes: The Request Pipeline

Before a request reaches your controller method, it passes through NestJS's request pipeline: Guards (canActivate) check permissions — return true or throw 401. Pipes (TransformPipe) validate and transform data — converting a JSON `"5"` into the number `5`, or validating a DTO against a class-validator schema. Interceptors wrap the method call, letting you add logging, caching, or response transformation before and after the handler runs. This pipeline is composable — you can apply guards globally, to specific controllers, or individual routes.

## Key Takeaway
NestJS's request pipeline lets you plug in cross-cutting concerns (auth, validation, logging) in a declarative, reusable way without polluting your business logic.

## Related Concepts
- class-validator and class-transformer DTOs
- Custom decorators for parameter injection
- Exception filters for error handling
