## 2025-05-15 - CSV Injection Prevention
**Vulnerability:** Unsanitized user input written to CSV files allows formula injection.
**Learning:** `csv.writer` does not automatically escape formula characters (`=`, `+`, `-`, `@`).
**Prevention:** Use `sanitize_for_csv` helper to prepend `'` to values starting with dangerous characters before writing to CSV.
