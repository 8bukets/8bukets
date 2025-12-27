## 2025-12-27 - Markdown Injection & XSS in Generated Reports
**Vulnerability:** User-controlled input (e.g., author names, categories) containing pipe characters (`|`) or HTML tags was directly inserted into Markdown tables in `REPORT.md`. This allowed for Markdown Table Injection (breaking report layout) and Stored XSS (if the report is viewed in a browser).
**Learning:** Generating Markdown or CSV programmatically requires strict escaping of delimiters (`|`, `,`) and HTML entities, just like SQL or HTML generation. Never trust data just because it was scraped; the source site could be compromised or malicious.
**Prevention:** Always use sanitization functions (like `html.escape` and specific character replacement) when generating structured text formats from untrusted input.
