---
title: "2026-03-25 - Redis - Learning Point 2"
tags:
  - learning
  - redis
created: 2026-03-25
---

# Pub/Sub and the Publish-Subscribe Pattern

Redis includes a built-in publish-subscribe (pub/sub) messaging system. Publishers send messages to channels, and subscribers receive messages from channels they've subscribed to — a one-to-many broadcast pattern. Unlike message queues (like RabbitMQ or Kafka), pub/sub is fire-and-forget: if a subscriber is offline when a message is published, that message is lost. Despite this limitation, Redis pub/sub is extremely lightweight and perfect for real-time features like chat notifications, live dashboards, or invalidating cache entries across multiple application instances.

## Key Takeaway
Redis pub/sub provides a lightweight, low-latency broadcast channel for real-time messaging, best suited for cases where message loss is acceptable.

## Related Concepts
- Channels vs Patterns subscriptions
- Redis Streams (for durable messaging)
- Real-time notification systems
