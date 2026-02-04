## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-02-04 - Markdown Injection in Analytics Report
**Vulnerability:** User-controlled data (authors, categories, domains) was written directly to a Markdown report. Special characters like `|` could break table layouts, and HTML characters could allow Stored XSS if the report is rendered in a vulnerable viewer.
**Learning:** Text-based formats like Markdown require sanitization just like HTML or SQL, especially when generating structured elements like tables.
**Prevention:** Sanitize untrusted input by escaping Markdown-specific characters (`|` -> `&#124;`) and HTML entities (`<` -> `&lt;`, `>` -> `&gt;`) before writing to the report.
