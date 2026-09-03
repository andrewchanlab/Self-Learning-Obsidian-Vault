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

---

## 中文：守衛攔截器與管道——請求處理流水線

守衛（Guards）在處理器運行前檢查權限（像門警）。攔截器（Interceptors）包裝回應（用於日誌、快取、轉換）。管道（Pipes）驗證和轉換輸入資料。這三層讓你可以在不污染業務邏輯的情況下添加橫切關注點。

## 核心要點
NestJS 的中介層流水線（守衛、攔截器、管道）提供了認證、日誌和驗證的掛鉤點，且不觸碰業務邏輯。

## 相關概念
- 中介層
- 請求流水線
- 橫切關注點
