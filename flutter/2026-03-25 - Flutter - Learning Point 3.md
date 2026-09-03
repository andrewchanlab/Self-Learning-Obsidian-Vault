---
title: "2026-03-25 - Flutter - Learning Point 3"
tags:
  - learning
  - flutter
created: 2026-03-25
---

# Platform Channels: Bridging Flutter to Native Code

Flutter can talk to native Android (Kotlin/Java) and iOS (Swift/Objective-C) code via Platform Channels — a bi-directional communication bridge. Your Dart code calls `MethodChannel.invokeMethod()`, which serializes the method name and arguments and sends them over a platform-specific channel to the native side, which processes it and returns a result. This is how Flutter accesses camera, Bluetooth, AR features, or any native SDK that doesn't have a Flutter plugin yet. Most native features you need are already available as pub packages, but understanding platform channels helps when you need to build custom native integrations.

## Key Takeaway
Platform channels let Flutter reach beyond its own capabilities — any native API can be called from Dart, making Flutter a true cross-platform framework, not a lowest-common-denominator solution.

## Related Concepts
- MethodChannel and EventChannel
- FlutterEngine and PlatformViewRegistry
- Pigeon for type-safe channel communication
