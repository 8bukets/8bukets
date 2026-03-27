## 2026-01-30 - [CSV Injection Vulnerability]
**Vulnerability:** Scraped data was written directly to CSV files without sanitization, allowing formula injection if fields started with `=`, `+`, `-`, or `@`.
**Learning:** External data sources must never be trusted, even if they seem benign like article titles. CSV viewers execute formulas by default.
**Prevention:** Sanitized all CSV output by prepending a single quote `'` to fields starting with dangerous characters.
