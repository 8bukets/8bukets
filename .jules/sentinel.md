## 2026-02-05 - CSV Injection (Formula Injection)
**Vulnerability:** Scraped data containing characters like `=`, `+`, `-`, or `@` was written directly to CSV files without sanitization, allowing malicious websites to inject spreadsheet formulas that could execute code or exfiltrate data when opened in Excel.
**Learning:** We often think of "sanitization" only in the context of XSS (HTML) or SQL Injection, but outputting to other formats like CSV requires format-specific sanitization. Trusting external input (titles, authors) to be safe for CSV is a mistake.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to any field starting with risky characters to force the spreadsheet software to treat it as text.
