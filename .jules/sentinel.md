## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-23 - Unbounded Response Size (DoS)
**Vulnerability:** The scraper used `await response.text()` which reads the entire response body into memory without a limit. A malicious server (or a compromised one) could send a massive response (e.g. 10GB), causing a Denial of Service via memory exhaustion.
**Learning:** `aiohttp.ClientResponse.text()` does not enforce a size limit by default. Always assume external inputs can be infinitely large.
**Prevention:** Use `response.content.iter_chunked()` to read the response in chunks and enforce a maximum size limit (e.g., 10MB) before decoding.
