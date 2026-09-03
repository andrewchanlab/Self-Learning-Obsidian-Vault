---
title: "2026-03-25 - Flutter - Learning Point 2"
tags:
  - learning
  - flutter
created: 2026-03-25
---

# State Management: Provider, Riverpod, and BLoC

Flutter apps need to manage state that lives above individual widgets. Provider (Flutter's officially recommended approach) lets you expose values from a parent widget to descendants via `context.read<T>()` or `context.watch<T>()`. Riverpod improves on Provider by making dependencies explicit and testable — providers are defined as functions, not classes. BLoC (Business Logic Component) separates events from states entirely: user actions dispatch events, a BLoC processes them and emits new states, and the UI rebuilds based on state. For simple apps, `setState()` is fine; for complex apps, BLoC or Riverpod prevent state-related bugs at scale.

## Key Takeaway
Flutter's state management options range from simple (setState) to structured (BLoC) — pick based on app complexity, not because of dogma.

## Related Concepts
- ChangeNotifier and ConsumerWidget
- Riverpod's generated providers
- BLoC events and state transitions
