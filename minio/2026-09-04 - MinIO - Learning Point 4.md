---
title: "2026-09-04 - MinIO - Learning Point 4"
tags:
  - learning
  - minio
created: 2026-09-04
---

# Distributed Mode: How MinIO Scales Horizontally

MinIO is designed as a distributed object storage system — you run multiple MinIO server nodes together as a single "server pool." Each node contributes its drives to a shared capacity pool, and the erasure coding layer distributes data across all nodes transparently. Adding more nodes increases both capacity AND performance (through parallel I/O), following a "scale-out" model similar to AWS S3 rather than "scale-up" of traditional NAS.

In production you typically run 4–16 nodes per pool, with each node on a separate physical machine. MinIO handles node-level failures through the same erasure coding that handles drive failures — no separate HA layer is needed.

## Key Takeaway
MinIO's distributed mode treats a cluster of servers as a single logical storage pool, scaling capacity and performance together without any shared-NAS dependency.

## Related Concepts
- Server pool vs standalone deployment
- Horizontal scaling (scale-out) vs vertical scaling (scale-up)
- Distributed erasure coding across nodes

---

# 分布式模式：MinIO 如何橫向擴展

MinIO 是一個分布式對象存儲系統 — 你將多個 MinIO 服務器節點組合在一起，作為一個「服務器池」運行。每個節點貢獻其硬盤形成共享容量池，糾刪碼層在所有節點間透明地分發數據。增加更多節點會同時提升容量和性能（通過並行 I/O），遵循的是類似 AWS S3 的「橫向擴展」模式，而非傳統 NAS 的「縱向擴展」。

生產環境中通常每個池部署 4–16 個節點，每個節點位於獨立的物理機上。MinIO 通过处理硬盘故障的同一套纠删码机制来处理节点故障 — 无需单独的 HA 层。

## 核心要點
MinIO 的分布式模式將一群服務器視為單一邏輯存儲池，在無需共享 NAS 的情況下同步擴展容量和性能。

## 相關概念
- 服務器池 vs 獨立部署
- 橫向擴展 vs 縱向擴展
- 跨節點分布式糾刪碼
