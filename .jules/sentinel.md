## 2024-05-23 - Prevent CSV Formula Injection
**Vulnerability:** User-controlled data (scraped titles, authors, categories, etc.) was being written directly to a CSV file. If this data started with special characters like `=`, `+`, `-`, or `@`, spreadsheet software (Excel, LibreOffice) would interpret it as a formula, potentially leading to command execution or data exfiltration.
**Learning:** Even when scraping data from "public" sources, the content is untrusted and can contain malicious payloads designed to target data analysts. Always treat scraped data as untrusted input.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` if the value starts with risky characters. This forces the spreadsheet software to treat the cell content as a string.
