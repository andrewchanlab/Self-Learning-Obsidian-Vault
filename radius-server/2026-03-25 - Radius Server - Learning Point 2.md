---
title: "2026-03-25 - Radius Server - Learning Point 2"
tags:
  - learning
  - radius-server
created: 2026-03-25
---

# FreeRADIUS: The Open-Source Powerhouse

FreeRADIUS is the most widely deployed open-source RADIUS server, running on Linux and supporting virtually every RADIUS feature. It uses a module-based architecture: authentication methods (PAP, CHAP, EAP-PEAP, EAP-TLS) are pluggable modules, and authorization policies are written in unlang (a domain-specific language). This flexibility means you can integrate FreeRADIUS with Active Directory via LDAP, authenticate WiFi clients against Azure AD, or implement complex policy rules — all without modifying the core server code.

## Key Takeaway
FreeRADIUS's modular design lets you mix and match authentication backends and policy logic to fit any enterprise network topology.

## Related Concepts
- unlang policy language
- EAP methods (PEAP, TTLS, TLS)
- LDAP and Active Directory integration
