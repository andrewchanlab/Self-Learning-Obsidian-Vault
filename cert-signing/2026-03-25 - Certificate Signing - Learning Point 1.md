---
title: "2026-03-25 - Certificate Signing - Learning Point 1"
tags:
  - learning
  - cert-signing
created: 2026-03-25
---

# Public Key Infrastructure: The Hierarchy of Trust

PKI is a system where trust flows from a root Certificate Authority (CA) through intermediate CAs to end-entity certificates. Your browser trusts ~100 root CAs pre-installed in its trust store — these roots sign intermediate CA certificates (splitting trust to limit damage if an intermediate is compromised). Intermediates then sign end-entity certificates (like `github.com`). This chain of trust means you only need to trust ~100 root CAs to trust billions of websites. The root CA never signs end-entity certs directly — intermediaries provide a security boundary: if an intermediate is compromised, the root CA revokes it and the CRL/OCSP system propagates that trust revocation.

## Key Takeaway
PKI's chain of trust means your device only needs to trust ~100 root CAs, and everything else flows from there — billions of certificates trusted by trusting their chain up to those roots.

## Related Concepts
- Root, intermediate, and end-entity certificates
- Certificate chain traversal
- Trust stores and CA bundles
