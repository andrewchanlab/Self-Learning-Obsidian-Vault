---
title: "2026-03-25 - MCP - Learning Point 3"
tags:
  - learning
  - mcp
created: 2026-03-25
---

# MCP vs Tool Use: Why Standardization Matters

Before MCP, every AI application that wanted to call external tools defined its own ad-hoc format — OpenAI's function calling, Anthropic's tool use, and LangChain's tool abstractions all look different. This meant developers had to re-implement "how to search a database" for every AI framework they used. MCP creates a vendor-neutral, cross-platform standard that works regardless of which LLM you're using. Once an MCP server exists (e.g., a Postgres MCP server), any MCP host — Claude Desktop, Cursor, your custom app — can use it. This is exactly the value of standards: the ecosystem builds shared infrastructure instead of duplicating effort.

## Key Takeaway
MCP's value isn't any single feature — it's the standard itself: shared infrastructure that grows the AI tool ecosystem by eliminating per-framework reinvention.

## Related Concepts
- Anthropic's Model Context Protocol specification
- MCP server registries and discovery
- JSON-RPC over stdio or HTTP/SSE transports
