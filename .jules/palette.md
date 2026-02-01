## 2026-02-01 - Web-Like Navigation in Static Reports
**Learning:** Generated Markdown reports often act as the primary UI for CLI tools. Users expect web-like navigation (ToC, Back to Top) even in static files to manage information density. Explicit HTML anchors (`<a name='slug'></a>`) are more robust than relying on implicit Markdown header anchors across different viewers.
**Action:** Always include a Table of Contents and explicit anchor tags for sections in generated Markdown reports that exceed one screen height.
