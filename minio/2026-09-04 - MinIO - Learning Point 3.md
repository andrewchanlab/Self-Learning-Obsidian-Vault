---
title: "2026-09-04 - MinIO - Learning Point 3"
tags:
  - learning
  - minio
created: 2026-09-04
---

# Erasure Coding — The Math Behind Data Durability

MinIO splits each file into data and parity chunks (e.g., 6 data + 3 parity = 9 total chunks). It can lose up to 3 drives and still reconstruct every file perfectly. This is the same mathematical principle behind RAID but designed for distributed, enterprise-scale storage.

## Key Takeaway
Erasure coding lets MinIO survive multiple drive failures without data loss while using less storage overhead than traditional full replication.

## Related Concepts
- Reed-Solomon Codes
- Data Durability
- Distributed Storage
