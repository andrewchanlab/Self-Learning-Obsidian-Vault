---
title: "2026-03-25 - MCP - Learning Point 2"
tags:
  - learning
  - mcp
created: 2026-03-25
---

# MCP Server Implementation: Tools, Resources, and Prompts

An MCP server exposes three types of capabilities. Tools are callable functions with typed input/output schemas — when an LLM decides to use a tool, it sends the tool name and arguments back through the protocol. Resources are data sources the LLM can read (like files, database rows, or API responses) — the server defines the resource URI scheme and the client fetches content on demand. Prompts are pre-written prompt templates stored on the server that the client can invoke with variables — useful for standardizing common workflows like "review this code" or "explain this error log."

## Key Takeaway
MCP's three primitives (tools, resources, prompts) cover the three ways an LLM interacts with the world: doing (tools), reading (resources), and templating (prompts).

## Related Concepts
- JSON-RPC 2.0 message format
- Tool call lifecycle (propose → call → result)
- Resource URI schemes and MIME types
