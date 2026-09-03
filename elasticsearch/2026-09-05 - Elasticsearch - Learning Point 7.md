---
title: "2026-09-05 - Elasticsearch - Learning Point 7"
tags:
  - learning
  - elasticsearch
created: 2026-09-05
---

# Elasticsearch 的倒排索引（Inverted Index）運作原理

倒排索引是 Elasticsearch（準確說是 Lucene）能快速搜尋的核心。每當你索引一份文件，Lucene 會對文字欄位進行分析（analyze）：分詞（tokenize）、小寫化（lowercase）、移除停用詞（stop words）、提取詞根（stemming），然後建立一個從 term 到 document IDs 的映射。例如「The quick brown fox」和「The quick fox」會產生：`quick → [doc1, doc2]`, `brown → [doc1]`, `fox → [doc1, doc2]`。搜尋時只需要在這個映射表裡查詢 term，時間複雜度是 O(1) 而不是 O(n)。

## 倒排索引的結構
- **Terms dictionary**：所有 term 的有序列表，支援二分搜尋
- **Postings list**：每個 term 對應的 document ID 列表
- **Terms index**（可選）：terms dictionary 的稀疏索引，加速定位

## 為什麼比關聯式資料庫快？
關聯式資料庫的全文字搜尋需要 scan every row。倒排索引把 lookup 變成 hash-map 等級的 O(1) 操作，代價是寫入時需要更新索引（寫入放大）。

## Related Concepts
- Tokenization and analyzers
- Posting list compression
- FST (Finite State Automaton) for terms dictionary
- Segment merging and refresh
