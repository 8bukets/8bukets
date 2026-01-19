## 2024-05-23 - [Preventing CSV Injection]
**Vulnerability:** Found CSV Injection (Formula Injection) vulnerability in `scraper.py`. User-controlled fields like title, date, author were written directly to CSV without sanitization.
**Learning:** Even if data is scraped from a "trusted" blog, it can contain malicious payloads. Any string starting with `=`, `+`, `-`, `@` can be interpreted as a formula by spreadsheet software.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with dangerous characters to force them to be treated as strings.
