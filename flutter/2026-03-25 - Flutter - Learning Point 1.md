---
title: "2026-03-25 - Flutter - Learning Point 1"
tags:
  - learning
  - flutter
created: 2026-03-25
---

# Widget Tree and Composition Model

Flutter's UI is built entirely from widgets — from the outermost `MaterialApp` to the smallest `Text` label. Widgets are immutable descriptions of UI, and they're composed hierarchically: a `Column` contains `Text` and `ElevatedButton` children, which might contain `Icon` children. When any widget's state changes (e.g., a checkbox is toggled), Flutter rebuilds only that widget's subtree — a process called reconciliation — and then calculates the minimal set of changes needed to update the rendered pixels. This is what Flutter calls its "declarative framework" — you describe what the UI should look like given the current state, and Flutter handles the rest.

## Key Takeaway
Flutter's everything-is-a-widget model means UIs are pure functions of state — no imperative DOM manipulation, no virtual DOM diffing, just efficient widget subtree updates.

## Related Concepts
- StatelessWidget vs StatefulWidget
- BuildContext and widget tree traversal
- Element and RenderObject trees
