## 2026-01-03 - Markdown Anchors and Emojis
**Learning:** Markdown anchors generated from headers with emojis (e.g., `## 💡 Recommendations`) are brittle and vary across renderers (GitHub, VS Code, etc.).
**Action:** Use explicit HTML anchors (e.g., `<a name="recommendations"></a>`) in headers and link to them directly (`#recommendations`) to ensure consistent navigation behavior.
