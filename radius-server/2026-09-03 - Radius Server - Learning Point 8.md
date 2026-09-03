---
title: "2026-09-03 - Radius Server - Learning Point 8"
tags:
  - learning
  - radius-server
created: 2026-09-03
---

# RADIUS over TLS (RadSec) — Encrypting the Entire RADIUS Conversation

## English

Standard RADIUS uses UDP and is typically deployed within a trusted network — but it's not encrypted. RadSec (RADIUS over TLS) wraps the entire RADIUS exchange in a TLS tunnel, providing confidentiality and integrity for the protocol itself. This is critical for: roaming federations (eduroam across the internet), cloud-to-on-prem RADIUS communication, and any deployment where the network path between NAS and RADIUS server is untrusted. RadSec uses TCP port 2083 by default.

### Key Takeaway
Advanced RADIUS features — Access-Challenge, CoA, RadSec, and device authentication — extend the protocol from simple password checking into a full-featured zero-trust access control platform.

## 中文

標準 RADIUS 使用 UDP，通常部署在可信網絡內——但它本身不加密。RadSec（RADIUS over TLS）將整個 RADIUS 對話包裝在 TLS 隧道中，為協議本身提供保密性和完整性。這對以下場景至關重要：漫遊聯合認證（eduroam 跨互聯網）、雲端到本地 RADIUS 通信，以及任何 NAS 與 RADIUS 伺服器之間網絡路徑不可信的部署。RadSec 預設使用 TCP 端口 2083。

### 重點摘要
高級 RADIUS 功能——Access-Challenge、CoA、RadSec 和設備認證——將協議從簡單的密碼檢查擴展為功能完整的零信任訪問控制平台。

## Related Concepts
- Access-Challenge
- CoA (Change of Authorization)
- RadSec
- 802.1X
- FreeRADIUS
