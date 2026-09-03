---
title: "2026-03-25 - Redis - Learning Point 1"
tags:
  - learning
  - redis
created: 2026-03-25
---

# Redis as an In-Memory Data Structure Server

Redis (REmote DIctionary Server) is an in-memory key-value store that also supports rich data structures — strings, lists, sets, sorted sets, hashes, bitmaps, and hyperloglogs. Unlike a traditional database where you query with SQL, Redis operations are atomic commands sent over a socket. The critical performance insight is that everything lives in RAM, making reads/writes sub-millisecond. To survive restarts, Redis optionally persists data to disk using RDB snapshots or AOF (Append-Only File) logs, giving you either fast-but-periodic or slower-but-constant durability trade-offs.

## Key Takeaway
Redis trades disk I/O for speed by keeping data in RAM, and its rich data structures let you model complex patterns (queues, leaderboards, pub/sub) directly in the store.

## Related Concepts
- RDB snapshots vs AOF persistence
- Key eviction policies (LRU, LFU, TTL)
- Single-threaded event loop architecture
