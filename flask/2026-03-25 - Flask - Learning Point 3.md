---
title: "2026-03-25 - Flask - Learning Point 3"
tags:
  - learning
  - flask
created: 2026-03-25
---

# Blueprints: Organizing Large Flask Applications

For larger apps, putting all routes in a single `app.py` becomes unwieldy. Flask Blueprints solve this by letting you group routes into modular components. A Blueprint registers routes with a URL prefix and optional template/static folder namespace, but doesn't fully initialize the app until it's registered with `app.register_blueprint()`. This means you can organize a project as `auth/`, `api/`, and `admin/` blueprints — each developer's team works independently, and the main app simply assembles them.

## Key Takeaway
Blueprints give Flask a modular architecture — each blueprint is a mini-app that can be developed, tested, and versioned independently before being plugged into the main app.

## Related Concepts
- Blueprint URL prefixes and namespaces
- Application factory pattern (create_app)
- Blueprint-specific error handlers
