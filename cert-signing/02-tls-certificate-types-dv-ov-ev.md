# TLS 憑證類型：DV、OV、EV / TLS Certificate Types: DV, OV, EV

## Learning Point 學習要點

TLS 憑證是網站實現 HTTPS 加密的核心。根據驗證等級，分為三種類型：DV（網域驗證）、OV（組織驗證）、EV（延伸驗證）。

TLS certificates are central to HTTPS encryption. They are divided into three types based on validation level: DV (Domain Validation), OV (Organization Validation), and EV (Extended Validation).

---

## 三種憑證類型比較 / Comparison of Three Certificate Types

| 特性 Feature | DV（網域驗證） Domain Validation | OV（組織驗證） Organization Validation | EV（延伸驗證） Extended Validation |
|---|---|---|---|
| **驗證等級** Validation Level | 低 Low | 中 Medium | 高 High |
| **驗證方式** How | 只需證明你控制該網域 / Prove domain control only | 驗證網域 + 組織存在性 / Domain + organization existence | 嚴格驗證：法律實體、代理人、網域 / Strict: legal entity, agent, domain |
| **頒發速度** Issuance Speed | 數分鐘～數小時 / Minutes to hours | 1～5 天 / 1–5 days | 5～10 天 / 5–10 days |
| **價格** Price | 免費～低價 / Free to low | 中等 / Medium | 高昂 / Expensive |
| **瀏覽器地址欄** Browser Address Bar | 鎖頭圖示（無組織名稱）/ Padlock only (no org name) | 鎖頭圖示 / Padlock | 綠色地址欄 + 組織名稱 / Green bar + org name |
| **適合場景** Use Case | 個人網站、部落格、測試環境 / Personal sites, blogs, testing | 企業網站、內部系統 / Corporate sites, internal systems | 電子商務、金融機構、高信任場景 / E-commerce, finance, high-trust scenarios |

---

## DV（網域驗證）憑證 / Domain Validation Certificate

### 什麼是 DV？/ What is DV?

DV 憑證僅驗證申請者對該網域具有控制權，是最基礎的 TLS 憑證類型。

A DV certificate only verifies that the applicant has control over the domain — the most basic type of TLS certificate.

### 驗證方式 / Validation Methods

```
1. 郵件驗證 / Email Validation
   CA 發送驗證郵件至 admin@example.com
   CA sends verification email to admin@example.com

2. DNS 記錄驗證 / DNS Record Validation
   在網域的 DNS 中新增特定 TXT 記錄
   Add a specific TXT record to the domain's DNS

3. HTTP 文件驗證 / HTTP File Validation
   在網站根目錄放置 CA 提供的驗證文件
   Place a verification file provided by CA in website root
```

### 例子：Let's Encrypt / Example: Let's Encrypt

Let's Encrypt 是最受歡迎的免費 DV 憑證提供者，自動化的 issuance 流程使其成為小型網站的熱門選擇。

Let's Encrypt is the most popular free DV certificate provider, with automated issuance making it a top choice for small websites.

### 優缺點 / Pros and Cons

```
✅ 優點 Advantages:
   - 免費或低成本 / Free or low cost
   - 頒發快速 / Fast issuance
   - 自動續期（ACME 協定）/ Auto-renewal (ACME protocol)

❌ 缺點 Disadvantages:
   - 無法驗證組織真實性 / Cannot verify organization authenticity
   - 攻擊者可用於惡意網站 / Attackers can use for malicious sites
   - 對金融、電商等高風險場景不足 / Insufficient for high-risk scenarios like finance/e-commerce
```

---

## OV（組織驗證）憑證 / Organization Validation Certificate

### 什麼是 OV？/ What is OV?

OV 憑證在 DV 的基礎上，增加了對申請組織真實合法存在的驗證。

An OV certificate adds verification of the organization's legitimate existence on top of DV.

### 驗證內容 / Verification Contents

| 驗證項目 Item | 說明 Description |
|---|---|
| 網域控制權 Domain Control | 與 DV 相同 / Same as DV |
| 組織合法註冊 Organization Legal Registration | 驗證公司已在政府部門註冊 / Verify company is registered with government |
| 組織地址 Organization Address | 驗證地址真實性 / Verify address authenticity |
| 電話驗證 Telephone Verification | CA 會致電組織確認 / CA calls organization to confirm |
| 申請人授權 Applicant Authorization | 確認申請人為組織合法代表 / Confirm applicant is authorized representative |

### 瀏覽器顯示 / Browser Display

點擊瀏覽器鎖頭圖示後，可看到組織名稱：

After clicking the browser padlock, you can see the organization name:

