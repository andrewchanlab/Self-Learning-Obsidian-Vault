---
title: "2026-09-03 - Certificate Signing - Learning Point 3"
tags:
  - learning
  - cert-signing
created: 2026-09-03
---

# Self-Signed Certificates — When and How to Use Them

## English

A **self-signed certificate** is signed by its own private key — no CA involved. The same key signs and validates the certificate. This means browsers will reject it (they can't verify against a trust store), so it's not suitable for public websites. But for internal/development use, self-signed certs are perfectly fine.

**When to use:**
- Local development (localhost, 127.0.0.1)
- Internal services behind a VPN or firewall
- Testing TLS configurations without paying a CA
- Internal tools, staging environments

**How to create (OpenSSL):**
```bash
# Generate ECDSA private key
openssl ecparam -name prime256v1 -genkey -noout -out key.pem
# Create self-signed cert (valid 365 days)
openssl req -new -x509 -key key.pem -out cert.pem -days 365 \
  -subj "/CN=localhost/O=Dev/C=HK"
# Verify
openssl x509 -in cert.pem -noout -text | head -20
```

To avoid browser warnings on localhost: Chrome accepts `https://localhost` with a self-signed cert if you add the cert to your OS trust store. For local development, **mkcert** automates this entire process.

### Key Takeaway
Self-signed certs skip the CA entirely — useful for local dev, internal services, and staging. Browsers reject them for public sites, but for localhost/VPN-internal use they're the fastest path to TLS.

### Related Concepts
- mkcert (local HTTPS automation)
- OpenSSL x509
- Trust store (adding certs manually)
- Localhost HTTPS
- Internal TLS / VPN

---

## 中文

**自簽名證書** 由其自己的私鑰簽名——不涉及 CA。同樣的密鑰既簽發又驗證證書。這意味著瀏覽器會拒絕它（無法通過信任存儲驗證），所以它不適合公共網站。但對於內部/開發用途，自簽名證書完全沒問題。

**使用時機：**
- 本地開發（localhost、127.0.0.1）
- 在 VPN 或防火牆後面的內部服務
- 在不支付 CA費用的情況下測試 TLS 配置
- 內部工具、預發布環境

**如何創建（OpenSSL）：**
```bash
# 生成 ECDSA 私鑰
openssl ecparam -name prime256v1 -genkey -noout -out key.pem
# 創建自簽名證書（有效期 365 天）
openssl req -new -x509 -key key.pem -out cert.pem -days 365 \
  -subj "/CN=localhost/O=Dev/C=HK"
# 驗證
openssl x509 -in cert.pem -noout -text | head -20
```

要在 localhost 上避免瀏覽器警告：Chrome 如果你將證書添加到操作系統信任存儲中，則接受 `https://localhost` 的自簽名證書。對於本地開發，**mkcert** 自動化整個過程。

### 核心要點
自簽名證書完全跳過 CA——對本地開發、內部服務和預發布環境有用。瀏覽器對公共站點拒絕它們，但對於 localhost/VPN 內部使用，它們是通往 TLS 最快的途徑。

### 相關概念
- mkcert（本地 HTTPS 自動化）
- OpenSSL x509
- 信任存儲（手動添加證書）
- Localhost HTTPS
- 內部 TLS / VPN
