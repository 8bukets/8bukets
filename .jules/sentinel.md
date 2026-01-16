## 2026-01-16 - Markdown Injection in Analytics Reports
**Vulnerability:** Scraped data (authors, categories, domains) was inserted directly into Markdown tables and text without sanitization, allowing for Table Injection (breaking report structure) and Stored XSS (if report is rendered to HTML).
**Learning:** When generating Markdown reports from external data, "formatting" characters like `|` must be treated as dangerous control characters, similar to how SQL injection works.
**Prevention:** Always use an `escape_markdown` helper function that escapes `|`, `<`, `>`, and other Markdown control characters before interpolating data into templates.
