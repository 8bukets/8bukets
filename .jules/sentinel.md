## 2026-02-01 - CSV Injection Vulnerability in Scraper

**Vulnerability:** The scraper was writing user-controlled data (titles, authors, etc.) directly to a CSV file without sanitization. If a field started with `=`, `+`, `-`, or `@`, it could be interpreted as a formula by spreadsheet software (Excel, LibreOffice), potentially leading to arbitrary code execution on the analyst's machine.

**Learning:** We often trust data scraped from "reputable" sites like WordPress blogs, but compromised sites or malicious user comments (if scraped) can introduce payloads. Scrapers must treat all external data as untrusted.

**Prevention:** Always sanitize data before writing to CSV. Prepending a single quote `'` to fields starting with special formula characters forces the spreadsheet to treat the cell as text.
