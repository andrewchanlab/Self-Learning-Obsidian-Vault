---
title: "2026-03-25 - HSM - Learning Point 3"
tags:
  - learning
  - hsm
created: 2026-03-25
---

# Cloud HSMs: AWS CloudHSM and Azure Dedicated HSM

Cloud providers offer HSM-as-a-Service with dedicated hardware (not shared multi-tenant HSMs). AWS CloudHSM provides a dedicated FIPS 140-2 Level 3 HSM in your VPC, with the benefit that AWS has no access to your keys — you manage the HSM entirely. Azure Dedicated HSM offers similar dedicated hardware from Gemalto/Sentinel. Google Cloud KMS takes a different approach: a shared but hardware-backed service where Google manages the HSM fleet, and you get cryptographic isolation via key rings and IAM permissions. The trade-off: dedicated HSMs give you full control (and full responsibility for availability), while managed KMS reduces operational burden.

## Key Takeaway
Cloud HSMs give you hardware-backed key protection without owning physical hardware — choose dedicated (full control, more ops burden) or managed KMS (less control, less ops burden).

## Related Concepts
- AWS CloudHSM cluster and HA setup
- GCP Cloud KMS and key hierarchy
- Bring Your Own Key (BYOK) patterns
