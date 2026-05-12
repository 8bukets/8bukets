## 2026-02-05 - Prevented CSV Injection
**Vulnerability:** Unsanitized scraped data (title, author, etc.) starting with `=`, `+`, `-`, or `@` could be executed as formulas when the CSV output is opened in Excel.
**Learning:** Even when scraping data from "trusted" platforms, the content can contain malicious payloads intended for downstream tools like spreadsheets.
**Prevention:** Always sanitize data before writing to CSV by prepending a single quote `'` to fields starting with risky characters.
