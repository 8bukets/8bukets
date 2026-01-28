## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-28 - Markdown Injection in Analytics Report
**Vulnerability:** Unsanitized scraped data (e.g., categories, authors) was written to the Markdown report. Malicious input containing `|` could break table layout, and HTML tags could lead to Stored XSS if the Markdown viewer renders raw HTML.
**Learning:** Markdown generation from untrusted input requires sanitization, just like HTML or SQL, especially when generating structural elements like tables.
**Prevention:** Escape special characters (HTML tags `< >` and Markdown table delimiters `|`) in all user-controlled data before adding to the report.
