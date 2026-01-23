## 2026-01-23 - [Reliable Anchors with Emojis]
**Learning:** Standard Markdown anchor generation often fails when headers contain emojis (e.g., `# 📊 Stats` might become `#--stats` or `#-%F0%9F%93%8A-stats` depending on the renderer).
**Action:** Use inline HTML anchors (e.g., `## <a id="stats"></a>📊 Stats`) to ensure reliable internal linking regardless of the Markdown processor.
