---
title: "2026-03-25 - Radius Server - Learning Point 3"
tags:
  - learning
  - radius-server
created: 2026-03-25
---

# Dynamic Authorization with CoA and DM

RADIUS was originally designed for one-time authentication, but modern networks need to change access policies dynamically — disconnecting a device when it violates policy, or upgrading its VLAN after hours. This is achieved through CoA (Change of Authorization) and DM (Disconnect Messages). When an external system (like a network access control manager) detects a policy violation, it sends a CoA-Request to the NAS, which then re-evaluates the session and applies the new authorization — for example, moving a compromised device to a quarantine VLAN.

## Key Takeaway
CoA/DM enables real-time policy enforcement by allowing external systems to push authorization changes to active sessions without requiring re-authentication.

## Related Concepts
- CoA (Change of Authorization) packets
- Session timeout and termination
- Posture assessment and quarantine VLANs
