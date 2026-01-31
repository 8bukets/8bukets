## 2026-01-31 - Navigation in Markdown Reports
**Learning:** Markdown reports acting as interfaces require explicit HTML anchors (`<a name="..."></a>`) because adding emojis to headers disrupts standard auto-generated ID linking.
**Action:** Always implement a `slugify` function and explicit anchors when creating navigable Markdown documents with rich headers.
