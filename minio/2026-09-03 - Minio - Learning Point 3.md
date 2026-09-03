---
title: "2026-09-03 - Minio - Learning Point 3"
tags:
  - learning
  - minio
created: 2026-09-03
---

# MinIO Stores Data as Objects with Metadata

Unlike block or file storage, MinIO stores data as objects — each object bundles the raw data plus user-defined metadata (key-value tags). This enables rich data description without a separate database. Objects can be versioned, encrypted (AES-256), and retain policies applied automatically. The metadata survives with the object through all operations.

## Key Takeaway
MinIO stores data as objects with user-defined metadata.

## Related Concepts
- Object Metadata
- Versioning
- Server-Side Encryption

---

# MinIO 將數據存儲為帶元數據的對象

不同於塊存儲或文件存儲，MinIO 將數據存儲為對象——每個對象捆綁了原始數據和用戶定義的元數據（鍵值標籤）。這使得豐富的數據描述無需額外的數據庫即可實現。對象可以版本化、加密（AES-256），並自動應用保留策略。元數據會伴隨對象在所有操作中保留下來。

## 核心要點
MinIO 將數據存儲為帶用戶定義元數據的對象。

## 相關概念
- 對象元數據
- 版本控制
- 服務端加密
