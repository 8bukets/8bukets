## 2024-02-14 - CSV Formula Injection
**Vulnerability:** User-controlled data (scraped content) was being written directly to CSV files without sanitization. This allowed attackers to craft malicious website titles or authors starting with `=`, `@`, `+`, or `-` that would execute as formulas when the CSV was opened in Excel (CSV Injection).
**Learning:** Even if the input comes from "public" websites, it must be treated as untrusted. CSVs are often opened in spreadsheet software that executes formulas by default.
**Prevention:** Always sanitize data written to CSVs by prepending a single quote `'` to fields starting with trigger characters. Use a dedicated method like `sanitize_for_csv` to handle this centrally.
