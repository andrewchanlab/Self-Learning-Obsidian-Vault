---
title: "2026-09-04 - Certificate Signing - Learning Point 4"
tags:
  - learning
  - cert-signing
created: 2026-09-04
---

# ACME Protocol — Automating Certificate Management

Let's Encrypt popularized the ACME (Automated Certificate Management Environment) protocol. Instead of manually generating CSRs and uploading them to a CA, ACME automates everything: domain validation, certificate issuance, and renewal. Certbot is the most common ACME client — it can install, configure, and auto-renew certificates with zero manual intervention.

## Key Takeaway
ACME automation replaced manual certificate renewal with a programmatic process — certificates can now renew themselves without human intervention.

## Related Concepts
- ACME Protocol
- Let's Encrypt
- Certbot

---

## 中文：ACME 協議 — 自動化憑證管理

Let's Encrypt 推廣了 ACME（自動化憑證管理環境）協議。不再需要手動生成 CSR 並上傳到 CA，ACME 自動化了一切：域名驗證、憑證頒發和續期。Certbot 是最常見的 ACME 客戶端 — 它可以安裝、配置和自動續期憑證，無需人工干預。

### 核心要點
ACME 自動化將手動憑證續期替換為程序化流程 — 憑證現在可以自動續期，無需人為干預。

### 相關概念
- ACME 協議
- Let's Encrypt
- Certbot
