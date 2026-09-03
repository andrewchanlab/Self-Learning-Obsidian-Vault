---
title: "2026-09-04 - NestJS - Learning Point 5"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# Exception Filters Handle Errors Globally

When something throws in your code, Exception Filters catch it. NestJS has a built-in `HttpException` and a global exception handler. You can throw `NotFoundException` or build custom filters that format errors consistently — every unhandled error gets caught and turned into a structured JSON response instead of a crash.

## Key Takeaway
NestJS's exception filter layer ensures all errors are caught and returned as structured HTTP responses — no raw crashes to the client.

## Related Concepts
- Error Handling
- HTTP Exceptions
- Global Exception Handler

---

## 中文：異常過濾器全局處理錯誤

當程式碼拋出異常時，異常過濾器會捕捉它。NestJS 有內建的 `HttpException` 和全局異常處理器。你可以拋出 `NotFoundException` 或建立自定義過濾器，統一格式化錯誤——每個未處理的錯誤都會被捕捉並轉換為結構化的 JSON 回應，而不是讓應用程式崩潰。

## 核心要點
NestJS 的異常過濾器層確保所有錯誤都被捕捉並以結構化的 HTTP 回應形式返回——不會讓客戶端看到原始的崩潰資訊。

## 相關概念
- 錯誤處理
- HTTP 異常
- 全局異常處理器
