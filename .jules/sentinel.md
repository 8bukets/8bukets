## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-05 - Markdown Output Encoding
**Vulnerability:** Scraped content (categories, authors, domains) was inserted directly into a Markdown report without sanitization. This allowed for Stored XSS (if the Markdown viewer renders HTML) and Markdown Table Injection (breaking the report layout with pipe characters).
**Learning:** Even "read-only" formats like Markdown generated from untrusted data require output encoding. Trusting scraped data to be safe for display is a common pitfall.
**Prevention:** Always sanitize dynamic content before inserting it into structured formats (HTML, Markdown, SQL, JSON). For Markdown tables, specifically escape pipe characters (`|`) and HTML tags (`<`, `>`).
