---
title: "2026-09-04 - Flask - Learning Point 8"
tags:
  - learning
  - flask
created: 2026-09-04
---

# Flask-RESTful — Build APIs Fast

Flask-RESTful simplifies API development with the `Resource` class. One class maps HTTP verbs to methods: `class User(Resource)` with `get`, `post`, `put`, `delete`. Register it with `api.add_resource(User, '/users/<int:id>')` and Flask handles routing. Output JSON with `marshal_with` decorators and field definitions — no manual `jsonify()` everywhere.

## Key Takeaway
Flask-RESTful structures your API around resources with clean HTTP verb mapping — build clean REST APIs with less boilerplate than vanilla Flask route functions.

## Related Concepts
- REST API
- JSON
- Request Parsing

---

## 中文：Flask-RESTful — 快速構建 API

Flask-RESTful 用 `Resource` 類簡化 API 開發。一個類將 HTTP 動詞映射到方法：`class User(Resource)` 帶有 `get`、`post`、`put`、`delete`。用 `api.add_resource(User, '/users/<int:id>')` 註冊它，Flask 處理路由。用 `marshal_with` 裝飾器和字段定義輸出 JSON — 不需要到處手動 `jsonify()`。

## 核心要點
Flask-RESTful 圍繞資源構建 API，清晰的 HTTP 動詞映射 — 用比普通 Flask 路由函數更少的樣板代碼構建乾淨的 REST API。

## 相關概念
- REST API
- JSON
- 請求解析
