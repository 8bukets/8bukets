## 2026-01-27 - Path Traversal in Scraper Output
**Vulnerability:** The scraper accepted arbitrary file paths for output files (JSON, CSV, TXT), allowing an attacker to potentially overwrite sensitive files on the system by providing paths like `../../etc/passwd`.
**Learning:** CLI tools that accept file paths as arguments are often overlooked for path traversal vulnerabilities. Relying on `open()` without validation assumes the user is benevolent or the environment is sandboxed, which may not be true.
**Prevention:** Implement a strict validation layer using `os.path.abspath` and `os.path.commonpath` to ensure all file operations occur within a designated safe directory (e.g., the current working directory).
## 2026-02-04 - Fix CSV Injection in Scraper
**Vulnerability:** The scraper saved untrusted input (e.g. titles, authors) directly to CSV files. If these fields started with special characters like `=`, `@`, `+`, or `-`, they could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), potentially leading to code execution (CSV Injection).
**Learning:** Even when scraping "static" sites, data can be crafted to exploit client-side tools used to view the data. Trusting the source content to be "safe" for all output formats is a mistake.
**Prevention:** Always sanitize data before exporting to CSV. Specifically, prepend a single quote `'` to fields starting with formula triggers (`=`, `@`, `+`, `-`) to force them to be treated as text.
## 2026-02-06 - CSV Injection Vulnerability
**Vulnerability:** The scraper was exporting data to CSV without sanitizing fields. Malicious input starting with `=`, `+`, `-`, or `@` could be executed as formulas in Excel.
**Learning:** Always sanitize user-controlled input before writing to CSV files, especially if they might be opened in spreadsheet software.
**Prevention:** Prepend a single quote `'` to fields starting with dangerous characters.
