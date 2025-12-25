## 2024-05-23 - CSV Injection in Scraper
**Vulnerability:** User-controlled input (like post titles) was written directly to CSV files without sanitization, allowing for potential CSV Injection (Formula Injection) attacks if the data starts with characters like `=`, `+`, `-`, or `@`.
**Learning:** Even when scraping data from seemingly benign sources, it should be treated as untrusted input when writing to formats like CSV that have executable capabilities in some viewers (Excel).
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote to potentially dangerous strings before writing to CSV.
