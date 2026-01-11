## 2024-03-24 - CSV Injection (Formula Injection)
**Vulnerability:** User-controlled input (like article titles or authors) starting with `=`, `+`, `-`, or `@` was written directly to CSV files. When opened in Excel/LibreOffice, these fields could execute arbitrary formulas, potentially leading to data exfiltration or command execution on the victim's machine.
**Learning:** Even if data is "just text", the *consumption* context (e.g., spreadsheet software) can introduce vulnerabilities. Sanitization must consider how the data will be used, not just how it's stored.
**Prevention:** Always prepend a single quote `'` to CSV fields starting with formula trigger characters. This forces the spreadsheet software to treat the cell content as literal text.
