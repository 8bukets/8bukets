## 2026-01-29 - Prevent CSV Injection
**Vulnerability:** User-controlled input (titles, authors, etc.) was written directly to CSV without sanitization. This exposed a Formula Injection (CSV Injection) vulnerability, where malicious values starting with `=`, `+`, `-`, or `@` could execute code when opened in spreadsheet software.
**Learning:** CSV files are interpreted by spreadsheet applications which often support executable formulas. Treating CSV export as a simple text write operation overlooks this risk.
**Prevention:** Always sanitize data before writing to CSV. A common and effective mitigation is to prepend a single quote `'` to any field starting with dangerous characters (`=`, `+`, `-`, `@`), forcing the application to treat the value as a string.
