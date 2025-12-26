## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-10-24 - Unsafe Link Extraction
**Vulnerability:** The scraper blindly extracted `href` and `src` attributes without validating the URI scheme, allowing `javascript:` URIs to be saved.
**Learning:** Scrapers must treat extracted URLs as untrusted user input and validate the protocol (scheme) before use/storage.
**Prevention:** Implement a strict allowlist of URI schemes (e.g., `http`, `https`) for all extracted links.
