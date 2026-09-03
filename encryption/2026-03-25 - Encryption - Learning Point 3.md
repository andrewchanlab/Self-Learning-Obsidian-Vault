---
title: "2026-03-25 - Encryption - Learning Point 3"
tags:
  - learning
  - encryption
created: 2026-03-25
---

# Digital Signatures: Proving Authenticity and Integrity

Digital signatures don't encrypt data — they prove that a message was created by a specific sender and wasn't altered in transit. The process: the sender hashes the message, then encrypts the hash with their private key. The recipient decrypts the signature using the sender's public key, re-hashes the received message, and compares the two hashes. If they match, the signature is valid. This works because only the holder of the private key could have encrypted the hash — so if the public key successfully decrypts it, the sender must own the matching private key. This is the foundation of code signing, TLS certificates, and SSH key authentication.

## Key Takeaway
Digital signatures bind a message to an identity — the sender's private key is the ultimate proof of authorship, and the public key anyone can verify.

## Related Concepts
- RSA-PSS and ECDSA signature schemes
- Certificate chains and trust stores
- Code signing and signed executable verification
