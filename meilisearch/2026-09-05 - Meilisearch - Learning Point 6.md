---
title: "2026-09-05 - Meilisearch - Learning Point 6"
tags:
  - learning
  - meilisearch
created: 2026-09-05
---

# Meilisearch 的錯字容忍（Typo Tolerance）機制

Meilisearch 最為人稱道的功能之一是錯字容忍——使用者打 "rewiew" 可以找到 "review"，打 "progarmming" 也能找到 "programming"。這是因為 Meilisearch 使用 fuzzy matching 演算法，允許每個詞有 1-2 個字元的編輯距離錯誤（edit distance），視詞的長度而定。短詞（4-6 字）容忍 1 個錯字，長詞（6+ 字）容忍 2 個。This is configurable per index via the `typoTolerance` 設定。

## 配置範例
```json
{
  "typoTolerance": {
    "enabled": true,
    "minWordSizeForTypos": {
      "oneTypo": 4,
      "twoTypos": 8
    }
  }
}
```

## 與 Elasticsearch 的對比
Elasticsearch 需要透過 `fuzziness` 參數手動開啟 fuzzy query，且預設不自動應用於所有查詢。Meilisearch 的錯字容忍是全自動的，無需使用者做任何事情。

## Related Concepts
- Edit distance (Levenshtein distance)
- Fuzzy matching algorithm
- Typo tolerance configuration
- Fuzzy query in Elasticsearch
