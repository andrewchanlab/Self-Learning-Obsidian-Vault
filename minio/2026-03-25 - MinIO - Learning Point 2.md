---
title: "2026-03-25 - MinIO - Learning Point 2"
tags:
  - learning
  - minio
created: 2026-03-25
---

# Erasure Coding: How MinIO Achieves Data Durability

MinIO uses erasure coding to protect data against hardware failures without traditional RAID. Data is split into data chunks and parity chunks — for example, a 10-drive setup might use 6 data + 4 parity blocks. This allows MinIO to reconstruct missing data blocks on the fly, achieving up to 14TB of raw capacity per instance while maintaining enterprise-grade durability. This approach is mathematically optimal: you get maximum storage efficiency for a given level of fault tolerance.

## Key Takeaway
Erasure coding lets MinIO deliver RAID-like data protection with better storage efficiency and no performance bottlenecks during rebuilds.

## Related Concepts
- Reed-Solomon error correction
- Data parity and checksums
- Distributed storage fault tolerance
