## 2026-01-22 - [Markdown Emojis & Anchors]
**Learning:** Adding semantic emojis to Markdown headers disrupts auto-generated ID slugs, breaking internal linking in Tables of Contents.
**Action:** Always insert explicit HTML anchors (`<a id="slug"></a>`) within headers that contain emojis to ensure reliable navigation.
