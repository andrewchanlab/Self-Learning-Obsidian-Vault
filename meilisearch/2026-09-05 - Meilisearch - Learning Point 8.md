---
title: "2026-09-05 - Meilisearch - Learning Point 8"
tags:
  - learning
  - meilisearch
created: 2026-09-05
---

# Meilisearch 的過濾（Filtering）與排序（Sorting）機制

Meilisearch 支援強大的過濾功能——你可以在搜尋時用 `filter` 參數指定條件，例如 `genre = "action" AND year > 2020`。過濾後的結果可以再用 `sort` 參數排序，例如 `sort=year:desc`。These two features are fundamental to building faceted search interfaces（分面搜尋），如電子商務的價格範圍、品牌篩選等。過濾和排序都基於文件欄位的型別——數字、字串、陣列欄位都可以作為過濾/排序的目標。

## API 使用範例
```bash
curl 'http://localhost:7700/indexes/movies/search' \\
  -H 'Content-Type: application/json' \\
  --data-binary '{
    "q": "action",
    "filter": "genre = \"action\" AND year >= 2020",
    "sort": ["year:desc", "rating:desc"],
    "limit": 20
  }'
```

## 重要限制
過濾/排序使用的欄位必須在 index 設定的 `filterableAttributes` 和 `sortableAttributes` 中預先宣告，否則會回傳錯誤。這是為了確保效能——未宣告的欄位不會被建立索引。

## Related Concepts
- Faceted search（分面搜尋）
- Filterable and sortable attributes declaration
- Query-time filtering vs index-time filtering
- Ascending/descending sort
