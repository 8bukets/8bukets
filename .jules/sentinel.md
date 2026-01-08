## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-23 - DoS via Large Response Bodies
**Vulnerability:** The scraper used `await response.text()` which loads the entire HTTP response body into memory. A malicious or misconfigured server could return a massive response (e.g., 10GB), causing memory exhaustion and crashing the application.
**Learning:** Never assume external resources will behave well. `aiohttp` (and `requests`) does not limit body size by default when using convenience methods like `.text()`.
**Prevention:** Stream the response content in chunks (using `iter_chunked`) and enforce a maximum byte limit (e.g., 10MB) before processing.
