## 2026-01-23 - [Markdown Report UX]
**Learning:** Adding emojis to Markdown headers improves scanability but can break internal linking (Table of Contents) in some renderers if not handled carefully. Pipe characters `|` in data can break Markdown table layouts.
**Action:** Use inline HTML anchors (e.g., `<a id="anchor"></a>Header`) to ensure stable linking regardless of emojis. Always sanitize data interpolated into Markdown tables by escaping pipes (`\|`).
