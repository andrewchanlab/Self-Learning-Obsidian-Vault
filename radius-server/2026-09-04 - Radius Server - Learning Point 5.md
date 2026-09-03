---
title: "2026-09-04 - Radius Server - Learning Point 5"
tags:
  - learning
  - radius-server
created: 2026-09-04
---

# RADIUS Proxy: Scaling Across Multiple Organizations

## English

What if one RADIUS server isn't enough? You can chain RADIUS servers using a **RADIUS Proxy** (also called a RADIUS Forwarder or RADIUS AAA Proxy). The proxy receives requests and forwards them to the appropriate RADIUS server based on **realms** (the part after the @ in your username, like @company.com).

This enables powerful architectures:
- **Multi-tenant environments** — an ISP hosts WiFi for hundreds of apartment buildings; each building gets its own RADIUS server, reached via the proxy
- **Federation** — university networks that trust each other's credentials (eduroam uses this)
- **Geographic distribution** — branch offices forward to the central corporate RADIUS

The proxy can also **modify requests in flight** — adding, removing, or rewriting attributes like VLAN tags or rate limits. It's the traffic cop of the RADIUS world.

### Key Takeaway
RADIUS proxies chain servers together using realms, enabling multi-tenant, federated, and geographically distributed authentication architectures.

## 中文

如果一台 RADIUS 伺服器不夠用怎麼辦？你可以使用 **RADIUS 代理**（也稱為 RADIUS 轉發器或 RADIUS AAA 代理）將 RADIUS 伺服器串聯起來。代理接收請求並根據**領域（realms）**（用戶名 @ 後面的部分，如 @company.com）將其轉發到相應的 RADIUS 伺服器。

這實現了強大的架構：
- **多租戶環境**——ISP 為數百棟公寓大樓提供 WiFi 托管；每棟大樓都有自己的 RADIUS 伺服器，通過代理訪問
- **聯合認證**——相互信任憑證的大學網絡（eduroam 就是這樣用的）
- **地理分佈**——分公司的請求轉發到企業中央 RADIUS

代理還可以在傳輸過程中**修改請求**——添加、刪除或重寫 VLAN 標籤或速率限制等屬性。它是 RADIUS 世界的交通警察。

### 重點摘要
RADIUS 代理使用領域將多台伺服器串聯起來，實現多租戶、聯合和地理分佈式認證架構。

## Related Concepts
- RADIUS Proxy
- Realm
- Multi-tenancy
