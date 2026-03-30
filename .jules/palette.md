## 2026-01-24 - [Markdown Report Readability]
**Learning:** Long tables in Markdown reports break layout and readability when content strings are too long. Users lose context when scrolling horizontally.
**Action:** Always truncate long text fields in generated reports and provide a "View details" mechanism or just show the start of the string.

## 2026-01-24 - [Information Overload in Reports]
**Learning:** Daily reports with large lists of items (e.g., 50+ new posts) overwhelm the user and hide critical summary insights.
**Action:** Use `<details>` and `<summary>` tags to collapse large lists by default, allowing users to opt-in to seeing the raw data.
