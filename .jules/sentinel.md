## 2024-05-24 - CSV Injection Prevention
**Vulnerability:** User-controlled input written directly to CSV files can lead to Formula Injection (CSV Injection) if it starts with characters like `=`, `+`, `-`, or `@`.
**Learning:** Even simple data export features can be a vector for attacks if the output format (CSV) is interpreted by other software (Excel, Google Sheets).
**Prevention:** Always sanitize data before writing to CSV by prepending a single quote `'` to risky fields.
