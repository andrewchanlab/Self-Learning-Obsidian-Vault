---
title: "2026-09-04 - Flask - Learning Point 6"
tags:
  - learning
  - flask
created: 2026-09-04
---

# Flask-SQLAlchemy — Flask's ORM

Flask-SQLAlchemy brings the SQLAlchemy ORM into Flask. Define models as Python classes, query with `User.query.filter_by(email='a@b.com').first()`. It handles session management, pagination, and relationship loading. `db.create_all()` generates tables from models — no raw SQL needed for standard operations.

## Key Takeaway
Flask-SQLAlchemy turns Python classes into database tables and methods into queries — interact with your database using idiomatic Python instead of SQL strings.

## Related Concepts
- ORM
- SQLAlchemy
- Database Models

---

## 中文：Flask-SQLAlchemy — Flask 的 ORM

Flask-SQLAlchemy 將 SQLAlchemy ORM 引入 Flask。用 Python 類定義模型，用 `User.query.filter_by(email='a@b.com').first()` 進行查詢。它處理會話管理、分頁和關係加載。`db.create_all()` 從模型生成表 — 標準操作無需原始 SQL。

## 核心要點
Flask-SQLAlchemy 將 Python 類轉換為數據庫表，將方法轉換為查詢 — 用慣用的 Python 而不是 SQL 字串與數據庫交互。

## 相關概念
- ORM
- SQLAlchemy
- 數據庫模型
