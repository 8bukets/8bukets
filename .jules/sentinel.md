## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-30 - Markdown Injection in Analytics Report
**Vulnerability:** User-controlled data (authors, categories) in `links.json` was written directly to `REPORT.md` without sanitization. This allowed Markdown table injection (via `|`) and Stored XSS (via HTML tags).
**Learning:** Generating reports in text formats like Markdown requires just as much sanitization as HTML or SQL to prevent injection attacks and rendering issues.
**Prevention:** Implemented `sanitize_markdown` to escape `|`, `<`, `>`, and `\` before writing to the report.
