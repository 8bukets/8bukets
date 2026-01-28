
## 2026-01-28 - CSV Injection Prevention
**Vulnerability:** Unsanitized user input being written directly to CSV files allows for formula injection (CSV Injection).
**Learning:** Python's `csv` module does not automatically sanitize fields for Excel/spreadsheet formula injection. Trusting scraped data implicitly is dangerous.
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, or `@` by prepending a single quote before writing to CSV.
