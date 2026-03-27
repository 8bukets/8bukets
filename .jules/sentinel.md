# Sentinel's Journal

## 2025-01-14 - CSV Injection in Scraper

**Vulnerability:** The scraper was taking untrusted input (post titles, authors, etc.) and writing them directly to a CSV file. If these fields contained characters like `=`, `@`, `+`, or `-`, they could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), potentially leading to command execution on the victim's machine.

**Learning:** Even "read-only" data collection tools can introduce security risks if the output format (CSV) has inherent vulnerabilities when opened by specific applications. We often sanitize for HTML/JS (XSS) but forget about CSV Injection.

**Prevention:** Always sanitize data before writing to CSV. A simple fix is to prepend a single quote `'` to any field starting with dangerous characters, which forces the spreadsheet software to treat the cell as text.
