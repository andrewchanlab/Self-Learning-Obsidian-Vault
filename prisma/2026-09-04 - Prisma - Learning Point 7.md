---
title: "2026-09-04 - Prisma - Learning Point 7"
tags:
  - learning
  - prisma
created: 2026-09-04
---

# Relations — One-to-Many and Many-to-Many Made Simple

In schema.prisma: `User { id, posts Post[] }` and `Post { id, author User }`. Prisma handles JOINs under the hood — `prisma.post.findMany({ include: { author: true } })` returns nested user data. For many-to-many, add `Post { tags Tag[] }` and Prisma creates the junction table automatically.

## Key Takeaway
Relations in Prisma are declared in the schema — the ORM manages foreign keys and JOINs automatically, letting you work with nested objects instead of flat SQL rows.

## Related Concepts
- Foreign Keys
- JOIN
- Many-to-Many Relations

---

## 中文：關係 — 一對多和多對多輕鬆搞定

在 schema.prisma 中：`User { id, posts Post[] }` 和 `Post { id, author User }`。Prisma 在幕後處理 JOIN — `prisma.post.findMany({ include: { author: true } })` 返回嵌套的用戶數據。對於多對多，添加 `Post { tags Tag[] }`，Prisma 會自動創建關聯表。

## 核心要點
Prisma 中的關係在模式中聲明 — ORM 自動管理外鍵和 JOIN，讓你用嵌套對象而不是扁平的 SQL 行來工作。

## 相關概念
- 外鍵
- JOIN
- 多對多關係
