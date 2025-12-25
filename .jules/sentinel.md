## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data was being written directly to CSV files without sanitization. If a scraped title or other field started with characters like `=`, `+`, `-`, or `@`, it could be executed as a formula when opened in spreadsheet software (CSV Injection).
**Learning:** Even in read-only tools like scrapers, output that is destined for other rich-client applications (like Excel) must be treated as untrusted and sanitized. Data "from the internet" is user input.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote `'` to dangerous start characters. Applied this to all fields in the CSV export function.
