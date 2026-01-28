## 2026-01-28 - CSV Injection in Data Export
**Vulnerability:** User-generated content (blog titles) was written directly to CSV files without sanitization, allowing for formula injection (CSV Injection) if the content started with =, +, -, or @.
**Learning:** Even when scraping data, we cannot trust the source. Malicious or accidental characters in scraped content can exploit the tools used to view that data (like Excel).
**Prevention:** Always sanitize data written to CSVs by prepending a single quote (') to values starting with risky characters (=, +, -, @). Use a dedicated sanitization helper for all CSV exports.
