---
title: "2026-09-05 - Elasticsearch - Learning Point 10"
tags:
  - learning
  - elasticsearch
created: 2026-09-05
---

# Elasticsearch 與 Meilisearch 的核心差異與選型指南

兩者都是搜尋引擎，但定位不同。Elasticsearch 是enterprise-grade 的全文搜尋和分析平台，支援複雜的 aggregation、scripting、跨平台整合，代價是較高的學習曲線和運維複雜度。Meilisearch 是 lightweight、易於部署的替代方案，專注於提供出色的開箱即用搜尋體驗，錯字容忍、同義詞、漸進式輸入都是原生支援。但 Meilisearch 不支援 aggregation、無法做 complex analytics、叢集能力也有限。

## 選型決策樹
```
需要複雜 analytics / log 分析？
  → Elasticsearch

只是網站/APP 的內部搜尋？
  → Meilisearch

需要即時错字容忍 + 簡單排序/過濾？
  → Meilisearch

需要 TB 等級資料 + 水平擴展？
  → Elasticsearch

需要最小運維負擔？
  → Meilisearch (或 Meilisearch Cloud)
```

## Related Concepts
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Search relevance tuning
- Managed search services
- When to choose Elasticsearch vs Meilisearch vs Algolia
