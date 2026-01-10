## 2025-10-26 - [CSV Injection in Scraper Output]
**Vulnerability:** The scraper writes untrusted data (post titles, authors, etc.) directly into a CSV file without sanitization. If these fields begin with `=`, `+`, `-`, or `@`, they could be interpreted as formulas by spreadsheet software, leading to arbitrary code execution on the user's machine.
**Learning:** Even when not handling user input on a server, data collected from external sources (scraping) and exported to formats like CSV for local consumption must be treated as untrusted and sanitized to protect the end-user.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` if the field starts with risky characters (`=`, `+`, `-`, `@`).
