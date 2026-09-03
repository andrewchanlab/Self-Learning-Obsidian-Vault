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

---

# 糾刪碼 — 數據耐用性的數學原理

MinIO 將每個文件拆分為數據塊和校驗塊（例如 6 個數據塊 + 3 個校驗塊 = 9 個塊）。即使最多 3 個硬盤同時損壞，MinIO 依然能完美重建每一個文件。這與 RAID 背後的數學原理相同，但專為分布式、企業級存儲而設計。

## 核心要點
糾刪碼讓 MinIO 能夠在承受多個硬盤故障的情況下不丟失數據，同時比傳統全量複製佔用更少的存儲空間。

## 相關概念
- 里德-所羅門碼
- 數據耐用性
- 分布式存儲
