## 2024-02-14 - CSV Injection in Scraper Output
**Vulnerability:** User-controlled data (titles, authors, categories) was being written directly to CSV files without sanitization. If a malicious user created a post with a title starting with `=`, `+`, `-`, or `@`, it could execute as a formula in Excel/Sheets when an admin opened the CSV.
**Learning:** Even "read-only" data from scraping can be a vector for attacks if it's consumed by other tools (like Excel) that interpret specific characters as commands.
**Prevention:** Implemented `sanitize_for_csv` method that prepends a single quote `'` to any field starting with dangerous characters, forcing Excel to treat it as plain text. Applied this to all fields in the CSV output.
