---
title: "2026-09-04 - Meilisearch - Learning Point 5"
tags:
  - learning
  - meilisearch
created: 2026-09-04
---

# Filterable, Sortable, and Faceted Attributes

Meilisearch lets you combine full-text search with structured filtering and sorting. Designate fields as "filterable" (e.g., `price`, `category`) and "sortable" (e.g., `created_at`, `rating`). When a user searches "laptop" and filters by `price < 1000 AND category = "electronics"`, Meilisearch uses a bitmap index for the filter — extremely fast bitwise operations. Faceted search (showing category counts alongside results) is also built-in, enabling Amazon-style drill-down.

## Key Takeaway
Meilisearch's filter/sort system combines the speed of bitmap indices with the ergonomics of a simple query language — powerful filtering without Elasticsearch complexity.

## Related Concepts
- Bitmap Indices
- Faceted Search
- Filtering and Sorting

---

## 中文：可过滤、可排序、可分面

Meilisearch 让你可以将全文搜索与结构化过滤和排序结合使用。将字段标记为"可过滤"（如 `price`、`category`）和"可排序"（如 `created_at`、`rating`）。当用户搜索"laptop"并按 `price < 1000 AND category = "electronics"` 过滤时，Meilisearch 使用位图索引来处理过滤——极快的位运算确定匹配文档。分面搜索（显示分类计数）也是内置的，实现类似亚马逊的分类下钻体验。

## 核心要点
Meilisearch 的过滤/排序系统将位图索引的速度与简单查询语言的 ergonomics 结合——无 Elasticsearch 的复杂性，却有强大的过滤能力。

## 相关概念
- 位图索引
- 分面搜索
- 过滤与排序
