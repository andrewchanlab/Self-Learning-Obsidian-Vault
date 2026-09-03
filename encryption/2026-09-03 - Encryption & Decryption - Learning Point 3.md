---
title: "2026-09-03 - Encryption & Decryption - Learning Point 3"
tags:
  - learning
  - encryption
created: 2026-09-03
---

# Digital Signatures — Proving Authenticity and Non-Repudiation

## English

Digital signatures don't encrypt — they **prove** that a message was created by a specific sender and wasn't altered. Think of it like a wax seal on a letter.

**How it works (RSA as example):**
1. Sender hashes the message with SHA-256 → produces a **digest**
2. Sender encrypts the digest with their **private key** → produces the **signature**
3. Sender sends: original message + signature + their **public key**
4. Receiver decrypts the signature with the public key → gets the digest
5. Receiver hashes the message themselves → compares both digests → match = valid

If the message changes by even one byte, the hashes won't match. If you don't have the correct public key, you can't decrypt the signature.

**Common algorithms:** RSA (PKCS#1 v1.5, RSA-PSS), ECDSA (secp256k1, P-256), EdDSA (Ed25519). ECDSA/EdDSA are preferred for new systems — smaller keys and signatures, faster verification.

### Key Takeaway
Signatures prove authorship and integrity, not confidentiality. Hash the message, encrypt the hash with the sender's private key. Anyone with the public key can verify; only the private key holder could have signed.

### Related Concepts
- Public key / private key
- RSA / ECDSA / EdDSA
- SHA-256 digest
- PKCS#1 v1.5 / RSA-PSS
- Non-repudiation

---

## 中文

數字簽名不加密——它**證明**消息由特定發送者創建且未被篡改。可以把它想像成信件上的蠟封。

**工作原理（以 RSA 為例）：**
1. 發送者用 SHA-256 對消息進行哈希 → 產生**摘要**
2. 發送者用他們的**私鑰**加密摘要 → 產生**簽名**
3. 發送者發送：原始消息 + 簽名 + 他們的**公鑰**
4. 接收者用公鑰解密簽名 → 獲得摘要
5. 接收者自己對消息進行哈希 → 比較兩個摘要 → 匹配 = 有效

如果消息哪怕只改變一個字節，哈希就不匹配。如果你沒有正確的公鑰，就無法解密簽名。

**常見算法：** RSA（PKCS#1 v1.5、RSA-PSS）、ECDSA（secp256k1、P-256）、EdDSA（Ed25519）。新系統首選 ECDSA/EdDSA——密鑰和簽名更小，驗證更快。

### 核心要點
簽名證明作者身份和完整性，不證明保密性。哈希消息，用發送者的私鑰加密哈希。任何擁有公鑰的人都可以驗證；只有私鑰持有者才能簽名。

### 相關概念
- 公鑰 / 私鑰
- RSA / ECDSA / EdDSA
- SHA-256 摘要
- PKCS#1 v1.5 / RSA-PSS
- 不可否認性
