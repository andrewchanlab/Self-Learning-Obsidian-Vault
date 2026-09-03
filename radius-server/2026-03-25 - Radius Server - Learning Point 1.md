---
title: "2026-03-25 - Radius Server - Learning Point 1"
tags:
  - learning
  - radius-server
created: 2026-03-25
---

# RADIUS Protocol: The Foundation of Network Access Control

RADIUS (Remote Authentication Dial-In User Service) is a client-server protocol that handles authentication, authorization, and accounting (AAA) for network access. When you connect to enterprise WiFi or a VPN, your device talks to an access point (the RADIUS client), which forwards your credentials to the RADIUS server. The server checks your username/password against a user database, then responds with Accept or Reject, optionally including authorization attributes like VLAN assignment or speed limits. This three-way handshake (Access-Request, Access-Challenge, Access-Accept/Reject) is the heartbeat of modern network security.

## Key Takeaway
RADIUS centralizes authentication so that one server can manage access across thousands of network devices — the de facto standard for enterprise WiFi and VPN authentication.

## Related Concepts
- AAA framework (Authentication, Authorization, Accounting)
- PAP, CHAP, and EAP authentication protocols
- Network access servers (NAS)
