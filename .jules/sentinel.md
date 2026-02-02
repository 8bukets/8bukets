## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-02-02 - Markdown Table Injection in Analytics Report
**Vulnerability:** Scraped data containing pipe characters (`|`) or HTML tags broke the Markdown table structure and allowed for Stored XSS/HTML injection in the generated report.
**Learning:** Generating Markdown programmatically requires sanitization just like HTML or SQL, especially when creating tables where `|` is a structural character.
**Prevention:** Use a `sanitize_markdown` function to HTML-escape content and replace pipe characters (`|`) with their HTML entity (`&#124;`) before inserting into Markdown tables.
