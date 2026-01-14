## 2026-01-14 - CSV Formula Injection
**Vulnerability:** User-controlled input starting with `=`, `+`, `-`, or `@` was written directly to CSV files without sanitization, allowing potential execution of malicious formulas in spreadsheet software.
**Learning:** Developers often forget that CSVs are not just text files but are often interpreted by active content engines like Excel. Simply escaping delimiters (like commas) is insufficient for security.
**Prevention:** Always sanitize fields starting with formula triggers by prepending a single quote `'` or space when exporting to CSV, or use a format like JSON/Parquet that doesn't support active content execution.
