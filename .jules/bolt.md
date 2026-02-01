## 2026-02-01 - Client-side Search Bottleneck
**Learning:** The site uses synchronous client-side filtering on the main thread for search. As the article list grows (driven by automated agents), this will become a major frame-drop source.
**Action:** Debounce inputs immediately when encountering client-side filtering loops.
