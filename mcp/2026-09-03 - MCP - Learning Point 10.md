---
title: "2026-09-03 - MCP - Learning Point 10"
tags:
  - learning
  - mcp
created: 2026-09-03
---

# MCP Security Model — Authentication, Authorization, and Trust Boundaries

## English

MCP servers may have vastly different trust requirements. A filesystem server needs access to your entire filesystem — that's a high-risk asset. A GitHub server needs OAuth tokens with potentially broad permissions. The MCP security model requires clients to explicitly grant each server its capabilities and scopes. Servers should declare the minimum permissions they need (principle of least privilege). Clients should verify server identities (via certificates or tokens) and log all tool invocations for audit. Never connect to untrusted MCP servers.

### Key Takeaway
MCP's open, vendor-neutral protocol design makes it the most interoperable way to connect AI models to external tools — built for portability across LLM providers, not locked into any single ecosystem.

## 中文

MCP 伺服器可能有截然不同的信任要求。文件系統伺服器需要訪問您的整個文件系統——這是高風險資產。GitHub 伺服器需要具有潛在廣泛權限的 OAuth 令牌。MCP 安全模型要求客戶端明確授予每個伺服器其功能和範圍。伺服器應聲明其所需的最小權限（最小權限原則）。客戶端應驗證伺服器身份（通過證書或令牌）並記錄所有工具調用以供審計。切勿連接到不受信任的 MCP 伺服器。

### 重點摘要
MCP 的開放、供應商中立協議設計使其成為將 AI 模型連接到外部工具最具互操作性的方式——為跨 LLM 提供商的可移植性而構建，而非鎖定在任何單一生態系統中。

## Related Concepts
- Tool Discovery
- MCP Security
- Streaming Responses
- Protocol Interoperability
- AI Integration
