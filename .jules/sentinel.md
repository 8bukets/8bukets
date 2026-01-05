## 2025-01-05 - CSV Injection in Scraper
**Vulnerability:** The scraper was directly writing unvalidated input (e.g., news titles) into a CSV file. Malicious titles starting with `=`, `@`, `+`, or `-` could execute code if the CSV is opened in spreadsheet software (Excel).
**Learning:** Even internal data scraping tools need input sanitization if the output format (like CSV) can be interpreted as executable code by other software.
**Prevention:** Sanitize all fields in `scraper.py` before writing to CSV by prepending a single quote `'` to risky characters.
