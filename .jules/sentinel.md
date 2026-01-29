## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-29 - Markdown and HTML Injection in Reports
**Vulnerability:** User-controlled input (e.g., author names, categories) was written directly to `REPORT.md` without sanitization. This allowed for HTML injection (XSS if rendered in browser) and Markdown table disruption via `|` characters.
**Learning:** Generating reports/artifacts from untrusted data requires the same level of sanitization as rendering web pages. Markdown is not inherently safe from injection.
**Prevention:** Implemented `sanitize_markdown` to escape `|`, `<`, and `>` before writing to the report.
