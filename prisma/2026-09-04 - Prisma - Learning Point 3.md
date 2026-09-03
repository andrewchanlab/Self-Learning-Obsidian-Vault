---
title: "2026-09-04 - Prisma - Learning Point 3"
tags:
  - learning
  - prisma
created: 2026-09-04
---

# One API, Multiple Databases

Switch from PostgreSQL to MySQL by changing one line in schema.prisma (the provider). The Prisma Client API stays identical. This database portability is rare in the ORM world and extremely valuable when evaluating database options during development.

## Key Takeaway
Prisma's unified API means you can swap underlying databases (PostgreSQL, MySQL, SQLite, MongoDB) without rewriting application code.

## Related Concepts
- Database Abstraction
- PostgreSQL
- Multi-Database Support

---

## 中文

# 一個 API，多個數據庫

只需要在 schema.prisma 中改一行（provider），就可以從 PostgreSQL 切換到 MySQL。Prisma Client API 保持不變。這種數據庫可移植性在 ORM 世界中很少見，對開發期間評估數據庫選項非常有價值。

## 核心要點
Prisma 的統一 API 意味著你可以替換底層數據庫（PostgreSQL、MySQL、SQLite、MongoDB）而無需重寫應用程序代碼。

## 相關概念
- 數據庫抽象
- PostgreSQL
- 多數據庫支持
