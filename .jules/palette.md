# Palette's Journal

This journal records critical UX and accessibility learnings.

## 2026-02-03 - CLI Visual Polish
**Learning:** Developers often ignore wall-of-text logs. Adding colors and emojis (e.g. ℹ️ for info, ❌ for errors) makes status checks scanning significantly faster.
**Action:** Use a custom `logging.Formatter` to inject ANSI codes and emojis into standard Python logging.
