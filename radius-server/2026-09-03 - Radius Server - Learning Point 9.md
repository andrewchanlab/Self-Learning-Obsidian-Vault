---
title: "2026-09-03 - Radius Server - Learning Point 9"
tags:
  - learning
  - radius-server
created: 2026-09-03
---

# Device Authentication vs. User Authentication in RADIUS

## English

RADIUS can authenticate both devices (machine certificates, MAC addresses) and users (username/password, OTP). Device authentication is common in 802.1X enterprise WiFi — the device presents its machine certificate before the user even logs in, giving pre-user network access (for domain join, policy download, etc.). Combo modes exist: the device authenticates first, then the user — or the RADIUS server checks both in one flow. Understanding which you're using matters for access control and compliance.

### Key Takeaway
Advanced RADIUS features — Access-Challenge, CoA, RadSec, and device authentication — extend the protocol from simple password checking into a full-featured zero-trust access control platform.

## 中文

RADIUS 可以同時認證設備（機器證書、MAC 地址）和用戶（用户名/密碼、OTP）。設備認證在 802.1X 企業 WiFi 中很常見——設備在使用戶登錄之前就呈現其機器證書，實現用戶預先網絡訪問（用於域加入、策略下載等）。也有組合模式：設備先認證，然後用戶再認證——或者 RADIUS 伺服器在同一流程中檢查兩者。了解您使用的是哪種模式對訪問控制和合規都很重要。

### 重點摘要
高級 RADIUS 功能——Access-Challenge、CoA、RadSec 和設備認證——將協議從簡單的密碼檢查擴展為功能完整的零信任訪問控制平台。

## Related Concepts
- Access-Challenge
- CoA (Change of Authorization)
- RadSec
- 802.1X
- FreeRADIUS
