## 2025-10-16 - CSV Injection Prevention
**Vulnerability:** Untrusted input from scraped websites was being written directly to CSV files without sanitization. If an article title started with `=`, `+`, `-`, or `@`, it could be interpreted as a malicious formula when opened in spreadsheet software (CSV Injection).
**Learning:** Even "trusted" data sources like news sites can contain content that is malicious in a specific context (like a CSV file opened in Excel). Output encoding/sanitization must be context-aware (e.g., specific to CSV format).
**Prevention:** Implemented a `sanitize_for_csv` method that prefixes risky characters with a single quote `'` to force them to be treated as text. Applied this to all fields written to CSV.
