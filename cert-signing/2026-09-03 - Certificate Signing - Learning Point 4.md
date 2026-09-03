---
title: "2026-09-03 - Certificate Signing - Learning Point 4"
tags:
  - learning
  - cert-signing
created: 2026-09-03
---

# PKCS Standards — PKCS#7, PKCS#8, PKCS#12 Explained

## English

The **PKCS (Public Key Cryptography Standards)** are a family of RSA Labs standards defining how cryptographic objects are formatted. Three are most relevant in everyday TLS/certificate work:

**PKCS#7 / CMS (Cryptographic Message Syntax):** A format for signing and/or encrypting data. Certificate chains are often exchanged as `.p7b` or `.p7c` files — a PKCS#7 envelope containing multiple certificates. Encode a chain: `openssl crl2pkcs7 -nocrl -certfile chain.pem -out certs.p7b`

**PKCS#8:** The standard format for **private keys**. A PKCS#8 file holds an RSA, EC, or any private key, optionally encrypted with a password (PBKDF2/AES). Most modern systems output PKCS#8. Convert: `openssl pkcs8 -topk8 -v2 aes256 -in key.pem -out key-p8.pem`

**PKCS#12:** A **keystore** bundling a private key + its certificate + intermediates into one password-protected file. Used by Java (`keytool`), Windows, and for identity cert import/export. `.pfx` files on Windows are PKCS#12. Extract: `openssl pkcs12 -in identity.pfx -nokeys -out cert.pem`

### Key Takeaway
PKCS#8 = private key format (often encrypted). PKCS#7/.p7b = certificate chain envelope. PKCS#12/.pfx = keystore bundling key + cert(s). Know which format your system expects.

### Related Concepts
- PKCS#7 / CMS / .p7b
- PKCS#8 (private key)
- PKCS#12 / .pfx (keystore)
- Java keytool
- OpenSSL pkcs8 / pkcs12

---

## 中文

**PKCS（公鑰密碼學標準）** 是 RSA Labs 標準系列，定義了密碼學對象的格式。三個標準與日常 TLS/證書工作最相關：

**PKCS#7 / CMS（密碼消息語法）：** 用於簽名和/或加密數據的格式。證書鏈通常以 `.p7b` 或 `.p7c` 文件形式交換——一個包含多個證書的 PKCS#7 信封。編碼鏈：`openssl crl2pkcs7 -nocrl -certfile chain.pem -out certs.p7b`

**PKCS#8：** **私鑰**的標準格式。PKCS#8 文件容納 RSA、EC 或任何私鑰，可選擇用密碼加密（PBKDF2/AES）。大多數現代系統輸出 PKCS#8。轉換：`openssl pkcs8 -topk8 -v2 aes256 -in key.pem -out key-p8.pem`

**PKCS#12：** 一種**密鑰庫**將私鑰 + 其證書 + 中級捆綁到一個密碼保護的文件中。由 Java（`keytool`）、Windows 使用，以及用於身份證書導入/導出。Windows 上的 `.pfx` 文件就是 PKCS#12。提取：`openssl pkcs12 -in identity.pfx -nokeys -out cert.pem`

### 核心要點
PKCS#8 = 私鑰格式（通常加密）。PKCS#7/.p7b = 證書鏈信封。PKCS#12/.pfx = 捆綁密鑰 + 證書的密鑰庫。知道你系統期望哪種格式。

### 相關概念
- PKCS#7 / CMS / .p7b
- PKCS#8（私鑰）
- PKCS#12 / .pfx（密鑰庫）
- Java keytool
- OpenSSL pkcs8 / pkcs12
