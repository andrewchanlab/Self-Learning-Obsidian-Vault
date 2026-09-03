---
title: "2026-09-04 - Flask - Learning Point 2"
tags:
  - learning
  - flask
created: 2026-09-04
---

# Routes Are Function Decorators — URL to Handler Mapping

@app.route('/users/<id>') maps a URL pattern to a Python function. Flask extracts URL parameters, query strings, form data, and JSON bodies into a `request` object. Return a string, a template, or JSON — Flask handles the HTTP response construction.

## Key Takeaway
Flask's decorator-based routing makes URL mapping intuitive — each route is a plain Python function with a decorator, not a class or configuration object.

## Related Concepts
- URL Routing
- Decorators
- REST API
