## 2026-01-25 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (news titles) was written directly to a CSV file without sanitization. If a title started with characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software (Excel, Google Sheets), potentially leading to command execution or data exfiltration.
**Learning:** Even data from seemingly trusted sources (like a specific corporate news site) should be treated as untrusted when crossing trust boundaries, especially when the output format (CSV) has known injection risks.
**Prevention:** Always sanitize or escape fields starting with dangerous characters (`=`, `+`, `-`, `@`) when exporting to CSV by prepending a single quote `'`.
