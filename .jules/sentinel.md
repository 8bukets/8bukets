## 2024-05-22 - CSV Injection in Scraper
**Vulnerability:** User-controlled content (titles, authors) starting with `=`, `@`, `+`, or `-` was written directly to CSV files, allowing formula execution (CSV Injection) if opened in spreadsheet software.
**Learning:** `csv.writer` in Python does not automatically sanitize fields for Excel/spreadsheet formula injection. It only handles CSV format escaping (quotes/commas).
**Prevention:** Always sanitize untrusted input before writing to CSVs intended for human consumption by prepending a single quote `'` to fields starting with dangerous characters.
