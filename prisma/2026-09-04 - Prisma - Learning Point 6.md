---
title: "2026-09-04 - Prisma - Learning Point 6"
tags:
  - learning
  - prisma
created: 2026-09-04
---

# Prisma Client — Chainable Query API

After `prisma generate`, you get `prisma.user.findMany({ where: { age: { gt: 18 } }, include: { posts: true } })`. Every clause — `where`, `select`, `include`, `orderBy`, `take`, `skip` — chains naturally. The result is fully typed: TypeScript knows `User & { posts: Post[] }` without you writing a single interface.

## Key Takeaway
Prisma Client's chainable API builds complex queries without raw SQL strings, while TypeScript infers every field — autocomplete everywhere, no runtime surprises.

## Related Concepts
- Query Builder
- TypeScript Types
- Relational Queries

---

## 中文：Prisma Client — 可鏈接的查詢 API

在 `prisma generate` 之後，你得到 `prisma.user.findMany({ where: { age: { gt: 18 } }, include: { posts: true } })`。每個子句 — `where`、`select`、`include`、`orderBy`、`take`、`skip` — 都可以自然鏈接。結果是完全類型化的：TypeScript 知道 `User & { posts: Post[] }`，無需你寫任何接口。

## 核心要點
Prisma Client 的可鏈接 API 無需原始 SQL 字串即可構建複雜查詢，同時 TypeScript 推斷每個字段 — 處處都有自動補全，沒有運行時意外。

## 相關概念
- 查詢構建器
- TypeScript 類型
- 關聯查詢
