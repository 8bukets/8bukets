## 2026-01-08 - Markdown Report Usability
**Learning:** Collapsing verbose sections (like full lists) using `<details>` and `<summary>` tags significantly improves the readability of generated Markdown reports, especially for CLI tools where users skim for high-level metrics first.
**Action:** Apply this pattern to all generated reports: put the executive summary first, followed by details, and collapse any section that exceeds 10 items.
