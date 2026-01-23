## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-23 - Stored XSS in Markdown Reports
**Vulnerability:** User-controlled data (e.g., author names, categories) was written directly to `REPORT.md` without sanitization, allowing for Stored XSS if the report is rendered in a browser.
**Learning:** Generating "safe" formats like Markdown can still lead to injection vulnerabilities if the viewer interprets HTML or if the syntax is broken (e.g., table injection).
**Prevention:** Always escape HTML special characters and format-specific delimiters (like `|` for Markdown tables) when inserting untrusted data into generated documents.
