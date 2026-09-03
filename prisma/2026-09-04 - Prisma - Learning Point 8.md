---
title: "2026-09-04 - Prisma - Learning Point 8"
tags:
  - learning
  - prisma
created: 2026-09-04
---

# Prisma's Data Validation with Zod

Prisma returns plain objects from queries. Pair it with Zod to validate at runtime: `z.object({ id: z.string(), name: z.string() })`. parse() throws on mismatch, safeParse() returns a result object. This adds a runtime safety layer on top of TypeScript's compile-time types — especially useful at API boundaries.

## Key Takeaway
TypeScript types + Zod validation = both compile-time and runtime safety. Prisma handles the DB; Zod handles the trust boundary between your API and external input.

## Related Concepts
- Zod
- Runtime Validation
- API Boundaries

---

## 中文：Prisma 配合 Zod 做數據驗證

Prisma 從查詢返回普通對象。配合 Zod 在運行時驗證：`z.object({ id: z.string(), name: z.string() })`。parse() 在不匹配時拋出異常，safeParse() 返回結果對象。這在 TypeScript 編譯時類型的基礎上增加了運行時安全層 — 在 API 邊界特別有用。

## 核心要點
TypeScript 類型 + Zod 驗證 = 編譯時和運行時雙重安全。Prisma 負責數據庫；Zod 負責在你的 API 和外部輸入之間建立信任邊界。

## 相關概念
- Zod
- 運行時驗證
- API 邊界
