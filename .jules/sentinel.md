## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-22 - Markdown Injection in Analytics Report
**Vulnerability:** User input (e.g., categories, authors) containing pipes `|` broke Markdown table structure in generated reports. HTML tags were also passed through, posing an XSS risk.
**Learning:** Text-based formats like Markdown are susceptible to injection attacks similar to SQL or HTML when delimiters are not escaped.
**Prevention:** Implement output encoding for Markdown generation, specifically escaping pipes `|` in tables and HTML characters `< >`.
