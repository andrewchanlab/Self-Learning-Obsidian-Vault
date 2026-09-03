---
title: "2026-09-04 - NestJS - Learning Point 8"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# NestJS Interceptors — Transform Requests and Responses

Interceptors wrap route handlers with `intercept()`. Add caching, logging, or response wrapping — e.g., wrap every response in `{ data: ..., meta: ... }`. Use `@UseInterceptors(LogInterceptor)` and access `CallHandler` to `pipe` the observable stream. Transform data before it reaches the client without touching the controller.

## Key Takeaway
Interceptors let you add cross-cutting behavior — logging, caching, response transformation — at the route level without polluting your service logic.

## Related Concepts
- AOP (Aspect-Oriented Programming)
- Response Transformation
- Observables

---

## 中文：NestJS Interceptors — 轉換請求和響應

Interceptors 用 `intercept()` 包裝路由處理程序。添加緩存、日誌或響應包裝 — 例如，將每個響應包裝在 `{ data: ..., meta: ... }` 中。使用 `@UseInterceptors(LogInterceptor)` 並訪問 `CallHandler` 來 `pipe` 可觀察流。在數據到達客戶端之前轉換它，而無需觸碰控制器。

## 核心要點
Interceptors 讓你在路由級別添加橫切關注點 — 日誌、緩存、響應轉換 — 而不污染你的服務邏輯。

## 相關概念
- AOP（面向切面編程）
- 響應轉換
- 可觀察對象
