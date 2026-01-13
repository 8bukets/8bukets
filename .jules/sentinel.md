## 2024-03-24 - [CSV Formula Injection in Scrapers]
**Vulnerability:** User-generated content from external websites (titles, authors) was written directly to CSV files without sanitization. Payloads starting with `=`, `+`, `-`, or `@` could execute arbitrary formulas when opened in Excel (CSV Injection).
**Learning:** Even when not using a database, "data storage" (like CSV) requires input sanitization. Scrapers often trust the source HTML too much. `csv.writer` does not automatically escape formula characters.
**Prevention:** Implement a `sanitize_for_csv` method that prepends a single quote `'` to any value starting with the dangerous characters (`=`, `+`, `-`, `@`) before writing to the CSV.
