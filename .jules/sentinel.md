## 2024-05-23 - CSV Injection in Scraper
**Vulnerability:** The scraper was writing scraped content (titles, authors, etc.) directly to a CSV file without sanitization. If a malicious website had a title starting with `=`, `+`, `-`, or `@`, opening the CSV in Excel could execute arbitrary code (CSV Injection/Formula Injection).
**Learning:** Even when processing "public" data, if the output format is CSV, we must consider how spreadsheet software interprets the data. Untrusted input should never be allowed to start with formula triggers.
**Prevention:** Sanitize all fields before writing to CSV. A common and effective mitigation is to prepend a single quote `'` to any field starting with `=`, `+`, `-`, or `@`. This forces the spreadsheet software to treat the cell content as text.
