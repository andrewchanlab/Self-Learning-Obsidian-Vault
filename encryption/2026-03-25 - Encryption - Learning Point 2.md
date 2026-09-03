---
title: "2026-03-25 - Encryption - Learning Point 2"
tags:
  - learning
  - encryption
created: 2026-03-25
---

# Hash Functions: One-Way Digital Fingerprints

A cryptographic hash function (SHA-256, SHA-3) takes any input and produces a fixed-length "fingerprint" with three critical properties: determinism (same input always produces same output), pre-image resistance (can't reverse a hash to find its input), and collision resistance (can't find two different inputs that produce the same output). Password storage uses hashes — you store `SHA-256(password)` not the password itself, and when a user logs in you compare hashes. Hashes also power blockchain (each block contains the previous block's hash), Git (commits are identified by content hashes), and HMAC (hash-based message authentication codes).

## Key Takeaway
Hash functions provide integrity verification and one-way transformations — they're the foundation of digital signatures, HMAC, proof-of-work, and secure password storage.

## Related Concepts
- SHA-256 vs SHA-3 algorithms
- Salt and bcrypt for password hashing
- HMAC for message authentication
