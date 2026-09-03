# PKI 與憑證授權階層 / PKI and Certificate Authority Hierarchy

## Learning Point 學習要點

### 什麼是 PKI？/ What is PKI?

**PKI（公開金鑰基礎設施，Public Key Infrastructure）** 是一套管理數位憑證與公開金鑰的系統，讓互聯網上的身份認證與加密通訊成為可能。

**PKI (Public Key Infrastructure)** is a system for managing digital certificates and public keys, enabling authentication and encrypted communication over the internet.

---

### 核心組成 / Core Components

| 組件 Component | 角色 Role | 說明 Description |
|---|---|---|
| **CA（憑證授權中心）** | Certificate Authority | 發行與管理數位憑證的受信任機構 / Trusted entity that issues and manages digital certificates |
| **RA（註冊授權機構）** | Registration Authority | 驗證憑證申請者身份的機構 / Entity that verifies identity of certificate applicants |
| **CRL（憑證撤銷清單）** | Certificate Revocation List | 被撤銷憑證的黑名單 / Blacklist of revoked certificates |
| **OCSP（線上憑證狀態協定）** | Online Certificate Status Protocol | 即時查詢憑證狀態的協定 / Protocol for real-time certificate status queries |

---

### 憑證授權階層 / CA Hierarchy

```
         🌟 Root CA（根憑證機構）
              │
              ├── Intermediate CA 1（中繼憑證機構）
              │        │
              │        └── Issuing CA（發行憑證機構）→ 發行終端實體憑證
              │
              └── Intermediate CA 2（中繼憑證機構）
                       │
                       └── Issuing CA → 發行終端實體憑證
```

**1. Root CA（根憑證機構）**
- PKI 信任鏈的頂點 / The apex of the PKI trust chain
- 通常離線儲存，防止被盜用 / Usually stored offline to prevent theft
- 自我簽署（Self-Signed）憑證 / Self-signed certificates

**2. Intermediate CA（中繼憑證機構）**
- 介於 Root CA 與終端憑證之間 / Between Root CA and end-entity certificates
- 分散風險，避免 Root CA 被直接用於簽發 / Reduces risk by isolating Root CA
- 由 Root CA 簽署 / Signed by the Root CA

**3. Issuing CA / End-Entity Certificate（發行憑證 / 終端實體憑證）**
- 直接頒發給網站或組織的憑證 / Certificates issued directly to websites or organizations
- 由 Intermediate CA 簽署 / Signed by Intermediate CA

---

### 信任鏈驗證 / Trust Chain Verification

瀏覽器驗證 TLS 憑證時，會沿著憑證鏈向上追溯至受信任的 Root CA：

When a browser verifies a TLS certificate, it traces up the chain to a trusted Root CA:

```
瀏覽器瀏覽 example.com
Browser visits example.com
        │
        ▼
  leaf certificate（example.com）
        │ 由 Intermediate CA 簽署 / Signed by Intermediate CA
        ▼
  intermediate certificate
        │ 由 Root CA 簽署 / Signed by Root CA
        ▼
  root certificate → 作業系統/瀏覽器內建受信任根憑證
  (stored in OS/browser trust store)
```

---

### 為什麼需要階層式設計？/ Why a Hierarchical Design?

- **安全性**：Root CA 保持離線，萬一 Intermediate CA 被入侵，Root 不受影響 / Security: Root CA stays offline — if Intermediate CA is compromised, Root remains safe
- **靈活性**：可快速撤銷或更換 Intermediate CA / Flexibility: Easy to revoke or replace Intermediate CAs
- **可控性**：大型組織可擁有自己的私有 PKI / Control: Organizations can run private PKIs

---

### 標準與規範 / Standards and Specifications

| 標準 Standard | 內容 Content |
|---|---|
| **X.509** | 數位憑證的標準格式 / Standard format for digital certificates |
| **PKCS#7/CMS** | 憑證簽章封裝格式 / Certificate signature envelope format |
| **PKCS#12** | 憑證與私鑰的交換格式 / Exchange format for certificates and private keys |
| **RFC 5280** | Internet X.509 公開金鑰基礎設施憑證與 CRL 設定檔 / PKI certificate and CRL profile |

---

### 快速記憶 / Quick Memory Aid

> **PKI = CA Hierarchy + Digital Certificates + Trust Chain**
> Think of it like a government ID system:
> - **Root CA** = 公安部（最高信任）/ Ministry of Public Security (highest trust)
> - **Intermediate CA** = 省市級公安局 / Provincial police
> - **End-entity cert** = 身份證（個人）/ ID card (individual)

---

### 面試常見問題 / Common Interview Questions

**Q: 為什麼 Root CA 要保持離線？**
A: 因為 Root CA 是整個 PKI 信任體系的根基，一旦 Root CA 的私鑰被盜，攻擊者可偽造任何憑證，整個 PKI 將失去信任。離線儲存能大幅降低被盜風險。

**Q: Why should Root CAs stay offline?**
A: Because the Root CA is the foundation of the entire PKI trust system. If a Root CA's private key is stolen, an attacker can forge any certificate, collapsing the entire PKI. Offline storage dramatically reduces theft risk.

---

### 延伸閱讀 / Further Reading

- [RFC 5280 - PKIX Certificate and CRL Profile](https://tools.ietf.org/html/rfc5280)
- [What is PKI?](https://en.wikipedia.org/wiki/Public_key_infrastructure)
