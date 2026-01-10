## 2025-05-15 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (news titles, authors) was written directly to CSV without sanitization. Characters like `=`, `+`, `-`, `@` at the start of a field could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), leading to potential command execution or data exfiltration.
**Learning:** Even when scraping "trusted" sites like Oracle, the content can be manipulated or contain unexpected characters. Always treat external input as untrusted. "CSV" is not just a text format; it's a spreadsheet format with executable capabilities.
**Prevention:** Sanitized all fields by prepending a single quote `'` if they start with dangerous characters. This forces the spreadsheet to treat the cell as text.
