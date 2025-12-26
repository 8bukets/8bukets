# Palette's Journal

## 2025-01-26 - [CLI Visual Polish]
**Learning:** CLI tools often lack visual hierarchy, making logs hard to scan. Emojis and colors act as visual anchors, allowing users to quickly identify success, errors, and specific agent activities.
**Action:** Implement a custom `ColorFormatter` for `logging` that assigns specific colors and emojis to different log levels and agent names. Use this formatter across all entry points (`run_system.py`, `scraper.py`).
