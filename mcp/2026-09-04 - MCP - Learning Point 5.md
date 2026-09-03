---
title: "2026-09-04 - MCP - Learning Point 5"
tags:
  - learning
  - mcp
created: 2026-09-04
---

# MCP Client-Server Architecture — Who Talks to Whom?

MCP follows a clear client-server model with three roles: the **MCP Host** (the AI application the user interacts with, like Claude Desktop), the **MCP Client** (a proxy inside the host that manages connections), and the **MCP Server** (a separate process exposing tools, resources, and prompts). Multiple servers can connect to one host simultaneously, and one server can serve multiple clients. Communication uses JSON-RPC 2.0 over stdio or HTTP — simple, universal, and easy to debug.

## Key Takeaway
MCP's three-role architecture (host/client/server) decouples the AI application from external integrations — swap or add servers without touching the client.

## English

### ELI5 Explanation

Imagine you're at a restaurant. You (the **customer/AI**) don't walk into the kitchen to cook — you tell the **waiter (MCP Client)** your order, the waiter talks to the **kitchen (MCP Server)**, and the kitchen prepares the food. The waiter can talk to multiple kitchens at once (seafood kitchen, dessert kitchen). You never need to learn how each kitchen works — you just talk to the waiter.

### Key Points

- **MCP Host**: The AI application you use (e.g., Claude Desktop). It's the user-facing layer.
- **MCP Client**: Lives inside the host, manages active connections to servers. One client per server connection.
- **MCP Server**: Standalone process that exposes tools, resources, and prompts. Can be local (Python script) or remote (cloud API).
- **JSON-RPC 2.0**: The messaging format — every request and response is a JSON object with `method`, `params`, and `id` fields.
- **Multiple servers**: A single MCP host can connect to a filesystem server, a GitHub server, and a database server at the same time.

### Real-World Analogy

```
You (AI) → [Waiter: MCP Client] → [Kitchen: MCP Server] → Food (tool results)
You (AI) → [Waiter 2: MCP Client] → [Dessert Kitchen: MCP Server] → Cake (tool results)
```

The AI never talks directly to kitchens — it goes through standardized waiter interactions.

### When This Matters

- When debugging "why is my MCP server not connecting?" — check the client-server handshake and JSON-RPC message format.
- When adding a new data source — you write a new MCP server, not a new AI integration.

## 中文

### ELI5 解释

想象你去餐厅吃饭。你（**顾客/AI**）不需要亲自走进厨房做菜——你告诉**服务员（MCP Client）**你要什么，服务员去跟**厨房（MCP Server）**沟通，厨房准备好菜。服务员可以同时跟多个厨房沟通（海鲜厨房、甜品厨房）。你永远不需要了解每个厨房是怎么运作的——你只跟服务员说话就行。

### 关键要点

- **MCP Host（主机）**：你使用的 AI 应用程序（如 Claude Desktop），即面向用户的那一层。
- **MCP Client（客户端）**：位于主机内部，管理与各服务器的活跃连接。每个服务器连接对应一个客户端。
- **MCP Server（服务器）**：独立进程，暴露工具、资源和提示模板。可以是本地的（Python 脚本），也可以是远程的（云端 API）。
- **JSON-RPC 2.0**：消息格式——每个请求和响应都是一个带有 `method`、`params` 和 `id` 字段的 JSON 对象。
- **多服务器连接**：一个 MCP 主机可以同时连接文件系统服务器、GitHub 服务器和数据库服务器。

### 实际应用类比

```
你（AI）→ [服务员：MCP Client] → [厨房：MCP Server] → 做好的菜（工具结果）
你（AI）→ [服务员2：MCP Client] → [甜品厨房：MCP Server] → 蛋糕（工具结果）
```

AI 从不直接与厨房对话——所有交互都通过标准化的服务员进行。

### 何时重要

- 调试"为什么我的 MCP 服务器连接不上？"——检查 client-server 握手和 JSON-RPC 消息格式。
- 添加新数据源时——只需编写一个新的 MCP 服务器，无需改动 AI 集成本身。

## Related Concepts
- JSON-RPC 2.0
- Client-Server Architecture
- MCP Host, Client, and Server Roles
- stdio and HTTP transport
