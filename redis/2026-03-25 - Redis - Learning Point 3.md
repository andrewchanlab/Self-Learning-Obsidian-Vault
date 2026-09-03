---
title: "2026-03-25 - Redis - Learning Point 3"
tags:
  - learning
  - redis
created: 2026-03-25
---

# Lua Scripting: Atomic Multi-Step Operations

Redis executes commands one at a time on a single thread, which guarantees atomicity but limits complex operations. Lua scripting solves this by letting you write multi-step scripts that Redis executes atomically — no other command can interleave during script execution. This is crucial for operations like "check if a key exists, increment it, and set a TTL only if it was newly created" (a common pattern for distributed locks). Redis loads the script once and caches it, so subsequent executions are as fast as native commands.

## Key Takeaway
Lua scripts let you bundle multiple Redis commands into a single atomic operation, enabling complex transactional logic without race conditions.

## Related Concepts
- EVAL and EVALSHA commands
- Script caching and SHA-based invocation
- Distributed locking patterns
