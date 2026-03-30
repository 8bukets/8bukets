## 2026-01-23 - [Collapsible Sections in Markdown Reports]
**Learning:** Users find long lists in automated reports overwhelming, leading to "banner blindness" where they skip important sections. Markdown's `<details>` tag provides a native, no-dependency way to implement "progressive disclosure" in text-based reports.
**Action:** When generating automated Markdown reports, always wrap list items exceeding 5 entries in a `<details>` block with a summary count (e.g., "View all 12 items"). This keeps the report scannable while retaining full data access.
