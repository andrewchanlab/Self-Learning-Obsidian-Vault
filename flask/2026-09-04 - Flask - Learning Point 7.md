---
title: "2026-09-04 - Flask - Learning Point 7"
tags:
  - learning
  - flask
created: 2026-09-04
---

# Flask-Migrate — Database Migrations with Alembic

Flask-Migrate wraps Alembic, SQLAlchemy's migration framework. `flask db init` creates a migrations repo; `flask db migrate -m "add age"` generates an upgrade script; `flask db upgrade` applies it. Migrations are versioned and reversible — `flask db downgrade` rolls back safely. Never manually ALTER TABLE again.

## Key Takeaway
Flask-Migrate brings version-controlled, reversible database schema changes to Flask — keeping development and production databases in sync with a clean audit trail.

## Related Concepts
- Alembic
- Database Migration
- Schema Versioning

---

## 中文：Flask-Migrate — 使用 Alembic 進行數據庫遷移

Flask-Migrate 封裝了 Alembic，這是 SQLAlchemy 的遷移框架。`flask db init` 創建一個遷移倉庫；`flask db migrate -m "add age"` 生成一個升級腳本；`flask db upgrade` 應用它。遷移是版本化的和可逆的 — `flask db downgrade` 安全回滾。再也不用手動 ALTER TABLE 了。

## 核心要點
Flask-Migrate 為 Flask 帶來版本控制的、可逆的數據庫模式變更 — 用清晰的審計追蹤保持開發和生產數據庫的同步。

## 相關概念
- Alembic
- 數據庫遷移
- 模式版本控制
