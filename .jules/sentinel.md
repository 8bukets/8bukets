## 2024-05-23 - CSV Injection in Scraper
**Vulnerability:** The scraper was writing user-controlled data (titles, authors, etc.) directly into a CSV file without sanitization. If a field started with `=`, `@`, `+`, or `-`, it could be interpreted as a formula by spreadsheet software (Excel), leading to potential command execution or data exfiltration on the user's machine.
**Learning:** Even simple data collection scripts can introduce client-side vulnerabilities if the data format (like CSV) has interpreted features. Always treat scraped data as untrusted.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` if they start with dangerous characters. This forces the spreadsheet to treat the cell as text.
