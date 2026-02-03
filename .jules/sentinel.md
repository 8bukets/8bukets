## 2026-02-03 - CSV Injection in Scraper
**Vulnerability:** The scraper was writing untrusted data (post titles, authors, etc.) directly to a CSV file. If this data contained formulas (starting with `=`, `+`, `-`, `@`), it could execute malicious code when opened in spreadsheet software.
**Learning:** Even data scraped from a blog can be malicious or problematic if not properly sanitized before export. Client-side vulnerabilities like CSV injection are easily overlooked in backend/scraper scripts.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote `'` to fields starting with trigger characters.
