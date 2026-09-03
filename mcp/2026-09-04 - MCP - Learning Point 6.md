---
title: "2026-09-04 - MCP - Learning Point 6"
tags:
  - learning
  - mcp
created: 2026-09-04
---

# MCP Tools — How an AI Actually Does Things

Tools are the "action" primitive in MCP. A tool is a typed function — the MCP server declares its name, description, and input schema (using JSON Schema). When an LLM decides it needs to do something (look up a stock price, search the web, run a SQL query), it sends a tool call request back through the MCP client to the server. The server executes the function and returns the result. The whole exchange is transparent: the AI sees the tool's description and output, so it can reason about what happened and decide the next step.

## Key Takeaway
MCP tools let an LLM take real actions in the world — each tool is a typed, documented function with structured input/output, making AI behavior predictable and debuggable.

## English

### ELI5 Explanation

Think of MCP tools like **magic spells in a video game**. Each spell has a name ("Fireball"), a description ("throws a ball of fire at the enemy"), and the magic book (MCP server) knows exactly how to cast it. When the AI decides "I need to throw a fireball," it calls the spell — the game casts it and shows the result. The difference from regular API calls? The AI *chooses* which spell to cast based on the situation, and it can chain spells together to solve multi-step problems.

### Key Points

- **Tool definition**: Each tool has a `name`, `description`, and `inputSchema` (JSON Schema) that tells the LLM what arguments it accepts.
- **Tool call flow**: LLM decides to call tool → sends `tools/call` request → MCP server executes function → returns result as JSON → LLM sees result and continues.
- **Idempotency**: Good MCP tools are idempotent — calling them multiple times with the same args produces the same result (no unintended side effects).
- **Tool vs. API**: A traditional API requires the developer to pre-code WHEN to call it. With MCP tools, the LLM decides dynamically based on the conversation context.
- **Schema-driven**: The input schema is machine-readable — MCP clients can validate arguments before sending, and LLMs use it to understand what the tool does.

### Example Tool Call

```json
// Tool definition (from server)
{
  "name": "get_weather",
  "description": "Get the current weather for a city",
  "inputSchema": {
    "type": "object",
    "properties": {
      "city": { "type": "string", "description": "City name" }
    },
    "required": ["city"]
  }
}

// LLM calls the tool
{
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": { "city": "Hong Kong" }
  }
}
```

### When This Matters

- Building autonomous AI agents that take real actions (not just generating text).
- When you need the AI to interface with live data or external systems.
- Debugging: because tool schemas are explicit, you can trace exactly what the AI tried to do and why.

## 中文

### ELI5 解释

把 MCP 工具想象成**电子游戏里的魔法咒语**。每个咒语都有名字（"火球术"）、描述（"向敌人投掷火球"），魔法书（MCP 服务器）知道怎么施放它。当 AI 决定"我需要施放火球术"时，它调用这个咒语——游戏执行它并显示结果。和普通 API 调用的区别？AI 会根据情况**自主选择**施放哪个咒语，而且可以把多个咒语链接起来解决多步骤问题。

### 关键要点

- **工具定义**：每个工具都有 `name`（名称）、`description`（描述）和 `inputSchema`（输入模式，JSON Schema），告诉 LLM 它接受什么参数。
- **工具调用流程**：LLM 决定调用工具 → 发送 `tools/call` 请求 → MCP 服务器执行函数 → 以 JSON 格式返回结果 → LLM 看到结果后继续。
- **幂等性**：好的 MCP 工具是幂等的——用相同参数多次调用产生相同结果（不会产生意外的副作用）。
- **工具 vs. API**：传统 API 需要开发者预先编码"何时"调用它。MCP 工具则由 LLM 根据对话上下文动态决定。
- **模式驱动**：输入 schema 是机器可读的——MCP 客户端可以在发送前验证参数，LLM 也能用它来理解工具的用途。

### 工具调用示例

```json
// 工具定义（来自服务器）
{
  "name": "get_weather",
  "description": "获取城市当前天气",
  "inputSchema": {
    "type": "object",
    "properties": {
      "city": { "type": "string", "description": "城市名称" }
    },
    "required": ["city"]
  }
}

// LLM 调用工具
{
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": { "city": "香港" }
  }
}
```

### 何时重要

- 构建能执行真实操作的自主 AI 智能体（不只是生成文本）。
- 当你需要 AI 与实时数据或外部系统对接时。
- 调试时：因为工具 schema 是显式的，你可以精确追踪 AI 尝试做了什么以及为什么。

## Related Concepts
- JSON Schema
- Tool Calling
- Function Calling
- LLM Agent Loop
- Idempotency
