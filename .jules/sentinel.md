## 2024-05-22 - CSV Injection in Scraper Output
**Vulnerability:** Scraper output to CSV was not sanitized, allowing formula injection (CSV Injection) if external data contains `=`, `+`, `-`, or `@`.
**Learning:** `csv.writer` does not automatically sanitize fields for Excel formula injection. External data from web scraping must be treated as untrusted.
**Prevention:** Sanitize all fields starting with dangerous characters by prepending `'` before writing to CSV.
