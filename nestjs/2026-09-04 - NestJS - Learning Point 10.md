---
title: "2026-09-04 - NestJS - Learning Point 10"
tags:
  - learning
  - nestjs
created: 2026-09-04
---

# NestJS Microservices — Building Distributed Systems

NestJS speaks multiple transports: TCP, Redis pub/sub, gRPC, MQTT. Decorate a controller with `@Controller({ protocol: 'tcp' })` and Nest routes messages across service boundaries. Combine with `@MessagePattern` for RPC-style calls or `@EventPattern` for pub/sub — your NestJS app scales from a monolith to a microservices mesh.

## Key Takeaway
NestJS's transport layer abstraction lets you start with a monolith and decompose into microservices without rewriting your services — just change the binding protocol.

## Related Concepts
- Microservices
- gRPC
- Redis Pub/Sub

---

## 中文：NestJS 微服務 — 構建分散式系統

NestJS 支持多種傳輸協議：TCP、Redis 發布/訂閱、gRPC、MQTT。用 `@Controller({ protocol: 'tcp' })` 裝飾控制器，Nest 就可以在服務邊界之間路由消息。配合 `@MessagePattern` 實現 RPC 風格調用，或 `@EventPattern` 實現發布/訂閱 — 你的 NestJS 應用可以從單體擴展到微服務網格。

## 核心要點
NestJS 的傳輸層抽象讓你可以從單體開始，逐步分解為微服務，而無需重寫服務 — 只需更改綁定協議。

## 相關概念
- 微服務
- gRPC
- Redis 發布/訂閱
