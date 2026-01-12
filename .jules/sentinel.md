## 2025-02-18 - [Fix CSV Injection Vulnerability]
**Vulnerability:** User-controlled input (like article titles or authors) starting with `=`, `+`, `-`, or `@` was written directly to CSV files, enabling potential Formula Injection (CSV Injection) attacks if opened in spreadsheet software.
**Learning:** Even simple data export features like CSV generation require strict input sanitization, as they can be vectors for client-side attacks against administrators or data analysts.
**Prevention:** Always sanitize data before writing to CSV. A common practice is to prepend a single quote `'` to fields starting with dangerous characters to force them to be treated as strings.
