---
title: "2026-09-03 - Encryption & Decryption - Learning Point 2"
tags:
  - learning
  - encryption
created: 2026-09-03
---

# Key Derivation Functions — PBKDF2, scrypt, and Argon2

## English

A **Key Derivation Function (KDF)** stretches a weak password into a strong cryptographic key. Instead of using the password directly, you feed it through thousands of iterations of a hash function, making brute-force attacks exponentially harder.

**PBKDF2** (RFC 2899): Applies a hash function (SHA-256 or SHA-512) thousands of times. Simple, widely supported, but vulnerable to GPU acceleration since it needs little memory.

**scrypt**: Uses a large memory-hard internal table. GPUs can't parallelize it efficiently because they'd need enormous on-chip memory — making it much costlier for attackers.

**Argon2** (2015 Password Hashing Competition winner): The modern standard. Has three variants — Argon2d (GPU-resistant), Argon2i (side-channel resistant), Argon2id (hybrid). Configurable time, memory, and parallelism. Best choice for new systems.

All KDFs take: **password + salt + iteration count (or time/memory parameters) → derived key**.

### Key Takeaway
KDFs convert weak passwords into strong keys by iterating a hash many times. Use Argon2id for new systems (best memory-hardness), scrypt as a proven alternative, and avoid PBKDF2 for new designs due to GPU vulnerability.

### Related Concepts
- PBKDF2 (RFC 2899)
- scrypt (memory-hard)
- Argon2 / Argon2id
- GPU-resistant hashing
- Salt (as KDF input)

---

## 中文

**密鑰派生函數 (KDF)** 將弱密碼擴展為強密碼密鑰。不是直接使用密碼，而是通過哈希函數的數千次迭代處理它，使暴力破解攻擊難度呈指數級上升。

**PBKDF2**（RFC 2899）：將哈希函數（SHA-256 或 SHA-512）應用數千次。簡單、广泛支持，但容易受到 GPU 加速攻擊，因為它只需要很少內存。

**scrypt**：使用大型內存硬內部表。GPU 無法有效並行化，因為它們需要巨大的芯片內存——這使得攻擊者代價更高。

**Argon2**（2015 年密碼哈希競賽冠軍）：現代標準。有三種變體——Argon2d（抗 GPU）、Argon2i（抗側通道）、Argon2id（混合）。可配置時間、內存和並行度。新系統的最佳選擇。

所有 KDF 都接受：**密碼 + 鹽值 + 迭代次數（或時間/內存參數）→ 派生密鑰**。

### 核心要點
KDF 通過多次迭代哈希將弱密碼轉換為強密鑰。新系統使用 Argon2id（最佳內存硬度），scrypt 作為經過驗證的替代方案，由於 GPU 漏洞避免在新設計中使用 PBKDF2。

### 相關概念
- PBKDF2（RFC 2899）
- scrypt（內存硬）
- Argon2 / Argon2id
- 抗 GPU 哈希
- 鹽值（作為 KDF 輸入）
