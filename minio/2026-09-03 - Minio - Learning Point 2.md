---
title: "2026-09-03 - Minio - Learning Point 2"
tags:
  - learning
  - minio
created: 2026-09-03
---

# Buckets Are the Top-Level Namespace in MinIO

In MinIO, buckets are the root container for objects — analogous to top-level directories in a filesystem, or root-level DNS domains. Bucket names must be globally unique across the entire deployment. You store files (objects) inside buckets, and each object is identified by a key (file path). You can set policies per bucket to control access.

## Key Takeaway
Buckets are the root container for objects in MinIO.

## Related Concepts
- Bucket Policy
- IAM
- Object Key

---

# Bucket 是 MinIO 中的頂級命名空間

在 MinIO 中，bucket 是對象的根容器——就像文件系統中的頂級目錄，或 DNS 根域。Bucket 名稱在整個部署中必須全局唯一。你將文件（對象）存儲在 bucket 內，每個對象由一個 key（文件路徑）標識。你可以為每個 bucket 設置策略來控制訪問權限。

## 核心要點
Bucket 是 MinIO 中對象的根容器。

## 相關概念
- Bucket 策略
- IAM
- 對象 Key
