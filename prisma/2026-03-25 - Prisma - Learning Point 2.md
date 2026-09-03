---
title: "2026-03-25 - Prisma - Learning Point 2"
tags:
  - learning
  - prisma
created: 2026-03-25
---

# Prisma Client: Type-Safe Queries Without Raw SQL

Prisma Client is an auto-generated, type-safe query builder for your specific database. Instead of writing raw SQL strings, you call methods like `prisma.user.findMany({ where: { email: "..." } })`. The returned types are inferred from your schema — no manual type definitions. For cases where you genuinely need raw SQL (complex reporting queries, for instance), Prisma provides `$queryRaw` which still returns typed results, keeping you within the safety net. The result is the productivity of an ORM with the performance visibility of SQL.

## Key Takeaway
Prisma Client gives you ORM ergonomics with full type safety — if the schema changes, your TypeScript compiler catches broken queries immediately.

## Related Concepts
- Fluent API for query building
- $queryRaw and $executeRaw
- Generated TypeScript types for all models
