## 2026-01-18 - Navigable Markdown Reports
**Learning:** For CLI tools that output Markdown reports, adding explicit HTML anchors (`<a name="..."></a>`), a Table of Contents, and "Back to Top" links significantly improves usability, especially for long documents. This mimics the "skip to content" pattern in web a11y.
**Action:** Apply this pattern to all future Markdown report generators. Ensure anchors are placed *before* the headers to avoid scrolling overlap issues in some viewers.
