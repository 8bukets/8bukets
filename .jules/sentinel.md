## 2024-03-25 - Prevented CSV Injection
**Vulnerability:** User-controlled data (post titles, authors, etc.) was written directly to CSV files without sanitization. This allowed for CSV Injection (Formula Injection) if the scraped content started with characters like `=`, `+`, `-`, or `@`.
**Learning:** Scrapers often trust the source content too much. Even "read-only" data from a blog can be malicious if it contains payloads targeting the tools used to analyze that data (like Excel).
**Prevention:** Always sanitize data before exporting to CSV. In this case, we implemented a `sanitize_for_csv` method that prefixes risky characters with a single quote `'` to force them to be treated as text.
