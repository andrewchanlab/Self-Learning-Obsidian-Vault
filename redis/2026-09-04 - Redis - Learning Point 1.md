---
title: "2026-09-04 - Redis - Learning Point 1"
tags:
  - learning
  - redis
created: 2026-09-04
---

# Redis Lives in RAM — The Fastest Storage Tier

Unlike databases that write to disk (slow but persistent), Redis stores everything in RAM. RAM access is 100-1000x faster than NVMe SSD. This makes Redis the ultimate cache layer — user sessions, API responses, and frequently-accessed data live here for sub-millisecond retrieval.

## Key Takeaway
Redis trades data durability for raw speed — by storing data in memory, it achieves performance unattainable with disk-based databases.

## Related Concepts
- In-Memory Computing
- Cache Design
- RAM vs Disk
