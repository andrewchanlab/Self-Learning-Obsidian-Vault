---
title: "2026-09-03 - Radius Server - Learning Point 7"
tags:
  - learning
  - radius-server
created: 2026-09-03
---

# RADIUS Dynamic Authorization (CoA) — Revoking Access in Real Time

## English

What if a user leaves mid-session or their authorization changes? RADIUS supports Change of Authorization (CoA), a mechanism to dynamically modify or terminate an active session. The RADIUS server sends a CoA request to the NAS (typically over port 3799), instructing it to reconfigure the session — change VLAN, update bandwidth limits, or disconnect the user immediately. This is essential for zero-trust architectures and incident response where access must be revoked the moment a policy is violated.

### Key Takeaway
Advanced RADIUS features — Access-Challenge, CoA, RadSec, and device authentication — extend the protocol from simple password checking into a full-featured zero-trust access control platform.

## 中文

如果用戶在會話中途離開或授權發生變化怎麼辦？RADIUS 支援授權變更（CoA），這是一種動態修改或終止活動會話的機制。RADIUS 伺服器向 NAS 發送 CoA 請求（通常通過端口 3799），指示其重新配置會話——更改 VLAN、更新帶寬限制或立即斷開用戶連接。這對零信任架構和事件響應至關重要，在這些場景中，授權必須在政策違規時立即撤銷。

### 重點摘要
高級 RADIUS 功能——Access-Challenge、CoA、RadSec 和設備認證——將協議從簡單的密碼檢查擴展為功能完整的零信任訪問控制平台。

## Related Concepts
- Access-Challenge
- CoA (Change of Authorization)
- RadSec
- 802.1X
- FreeRADIUS
