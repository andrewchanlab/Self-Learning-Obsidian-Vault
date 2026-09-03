---
title: "2026-09-04 - Prisma - Learning Point 5"
tags:
  - learning
  - prisma
created: 2026-09-04
---

# Prisma Migrate — Version-Controlled Database Schema

`prisma migrate dev` compares your schema.prisma against the current database state and generates a SQL migration file. These migrations are stored in `prisma/migrations/` and tracked in git. `prisma migrate deploy` applies them in production — making your schema changes reviewable, reversible, and reproducible across environments.

## Key Takeaway
Prisma Migrate turns database schema changes into safe, auditable, version-controlled steps — no more manual ALTER TABLE scripts floating around.

## Related Concepts
- Database Migration
- Schema Versioning
- DevOps

---

## 中文：Prisma Migrate — 版本控制的數據庫模式

`prisma migrate dev` 會將你的 schema.prisma 與當前數據庫狀態進行比較，並生成一個 SQL 遷移文件。這些遷移文件存儲在 `prisma/migrations/` 中並在 git 中追蹤。`prisma migrate deploy` 在生產環境中執行它們 — 使你的模式變更可審查、可撤銷，並可在不同環境中重現。

## 核心要點
Prisma Migrate 將數據庫模式變更轉變為安全的、可審計的、版本控制的步驟 — 不再需要手動的 ALTER TABLE 腳本四處飄蕩。

## 相關概念
- 數據庫遷移
- 模式版本控制
- DevOps
