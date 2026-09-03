---
title: "2026-03-25 - StreamLit - Learning Point 2"
tags:
  - learning
  - streamlit
created: 2026-03-25
---

# Session State: Maintaining State Across Interactions

Unlike traditional web frameworks where state persists between requests, Streamlit's request-response model resets after each interaction — except for Session State. By using `st.session_state`, you can store variables that persist across re-runs triggered by user interactions. For example, if a user uploads a file and then clicks "Process," you need `session_state` to remember which file was uploaded. Without it, every button click would reset all variables and your app would "forget" everything between interactions.

## Key Takeaway
Session State is Streamlit's mechanism for preserving data across re-runs — essential for multi-step workflows and any app where previous user actions should influence future behavior.

## Related Concepts
- st.session_state dictionary
- Callback functions in Streamlit
- Widget key binding to session state
