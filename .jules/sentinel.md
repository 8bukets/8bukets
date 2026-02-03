## 2026-02-03 - CSV Injection Vulnerability
**Vulnerability:** Scraper output directly wrote user-controlled strings (like titles and links) to CSV without sanitization, allowing formula injection (e.g., `=cmd|'/C calc'!A0`).
**Learning:** Even simple data export formats like CSV can be vectors for code execution if opened in spreadsheet software. Input validation/sanitization is crucial at every boundary, including file output.
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote `'` to any field starting with `=`, `+`, `-`, or `@`, neutralizing the formula.
