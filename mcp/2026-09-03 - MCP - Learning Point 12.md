---
title: "2026-09-03 - MCP - Learning Point 12"
tags:
  - learning
  - mcp
created: 2026-09-03
---

# MCP vs. Tool Use in Other AI Protocols — A Comparison

## English

How does MCP compare to OpenAI's function calling, Anthropic's tool use, or LangChain tools? All serve the same goal (letting LLMs invoke external functions), but MCP is protocol-level — it standardizes the transport, discovery, and interface across any LLM client or server. Proprietary APIs (OpenAI functions, etc.) only work within their own ecosystem. MCP's open, vendor-neutral design means an MCP server works with any MCP-compatible client, regardless of the LLM provider. For building portable AI integrations, MCP wins on interoperability.

### Key Takeaway
MCP's open, vendor-neutral protocol design makes it the most interoperable way to connect AI models to external tools — built for portability across LLM providers, not locked into any single ecosystem.

## 中文

MCP 與 OpenAI 的 function calling、Anthropic 的 tool use 或 LangChain tools 相比如何？它們都服務於相同目標（讓 LLM 調用外部函數），但 MCP 是協議級別的——它標準化了傳輸、發現和接口，適用於任何 LLM 客戶端或伺服器。專有 API（如 OpenAI functions）只在自身生態系統內工作。MCP 的開放、供應商中立設計意味著一個 MCP 伺服器可與任何 MCP 相容的客戶端協作，無論 LLM 提供商是誰。對於構建可移植的 AI 整合，MCP 在互操作性方面獲勝。

### 重點摘要
MCP 的開放、供應商中立協議設計使其成為將 AI 模型連接到外部工具最具互操作性的方式——為跨 LLM 提供商的可移植性而構建，而非鎖定在任何單一生態系統中。

## Related Concepts
- Tool Discovery
- MCP Security
- Streaming Responses
- Protocol Interoperability
- AI Integration
