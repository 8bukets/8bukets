## 2024-05-23 - CSV Injection (Formula Injection)
**Vulnerability:** User-controlled input (title, author, categories) scraped from external websites was written directly to a CSV file. If these fields started with `=`, `+`, `-`, or `@`, they could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), potentially leading to command execution on the victim's machine.
**Learning:** Even "read-only" data scraping can introduce vulnerabilities if the output format (like CSV) has active content features. Trusting scraped content is dangerous.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` to any value starting with the dangerous characters.
