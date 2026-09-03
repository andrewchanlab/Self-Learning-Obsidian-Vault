---
title: "2026-03-25 - Meilisearch - Learning Point 3"
tags:
  - learning
  - meilisearch
created: 2026-03-25
---

# Filterable, Sortable, and Faceted Attributes

Unlike basic keyword search engines, Meilisearch lets you combine full-text search with structured filtering and sorting. You designate certain fields as "filterable" (e.g., `price`, `category`, `in_stock`) and "sortable" (e.g., `created_at`, `rating`). When a user searches "laptop" and filters by `price < 1000 AND category = "electronics"`, Meilisearch uses a bitmap index for the filter — extremely fast bitwise operations determine matching documents. Faceted search (showing "smartphone," "tablet," "laptop" counts alongside results) is also built-in, enabling Amazon-style category drill-down.

## Key Takeaway
Meilisearch's filter/sort system combines the speed of bitmap indices with the ergonomics of a simple query language — powerful filtering without Elasticsearch complexity.

## Related Concepts
- Bitmap indices for boolean filtering
- Faceted search and navigation
- Distributed search architecture
