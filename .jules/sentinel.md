## 2024-02-14 - Prevented CSV Injection in Scraper Data

**Vulnerability:**
The `MarkPositionScraperAsync` class in `scraper.py` was directly writing scraped data (Title, Author, etc.) to a CSV file without sanitization. If an attacker managed to inject a malicious string starting with `=`, `+`, `-`, or `@` into a blog post title or author name, it could execute arbitrary code or formulas when the CSV file is opened in a spreadsheet application (Excel, LibreOffice).

**Learning:**
Even when scraping "public" data, we must treat it as untrusted input. Autonomous agents that generate files for human consumption (like CSV reports) effectively bridge the gap between untrusted web content and the user's local environment. This is a subtle but critical attack vector for data-gathering agents.

**Prevention:**
Implemented a `sanitize_for_csv` method that prepends a single quote `'` to any field starting with dangerous characters (`=`, `+`, `-`, `@`). This forces the spreadsheet software to treat the cell content as a literal string rather than a formula. This pattern should be applied to all CSV generation logic in the system.
