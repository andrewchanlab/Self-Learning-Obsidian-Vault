---
title: "2026-09-04 - Certificate Signing - Learning Point 1"
tags:
  - learning
  - cert-signing
created: 2026-09-04
---

# PKI — The Trust Hierarchy Behind HTTPS

Public Key Infrastructure (PKI) is the system that makes HTTPS work. It involves Certificate Authorities (CAs), root certificates, intermediate certificates, and end-entity certificates. Your browser trusts a small set of root CAs (pre-installed), which trust intermediate CAs, which trust the certificates websites use. This chain of trust lets you trust a random website without manually trusting each one.

## Key Takeaway
PKI's chain of trust hierarchy means browsers only need to trust ~150 root CAs to trust millions of websites — a scalable trust model.

## Related Concepts
- Certificate Authority
- Root Certificate
- Chain of Trust

---

## 中文：PKI — HTTPS 背後的信任階層

公開金鑰基礎設施（PKI）是讓 HTTPS 運作的系統。它涉及憑證機構（CA）、根憑證、中繼憑證和終端實體憑證。你的瀏覽器信任少量預先安裝的根 CA，而根 CA 信任中繼 CA，中繼 CA 信任網站使用的憑證。這條信任鏈讓你可以信任任意網站，而不需要手動信任每一個。

### 核心要點
PKI 的信任鏈階層結構意味著瀏覽器只需信任約 150 個根 CA，就能信任數百萬個網站 — 這是一個可擴展的信任模型。

### 相關概念
- 憑證機構
- 根憑證
- 信任鏈
