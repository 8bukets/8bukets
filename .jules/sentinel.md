## 2024-04-18 - CSV Injection Mitigation
**Vulnerability:** User-controlled data (e.g., post titles, authors) was written directly to CSV files without sanitization. Malicious inputs starting with `=`, `+`, `-`, or `@` could execute formulas (CSV Injection) when opened in spreadsheet software like Excel.
**Learning:** Even simple data export formats like CSV can be vectors for client-side attacks if untrusted input is treated as trusted. Sanitization must happen at the point of egress (writing to the file).
**Prevention:** Implemented a `sanitize_for_csv` method that prepends a single quote (`'`) to any field starting with dangerous characters (`=`, `+`, `-`, `@`), neutralizing potential formulas.
