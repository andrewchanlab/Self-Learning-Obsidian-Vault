---
title: "2026-09-05 - Meilisearch - Learning Point 10"
tags:
  - learning
  - meilisearch
created: 2026-09-05
---

# Meilisearch 的 SDK 與 HTTP API：何時用哪個

Meilisearch 提供多種官方 SDK（JavaScript/TypeScript、Python、Ruby、PHP、Go 等）以及一個完整的 HTTP REST API。大多數情況下，官方 SDK 是首選——它們是類型安全的（尤其 TypeScript SDK）、自動處理序列化、且與框架整合良好（如 Laravel Scout 整合）。但當你需要從不支援 SDK 的語言或環境（如某些邊緣運算場景）存取時，HTTP API 就是你的備案。Both expose the same capabilities — the SDK is just a convenience wrapper.

## SDK vs HTTP API 選擇指南
- **使用 SDK**：大多數 Web 應用、後端服務、有官方 SDK 的語言
- **使用 HTTP API**：邊緣函數、沒有 SDK 的語言、簡單的 curl 測試、嵌入式裝置

## HTTP API 端點概覽
```
POST /indexes/{index_uid}/documents  # 新增文件
GET  /indexes/{index_uid}/search     # 搜尋
GET  /indexes/{index_uid}/documents  # 取得文件
PUT  /indexes/{index_uid}/settings   # 更新設定
```

## Related Concepts
- Official SDKs for major languages
- REST API design
- Laravel Scout integration
- Meilisearch Cloud (managed service)
