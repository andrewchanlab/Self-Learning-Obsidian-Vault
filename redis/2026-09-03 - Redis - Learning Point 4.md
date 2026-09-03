---
title: "2026-09-03 - Redis - Learning Point 4"
tags:
  - learning
  - redis
created: 2026-09-03
---

# Redis Persistence: RDB Snapshots vs AOF Log Are Complementary Strategies

Redis offers two persistence options: RDB takes point-in-time snapshots at intervals (fast, compact, but risks losing data since last snapshot), while AOF (Append Only File) logs every write operation (slower, larger, but more durable). Production deployments often use both: AOF for durability + RDB for fast restarts. The `BGSAVE` command triggers snapshots without blocking the main thread.

## Key Takeaway
RDB and AOF are complementary persistence strategies — use both in production for durability and fast restart.

## Related Concepts
- RDB Snapshots
- AOF
- BGSAVE

---

# Redis 持久化：RDB 快照 vs AOF 日誌是互補策略

Redis 提供兩種持久化選項：RDB 按間隔拍攝時間點快照（快速、緊湊，但有自上次快照以來丟失數據的風險），而 AOF（僅追加文件）記錄每個寫操作（日誌更慢、文件更大，但更持久）。生產環境通常兩者結合使用：AOF 保證持久性 + RDB 加快重啟速度。`BGSAVE` 命令在不阻塞主線程的情況下觸發快照。

## 核心要點
RDB 和 AOF 是互補的持久化策略——生產環境兩者結合使用，兼顧持久性和快速重啟。

## 相關概念
- RDB 快照
- AOF
- BGSAVE
