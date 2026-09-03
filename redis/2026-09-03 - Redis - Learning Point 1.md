---
title: "2026-09-03 - Redis - Learning Point 1"
tags:
  - learning
  - redis
created: 2026-09-03
---

# Redis Key-Value Model: Everything Is Stored and Retrieved by a String Key

Redis is a key-value store — you set a value with `SET key value` and retrieve it with `GET key`. Keys are binary-safe strings (can contain any data). Values support multiple data structures: strings, lists, sets, sorted sets, hashes, bitmaps, hyperloglogs, and geospatial indexes. This variety makes Redis a versatile data server, not just a simple cache.

## Key Takeaway
Redis stores values by string keys and supports rich data structures beyond simple strings.

## Related Concepts
- Data Structures
- Key Design
- SET / GET Commands

---

# Redis 鍵值模型：所有數據都通過字符串鍵存儲和檢索

Redis 是一個鍵值存儲——你用 `SET key value` 設置值，用 `GET key` 檢索。鍵是二進制安全的字符串（可以包含任何數據）。值支持多種數據結構：字符串、列表、集合、有序集合、哈希、位圖、HyperLogLog 和地理空間索引。這種多樣性使 Redis 不僅是簡單的緩存，而是一個多功能的數據服務器。

## 核心要點
Redis 通過字符串鍵存儲值，並支持超越簡單字符串的豐富數據結構。

## 相關概念
- 數據結構
- 鍵設計
- SET / GET 命令
