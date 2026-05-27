<<<<<<< palette-analytics-report-ux-1529011215089105936
## 2026-01-27 - Markdown Reports as UI
**Learning:** For CLI tools where the primary output is a Markdown report, users treat it as a read-only UI. Lacking navigation (TOC, anchors) makes data consumption difficult, similar to a webpage without a menu.
**Action:** Always include a Table of Contents, explicit HTML anchors (for reliability with emojis), and "Back to Top" links in generated Markdown reports to simulate web navigation.
=======
## 2026-02-06 - ASCII Visualizations in CLI Reports
**Learning:** Text-based reports (Markdown/CLI) are often hard to scan for trends. Adding simple ASCII bar charts (e.g., `█████░░░`) to tables significantly improves the ability to visualize distributions at a glance without needing external tools.
**Action:** When generating text-based reports, always look for opportunities to add "Distribution" columns with ASCII visualizations for numerical data.
>>>>>>> jules/scraper-markposition-17752547678215960211
