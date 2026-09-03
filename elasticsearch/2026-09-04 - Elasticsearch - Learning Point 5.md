---
title: "2026-09-04 - Elasticsearch - Learning Point 5"
tags:
  - learning
  - elasticsearch
created: 2026-09-04
---

# Inverted Index — The Secret Behind Blazing Fast Full-Text Search

When you index a document, Elasticsearch doesn't scan every word of every document. Instead, it builds an **inverted index**: a map from every word to the documents that contain it. Searching is just a hash lookup + merge — not a full table scan. This is why Elasticsearch can return results from billions of documents in milliseconds.

## Key Takeaway
Elasticsearch's inverted index turns search from a slow full-scan into a fast dictionary lookup — the core reason it outperforms traditional databases on text search.

## Related Concepts
- Inverted Index
- Full-Text Search
- Apache Lucene

---

# 倒排索引 — 極速全文搜索的秘密

當你索引一份文檔時，Elasticsearch 不會掃描每份文檔的每個單詞。它建立的是一個**倒排索引**：從每個單詞映射到包含它的文檔。搜索只是一次哈希查找 + 合併——而非全表掃描。這就是為什麼 Elasticsearch 能夠在毫秒內從數十億份文檔中返回結果。

## 核心要點
Elasticsearch 的倒排索引將搜索從緩慢的全表掃描變為快速的字典查找——這是它在大規模文本搜索中優於傳統數據庫的核心原因。

## 相關概念
- 倒排索引（Inverted Index）
- 全文搜索（Full-Text Search）
- Apache Lucene
