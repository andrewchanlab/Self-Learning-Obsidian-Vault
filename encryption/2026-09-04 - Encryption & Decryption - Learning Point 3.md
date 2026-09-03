---
title: "2026-09-04 - Encryption & Decryption - Learning Point 3"
tags:
  - learning
  - encryption
created: 2026-09-04
---

# Asymmetric Encryption Solves the Key Exchange Problem with a Key Pair

Public key cryptography uses two linked keys: a public key (which you share freely — anyone can use it to encrypt a message to you) and a private key (which you keep secret — only it can decrypt those messages). RSA and ECC are common algorithms. This elegantly solves the key distribution problem: you can publish your public key anywhere, and anyone can send you encrypted messages without ever needing a secret pre-shared key. This is the foundation of HTTPS, SSH, and digital signatures.

## Key Takeaway
Asymmetric encryption's key pair design solves the key distribution problem — share your public key freely, guard your private key with your life.

## Related Concepts
- Public Key Cryptography
- RSA / ECC
- Public Key / Private Key

---

## 中文：非對稱加密用密鑰對解決了密鑰交換難題

公鑰密碼學使用一對相關联的密鑰：公鑰（你可以自由分享——任何人都可以用它來向你發送加密訊息）和私鑰（你必須保密——只有它能解開那些加密訊息）。RSA 和 ECC 是常見的算法。這優雅地解決了密鑰分發問題：你可以在任何地方公開你的公鑰，任何人都可以給你發加密訊息，完全不需要預先共享秘密密鑰。這是 HTTPS、SSH 和數字簽名的基礎。

## 核心要點
非對稱加密的密鑰對設計解決了密鑰分發難題——自由分享你的公鑰，用生命守護你的私鑰。

## 相關概念
- 公鑰密碼學
- RSA / ECC
- 公鑰 / 私鑰
