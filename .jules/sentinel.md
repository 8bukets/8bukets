## 2024-05-23 - CSV Injection (Formula Injection)
**Vulnerability:** User-controlled input (like titles starting with `=`) in `scraper.py` was being written directly to a CSV file.
**Learning:** Even internal tools that export data to CSV can be vectors for attacks if the CSV is opened in spreadsheet software (Excel, LibreOffice) which executes formulas.
**Prevention:** Always sanitize CSV fields by prepending a single quote `'` if the value starts with `=`, `+`, `-`, or `@`.
