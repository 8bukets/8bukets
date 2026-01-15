## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-24 - Unbounded Response Size in Scraper
**Vulnerability:** The scraper used `await response.text()` to read the full HTTP response body into memory. A malicious or misconfigured server could return a massive payload (e.g., 10GB), causing a Denial of Service (DoS) via memory exhaustion.
**Learning:** Never assume external resources will respect reasonable size limits. `aiohttp`'s `text()` method buffers the entire response.
**Prevention:** Use a maximum response size limit. Check `Content-Length` header first, and read the response stream in chunks (`response.content.iter_chunked`), aborting if the accumulated size exceeds the limit.
