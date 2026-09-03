---
title: "2026-09-04 - NestJS - Learning Point 7"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# NestJS Guards — Gatekeepers for Your Routes

Guards implement `CanActivate` and return `true`/`false` to allow or block requests. Use `@UseGuards(AuthGuard)` on a controller or route. Guards have access to `ExecutionContext` — read headers, roles, tokens. Common use: JWT authentication guard that extracts and validates a Bearer token before the handler runs.

## Key Takeaway
Guards are the authorization layer — they answer "who can access this endpoint?" at the routing level, before any business logic runs.

## Related Concepts
- Authentication
- Authorization
- Middleware

---

## 中文：NestJS Guards — 路由的守門人

Guards 實現 `CanActivate`，返回 `true`/`false` 來允許或阻止請求。在控制器或路由上使用 `@UseGuards(AuthGuard)`。Guards 可以訪問 `ExecutionContext` — 讀取 headers、roles、tokens。常見用法：JWT 認證 guard，在處理程序運行之前提取和驗證 Bearer token。

## 核心要點
Guards 是授權層 — 它們在路由級別回答"誰可以訪問這個端點？"的問題，在任何業務邏輯運行之前。

## 相關概念
- 認證
- 授權
- 中間件
