---
title: "2026-09-03 - Certificate Signing - Learning Point 5"
tags:
  - learning
  - cert-signing
created: 2026-09-03
---

# Certificate Pinning — Locking Keys to Prevent MITM Attacks

## English

**Certificate Pinning** prevents Man-in-the-Middle (MITM) attacks even if an attacker obtains a valid certificate. Instead of trusting any certificate signed by a trusted CA, your app hard-codes which certificate (or public key) is expected for a given domain.

**What you pin (in order of robustness):**
1. **Public key pin** (SPKI pin) — pin the SubjectPublicKeyInfo of the leaf cert. Survives certificate renewal. Most common.
2. **Certificate pin** — pin the entire DER-encoded certificate. More stable but breaks on cert renewal.
3. **Issuer pin** — pin the intermediate CA. Less common.

**How it works:** On first connection, extract and store the pin. On subsequent connections, verify the server's certificate matches the pinned value. If it doesn't match → reject the connection. This stops attackers using a valid cert from a different CA.

**HPKP (HTTP Public Key Pinning)** was deprecated in browsers due to permanent lockout risk if the pinned cert expires. Mobile apps using **SSL pinning libraries** (TrustKit, OkHttp CertificatePinner) don't have this problem — they control the pin refresh cycle through app updates.

### Key Takeaway
Certificate pinning hard-codes which cert/key a domain must present, blocking MITM even if a rogue CA issues a valid cert. Mobile SSL pinning libraries manage the refresh cycle safely; avoid browser HPKP.

### Related Concepts
- Public key pinning / SPKI
- TrustKit / OkHttp CertificatePinner
- HPKP (deprecated)
- MITM attack
- SSL pinning (mobile)

---

## 中文

**證書固定**即使在攻擊者獲得有效證書的情況下，也能防止中間人（MITM）攻擊。你的應用不是信任任何由可信 CA 簽名的證書，而是硬編碼預期給定域名的證書（或公鑰）。

**固定的內容**（按穩健性排序）：
1. **公鑰固定**（SPKI pin）——固定葉證書的 SubjectPublicKeyInfo。在證書更新後仍然有效。最常見。
2. **證書固定**——固定整個 DER 編碼的證書。更穩定但會在證書更新時失效。
3. **簽發者固定**——固定中級 CA。較少見。

**工作原理：** 首次連接時，提取並存儲 pin。後續連接時，驗證伺服器的證書是否與固定值匹配。如果不匹配 → 拒絕連接。這阻止攻擊者使用從不同 CA 獲得的有效證書。

**HPKP（HTTP 公鑰固定）** 因為固定證書過期時永久鎖定的風險已被瀏覽器棄用。使用**證書固定庫**（如 TrustKit、OkHttp CertificatePinner）的手機應用沒有這個問題——它們通過應用更新控制 pin 刷新週期。

### 核心要點
證書固定硬編碼域必須出示的證書/密鑰，即使流氓 CA 簽發有效證書也能阻止 MITM。移動 SSL 固定庫安全地管理刷新週期；避免使用瀏覽器 HPKP。

### 相關概念
- 公鑰固定 / SPKI
- TrustKit / OkHttp CertificatePinner
- HPKP（已棄用）
- MITM 攻擊
- SSL 固定（移動端）
