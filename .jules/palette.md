## 2026-01-22 - [Generated Markdown Navigation]
**Learning:** When generating Markdown reports programmatically (`analytics.py`), inserting semantic emojis in headers (e.g., `## 📈 Stats`) breaks standard auto-generated anchors.
**Action:** Always inject explicit HTML anchors inline (e.g., `## <a id="stats"></a>📈 Stats`) to ensure the Table of Contents works reliably.
