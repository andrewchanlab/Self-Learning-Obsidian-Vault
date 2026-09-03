---
title: "2026-09-04 - Certificate Signing - Learning Point 5"
tags:
  - learning
  - cert-signing
created: 2026-09-04
---

# Self-Signed Certificates — When to Roll Your Own

Self-signed certificates are certificates where the issuer and subject are the same entity — no CA in the middle. Browsers reject them for public sites because there's no trusted third party to verify identity. But they're perfectly fine for internal development, staging environments, or local services behind a VPN. OpenSSL is the classic tool to generate them: `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365`.

## Key Takeaway
Self-signed certificates work when trust is established by other means (e.g., network isolation) — they're not a flaw, just the wrong tool for public HTTPS.

## Related Concepts
- OpenSSL
- Self-Signed Certificate
- Internal PKI

---

## 中文：自簽名憑證 — 何時使用自己生成的

自簽名憑證是頒發者和主題相同的憑證 — 中間沒有 CA。瀏覽器會拒絕它們用於公共網站，因為沒有可信的第三方來驗證身份。但它們非常適合內部開發、預發布環境或 VPN 後的本地服務。OpenSSL 是生成它們的經典工具：`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365`。

### 核心要點
當信任由其他方式建立時（例如網絡隔離），自簽名憑證可以正常工作 — 它們不是缺陷，只是對公共 HTTPS 來說用錯了工具。

### 相關概念
- OpenSSL
- 自簽名憑證
- 內部 PKI
