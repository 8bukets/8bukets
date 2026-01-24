## 2026-01-24 - Markdown Navigation Robustness
**Learning:** Implicit header anchors in Markdown are inconsistent across renderers, especially when headers include emojis or special characters.
**Action:** Always use explicit HTML anchors (`<a id='...'></a>`) before headers when generating navigable Markdown reports.
