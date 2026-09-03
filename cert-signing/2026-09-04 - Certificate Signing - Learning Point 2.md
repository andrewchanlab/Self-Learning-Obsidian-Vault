---
title: "2026-09-04 - Certificate Signing - Learning Point 2"
tags:
  - learning
  - cert-signing
created: 2026-09-04
---

# TLS Certificates — The Digital ID Cards of the Internet

A TLS certificate binds a public key to a domain name (and optionally organization). It contains: the public key, the domain name it belongs to, the validity period, the issuer (CA), and the CA's digital signature. When you visit https://example.com, the server presents its certificate proving it owns the private key for that domain.

## Key Takeaway
TLS certificates are verifiable identity proofs — they prove a server owns the private key corresponding to a domain name.

## Related Concepts
- TLS Handshake
- Server Certificate
- Domain Validation
