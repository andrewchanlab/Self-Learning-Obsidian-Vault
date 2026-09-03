---
title: "2026-09-04 - NestJS - Learning Point 9"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# NestJS Pipes — Validation at the Edge of Your API

Pipes transform or validate data before it reaches the controller. Built-in `ValidationPipe` with class-validator decorators (`@IsEmail()`, `@IsInt()`, `@Min(0)`) auto-rejects malformed input. Use `@UsePipes(new ValidationPipe({ transform: true }))` to also auto-convert plain objects to typed DTOs.

## Key Takeaway
Pipes are the input sanitizer layer — validate and transform incoming data before it touches your business logic, returning 400 Bad Request automatically on validation failure.

## Related Concepts
- DTO (Data Transfer Object)
- class-validator
- Input Validation

---

## 中文：NestJS Pipes — 在 API 邊緣做驗證

Pipes 在數據到達控制器之前進行轉換或驗證。帶有 class-validator 裝飾器的內置 `ValidationPipe`（`@IsEmail()`、`@IsInt()`、`@Min(0)`）自動拒絕格式錯誤的輸入。使用 `@UsePipes(new ValidationPipe({ transform: true }))` 還可以自動將普通對象轉換為類型化 DTO。

## 核心要點
Pipes 是輸入淨化層 — 在數據觸碰業務邏輯之前驗證和轉換輸入，在驗證失敗時自動返回 400 Bad Request。

## 相關概念
- DTO（數據傳輸對象）
- class-validator
- 輸入驗證
