## 2026-01-19 - CSV Injection (Formula Injection) Prevention
**Vulnerability:** The scraper was writing unsanitized input directly to CSV files. Maliciously crafted content (e.g., titles starting with `=`) could execute commands when the CSV is opened in spreadsheet software like Excel.
**Learning:** Data extracted from the web should always be treated as untrusted. Output encoding/sanitization must match the destination format's specific risks (in this case, CSV formula execution).
**Prevention:** Implemented `sanitize_for_csv` in `MarkPositionScraperAsync` to prepend a single quote `'` to fields starting with `=`, `+`, `-`, or `@`, neutralizing them as text.
