---
title: "2026-09-05 - Elasticsearch - Learning Point 8"
tags:
  - learning
  - elasticsearch
created: 2026-09-05
---

# Elasticsearch 的分片（Sharding）與副本（Replica）策略

每個 Elasticsearch index 由多個分片（shard）組成，每個分片是一個獨立的 Lucene 索引。預設情况下 index 有 1 個 primary shard（可調整），但可以在建立 index 時指定更多。副本（replica）是 primary shard 的複製，當 primary 所在節點掛掉時會自動提升為 primary，確保高可用。分片數量在 index 建立後就固定了，後悔代價很高（需要 reindex），所以規劃時要考慮未來資料增長。過多分片會增加 overhead，過少則無法水平擴展。

## 分片數量規劃公式（經驗法則）
```
最佳分片數 ≈ 節點數 × (30-50GB heap per node) / 資料量大小
```
或者：
```
分片數 = 預期資料量 / 50GB（每分片理想大小）
```

## 常見錯誤
- `number_of_shards: 5` 設在 index settings 後就無法改變（除非 reindex）
- `number_of_replicas` 可以隨時調整，這個不怕

## Related Concepts
- Primary shard vs replica shard
- Shard allocation and routing
- Index lifecycle management (ILM)
- Hot-warm-cold architecture
