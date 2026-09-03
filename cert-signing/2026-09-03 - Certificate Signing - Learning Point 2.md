---
title: "2026-09-03 - Certificate Signing - Learning Point 2"
tags:
  - learning
  - cert-signing
created: 2026-09-03
---

# CSR — Certificate Signing Request Walkthrough

## English

A **CSR (Certificate Signing Request)** is the file you send to a Certificate Authority to get your certificate issued. It contains your public key and identity info, digitally signed by you (the applicant).

**What a CSR contains:**
- Your public key (the one your server will use)
- Common Name (CN) — typically your domain name
- Subject Alternative Names (SANs) — additional domains/subdomains
- Organization, Country, State (for OV/EV certs)
- A signature over all the above, made with your **private key**

**The CA's role:** The CA verifies your identity (domain ownership, organization docs for OV, legal existence for EV), then creates a certificate binding your public key to your identity, and signs it with the CA's private key.

**Tools to generate a CSR:**
```bash
# OpenSSL ECDSA CSR
openssl ecparam -name prime256v1 -genkey -noout -out key.pem
openssl req -new -key key.pem -out csr.pem -subj "/CN=example.com"
# View CSR contents
openssl req -in csr.pem -noout -text
```

### Key Takeaway
A CSR is your application to a CA — it contains your public key and identity, signed by your private key. The CA then issues a certificate binding your identity to your public key, signed by the CA's private key.

### Related Concepts
- Common Name (CN) / SAN
- OV / EV certificates
- CA private key signing
- OpenSSL req
- Certificate issuance workflow

---

## 中文

**CSR（證書簽名請求）** 是你發送給證書頒發機構以獲取證書的文件。它包含你的公鑰和身份信息，由你（申請者）數字簽名。

**CSR 包含的內容：**
- 你的公鑰（你的伺服器將使用的）
- 通用名稱（CN）——通常是你的域名
- 主體備選名稱（SANs）——附加域名/子域名
- 組織、國家、州（用於 OV/EV 證書）
- 對上述所有內容的簽名，使用你的**私鑰**製作

**CA 的角色：** CA 驗證你的身份（域名所有權、OV 的組織文檔、EV 的法律存在），然後創建一個將你的公鑰綁定到你的身份的證書，並用 CA 的私鑰簽名。

**生成 CSR 的工具：**
```bash
# OpenSSL ECDSA CSR
openssl ecparam -name prime256v1 -genkey -noout -out key.pem
openssl req -new -key key.pem -out csr.pem -subj "/CN=example.com"
# 查看 CSR 內容
openssl req -in csr.pem -noout -text
```

### 核心要點
CSR 是你向 CA 的申請——它包含你的公鑰和身份，由你的私鑰簽名。CA 然後簽發一個將你的身份綁定到你的公鑰的證書，由 CA 的私鑰簽名。

### 相關概念
- 通用名稱（CN）/ SAN
- OV / EV 證書
- CA 私鑰簽名
- OpenSSL req
- 證書簽發工作流程
