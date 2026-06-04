## 2026-02-06 - ASCII Visualizations in CLI Reports
**Learning:** Adding simple ASCII bar charts (e.g., ▓▓░░) to Markdown tables significantly improves the scannability of data distributions in CLI-generated reports without adding heavyweight dependencies.
**Action:** identifying opportunities to add "Distribution" columns to other text-based analytics tools.
## 2026-01-27 - [Visual Hierarchy in Generated Reports]
**Learning:** CLI tools often output dry text. Adding simple visual hierarchy (emojis, highlights) and navigation (TOC) to generated Markdown reports significantly increases perceived value and accessibility without adding dependencies.
**Action:** Always structure generated reports with a clear summary/highlight at the top and navigable sections.
## 2024-05-22 - CLI Visual Hierarchy
**Learning:** CLI tools often output dense blocks of white text, making it difficult for users to quickly scan for errors or success states. Adding simple ANSI colors and semantic emojis (e.g., ❌ for error, 💾 for save) drastically reduces cognitive load and improves perceived quality.
**Action:** Always check if a CLI tool has a `logging` configuration and propose a custom `Formatter` to inject visual hierarchy.
