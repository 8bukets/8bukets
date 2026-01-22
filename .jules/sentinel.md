## 2024-03-25 - CSV Injection Vulnerability Fix
**Vulnerability:** The scraper was writing untrusted input (titles, authors, etc.) directly to a CSV file. If this input started with `=`, `+`, `-`, or `@`, it could be executed as a formula in spreadsheet software like Excel, leading to client-side code execution.
**Learning:** Even if data is quoted in a CSV (e.g., `"=SUM(1,1)"`), Excel will still interpret it as a formula. The field content itself must be sanitized by prefixing it with a character like `'` that forces it to be treated as text.
**Prevention:** Always sanitize user-controlled input before writing to CSVs. Use a helper function `sanitize_for_csv` to prefix risky characters (`=`, `+`, `-`, `@`) with a single quote.
