## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-19 - Markdown Injection in Analytics Report
**Vulnerability:** The `analytics.py` script generated Markdown reports by directly embedding scraped content (like category names and authors) into the document. This allowed for Markdown Injection (breaking tables) and Stored XSS (injecting HTML/Scripts) if the report is rendered in a browser.
**Learning:** Generating structured files (Markdown, HTML, XML) by string concatenation with untrusted input is inherently risky.
**Prevention:** Always sanitize or escape user-controlled data before inserting it into a structured format. For Markdown, escape HTML special characters and syntax-specific characters like pipes (`|`).
