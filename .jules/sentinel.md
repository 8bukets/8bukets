## 2026-01-26 - CSV Injection / Formula Injection
**Vulnerability:** Scraper data (e.g., titles, authors) was written directly to CSV files without sanitization. Malicious inputs starting with `=`, `+`, `-`, or `@` could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), leading to arbitrary command execution on the victim's machine.
**Learning:** Even when scraping "static" web content, data must be treated as untrusted. Output formats like CSV have hidden execution risks when opened in rich editors.
**Prevention:** Sanitized all CSV fields by prepending a single quote `'` to strings starting with dangerous characters (`=`, `+`, `-`, `@`). Implemented `sanitize_for_csv` method in the scraper class.
