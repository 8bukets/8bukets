## 2025-02-18 - CSV Injection in Scraper Output
**Vulnerability:** User-controlled input (e.g., blog titles) starting with characters (`=`, `+`, `-`, `@`) was written directly to CSV files without sanitization, allowing potential formula injection.
**Learning:** Data scraped from the web must be treated as untrusted. When writing to CSV, specific characters can trigger formula execution in spreadsheet software, converting a data file into a code execution vector.
**Prevention:** Sanitize all fields written to CSVs by checking for dangerous prefixes and escaping them (e.g., prepending a single quote `'`).
