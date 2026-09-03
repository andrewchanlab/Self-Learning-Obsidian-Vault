---
title: "2026-09-04 - Encryption & Decryption - Learning Point 2"
tags:
  - learning
  - encryption
created: 2026-09-04
---

# Symmetric Encryption Uses One Key for Both Locking and Unlocking

Symmetric encryption uses the same key to encrypt and decrypt data. AES (Advanced Encryption Standard) is the gold standard — it's fast, efficient, and used everywhere from file encryption to HTTPS. The big challenge: you must securely share the key with the recipient before they can read your message. Sending the key over the same insecure channel defeats the whole purpose — this is called the key distribution problem.

## Key Takeaway
Symmetric encryption (e.g., AES) is fast and efficient but requires secure key exchange — the key must reach the recipient without being intercepted.

## Related Concepts
- AES Algorithm
- Symmetric Key
- Key Distribution Problem

---

## 中文：對稱加密用同一把鑰匙鎖門和解鎖

對稱加密使用相同的密鑰來加密和解密數據。AES（高級加密標準）是業界標桿——它速度快、效率高，從文件加密到 HTTPS 到處都在用。最大的挑戰是：你必須在收件人讀懂你的訊息之前，安全地將密鑰交給他們。如果用同一個不安全的渠道發送密鑰，就等於白費功夫——這就是所謂的「密鑰分發問題」。

## 核心要點
對稱加密（如 AES）速度快、效率高，但需要安全地交換密鑰——密鑰必須在不被人截獲的情況下送達收件人。

## 相關概念
- AES 算法
- 對稱密鑰
- 密鑰分發問題
