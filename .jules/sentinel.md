## 2026-01-31 - CSV Injection in Scraper
**Vulnerability:** The scraper wrote data directly to CSV files without sanitization. If a scraped post title or other field started with characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software (CSV Injection/Formula Injection), potentially leading to code execution on the analyst's machine.
**Learning:** Any external input destined for CSV output must be treated as untrusted, regardless of the source. Standard `csv` libraries do not handle formula injection protection by default.
**Prevention:** Implement a sanitization layer that detects dangerous starting characters and escapes them (e.g., by prepending a single quote) before writing to CSV.
