---
title: "2026-09-04 - MinIO - Learning Point 1"
tags:
  - learning
  - minio
created: 2026-09-04
---

# MinIO Is Your Own Amazon S3 — Object Storage Basics

MinIO is a self-hosted object storage system that speaks the S3 language. Think of it as a huge digital filing cabinet where you store photos, videos, backups, and documents in "buckets". Unlike cloud services where Amazon owns your data, MinIO runs on YOUR servers. It uses erasure coding to spread file pieces across drives — even if some drives fail, your data survives.

## Key Takeaway
MinIO provides S3-compatible object storage that you control entirely, running on your own infrastructure with enterprise-grade durability.

## Related Concepts
- Distributed Storage
- Cloud Native
- Erasure Coding

---

# MinIO 就是你自己的 Amazon S3 — 對象存儲基礎

MinIO 是一個自托管的對象存儲系統，採用與 Amazon S3 相同的協議。可以把它想像成一個巨大的數字文件櫃，用「桶」（buckets）來存放照片、視頻、備份和文檔。與雲服務不同，亞馬遜並不擁有你的數據 — MinIO 运行在你自己的服務器上。它使用糾刪碼（erasure coding）將文件分散存儲在多個硬盤上，即使部分硬盤故障，數據依然完好無損。

## 核心要點
MinIO 提供了完全由你掌控的 S3 兼容對象存儲，運行在自有基礎設施上，具備企業級耐用性。

## 相關概念
- 分布式存儲
- 雲原生
- 糾刪碼
