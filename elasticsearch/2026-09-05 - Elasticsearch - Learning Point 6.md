---
title: "2026-09-05 - Elasticsearch - Learning Point 6"
tags:
  - learning
  - elasticsearch
created: 2026-09-05
---

# Elasticsearch 的查詢 DSL（Query DSL）詳解

Elasticsearch 提供一套豐富的 JSON-based Query DSL，區分為兩大類：**Query context**（回答「這個 document 有多匹配」）和 **Filter context**（回答「這個 document 是否符合條件」）。Query context 會計算相關性分數（_score），而 Filter context 不計算分數並且可以被快取。常見的 query 包括 `match`（全文搜尋）、`term`（精確值）、`range`（範圍查詢）、`bool`（組合查詢）。理解這兩種 context 的區分是寫出高效 ES 查詢的關鍵。

## Query vs Filter 對比
| | Query Context | Filter Context |
|--|--------------|----------------|
| 計算分數 | ✅ 是 | ❌ 否 |
| 可快取 | ❌ 否 | ✅ 是 |
| 使用場景 | 全文搜尋相關性 | yes/no 條件過濾 |

## bool 查詢範例
```json
{
  "bool": {
    "must":   [{ "match": { "title": "elasticsearch" } }],
    "filter": [{ "term":  { "status": "published" } }],
    "must_not": [{ "range": { "year": { "lt": 2020 } } }]
  }
}
```

## Related Concepts
- Query context vs filter context
- bool query (must, should, must_not, filter)
- match, term, range queries
- _score relevance scoring
