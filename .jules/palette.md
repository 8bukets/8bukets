## 2026-02-05 - [CLI Report Visuals]
**Learning:** Text-based reports (Markdown/CLI) are hard to scan without visual weight.
**Action:** Use simple ASCII bar charts (e.g., `████░`) in tables to visualize relative magnitudes in generated reports.
## 2025-02-03 - Rich CLI Feedback Pattern
**Learning:** CLI tools often lack visual hierarchy, making it hard to spot errors in a wall of text. Adding ANSI colors and emojis (✅, ❌, ⚠️) significantly improves scanability and user confidence during long-running processes.
**Action:** Implement `UXFormatter` class in all CLI scripts to standardize colored feedback for Info, Success, Warning, and Error states.
## 2024-05-22 - Improved Analytics Report UX
**Learning:** Adding a Table of Contents and emojis to Markdown reports significantly improves scanability and user delight.
**Action:** Always include a TOC and visual indicators (emojis) in generated reports to help users quickly navigate content.
## 2026-01-27 - Report Navigation Patterns
**Learning:** For generated Markdown reports, adding explicit 'Back to Top' links significantly improves navigation on long documents, but requires a stable Table of Contents anchor.
**Action:** Always include a ToC with a fixed ID (`#table-of-contents`) when generating multi-section reports.
## 2026-02-06 - ASCII Charts for Markdown Reports
**Learning:** Adding simple ASCII bar charts (e.g., `████░`) to CLI-generated Markdown reports significantly improves data readability without adding dependencies.
**Action:** Use `create_ascii_bar` helper in future CLI report generators to visualize distributions.
