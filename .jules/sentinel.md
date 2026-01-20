## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-20 - Markdown Table Injection and Stored XSS in Reports
**Vulnerability:** The `analytics.py` script generated Markdown reports by directly concatenating scraped data into table rows. Malicious input containing pipe characters `|` broke the table structure (Table Injection), and input containing HTML tags could execute scripts (Stored XSS) if rendered in a vulnerable viewer.
**Learning:** Generating structured formats (like Markdown tables) from untrusted data requires context-specific escaping. Simply trusting the scraper's output is insufficient as the data source might be compromised or contain malicious user-generated content.
**Prevention:** Implement a sanitization function that escapes HTML characters (using `html.escape`) and escapes Markdown table delimiters (replacing `|` with `\|`). Apply this to all dynamic fields before interpolation into the report template.
