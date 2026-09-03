---
title: "2026-09-04 - Radius Server - Learning Point 1"
tags:
  - learning
  - radius-server
created: 2026-09-04
---

# RADIUS Is the Network's Centralized Bouncer

## English

A RADIUS server acts as a single authentication checkpoint for your entire network. Instead of managing usernames on every WiFi access point, you have **one RADIUS server** that every device queries. When you log into office WiFi with a personal username/password instead of a shared password — that's RADIUS working behind the scenes.

Think of it like a concert venue: instead of each door guard having their own guest list, there's one central bouncer that every entrance checks with. The WiFi router (called the **Network Access Server** or NAS) is just the door — it asks the RADIUS server "Is this person allowed in?"

### Key Takeaway
RADIUS centralizes network authentication — one server manages all users, all access points trust it, and you manage accounts in one place.

## 中文

RADIUS 伺服器是整個網絡的中央認證關卡。不需要在每個 WiFi 接入點管理用戶名單，而是設立**一台 RADIUS 伺服器**，所有設備都向它查詢。當你用自己的個人用戶名/密碼登入辦公室 WiFi，而不是用共享密碼時——這就是 RADIUS 在幕後工作的例子。

把它想像成演唱會場地：每個入口的保安不需要各自持有一份嘉賓名單，而是由一位中央保全把關，所有入口都向他確認「這個人可以進來嗎？」WiFi 路由器（稱為**網絡接入伺服器**或 NAS）只是那扇門——它負責問 RADIUS 伺服器：「這個人可以訪問網絡嗎？」

### 重點摘要
RADIUS 集中管理網絡認證——一台伺服器管理所有用戶，所有接入點信任它，你只需在一個地方管理帳戶。

## Related Concepts
- Network Security
- AAA Protocol
- WPA2-Enterprise
