## 2026-02-04 - Dynamic TOC in Markdown Reports
**Learning:** When generating Markdown reports with conditional sections (e.g., "New Posts" only if data exists), the Table of Contents must also be dynamically generated to match. Static TOCs frustrate users when links point to missing sections.
**Action:** Always check the same conditions for TOC items as for the content sections. Use explicit HTML anchors (`<a name="..."></a>`) for reliable linking across different Markdown viewers.
