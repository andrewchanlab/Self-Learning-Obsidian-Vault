---
title: "2026-09-03 - Certificate Signing - Learning Point 1"
tags:
  - learning
  - cert-signing
created: 2026-09-03
---

# Certificate Chains — From Root CA to End-Entity Certificate

## English

When you visit `https://example.com`, your browser doesn't just check one certificate — it follows a **certificate chain** up to a trusted Root CA.

**The chain (bottom to top):**
1. **End-entity certificate** — `example.com`, issued by an Intermediate CA. Contains your public key, domain name, validity dates, and the digital signature of the issuer.
2. **Intermediate CA certificate(s)** — intermediate authorities between the Root and end-entity. Each signs the one below it. Chains can have 1–3 intermediates.
3. **Root CA certificate** — pre-installed in your OS/browser's trust store. Self-signed. The buck stops here.

**Why intermediates?** Root CAs never issue end-entity certs directly — they sign intermediates, which do the actual issuance. If an intermediate is compromised, the Root can revoke it without replacing the Root itself.

Your browser verifies each signature in the chain, checks validity dates, and confirms the Root is in the trust store. If any step fails → TLS connection fails with a certificate error.

### Key Takeaway
Certificate chains go from end-entity → intermediate(s) → Root CA. Browsers trust only the Root; intermediates and end-entity certs are validated by signature. Compromised intermediates can be revoked without touching the Root.

### Related Concepts
- Root CA (Certificate Authority)
- Intermediate CA
- Trust store (OS / browser)
- TLS handshake
- Certificate revocation

---

## 中文

當你訪問 `https://example.com` 時，你的瀏覽器不是只檢查一個證書——它會沿著**證書鏈**向上追溯到可信的根 CA。

**鏈條（從下到上）：**
1. **終端實體證書** — `example.com`，由中級 CA 簽發。包含你的公鑰、域名、有效期，以及簽發者的數字簽名。
2. **中級 CA 證書** — 位於根和終端實體之間的中間機構。每個都簽名下一個。鏈可以有 1–3 個中級。
3. **根 CA 證書** — 預裝在你操作系統/瀏覽器的信任存儲中。自簽名。一切在此終止。

**為什麼要有中級？** 根 CA 從不直接簽發終端實體證書——它們簽發中級，中級負責實際簽發。如果中級被洩露，根可以撤銷它而無需替換根本身。

你的瀏覽器驗證鏈中的每個簽名、檢查有效期，並確認根在信任存儲中。任何一步失敗 → TLS 連接失敗並顯示證書錯誤。

### 核心要點
證書鏈從終端實體 → 中級 → 根 CA。瀏覽器只信任根；中級和終端實體證書通過簽名驗證。被洩露的中級可以撤銷而不影響根。

### 相關概念
- 根 CA（證書頒發機構）
- 中級 CA
- 信任存儲（操作系統 / 瀏覽器）
- TLS 握手
- 證書撤銷
