## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-23 - Malicious Link Extraction
**Vulnerability:** Scraper extracted `javascript:` links as valid URLs, creating XSS vectors in generated reports and downstream data usage.
**Learning:** regex validation for URLs must be applied to ALL sources of URL input (href, src, text), not just some. "Looks like a URL" heuristics should strictly enforce safe protocols (http/s).
**Prevention:** Validate all extracted URLs with an allow-list protocol check (e.g., `^https?://`) before storing.
