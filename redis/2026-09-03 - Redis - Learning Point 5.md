---
title: "2026-09-03 - Redis - Learning Point 5"
tags:
  - learning
  - redis
created: 2026-09-03
---

# Redis Transactions Use MULTI/EXEC for Atomic Command Batching

Redis transactions bundle commands with `MULTI` / `EXEC`: all commands between them are queued and executed atomically — no other client commands interleave. If any command fails, `EXEC` returns an error but all commands are still executed (use `WATCH` for optimistic locking to abort on external changes). Transactions do not support rollbacks for logical errors — this is by design for performance.

## Key Takeaway
MULTI/EXEC batches commands atomically; WATCH provides optimistic locking; no rollback for logic errors.

## Related Concepts
- MULTI / EXEC
- WATCH
- Atomic Operations

---

# Redis 事務使用 MULTI/EXEC 實現原子命令批處理

Redis 事務用 `MULTI` / `EXEC` 打包命令：兩者之間的所有命令都會被排隊並原子執行——不會有其他客戶端命令穿插其中。如果任何命令失敗，`EXEC` 會返回錯誤但所有命令仍會執行（使用 `WATCH` 實現樂觀鎖，在外部變化時中止）。事務不支持邏輯錯誤的回滾——這是出於性能考慮的設計選擇。

## 核心要點
MULTI/EXEC 原子批處理命令；WATCH 提供樂觀鎖；不支持邏輯錯誤回滾。

## 相關概念
- MULTI / EXEC
- WATCH
- 原子操作
