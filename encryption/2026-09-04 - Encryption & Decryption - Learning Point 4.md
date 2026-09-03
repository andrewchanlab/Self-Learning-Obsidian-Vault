---
title: "2026-09-04 - Encryption & Decryption - Learning Point 4"
tags:
  - learning
  - encryption
created: 2026-09-04
---

# Hashing Is One-Way — You Can Hash Data but Never Recover It

A hash function takes any input (a password, a file, a sentence) and produces a fixed-length "fingerprint" called a digest. SHA-256 always spits out exactly 256 bits, no matter your input size. The critical property: it's one-way. Given the digest, you cannot reverse-engineer the original input. This makes it perfect for storing passwords — websites store the hash, not your actual password. When you log in, they hash what you typed and compare. Rainbow tables attack this by pre-computing hashes of billions of common passwords — salt (random data added before hashing) defeats rainbow tables.

## Key Takeaway
Hashing is a one-way function — use it for password storage and integrity checks, never for reversible encryption.

## Related Concepts
- SHA-256
- Password Hashing + Salt
- Rainbow Tables

---

## 中文：哈希是單向的——可以計算哈希，但永遠無法逆向恢復

哈希函數將任何輸入（密碼、文件、一句話）轉換成固定長度的「指紋」，稱為摘要。SHA-256 無論輸入多長，都永遠輸出 256 位。關鍵特性：它是單向的。給你一個摘要，你無法反推原始輸入。這使它非常適合存儲密碼——網站只存哈希值，不存你的實際密碼。登錄時，他們會對你輸入的內容做哈希並比較。彩虹表攻擊則是事先計算數十億個常見密碼的哈希值——加鹽（在哈希前添加隨機數據）可以擊敗彩虹表。

## 核心要點
哈希是單向函數——適合用於密碼存儲和完整性校驗，絕不能用於可逆加密。

## 相關概念
- SHA-256
- 密碼哈希 + 加鹽
- 彩虹表
