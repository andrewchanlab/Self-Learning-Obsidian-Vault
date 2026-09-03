---
title: "2026-03-25 - HSM - Learning Point 1"
tags:
  - learning
  - hsm
created: 2026-03-25
---

# Hardware Security Modules: Purpose and Threat Model

An HSM is a dedicated hardware appliance (or PCIe card) designed to generate, store, and use cryptographic keys in a way that makes extraction virtually impossible. The key insight: cryptographic key material never leaves the HSM — operations (sign, decrypt) happen inside the tamper-resistant hardware. If you try to drill into the device, it zeroizes (instantly erases) all keys. This protects against software attacks, insider threats, and physical theft. HSMs are required by regulation for payment processing (PCI-DSS), certificate authorities issuing EV certificates, and financial institutions handling signing keys.

## Key Takeaway
HSMs protect keys at the hardware level — the cryptographic material never exists outside the secure boundary, making software compromise irrelevant to key extraction.

## Related Concepts
- Tamper-evident and tamper-resistant hardware
- Key zeroization on breach
- FIPS 140-2 Level 3 certification
