## 2025-01-29 - [CLI Emoji Alignment]
**Learning:** In Python CLI formatting, emojis like 🚀, 📄, 📊, and 🔗 have a string length of 1 but a visual width of 2 (requiring +1 padding), whereas the stopwatch emoji ⏱️ has a string length of 2 and a visual width of 2 (requiring no padding adjustment).
**Action:** When creating CLI tables with emojis, manually check string length vs visual width and adjust padding logic accordingly to ensure vertical alignment.
