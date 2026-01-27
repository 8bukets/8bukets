## 2026-01-27 - [Anchor Links with Emojis]
**Learning:** Markdown headers with emojis (e.g., `## 📊 Title`) create unreliable anchor links across different renderers. Implicit slugs often strip emojis or handle them inconsistently.
**Action:** Use explicit HTML anchors (e.g., `## <a id="title"></a>📊 Title`) in generated Markdown reports to guarantee functional navigation.
