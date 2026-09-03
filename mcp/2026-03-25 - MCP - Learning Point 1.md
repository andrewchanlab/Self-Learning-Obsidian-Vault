---
title: "2026-03-25 - MCP - Learning Point 1"
tags:
  - learning
  - mcp
created: 2026-03-25
---

# Model Context Protocol: Solving the Context Window Problem

MCP (Model Context Protocol) is an open protocol developed by Anthropic that lets AI models connect to external data sources and tools in a standardized way. The core problem it solves: an LLM's context window is finite, but the knowledge needed to answer questions is vast. MCP provides a client-server architecture where an AI application (the MCP host) connects to servers that expose tools, resources, and prompts. Instead of hard-coding "how to query my database," developers implement an MCP server once, and any MCP-compatible AI application can use it — a USB-C port for AI integrations.

## Key Takeaway
MCP turns the wild west of AI tool integrations into a standardized plug-and-play ecosystem — one MCP server works across all MCP-compatible clients.

## Related Concepts
- MCP host, client, and server roles
- Tool definitions as structured JSON schemas
- Prompt templates and resource templates
