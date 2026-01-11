## 2024-04-20 - [CSV Injection Vulnerability in Scraper]
**Vulnerability:** The scraper writes unsanitized user-controlled data (titles, authors, etc.) directly into a CSV file.
**Learning:** Even internal tools that generate CSVs can be vectors for attacks if the output is opened in spreadsheet software (Excel, LibreOffice) which executes formulas starting with `=`, `+`, `-`, or `@`.
**Prevention:** Sanitize all fields starting with these characters by prepending a single quote `'` before writing to CSV.
