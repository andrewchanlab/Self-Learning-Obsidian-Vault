---
title: "2026-09-04 - Certificate Signing - Learning Point 1"
tags:
  - learning
  - cert-signing
created: 2026-09-04
---

# PKI — The Trust Hierarchy Behind HTTPS

Public Key Infrastructure (PKI) is the system that makes HTTPS work. It involves Certificate Authorities (CAs), root certificates, intermediate certificates, and end-entity certificates. Your browser trusts a small set of root CAs (pre-installed), which trust intermediate CAs, which trust the certificates websites use. This chain of trust lets you trust a random website without manually trusting each one.

## Key Takeaway
PKI's chain of trust hierarchy means browsers only need to trust ~150 root CAs to trust millions of websites — a scalable trust model.

## Related Concepts
- Certificate Authority
- Root Certificate
- Chain of Trust
