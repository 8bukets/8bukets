## 2026-01-25 - Fix CSV Injection (Formula Injection)
**Vulnerability:** Scraper output to CSV was not sanitized, allowing malicious field values (starting with =, @, +, -) to be interpreted as formulas by spreadsheet software.
**Learning:** External data sources, even scraped ones, must be treated as untrusted when generating file formats consumed by rich clients (like Excel/CSV).
**Prevention:** Always sanitize CSV fields by prepending a single quote `'` if the value starts with dangerous characters.
