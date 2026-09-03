---
title: "2026-09-04 - Radius Server - Learning Point 2"
tags:
  - learning
  - radius-server
created: 2026-09-04
---

# The Three-Party AAA Protocol

RADIUS involves three parties: the User (client), the Network Access Server (NAS — your WiFi router or VPN gateway), and the RADIUS server. The NAS forwards authentication requests to RADIUS, which checks the user database and replies Allow/Deny. This separation lets you swap routers without reconfiguring user accounts.

## Key Takeaway
The NAS sits between users and RADIUS — routers and VPN gateways act as pass-through agents, not authentication authorities.

## Related Concepts
- Authentication
- Network Access Server
- RADIUS Protocol
