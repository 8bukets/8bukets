# Sentinel's Journal

## 2025-02-20 - CSV Injection Vulnerability
**Vulnerability:** The scraper was writing untrusted data (post titles, authors, etc.) directly to a CSV file without sanitization. If the data started with characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software (Excel, Google Sheets), potentially executing arbitrary commands or exfiltrating data.
**Learning:** Even "internal" tools that generate reports can be vectors for attack if the output is consumed by vulnerable software like Excel. Data from the web is always untrusted.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with dangerous characters (`=`, `+`, `-`, `@`) to force them to be treated as strings.
