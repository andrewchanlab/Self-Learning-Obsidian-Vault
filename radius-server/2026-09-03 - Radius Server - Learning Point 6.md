---
title: "2026-09-03 - Radius Server - Learning Point 6"
tags:
  - learning
  - radius-server
created: 2026-09-03
---

# RADIUS Access-Challenge and Step-Up Authentication

## English

Basic RADIUS authentication is username + password. But what if you need more? RADIUS supports Access-Challenge — the server sends a challenge (like an OTP code) and the NAS prompts the user, then the user's response goes back to the RADIUS server for verification. This enables step-up authentication: normal password for routine access, OTP/token for sensitive operations. The challenge-response loop happens entirely via RADIUS attributes — no changes needed on the NAS side.

### Key Takeaway
Advanced RADIUS features — Access-Challenge, CoA, RadSec, and device authentication — extend the protocol from simple password checking into a full-featured zero-trust access control platform.

## 中文

基本 RADIUS 認證是用户名 + 密碼。但如果需要更多呢？RADIUS 支援 Access-Challenge——伺服器發送挑戰（如 OTP 驗證碼），NAS 提示用戶，然後用戶的回應被發回 RADIUS 伺服器驗證。這實現了升級認證（step-up authentication）：常規訪問用普通密碼，敏感操作用 OTP/令牌。挑戰-回應循環完全通過 RADIUS 屬性完成——NAS 端無需更改。

### 重點摘要
高級 RADIUS 功能——Access-Challenge、CoA、RadSec 和設備認證——將協議從簡單的密碼檢查擴展為功能完整的零信任訪問控制平台。

## Related Concepts
- Access-Challenge
- CoA (Change of Authorization)
- RadSec
- 802.1X
- FreeRADIUS
