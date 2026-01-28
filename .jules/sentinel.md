## 2026-01-28 - Markdown Table Injection & XSS
**Vulnerability:** Unsanitized user input in `analytics.py` allowed Markdown table injection (via pipes `|`) and HTML injection (XSS) in the generated `REPORT.md`.
**Learning:** Generating Markdown programmatically requires escaping special characters, just like HTML or SQL. Python's `html.escape` handles HTML tags, but Markdown tables need specific escaping for pipes `|`.
**Prevention:** Implement a `sanitize_markdown` helper function that escapes HTML entities and backslashes pipe characters before interpolating data into Markdown templates.
