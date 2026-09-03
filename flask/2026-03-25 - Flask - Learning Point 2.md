---
title: "2026-03-25 - Flask - Learning Point 2"
tags:
  - learning
  - flask
created: 2026-03-25
---

# The Application Context and Request Lifecycle

Flask maintains two contexts: the application context (holds current_app and g) and the request context (holds request and session). The application context is pushed automatically when a request arrives and provides access to `current_app` (the running Flask instance) and `g` (a per-request storage object). The request context wraps the HTTP request, giving you access to `request.args`, `request.form`, `request.json`, and `session`. When the request finishes, both contexts are popped — this is why Flask can handle thousands of concurrent requests with a single worker.

## Key Takeaway
Flask's context system is a thread-local stack — each request gets isolated storage without explicit thread management, making Flask lightweight and fast.

## Related Concepts
- Thread-local variables and current_app
- g object for per-request storage
- Request context and session management
