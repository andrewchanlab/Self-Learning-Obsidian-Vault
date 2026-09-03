---
title: "2026-09-04 - Certificate Signing - Learning Point 2"
tags:
  - learning
  - cert-signing
created: 2026-09-04
---

# TLS Certificates — The Digital ID Cards of the Internet

A TLS certificate binds a public key to a domain name (and optionally organization). It contains: the public key, the domain name it belongs to, the validity period, the issuer (CA), and the CA's digital signature. When you visit https://example.com, the server presents its certificate proving it owns the private key for that domain.

## Key Takeaway
TLS certificates are verifiable identity proofs — they prove a server owns the private key corresponding to a domain name.

## Related Concepts
- TLS Handshake
- Server Certificate
- Domain Validation

---

## 中文：TLS 憑證 — 互聯網的數碼身份證

TLS 憑證將公鑰綁定到域名（也可選機構）。它包含：公鑰、所屬域名、有效期限、頒發者（CA）和 CA 的數碼簽名。當你訪問 https://example.com 時，伺服器出示其憑證，證明它擁有該域名的私鑰。

### 核心要點
TLS 憑證是可驗證的身份證明 — 它們證明伺服器擁有與域名對應的私鑰。

### 相關概念
- TLS 握手
- 伺服器憑證
- 網域驗證
