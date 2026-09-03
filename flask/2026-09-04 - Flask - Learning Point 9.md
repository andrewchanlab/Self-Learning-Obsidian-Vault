---
title: "2026-09-04 - Flask - Learning Point 9"
tags:
  - learning
  - flask
created: 2026-09-04
---

# Flask-JWT-Extended — Stateless Authentication

Flask-JWT-Extended adds Bearer token (JWT) auth to Flask. `create_access_token(identity=user_id)` creates a signed token; `@jwt_required()` on a route blocks unauthenticated access; `get_jwt_identity()` reads the user ID inside the handler. Tokens are stateless — no server-side session store needed, and they expire automatically.

## Key Takeaway
JWT tokens let you build stateless authentication: the server signs a token, the client sends it on every request — no database lookup on each call, and tokens expire automatically.

## Related Concepts
- JWT
- Bearer Token
- Stateless Auth

---

## 中文：Flask-JWT-Extended — 無狀態認證

Flask-JWT-Extended 為 Flask 添加 Bearer token（JWT）認證。`create_access_token(identity=user_id)` 創建一個簽名 token；在路由上加 `@jwt_required()` 阻止未經認證的訪問；`get_jwt_identity()` 在處理程序中讀取用戶 ID。Token 是無狀態的 — 無需服務器端會話存儲，並且它們會自動過期。

## 核心要點
JWT token 讓你構建無狀態認證：服務器簽名一個 token，客戶端在每個請求中發送它 — 每次調用無需數據庫查詢，並且 token 自動過期。

## 相關概念
- JWT
- Bearer Token
- 無狀態認證
