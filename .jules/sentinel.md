## 2026-01-27 - CSV Injection and Path Traversal in Scraper
**Vulnerability:** The scraper accepted unsanitized input for CSV generation and unvalidated file paths for output.
**Learning:** Python's `csv` module does not automatically sanitize formula injection characters (`=`, `+`, `-`, `@`). CLI tools accepting paths must validate them against the CWD.
**Prevention:** Implement input sanitization for CSV fields and strict path validation using `os.path.abspath` and `os.path.commonpath`.
## 2026-02-05 - Prevented CSV Injection
**Vulnerability:** Unsanitized scraped data (title, author, etc.) starting with `=`, `+`, `-`, or `@` could be executed as formulas when the CSV output is opened in Excel.
**Learning:** Even when scraping data from "trusted" platforms, the content can contain malicious payloads intended for downstream tools like spreadsheets.
**Prevention:** Always sanitize data before writing to CSV by prepending a single quote `'` to fields starting with risky characters.
