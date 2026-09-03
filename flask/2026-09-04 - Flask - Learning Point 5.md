---
title: "2026-09-04 - Flask - Learning Point 5"
tags:
  - learning
  - flask
created: 2026-09-04
---

# Blueprints — Scalable Project Structure

Flask Blueprints let you organize routes into reusable modules. Instead of defining all routes in one `app.py`, you register blueprints for auth, API, admin — each with its own URL prefix. This scales from 5 routes to 500 without a messy `app.py`.

## Key Takeaway
Blueprints provide namespacing and modular structure — register them in `app.py` to compose a large app from small, focused pieces.

## Related Concepts
- Modular Architecture
- Blueprint
- App Factory Pattern

---

## 中文：藍圖（Blueprints）— 可擴展的項目結構

Flask 藍圖讓你將路由組織成可重用的模組。不把所有路由寫在一個 `app.py` 裡，而是為認證、API、管理後台等各自註冊藍圖，每個都有自己的 URL 前綴。這樣可以從 5 條路由擴展到 500 條而不會讓 `app.py` 變得一團糟。

### 核心要點
藍圖提供命名空間和模組化結構 — 在 `app.py` 中註冊它們，將大型應用程式由多個專注的小零件組合而成。
