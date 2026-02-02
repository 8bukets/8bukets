## 2024-05-22 - [Enhancing Generated Reports]
**Learning:** Adding a Table of Contents and emojis to auto-generated Markdown reports significantly improves scannability and makes the output feel more like a polished product than a raw log.
**Action:** Always include a TOC for reports longer than one page, and use consistent emojis to denote section types (e.g., 📊 for stats, 🔗 for links).

## 2024-05-22 - [Markdown Table Sanitization]
**Learning:** Generated Markdown tables are fragile; a single pipe character `|` in the data can break the entire layout.
**Action:** Always sanitize data injected into Markdown tables by replacing `|` with `&#124;`.
