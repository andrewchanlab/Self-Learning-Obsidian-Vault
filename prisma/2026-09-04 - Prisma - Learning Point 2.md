---
title: "2026-09-04 - Prisma - Learning Point 2"
tags:
  - learning
  - prisma
created: 2026-09-04
---

# Migrations as Code — Database Version Control

Prisma Migrate turns schema changes into SQL migration files tracked in git. `prisma migrate dev` auto-generates the migration SQL from your schema diff. `prisma db push` syncs schema to database without migrations (great for prototyping). `prisma db pull` reverse-engineers an existing database into a schema.

## Key Takeaway
Prisma Migrate treats database schema changes like code — versioned, reviewable, and reversible.

## Related Concepts
- Database Migrations
- Version Control
- Schema Management

---

## 中文

# 遷移即代碼 — 數據庫版本控制

Prisma Migrate 將模式變更轉換為在 git 中追蹤的 SQL 遷移文件。`prisma migrate dev` 從你的模式差異自動生成遷移 SQL。`prisma db push` 將模式同步到數據庫而無需遷移（非常適合原型開發）。`prisma db pull` 可以從現有數據庫反向工程生成模式。

## 核心要點
Prisma Migrate 像對待代碼一樣對待數據庫模式變更 — 可版本化、可審查、可逆轉。

## 相關概念
- 數據庫遷移
- 版本控制
- 模式管理
