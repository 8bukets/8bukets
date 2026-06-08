## 2026-02-06 - ASCII Visualizations in CLI Reports
**Learning:** Text-only tables in Markdown reports are hard to scan for magnitude differences. Adding simple ASCII bar charts (using '█' and '░') significantly improves the ability to visualize distributions without needing a GUI.
**Action:** Use `create_ascii_bar` helper for any future CLI-generated statistics reports to maintain visual consistency.
## 2026-01-27 - Report Navigation & Readability
**Learning:** In text-heavy CLI reports, users struggle to jump between data sections without a Table of Contents and visual anchors (emojis), leading to excessive scrolling.
**Action:** Standardize generated Markdown reports to always include a TOC, emoji headers for scanning, and "Back to Top" links for navigation.
