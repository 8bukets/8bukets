## 2026-01-22 - Markdown Reports as UI
**Learning:** The application uses generated Markdown files as its primary user interface. These files lacked navigation and deep linking capabilities, making them hard to scan.
**Action:** When generating Markdown reports, always include a Table of Contents and ensure section headers use HTML anchors (e.g., `## <a id="section"></a>Title`) to allow for reliable internal linking and improved accessibility.
