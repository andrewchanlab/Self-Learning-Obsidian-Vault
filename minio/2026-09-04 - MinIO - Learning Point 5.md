---
title: "2026-09-04 - MinIO - Learning Point 5"
tags:
  - learning
  - minio
created: 2026-09-04
---

# Bucket Replication and Versioning

MinIO supports **bucket versioning** (keeping multiple versions of the same object) and **bucket replication** (asynchronously copying objects to a second MinIO cluster). Versioning is enabled per-bucket and lets you retrieve any previous version of an object — useful for accidental deletion/overwrite protection without needing external backups.

Bucket replication works in two modes: **active-passive** (one-way sync from source to replica cluster) and **active-active** (bi-directional sync between two clusters). Replication is asynchronous and S3-compatible — it uses the same `s3:Replication` configuration XML that AWS S3 uses, meaning tools like the AWS CLI work directly against MinIO with no modifications.

Site replication goes beyond simple object copy: it also replicates IAM policies, bucket configurations, and lifecycle rules, making it suitable for disaster recovery and multi-region active-active deployments.

## Key Takeaway
MinIO's versioning and replication features provide S3-compatible data protection and disaster recovery — enabling active-passive or active-active topologies with no vendor lock-in.

## Related Concepts
- Object versioning and lifecycle policies
- Active-passive vs active-active replication
- Site-level replication for DR

---

# 桶複製與版本控制

MinIO 支持**桶版本控制**（保留同一對象的多個版本）和**桶複製**（異步將對象複製到第二個 MinIO 集群）。版本控制按桶開啟，可以調取對象的任意歷史版本 — 無需外部備份即可防止意外刪除或覆蓋。

桶複製有兩種模式：**主動-被動**（從源集群單向同步到副本集群）和**雙向同步**（兩個集群之間的雙向同步）。複製是異步的且兼容 S3 — 使用與 AWS S3 相同的 `s3:Replication` 配置 XML，意味著 AWS CLI 等工具可直接對接 MinIO，無需任何修改。

站點複製不僅僅是簡單的對象複製：它還會同步 IAM 策略、桶配置和生命週期規則，適合災難恢復和多區域雙向同步部署。

## 核心要點
MinIO 的版本控制和複製功能提供了兼容 S3 的數據保護和災難恢復能力 — 可實現主動-被動或雙向同步架構，無需供應商綁定。

## 相關概念
- 對象版本控制與生命週期策略
- 主動-被動 vs 雙向複製
- 站點級複製實現災難恢復
