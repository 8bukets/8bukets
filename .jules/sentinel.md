## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-24 - Unsafe URL Extraction in Scraper
**Vulnerability:** The scraper extracted `href` and `src` attributes without validating the URL scheme, allowing `javascript:` or `data:` URIs to be stored and potentially executed by report viewers.
**Learning:** Scraped data is untrusted input. Attributes like `href` can contain executable code (XSS vectors) instead of valid navigation links.
**Prevention:** Validate all extracted URLs against an allowlist of schemes (`http://`, `https://`) before storage.
