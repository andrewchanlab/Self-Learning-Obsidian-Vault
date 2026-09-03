---
title: "2026-09-04 - Flask - Learning Point 2"
tags:
  - learning
  - flask
created: 2026-09-04
---

# Routes Are Function Decorators — URL to Handler Mapping

@app.route('/users/<id>') maps a URL pattern to a Python function. Flask extracts URL parameters, query strings, form data, and JSON bodies into a `request` object. Return a string, a template, or JSON — Flask handles the HTTP response construction.

## Key Takeaway
Flask's decorator-based routing makes URL mapping intuitive — each route is a plain Python function with a decorator, not a class or configuration object.

## Related Concepts
- URL Routing
- Decorators
- REST API

---

## 中文：路由就是函數裝飾器 — URL 對應處理函數

`@app.route('/users/<id>')` 將 URL 模式對應到 Python 函數。Flask 從 URL 參數、查詢字串、表單資料和 JSON 主體中提取數據，傳入 `request` 物件。回傳字串、模板或 JSON — Flask 幫你處理 HTTP 回應的建構。

### 核心要點
Flask 基於裝飾器的路由系統讓 URL 對應直覺自然 — 每條路由就是一個普通的 Python 函數，加上裝飾器，不需要類別或設定物件。
