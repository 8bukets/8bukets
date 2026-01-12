## 2024-03-24 - CSV Formula Injection
**Vulnerability:** User-controlled input (e.g., article titles) starting with `=`, `+`, `-`, or `@` was written directly to CSV files, enabling potential Formula Injection (CSV Injection) attacks if opened in Excel.
**Learning:** Even "read-only" formats like CSV can carry payload risks when interpreted by specific client-side applications like Excel. Data sanitization must happen at the boundary (writing to file), not just at input (reading from web).
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` to any value starting with `=`, `+`, `-`, or `@`.
