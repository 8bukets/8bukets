## 2026-01-27 - Handling Emojis in Markdown Headers
**Learning:** Standard Markdown renderers often strip emojis or handle them inconsistently in auto-generated anchor links. To ensure ToC links work reliably, manually verify that anchor links target text-only slugs (e.g., `#general-statistics` instead of `#📊-general-statistics`).
**Action:** When adding emojis to headers, always verify the resulting anchor slug matches the link target.
## 2026-02-06 - ASCII Visualizations in CLI Reports
**Learning:** Text-based reports (Markdown/CLI) are often hard to scan for trends. Adding simple ASCII bar charts (e.g., `█████░░░`) to tables significantly improves the ability to visualize distributions at a glance without needing external tools.
**Action:** When generating text-based reports, always look for opportunities to add "Distribution" columns with ASCII visualizations for numerical data.
