---
title: "2026-09-03 - Redis - Learning Point 3"
tags:
  - learning
  - redis
created: 2026-09-03
---

# Redis Streams Are a Log-Based Data Structure for Event Sourcing

Redis Streams (`XADD`, `XREAD`, `XRANGE`, `XGROUP`) implement an append-only log structure similar to Kafka. Consumers form consumer groups for parallel processing, each message delivered exactly once within a group. Streams support consumer acknowledgment, blocking reads, and range queries. They are ideal for building event-sourced systems, job queues, and real-time analytics pipelines.

## Key Takeaway
Redis Streams provide a Kafka-like log structure with consumer groups and exactly-once delivery.

## Related Concepts
- Streams
- Consumer Groups
- Event Sourcing

---

# Redis Streams 是用於事件溯源的日誌型數據結構

Redis Streams（`XADD`、`XREAD`、`XRANGE`、`XGROUP`）實現了類似 Kafka 的只追加日誌結構。消費者形成消費者組以並行處理，每條消息在組內只傳遞一次。Streams 支持消費者確認、阻塞讀取和範圍查詢。它們是構建事件溯源系統、作業隊列和實時分析管道的理想選擇。

## 核心要點
Redis Streams 提供類似 Kafka 的日誌結構，帶消費者組和精確一次傳遞保證。

## 相關概念
- Streams
- 消費者組
- 事件溯源
