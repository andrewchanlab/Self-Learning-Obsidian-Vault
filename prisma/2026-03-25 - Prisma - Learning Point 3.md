---
title: "2026-03-25 - Prisma - Learning Point 3"
tags:
  - learning
  - prisma
created: 2026-03-25
---

# Prisma Migrate: Schema Migrations as a First-Class Concept

Prisma Migrate turns your schema.prisma changes into SQL migration files. When you run `prisma migrate dev`, Prisma compares the current schema to the migration history and generates a new SQL file with the necessary ALTER TABLE statements. This SQL is reviewed, committed to version control, and applied via `prisma migrate deploy` in production. Unlike "schema sync" tools that blindly apply changes, Prisma's migration system gives you audit trails, rollback capability, and the ability to inspect generated SQL before it runs — essential for production databases where a bad migration means data loss.

## Key Takeaway
Prisma Migrate treats database schema changes as versioned, reviewable SQL migrations — safe for production, with full rollback capability.

## Related Concepts
- SQL migration files and history
- Development vs production migration workflows
- Reset and seed commands
