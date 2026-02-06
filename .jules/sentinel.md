## 2026-02-06 - Markdown Injection in Analytics Report
**Vulnerability:** Scraped data (categories, author names) containing Markdown table characters (`|`) or HTML tags was injected directly into the generated `REPORT.md`, breaking table structure and introducing XSS risks.
**Learning:** Generating reports from untrusted data requires sanitization, even for simple text formats like Markdown, as they often support HTML and have strict structural requirements (tables).
**Prevention:** Implemented `escape_markdown` function to sanitize critical characters (`|`, `<`, `>`) before inserting data into the report.
