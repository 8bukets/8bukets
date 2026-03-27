## 2024-10-27 - CSV Injection in Scraper
**Vulnerability:** The scraper was writing untrusted input directly to a CSV file. Fields starting with `=`, `+`, `-`, or `@` could be interpreted as formulas by spreadsheet software (Excel), leading to potential command execution on the analyst's machine.
**Learning:** Even "read-only" scrapers can introduce vulnerabilities if they generate files consumed by other insecure tools. Sanitization must occur at the boundary where data leaves the system (output sanitization).
**Prevention:** Always sanitize data written to CSVs by prepending `'` to fields starting with dangerous characters.
