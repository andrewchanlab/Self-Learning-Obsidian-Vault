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
