---
title: "2026-03-25 - Prisma - Learning Point 1"
tags:
  - learning
  - prisma
created: 2026-03-25
---

# The Prisma Schema: Your Database as Code

Prisma's core is the `schema.prisma` file, which defines your data model in a declarative, language-agnostic syntax. You describe models (tables), their fields (columns), and relations (foreign keys), and Prisma generates a type-safe client tailored to your schema. This means if you rename a column in the schema, TypeScript will flag every outdated query at compile time — a massive improvement over string-based SQL queries where typos only surface at runtime. The schema also defines the data source (PostgreSQL, MySQL, SQLite, etc.) and the generator output.

## Key Takeaway
Prisma schema = the single source of truth for your database structure, generating type-safe database clients automatically.

## Related Concepts
- Prisma models and scalar types
- Relations (one-to-many, many-to-many)
- Prisma Client generated types
