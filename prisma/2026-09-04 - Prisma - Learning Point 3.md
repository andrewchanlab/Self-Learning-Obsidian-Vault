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
