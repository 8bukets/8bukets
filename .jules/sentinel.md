## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-02-06 - Markdown/HTML Injection in Analytics Report
**Vulnerability:** User-controlled data (categories, author names) was directly embedded into Markdown tables in `REPORT.md`, allowing HTML injection (XSS in viewers) and table structure manipulation (via pipe characters).
**Learning:** Markdown generation is susceptible to injection attacks similar to HTML/SQL. Pipe characters in data can break table layouts, and HTML tags are often rendered by Markdown viewers.
**Prevention:** Implemented `escape_markdown()` helper to sanitize inputs by escaping HTML entities and pipe characters before generating the report.
