---
title: "2026-09-04 - Radius Server - Learning Point 3"
tags:
  - learning
  - radius-server
created: 2026-09-04
---

# RADIUS Handles All Three AAA Functions

## English

AAA stands for **Authentication, Authorization, and Accounting** — and RADIUS handles all three:

- **Authentication** — "Who are you?" The server verifies username/password against a database (like Active Directory or LDAP).
- **Authorization** — "What can you do?" After authentication, RADIUS can specify attributes: which VLAN you join, your bandwidth limit, or which network resources you can access.
- **Accounting** — "What did you do?" RADIUS logs session start/stop times, data usage, and connection duration — essential for billing and security audits.

Real-world example: A corporate employee authenticates with their AD password, gets authorized to the "Engineering VLAN" with 100Mbps limit, and their 3-hour VPN session is logged for compliance records.

### Key Takeaway
RADIUS's three A's — Authentication, Authorization, and Accounting — provide a complete picture of network access for security, compliance, and billing.

## 中文

AAA 代表**認證（Authentication）、授權（Authorization）和計帳（Accounting）**——RADIUS 三者兼顧：

- **認證**——「你是誰？」伺服器根據資料庫（如 Active Directory 或 LDAP）驗證用戶名/密碼。
- **授權**——「你可以做什麼？」認證後，RADIUS 可以指定屬性：你加入哪個 VLAN、頻寬限制是多少、或你可以訪問哪些網絡資源。
- **計帳**——「你做了什麼？」RADIUS 記錄會话的開始/結束時間、數據使用量和連接持續時間——這些對帳單和安全審計至關重要。

實際例子：企業員工使用 AD 密碼認證，獲授權進入「工程 VLAN」並享有 100Mbps 限制，其 3 小時的 VPN 會话被記錄在合規檔案中。

### 重點摘要
RADIUS 的三 A——認證、授權、計帳——為安全、合規和帳單提供完整的網絡訪問概覽。

## Related Concepts
- Authentication
- Authorization
- Accounting
