---
title: "2026-09-03 - Encryption & Decryption - Learning Point 5"
tags:
  - learning
  - encryption
created: 2026-09-03
---

# Zero-Knowledge Proofs — Proving You Know Without Revealing

## English

A **Zero-Knowledge Proof (ZKP)** lets you prove to someone that you **know a secret**, without revealing the secret itself. The verifier learns nothing except that the prover knows the secret.

**Classic analogy:** You want to prove you know the password to a door, without telling me the password. I stand outside while you prove you're inside. Your presence inside proves you know the password — I never learn what it is.

**How it works (simplified):** Prover commits to a value, verifier challenges with a random bit, prover responds. Over many rounds, if the prover is lying, the probability of passing all challenges approaches zero. If they really know the secret, they can answer correctly every time.

**Applications:** zk-SNARKs / zk-STARKs in blockchains (Zcash, Ethereum L2s) — prove transaction validity without revealing amount or addresses. Authentication (prove you know the password without sending it). Privacy-preserving identity verification.

**Key distinction:** zk-SNARKs need a trusted setup (toxic waste), zk-STARKs don't (but produce larger proofs).

### Key Takeaway
Zero-Knowledge Proofs prove knowledge of a secret without revealing it. zk-SNARKs are compact but require a trusted setup; zk-STARKs are trust-free but larger. Both power privacy-preserving blockchain and authentication systems.

### Related Concepts
- zk-SNARK / zk-STARK
- Trusted setup (ceremony)
- Interactive vs non-interactive proofs
- Prover / Verifier
- Blockchain privacy (Zcash, Ethereum L2)

---

## 中文

**零知識證明 (ZKP)** 讓你能夠向某人證明你**知道一個秘密**，而無需透露秘密本身。驗證者除了知道證明者知道秘密之外，什麼也學不到。

**經典比喻：** 你想證明你知道一扇門的密碼，但不告訴我密碼。我站在外面，你證明你在裡面。你在裡面的存在證明你知道密碼——我永遠不知道它是什麼。

**工作原理（簡化版）：** 證明者承諾一個值，驗證者用隨機位挑戰，證明者回覆。經過多輪，如果證明者在撒謊，通過所有挑戰的概率趨近於零。如果他們真的知道秘密，他們每次都能正確回答。

**應用：** 區塊鏈中的 zk-SNARKs / zk-STARKs（Zcash、以太坊 L2）——在不透露金額或地址的情況下證明交易有效性。認證（在不發送密碼的情況下證明你知道密碼）。隱私保護的身份驗證。

**關鍵區分：** zk-SNARKs 需要信任設置（toxic waste），zk-STARKs 不需要（但產生更大的證明）。

### 核心要點
零知識證明在不透露秘密的情況下證明你知道了它。zk-SNARKs 緊湊但需要信任設置；zk-STARKs 無需信任但更大。兩者都為隱私保護的區塊鏈和認證系統提供動力。

### 相關概念
- zk-SNARK / zk-STARK
- 信任設置（儀式）
- 互動式與非互動式證明
- 證明者 / 驗證者
- 區塊鏈隱私（Zcash、以太坊 L2）
