## 2025-02-18 - [CSV Formula Injection Vulnerability]
**Vulnerability:** Scraper output directly wrote user-controlled strings (titles, authors) to CSV without sanitization. Fields starting with `=`, `+`, `-`, or `@` could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), allowing for command execution (CSV Injection).
**Learning:** Even "read-only" formats like CSV can store executable payloads if the consuming application interprets them as formulas. Simple `csv.writer` usage is not sufficient for security against active content.
**Prevention:** Explicitly sanitize any text field starting with formula triggers (`=`, `+`, `-`, `@`) by prepending a single quote `'` or similar escape character before writing to CSV.
