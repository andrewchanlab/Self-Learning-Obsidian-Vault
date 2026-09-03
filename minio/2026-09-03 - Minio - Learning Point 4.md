---
title: "2026-09-03 - Minio - Learning Point 4"
tags:
  - learning
  - minio
created: 2026-09-03
---

# MinIO Supports Distributed Mode for High Availability

MinIO in distributed mode runs multiple nodes as a single erasure-coded cluster. Data is automatically sharded and parity blocks computed — you can lose up to half the nodes with zero data loss. This is called N/2 resilience. Adding nodes scales both capacity and throughput linearly. No shared NFS or external storage required.

## Key Takeaway
Distributed mode gives MinIO N/2 resilience with linear scaling.

## Related Concepts
- Erasure Coding
- High Availability
- Horizontal Scaling

---

# MinIO 支援分散式模式以實現高可用性

分散式模式的 MinIO 將多個節點作為單一的糾刪碼集群運行。數據自動分片並計算奇偶校驗塊——你最多可以失去一半的節點而零數據丟失。這稱為 N/2 彈性。添加節點可以線性擴展容量和吞吐量。無需共享 NFS 或外部存儲。

## 核心要點
分散式模式為 MinIO 提供 N/2 彈性和線性擴展能力。

## 相關概念
- 糾刪碼
- 高可用性
- 水平擴展
