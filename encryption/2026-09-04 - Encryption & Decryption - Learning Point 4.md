---
title: "2026-09-04 - Encryption & Decryption - Learning Point 4"
tags:
  - learning
  - encryption
created: 2026-09-04
---

# Hashing Is One-Way — You Can't Reverse It

A hash function maps any input to a fixed-length fingerprint. SHA-256 always produces 256 bits. Given the hash, you cannot recover the original input. Passwords are stored as hashes — when you log in, your password is hashed and compared. Rainbow tables attack this by pre-computing hashes of common passwords.

## Key Takeaway
Hashing is a one-way function used for integrity verification and password storage — salting passwords prevents rainbow table attacks.

## Related Concepts
- SHA-256
- Password Hashing
- Rainbow Tables
