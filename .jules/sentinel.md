## 2024-05-23 - Prevent CSV Formula Injection
**Vulnerability:** User-controlled data (titles, authors) was written directly to CSV files without sanitization. If a field started with `=`, `+`, `-`, or `@`, spreadsheet software could execute it as a formula, leading to data exfiltration or code execution.
**Learning:** Standard CSV writers in Python (and other languages) do not automatically sanitize for formula injection; they only handle CSV formatting (escaping commas/quotes). Security sanitization must be applied explicitly.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to any field starting with dangerous characters (`=`, `+`, `-`, `@`) to force the spreadsheet to treat it as text.
