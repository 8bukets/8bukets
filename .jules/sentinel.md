## 2025-05-18 - [Preventing CSV Formula Injection]
**Vulnerability:** User-controlled input (like article titles or authors) starting with `=`, `+`, `-`, or `@` was written directly to CSV files, allowing for potential CSV Injection (Formula Injection) attacks if opened in spreadsheet software.
**Learning:** Even simple data export formats like CSV require sanitization when they might be consumed by "smart" applications like Excel or LibreOffice Calc.
**Prevention:** Implement a sanitization layer that prepends a single quote `'` to any field starting with dangerous characters, forcing the application to treat it as a string literal.
