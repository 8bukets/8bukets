## 2026-02-02 - Enhanced Analytics Report UX
**Learning:** Adding a Table of Contents and emojis to Markdown reports significantly improves scanability and user delight, but table generation requires careful sanitization of pipe characters (`|`) to prevent layout breakage.
**Action:** Always include a `sanitize()` helper for Markdown table generation that escapes pipes as `&#124;`.
