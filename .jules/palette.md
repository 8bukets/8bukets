## 2026-01-24 - Robust Markdown Navigation
**Learning:** Implicit header IDs in generated Markdown are unreliable across different viewers. Explicit HTML anchors (`<a id='...'></a>`) are necessary for robust Tables of Contents and "Back to Top" links.
**Action:** Always inject explicit anchors when programmatically generating markdown reports that require navigation.
