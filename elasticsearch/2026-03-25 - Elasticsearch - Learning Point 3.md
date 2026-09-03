---
title: "2026-03-25 - Elasticsearch - Learning Point 3"
tags:
  - learning
  - elasticsearch
created: 2026-03-25
---

# Mapping and Data Types: Defining Your Schema

Elasticsearch uses dynamic mapping — when you index a JSON document, it guesses field types automatically (integers stay integers, strings become text + keyword). But for production, explicit mappings give you control: you define which fields are `text` (full-text searchable), `keyword` (exact match, sortable), `integer`, `date`, `geo_point`, or nested objects. The `text` type uses an analyzer (like the standard analyzer that lowercases and stems), while `keyword` stores the raw value verbatim — essential for aggregations and exact-match filters where "Apple" ≠ "apple."

## Key Takeaway
Always define explicit mappings in production — dynamic mapping is convenient but leads to mapping explosions and unexpected behavior with string fields.

## Related Concepts
- text vs keyword field types
- Dynamic mapping and template inheritance
- Index templates for consistent mappings
