## 2026-01-27 - CLI Report Experience
**Learning:** Generated Markdown reports are a primary UI for CLI tools. Adding TOCs, anchor links, and emojis significantly improves readability and scanability, much like a web page.
**Action:** Treat generated documentation as a first-class UI surface. Ensure anchor links are slugified correctly (stripping emojis) for compatibility.
## 2026-02-06 - ASCII Charts in Markdown Reports
**Learning:** ASCII visualizations (like bar charts using block characters) significantly improve the readability of data-heavy markdown reports. Handling small non-zero values with a distinct character (like '▏') is crucial to avoid misleading 'empty' bars.
**Action:** Always consider adding simple text-based visualizations and handle edge cases for small values.
