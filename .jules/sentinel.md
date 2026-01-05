## 2024-02-14 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (titles, authors) scraped from websites could contain formula injection payloads (`=`, `+`, `-`, `@`) which execute when the CSV is opened in spreadsheet software.
**Learning:** Even if data comes from a "trusted" source (the scraped website), it can be malicious if that site was compromised or allows user content. Scrapers essentially trust the source blindly.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` to any field starting with dangerous characters. This forces the spreadsheet to treat it as a string.

## 2024-02-14 - Missing Timeout in Scraper
**Vulnerability:** `aiohttp` requests were made without an explicit timeout in the scraper loop.
**Learning:** Default timeouts might not exist or be too long (e.g. 5 mins), leading to resource exhaustion (DoS) if the server hangs.
**Prevention:** Always set an explicit `ClientTimeout` (e.g., 30s) when making external network requests.
