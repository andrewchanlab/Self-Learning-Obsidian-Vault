---
title: "2026-09-03 - Encryption & Decryption - Learning Point 4"
tags:
  - learning
  - encryption
created: 2026-09-03
---

# Homomorphic Encryption — Computing on Encrypted Data

## English

**Homomorphic Encryption (HE)** lets you perform computations on encrypted data without ever decrypting it. The result of the computation, when decrypted, matches what you'd get if you had done the computation on the plaintext.

Imagine: you encrypt your health data and upload it to a cloud server. The server runs a machine learning model on your encrypted data — it never sees your actual health records — and returns an encrypted prediction. You decrypt it locally and learn your risk score. The cloud never learns anything about your data.

**Why it matters:** Solves the fundamental tension between cloud computing and privacy. You get the benefits of cloud processing without exposing raw data.

**Types:** Partially HE (only additions or multiplications), Somewhat HE (limited depth), Fully HE / FHE (arbitrary computation). FHE is still slow — 10⁴ to 10⁹ times slower than plaintext computation. Libraries: Microsoft SEAL, PALISADE, HEAAN.

### Key Takeaway
Homomorphic Encryption lets cloud services compute on your encrypted data without ever seeing it. FHE is theoretically powerful but currently very slow — practical applications use partially or somewhat HE for specific use cases.

### Related Concepts
- FHE (Fully Homomorphic Encryption)
- Paillier encryption (additive HE)
- Microsoft SEAL
- Privacy-preserving computation
- Cloud security / data isolation

---

## 中文

**同態加密 (HE)** 讓你能夠在加密數據上執行計算，而無需先解密。計算結果在解密後，與在明文上進行相同計算的結果一致。

想像：你加密你的健康數據並上傳到雲端服務器。服務器在你的加密數據上運行機器學習模型——它從未看到你真實的健康記錄——並返回加密的預測結果。你在本地解密並獲得風險評分。雲端從未得知你數據的任何信息。

**為什麼重要：** 解決了雲計算與隱私之間的根本矛盾。你獲得雲端處理的好處，而無需暴露原始數據。

**類型：** 部分 HE（僅加法或乘法）、有限 HE（有限深度）、完全 HE/FHE（任意計算）。FHE 仍然很慢——比明文計算慢 10⁴ 到 10⁹ 倍。庫：Microsoft SEAL、PALISADE、HEAAN。

### 核心要點
同態加密讓雲端服務在你的加密數據上進行計算而從不查看它。FHE 在理論上很強大，但目前非常緩慢——實際應用對特定用例使用部分或有限 HE。

### 相關概念
- FHE（完全同態加密）
- Paillier 加密（加法 HE）
- Microsoft SEAL
- 隱私保護計算
- 雲安全 / 數據隔離
