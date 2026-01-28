# Sentinel's Journal

## 2026-01-28 - CSV Formula Injection in Scraper
**Vulnerability:** User-controlled content (titles, authors, etc.) scraped from external sites was written directly to CSV files without sanitization. If a value started with `=`, `+`, `-`, or `@`, spreadsheet software could interpret it as a formula, leading to potential command execution or data exfiltration.
**Learning:** Even "read-only" data from external sources can be dangerous when processed by other applications (like Excel) that interpret special characters as instructions. Trusting scraped data implicitly is a common oversight.
**Prevention:** Always sanitize data before exporting to CSV. Specifically, prepend a single quote `'` to fields starting with formula triggers (`=`, `+`, `-`, `@`) to force them to be treated as string literals.
