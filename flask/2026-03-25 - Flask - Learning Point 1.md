---
title: "2026-03-25 - Flask - Learning Point 1"
tags:
  - learning
  - flask
created: 2026-03-25
---

# Flask's Minimalist Routing Model

Flask maps HTTP routes using Python decorators — `@app.route('/users/<int:user_id>')` binds URL patterns to view functions. Flask uses the Werkzeug routing engine, which supports variable converters (`int:`, `float:`, `path:`) and automatically casts URL segments to the right Python types. Route matching is in order of specificity (static routes before dynamic ones), and Flask can also generate URLs programmatically using `url_for()` — useful for redirects and template links, since it decouples your templates from hardcoded URLs.

## Key Takeaway
Flask's decorator-based routing is elegant and Pythonic — define a function, annotate it with a route, and Flask handles the URL matching.

## Related Concepts
- Werkzeug routing engine
- Variable converters and URL building
- HTTP method binding (GET, POST, etc.)
