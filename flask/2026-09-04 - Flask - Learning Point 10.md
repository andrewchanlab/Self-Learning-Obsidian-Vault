---
title: "2026-09-04 - Flask - Learning Point 10"
tags:
  - learning
  - flask
created: 2026-09-04
---

# Flask Testing — Unit Tests with pytest

Flask apps pair naturally with pytest. Use `app = Flask(__name__)` or `app = create_app('testing')` for a test config. `client = app.test_client()` sends fake requests without running a server. Patch database calls with `monkeypatch` or use `app_context()` to run code inside Flask's request lifecycle. Assert on status codes and JSON responses — `assert response.status_code == 200`.

## Key Takeaway
pytest + Flask's test client = fast, repeatable unit tests. No server needed — send requests, check responses, and mock dependencies directly in Python.

## Related Concepts
- pytest
- Unit Testing
- Test Client

---

## 中文：Flask 測試 — 使用 pytest 進行單元測試

Flask 應用程序自然地與 pytest 配對。使用 `app = Flask(__name__)` 或 `app = create_app('testing')` 來獲取測試配置。`client = app.test_client()` 發送假請求而無需運行服務器。用 `monkeypatch` 打補丁數據庫調用，或使用 `app_context()` 在 Flask 的請求生命周期內運行代碼。對狀態碼和 JSON 響應進行斷言 — `assert response.status_code == 200`。

## 核心要點
pytest + Flask 的測試客戶端 = 快速、可重複的單元測試。無需服務器 — 發送請求、檢查響應，並直接在 Python 中模擬依賴。

## 相關概念
- pytest
- 單元測試
- 測試客戶端
