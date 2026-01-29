## 2025-10-16 - [CSV Injection Vulnerability]
**Vulnerability:** The scraper saved user-controlled data directly to CSV without sanitization, allowing for formula injection (CWE-1236).
**Learning:** Always sanitize data before exporting to formats like CSV that may be opened in spreadsheet software which executes formulas.
**Prevention:** Implemented `sanitize_for_csv` to prepend a single quote to values starting with dangerous characters (`=`, `+`, `-`, `@`).
