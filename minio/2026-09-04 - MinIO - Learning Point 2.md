---
title: "2026-09-04 - MinIO - Learning Point 2"
tags:
  - learning
  - minio
created: 2026-09-04
---

# S3-Compatible Means Universal Compatibility

MinIO implements the Amazon S3 API, meaning any app written for S3 works with MinIO out of the box. This is like having a USB-C port that accepts any USB-C cable — no adapter needed. Tools like boto3 (AWS SDK), rclone, and even the AWS CLI work directly with MinIO, making migration between MinIO and S3 trivial.

## Key Takeaway
The S3 API compatibility means MinIO is a drop-in replacement for AWS S3 — tools and libraries designed for S3 work with MinIO without code changes.

## Related Concepts
- API Compatibility
- Storage Abstraction
- Multi-Cloud Strategy

---

# S3 兼容意味著通用兼容性

MinIO 完整實現了 Amazon S3 API，這意味著任何為 S3 開發的應用都可以零改動地直接使用 MinIO。這就像一個 USB-C 接口能接受任何 USB-C 線纜 — 無需轉接頭。boto3（AWS SDK）、rclone、甚至 AWS CLI 都可以直接對接 MinIO，在 MinIO 和 S3 之間遷移易如反掌。

## 核心要點
S3 API 兼容性使 MinIO 成為 AWS S3 的完美替代品 — 原本為 S3 設計的工具和庫無需任何代碼修改即可使用。

## 相關概念
- API 兼容性
- 存儲抽象層
- 多雲策略
