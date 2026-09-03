---
title: "2026-09-03 - Encryption & Decryption - Learning Point 1"
tags:
  - learning
  - encryption
created: 2026-09-03
---

# Password Hashing — Why You Never Store Plain Passwords

## English

Passwords should **never** be stored as-is. When a user registers, you **hash** the password (bcrypt, Argon2, PBKDF2) and store only the hash. At login, you hash the submitted password and compare it to the stored hash. Hashing is **one-way**: you can't derive the original password from the hash.

**Why not encryption?** Encryption is reversible — if the key leaks, all passwords are exposed. Hashing is irreversible by design.

**Salting:** Each password gets a unique random **salt** before hashing. This prevents rainbow table attacks (precomputed hash→password tables) and ensures identical passwords produce different hashes. The salt is stored alongside the hash — it's not secret, just unique per user.

**bcrypt** is the classic choice — it has a built-in salt, configurable cost factor, and is intentionally slow to resist brute-force. **Argon2** (winner of PHC 2015) is more modern and memory-hard.

### Key Takeaway
Never store plain passwords — hash with a salted algorithm (bcrypt or Argon2). Hashing is one-way; if the database leaks, attacker gets hashes they can't reverse. Salting prevents precomputed rainbow table attacks.

### Related Concepts
- bcrypt / Argon2 / PBKDF2
- Salt (cryptographic)
- Rainbow tables
- One-way function
- Cost factor / iteration count

---

## 中文

密碼**永遠不應該**以明文存儲。當用戶註冊時，你**哈希**密碼（bcrypt、Argon2、PBKDF2）並只存儲哈希值。登錄時，你哈希提交的密碼並與存儲的哈希比較。哈希是**單向的**：你無法從哈希反推原始密碼。

**為什麼不用加密？** 加密是可逆的——如果密鑰泄露，所有密碼都暴露了。哈希在設計上不可逆。

**加鹽：** 每個密碼在哈希前都會獲得一個唯一的隨機**鹽值**。這防止彩虹表攻擊（預計算的哈希→密碼表），並確保相同密碼產生不同哈希。鹽值與哈希一起存儲——它不是秘密，只是每個用戶唯一。

**bcrypt** 是經典選擇——它有內置鹽值、可配置的成本因子，並且故意設計得很慢以抵抗暴力破解。**Argon2**（2015年 PHC 冠軍）更現代，內存硬度更高。

### 核心要點
永遠不要以明文存儲密碼——用加鹽算法（bcrypt 或 Argon2）哈希。哈希是單向的；如果數據庫洩露，攻擊者獲得哈希但無法反推。鹽值防止預計算的彩虹表攻擊。

### 相關概念
- bcrypt / Argon2 / PBKDF2
- 鹽值（密碼學）
- 彩虹表
- 單向函數
- 成本因子 / 迭代次數
