---
title: "2026-09-04 - MCP - Learning Point 2"
tags:
  - learning
  - mcp
created: 2026-09-04
---

# MCP Architecture — Hosts, Clients, and Servers

An MCP **host** is the AI application (like Claude Desktop or an IDE). An MCP **client** lives inside the host and maintains a 1:1 connection with an MCP **server**. The server exposes tools, resources, and prompts. The client discovers them and presents them to the AI model. Multiple servers can connect to one host, giving the AI access to many tool sources simultaneously.

## Key Takeaway
MCP's client-server architecture lets a single AI application connect to multiple external tool sources through standardized MCP servers.

## Related Concepts
- Client-Server Architecture
- Protocol Stack
- Plugin Architecture
