## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2025-12-30 - Markdown Table Injection & XSS
**Vulnerability:** User-controlled data (e.g., categories, authors) was written directly to a Markdown report without sanitization. Malicious input containing `|` could break table layouts (Markdown Table Injection), and HTML tags could lead to Stored XSS if the report is rendered in a browser.
**Learning:** Markdown generation is not inherently safe; special characters like `|` and `<` must be escaped when handling dynamic content.
**Prevention:** Use `html.escape()` for all dynamic content in Markdown, and explicitly escape `|` as `\|` within table cells.
