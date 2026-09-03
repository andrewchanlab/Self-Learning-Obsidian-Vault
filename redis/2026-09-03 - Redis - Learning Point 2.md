---
title: "2026-09-03 - Redis - Learning Point 2"
tags:
  - learning
  - redis
created: 2026-09-03
---

# Redis Pub/Sub Enables Real-Time Message Broadcasting

Redis has a built-in publish/subscribe message broker. Clients subscribe to channels with `SUBSCRIBE channel`, and other clients broadcast to channels with `PUBLISH channel message`. Messages are fire-and-forget — if a subscriber is offline, the message is lost. Despite this limitation, Redis Pub/Sub is widely used for real-time dashboards, chat systems, and microservices event buses.

## Key Takeaway
Redis Pub/Sub broadcasts messages to channels in real time with fire-and-forget semantics.

## Related Concepts
- Pub/Sub Pattern
- Channels
- Real-Time Communication

---

# Redis Pub/Sub 實現實時消息廣播

Redis 有內置的發布/訂閱消息代理。客戶端用 `SUBSCRIBE channel` 訂閱頻道，其他客戶端用 `PUBLISH channel message` 向頻道廣播。消息是即發即忘的——如果訂閱者離線，消息就會丟失。儘管有這個限制，Redis Pub/Sub 仍被廣泛用於實時儀表板、聊天系統和微服務事件總線。

## 核心要點
Redis Pub/Sub 以即發即忘語義實時向頻道廣播消息。

## 相關概念
- Pub/Sub 模式
- 頻道
- 實時通信
