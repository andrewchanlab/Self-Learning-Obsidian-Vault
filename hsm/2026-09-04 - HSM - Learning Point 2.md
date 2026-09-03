---
title: "2026-09-04 - HSM - Learning Point 2"
tags:
  - learning
  - hsm
created: 2026-09-04
---

# HSMs Protect Keys That Software Can't

Software-based key storage (files, environment variables, key vaults) is vulnerable to memory dumps, process compromise, and insider threats. An HSM requires physical or authenticated access to perform operations. Even if your entire cloud environment is compromised, the attacker cannot extract the private key from the HSM — they can only request signing operations if they have valid credentials.

## Key Takeaway
HSMs isolate cryptographic operations from the broader software stack — compromising the OS or application doesn't expose the protected keys.

## Related Concepts
- Key Isolation
- Security Boundaries
- Defense in Depth
