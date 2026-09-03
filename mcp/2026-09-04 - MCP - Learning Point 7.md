---
title: "2026-09-04 - MCP - Learning Point 7"
tags:
  - learning
  - mcp
created: 2026-09-04
---

# MCP Resources and Prompts — The "Read" and "Template" Primitives

While tools let the AI *do* things, Resources let the AI *read* data, and Prompts let the AI *reuse* structured instructions. Resources are content-addressable data (identified by URIs like `file://config/app.yaml` or `db://users/123`) that the MCP server exposes for the client to fetch on demand. Prompts are pre-defined prompt templates stored on the server with placeholder variables — the client invokes them with arguments, and the server returns a fully-rendered prompt string. Together with tools, these three primitives cover every way an LLM interacts with the outside world.

## Key Takeaway
MCP's three primitives — Tools (do), Resources (read), Prompts (template) — give an LLM complete, structured access to act, retrieve, and reuse instructions in any external system.

## English

### ELI5 Explanation

**Resources** are like **reference books in a library**. You don't edit them — you open them and read. The librarian (MCP server) keeps them organized and lets you fetch the right one when you ask. The AI can say "show me the configuration file" and the MCP server returns the file content.

**Prompts** are like **form letter templates** at an office. Instead of writing "Dear Customer, thank you for..." from scratch every time, staff fill in the blanks (name, date, account number) and get a ready-to-send letter. The AI can invoke a prompt template with variables and get a consistent, pre-reviewed instruction.

### Key Points — Resources

- **URI-based addressing**: Resources are identified by URIs (`file://`, `db://`, `api://`) — predictable and unambiguous.
- **On-demand fetching**: The client fetches a resource only when the LLM requests it — no continuous polling.
- **MIME types**: Each resource declares its MIME type so the client knows how to parse it (JSON, text, binary, etc.).
- **Resource templates**: Patterns like `db://users/{user_id}` let the LLM request any user by ID without hardcoding specific IDs.

### Key Points — Prompts

- **Prompt templates**: Server-side templates with `{{variable}}` placeholders — invoked by name with argument values.
- **Consistency**: Prompts are pre-written and reviewed — the AI always uses a well-crafted instruction instead of improvising.
- **Use cases**: "Summarize this code review", "Draft a reply to this support ticket", "Analyze this error log."
- **Prompts vs. System Prompt**: A system prompt is hard-coded in the AI application. MCP prompts are dynamic, server-defined, and can vary by context.

### When This Matters

- When your AI needs to access private data (files, databases) — use Resources with proper URI schemas.
- When you want consistent AI behavior for routine tasks — use Prompt templates to standardize outputs.
- Combining all three: an LLM can use a Resource to read data → use a Tool to process it → use a Prompt to format the output.

## 中文

### ELI5 解释

**资源（Resources）** 就像图书馆里的**参考书**。你不能编辑它们——你只能打开并阅读。图书管理员（MCP 服务器）把它们整理好，当你有需要时帮你取出来。AI 可以说"给我看看配置文件"，MCP 服务器就会返回文件内容。

**提示模板（Prompts）** 就像办公室里的**信函模板**。员工不用每次都从头写"尊敬的客户，感谢您……"，而是填入空白处（姓名、日期、账号）然后发送。AI 同样可以调用带有变量的提示模板，得到一个经过审核的、格式规范的指令。

### 关键要点 — 资源

- **基于 URI 寻址**：资源用 URI 标识（`file://`、`db://`、`api://`）——可预测且无歧义。
- **按需获取**：客户端只在 LLM 请求时才拉取资源——无需持续轮询。
- **MIME 类型**：每个资源声明其 MIME 类型，让客户端知道如何解析（JSON、text、二进制等）。
- **资源模板**：类似 `db://users/{user_id}` 的模式，让 LLM 无需硬编码特定 ID 就能按 ID 请求任意用户。

### 关键要点 — 提示模板

- **提示模板**：服务器端带有 `{{变量}}` 占位符的模板——通过名称加参数值调用。
- **一致性**：提示是预先编写和审核过的——AI 始终使用经过精心设计的指令，而不是临时发挥。
- **使用场景**："总结这次代码审查"、"起草这封工单的回复"、"分析这个错误日志"。
- **Prompts vs. System Prompt**：System Prompt 硬编码在 AI 应用里。MCP Prompts 是动态的、由服务器定义的，可根据上下文变化。

### 何时重要

- 当 AI 需要访问私有数据（文件、数据库）时——使用带正确 URI schema 的资源。
- 当你想让 AI 处理常规任务时保持一致行为——使用提示模板来标准化输出。
- 三者结合：LLM 可以用 Resource 读取数据 → 用 Tool 处理数据 → 用 Prompt 格式化输出。

## Related Concepts
- URI Schemes
- MIME Types
- Prompt Templates
- Resource Templates
- LLM Tool Use
