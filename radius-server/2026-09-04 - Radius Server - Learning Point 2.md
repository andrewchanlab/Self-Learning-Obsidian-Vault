---
title: "2026-09-04 - Radius Server - Learning Point 2"
tags:
  - learning
  - radius-server
created: 2026-09-04
---

# The Three-Party AAA Protocol

## English

RADIUS involves three parties working together:

1. **The User** — your laptop, phone, or any device trying to connect
2. **The Network Access Server (NAS)** — your WiFi router, VPN gateway, or switch that physically connects users to the network
3. **The RADIUS Server** — the central brain that validates credentials

The magic is in the **separation of roles**: the NAS doesn't make decisions, it just forwards requests. When you try to connect to WiFi, your device sends credentials to the router (NAS), which wraps them in a RADIUS packet and sends it to the RADIUS server. The RADIUS server says "Allow" or "Deny," and the router acts on that verdict.

### Key Takeaway
The NAS sits between users and RADIUS — routers and VPN gateways act as pass-through agents, not authentication authorities. This separation means you can replace any router without touching user accounts.

## 中文

RADIUS 涉及三方協作：

1. **用戶**——你的筆電、手機或任何想要連接的設備
2. **網絡接入伺服器 (NAS)**——你的 WiFi 路由器、VPN 網關或交換機，負責將用戶物理連接到網絡
3. **RADIUS 伺服器**——驗證憑證的中央大腦

巧妙之處在於**角色的分離**：NAS 不做決定，只是轉發請求。當你嘗試連接 WiFi 時，你的設備將憑證發送到路由器（NAS），路由器將其包裝成 RADIUS 數據包並發送到 RADIUS 伺服器。RADIUS 伺服器說「允許」或「拒絕」，路由器則執行該裁決。

### 重點摘要
NAS 位於用戶和 RADIUS 之間——路由器和 VPN 網關扮演轉發代理的角色，而不是認證機構。這種分離意味著你可以替換任何路由器而不影響用戶帳戶。

## Related Concepts
- Authentication
- Network Access Server (NAS)
- RADIUS Protocol
