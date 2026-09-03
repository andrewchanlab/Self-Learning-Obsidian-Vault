---
title: "2026-09-03 - MCP - Learning Point 9"
tags:
  - learning
  - mcp
created: 2026-09-03
---

# MCP Tool Naming Conventions and Namespacing

## English

MCP tools have namespaced identifiers — a tool is identified as namespace/tool-name (e.g., github/create-issue, filesystem/read-file). This prevents collisions when multiple servers expose tools with the same simple name. A server can also expose multiple tools under its own namespace. Clients resolve a tool call by finding the server that owns that namespace, then invoking the corresponding function. Good namespacing makes MCP tool sets predictable and self-documenting.

### Key Takeaway
MCP's open, vendor-neutral protocol design makes it the most interoperable way to connect AI models to external tools — built for portability across LLM providers, not locked into any single ecosystem.

## 中文

MCP 工具有命名空間標識符——工具識別為 命名空間/工具名（例如 github/create-issue、filesystem/read-file）。這防止了當多個伺服器暴露相同簡單名稱的工具時發生衝突。伺服器也可以在自己的命名空間下暴露多個工具。客戶端通過找到擁有該命名空間的伺服器，然後調用相應函數來解析工具調用。良好的命名空間使 MCP 工具集可預測且自我記錄。

### 重點摘要
MCP 的開放、供應商中立協議設計使其成為將 AI 模型連接到外部工具最具互操作性的方式——為跨 LLM 提供商的可移植性而構建，而非鎖定在任何單一生態系統中。

## Related Concepts
- Tool Discovery
- MCP Security
- Streaming Responses
- Protocol Interoperability
- AI Integration
