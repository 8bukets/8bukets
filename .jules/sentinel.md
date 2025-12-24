## 2024-05-23 - CSV Injection in Report Exports
**Vulnerability:** The scraper was writing user-controlled data (scraped titles, authors, categories) directly into CSV files without sanitization. This allows malicious websites to embed CSV injection payloads (starting with `=`, `+`, `-`, `@`) which could execute arbitrary code when the CSV is opened in Excel.
**Learning:** Even "read-only" tools that export data can introduce client-side vulnerabilities if the export format (CSV) is interpreted as code by the consuming application (Excel).
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to any field starting with injection characters.
