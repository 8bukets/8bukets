## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-02-03 - Markdown Injection in Analytics Report
**Vulnerability:** Scraped data (e.g., categories, domains) was inserted directly into a Markdown report without sanitization. This allowed for Stored XSS via HTML tags and table structure disruption via pipe characters ('|').
**Learning:** Generating "safe" formats like Markdown still requires sanitization if the viewer supports HTML or if the format has structural delimiters that can be injected.
**Prevention:** Always escape HTML characters (e.g., using 'html.escape') and format-specific delimiters (like '|') when generating structured text files from untrusted input.
