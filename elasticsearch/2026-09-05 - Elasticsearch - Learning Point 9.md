---
title: "2026-09-05 - Elasticsearch - Learning Point 9"
tags:
  - learning
  - elasticsearch
created: 2026-09-05
---

# Elasticsearch 的叢集（Cluster）管理與節點類型

Elasticsearch 叢集由多個節點（node）組成，每個節點可以有不同的角色：`master-eligible`（參與 master 選舉）、`data`（儲存分片）、`ingest`（預處理文件）、`coordinating`（負載均衡）。小型部署常見 all-in-one 節點，但生產環境應該分開——特別是 master node 不應該儲存資料，否則大量查詢會影響 cluster management 的穩定性。叢集狀態（cluster state）由 master node 維護並廣播給所有節點，a large cluster with frequent state changes can suffer from master node bottleneck。

## 節點類型總覽
| 節點類型 | 儲存分片 | 處理查詢 | 參與選舉 |
|----------|---------|---------|---------|
| Master-eligible | ❌ | ❌ | ✅ |
| Data | ✅ | ✅ | ❌ |
| Ingest | ❌ | ❌ | ❌ |
| Coordinating | ❌ | ✅ | ❌ |

## Related Concepts
- Master node election (ZenDB / Voting Configurations)
- Cluster state and broadcasting
- Node roles separation in production
- Dedicated master nodes
