## 2026-01-04 - CSV Formula Injection
**Vulnerability:** The scraper was writing user-controlled input (Post Title, Author, etc.) directly to a CSV file. Malicious input starting with `=`, `+`, `-`, or `@` could be interpreted as a formula by spreadsheet software (Excel, Sheets), potentially executing arbitrary code (CSV Injection).
**Learning:** Even simple data export formats like CSV require sanitization if the data comes from an untrusted source. "Trusted" sources like a specific Wordpress site can still be compromised or have malicious comments/content.
**Prevention:** Implemented a `sanitize_for_csv` method that prefixes risky characters with a single quote `'` to force them to be treated as text. This pattern should be applied to all CSV exports.