```
🔒 連線安全 / Connection is secure
   憑證有效 / Certificate is valid
   頒發給 / Issued to: Example Corporation Ltd.
   頒發者 / Issued by: GlobalSign Organization Validation CA
```

---

## EV（延伸驗證）憑證 / Extended Validation Certificate

### 什麼是 EV？/ What is EV?

EV 是最嚴格的憑證類型，需要通過 CA/Browser Forum 定義的標準化驗證流程，確認申請組織的法律實體地位、運營存在性，以及授權個人的真實身份。

EV is the strictest certificate type, requiring a standardized validation process defined by the CA/Browser Forum to confirm the organization's legal entity status, operational existence, and the true identity of authorized individuals.

### 嚴格驗證流程 / Strict Validation Process

```
1. 法律實體驗證 / Legal Entity Verification
   ├── 確認組織在政府機關的正式註冊 / Confirm official registration with government
   ├── 驗證組織章程或成立文件 / Verify articles of incorporation
   └── 確認組織未被解散或破產 / Confirm organization is not dissolved/bankrupt

2. 運營存在性驗證 / Operational Existence Verification
   ├── 驗證組織有實際的物理地址 / Verify physical address
   ├── 確認組織有獨立電話線路 / Confirm independent phone line
   └── 驗證銀行帳戶或公用事業帳單 / Verify bank account or utility bills

3. 授權個人驗證 / Authorized Individual Verification
   ├── 確認聯絡人是組織的員工 / Confirm contact is an employee
   ├── 驗證個人身份證件 / Verify personal identity documents
   └── 確認該員工有權申請憑證 / Confirm employee is authorized to request certificates

4. 網域權利驗證 / Domain Right Verification
   └── 與 DV/OV 相同 / Same as DV/OV
```

### 瀏覽器顯示 / Browser Display

EV 憑證在現代瀏覽器中顯示綠色地址欄（部分瀏覽器已移除綠色顯示但仍執行 EV 驗證）：

EV certificates display a green address bar in older browsers (some browsers have removed the green display but still perform EV validation):

```
🟢 https://www.highsecuritybank.com
   頒發給 / Issued to: High Security Bank Corporation
   組織類型 / Organization Type: Public Limited Company
   頒發者 / Issued by: DigiCert Extended Validation CA
```

### 為何 EV 越來越少用？/ Why is EV Declining?

- **費用高昂**：每年數百至數千美元 / High cost: hundreds to thousands of dollars per year
- **頒發緩慢**：需要大量人工審核 / Slow issuance: requires extensive manual review
- **瀏覽器變更**：Chrome 77 起移除了 EV 綠色標示，改為只在憑證資訊中顯示 / Browser changes: Chrome 77+ removed green EV indicator, showing info in certificate details only
- **CT Logs**：Certificate Transparency 日誌提供了替代性的信任信號 / Certificate Transparency logs provide alternative trust signals

---

## 選擇指南 / Selection Guide

```
個人部落格 / Personal Blog
    └── → DV（免費，如 Let's Encrypt）

公司官網 / Corporate Website
    └── → OV（顯示組織名稱，增加信任）

電子商務 / E-commerce
    └── → OV 或 EV（金融相關建議 EV）

銀行金融 / Banking & Finance
    └── → EV + CT Logs（最高信任等級）
```

---

## 面試常見問題 / Common Interview Questions

**Q: DV 憑證是否安全？**
A: DV 憑證提供與 OV/EV 相同的傳輸層加密（TLS 加密）。安全性分為兩層：加密安全（DV=OV=EV）和身份驗證（DV < OV < EV）。DV 適合不需要驗證組織身份的場景。

**Q: Are DV certificates secure?**
A: DV certificates provide the same transport-layer encryption as OV/EV. Security has two layers: encryption security (DV=OV=EV) and identity verification (DV < OV < EV). DV is suitable for scenarios where organizational identity verification is not required.

**Q: 為何很多銀行仍在使用 EV？**
A: 部分金融機構基於合規要求、品牌信任和用戶教育理由繼續使用 EV。雖然瀏覽器已移除綠色標示，但 EV 驗證流程仍在幕後執行。

**Q: Why do many banks still use EV?**
A: Some financial institutions continue using EV based on compliance requirements, brand trust, and user education reasons. Even though browsers removed the green indicator, EV validation process still runs behind the scenes.

---

### 延伸閱讀 / Further Reading

- [CA/Browser Forum EV Guidelines](https://cabforum.org/extended-validation/)
- [Certificate Transparency (CT) Logs](https://www.certificate-transparency.org/)
- [Let's Encrypt Documentation](https://letsencrypt.org/docs/)
