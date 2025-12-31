# Sentinel Journal

This journal records critical security learnings and vulnerability patterns found in the codebase.

## 2025-02-18 - [CSV Formula Injection Risk]
**Vulnerability:** The `scraper.py` script writes user-controlled data (scraped titles) directly to a CSV file without sanitization. If a title starts with characters like `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software, potentially executing malicious commands (CSV Injection).
**Learning:** When generating CSV files from untrusted sources (like web scraping), always assume the content can contain malicious payloads targeting the *consumer* of the file (e.g., Excel), not just the server.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote (`'`) if the field starts with dangerous characters.
