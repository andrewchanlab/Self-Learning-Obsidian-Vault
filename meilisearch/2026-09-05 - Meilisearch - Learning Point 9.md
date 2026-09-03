---
title: "2026-09-05 - Meilisearch - Learning Point 9"
tags:
  - learning
  - meilisearch
created: 2026-09-05
---

# Meilisearch 的聚合（Aggregation）與分面搜尋（Faceted Search）

當你有電子商務網站，使用者搜尋「運動鞋」時，通常希望看到「品牌：Nike、Adidas...」和「價格區間：0-500、500-1000...」這樣的分面導航。Meilisearch 的 `facets` 參數讓你一次返回每個 facet 的文件計數（facet distribution）。Elasticsearch 的 aggregation 概念類似，但 Meilisearch 更加無縫——你只需要宣告哪些欄位是 facets，搜尋時指定 `facets=["brand", "category"]`，結果就會包含每個 facet 值對應的文件數量。

## Facets vs Aggregations
| 特性 | Meilisearch Facets | Elasticsearch Aggregations |
|------|--------------------|----------------------------|
| 語法複雜度 | 簡單，宣告式 | 複雜，JSON DSL |
| 即時分面計數 | 內建 | 需寫 aggregation query |
| 效能 | 自動優化 | 需要手動優化 |

## Related Concepts
- Faceted navigation in e-commerce
- Facet distribution counts
- Elasticsearch aggregations (terms, range)
- Drill-down filtering
