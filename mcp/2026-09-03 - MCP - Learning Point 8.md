---
title: "2026-09-03 - MCP - Learning Point 8"
tags:
  - learning
  - mcp
created: 2026-09-03
---

# MCP Server Discovery and the Registry Model

## English

How does an AI client find MCP servers? There's no single mandated registry in the spec, but common patterns include: a configuration file listing servers (like a mcp.json config in the client's home directory), a discovery endpoint where servers announce themselves, or a marketplace where servers are published with their capabilities described. Clients typically maintain a manifest of known servers, fetch their tool manifests on startup, and cache the results. The client is always in control of which servers it connects to.

### Key Takeaway
MCP's open, vendor-neutral protocol design makes it the most interoperable way to connect AI models to external tools — built for portability across LLM providers, not locked into any single ecosystem.

## 中文

AI 客戶端如何發現 MCP 伺服器？規范中沒有單一強制性註冊中心，但常見模式包括：配置文件列出伺服器（如客戶端主目錄中的 mcp.json 配置）、發現端點讓伺服器自我宣告，或市場發布帶有功能描述的伺服器。客戶端通常維護已知伺服器列表，在啟動時獲取其工具清單並緩存結果。客戶端始終控制連接到哪些伺服器。

### 重點摘要
MCP 的開放、供應商中立協議設計使其成為將 AI 模型連接到外部工具最具互操作性的方式——為跨 LLM 提供商的可移植性而構建，而非鎖定在任何單一生態系統中。

## Related Concepts
- Tool Discovery
- MCP Security
- Streaming Responses
- Protocol Interoperability
- AI Integration
