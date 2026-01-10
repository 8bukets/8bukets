## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2025-05-15 - Unbounded Response Size in Scraper
**Vulnerability:** The scraper used `await response.text()` to read the full response body into memory without a size limit. A compromised or malicious server could serve an infinitely large response, causing a Denial of Service (OOM Crash).
**Learning:** Network clients must never assume the server will behave nicely. Default library methods often favor convenience (read all) over safety.
**Prevention:** Always enforce a maximum size limit when reading data from untrusted network sources, using chunked reading to abort early.
