---
title: "2026-03-25 - Encryption - Learning Point 1"
tags:
  - learning
  - encryption
created: 2026-03-25
---

# Symmetric vs Asymmetric Encryption

Symmetric encryption uses the same key to encrypt and decrypt — think of it as a password-protected ZIP file. AES (Advanced Encryption Standard) is the gold standard for symmetric encryption: it's fast, well-understood, and variants like AES-256-GCM provide both confidentiality and integrity checking (via authenticated encryption). Asymmetric encryption uses a key pair — a public key that encrypts or verifies, and a private key that decrypts or signs. RSA is the classic algorithm; for the same security level, RSA keys need to be much larger than AES keys (3072-bit RSA ≈ 256-bit AES), making RSA slower and suited to small payloads like signing hashes or encrypting session keys.

## Key Takeaway
Use AES for bulk data encryption (fast, efficient), and RSA (or better, elliptic curve cryptography) for key exchange and digital signatures — they solve different problems.

## Related Concepts
- AES-256-GCM authenticated encryption
- RSA modulus and public/private exponents
- Key sizes and security equivalence
