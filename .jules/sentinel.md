## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-24 - Path Traversal in CLI Arguments
**Vulnerability:** `scraper.py` and `analytics.py` accepted file paths as command-line arguments without validation. This allowed writing/reading files outside the intended directory using `../` (e.g., overwriting system files).
**Learning:** CLI tools that accept file paths are susceptible to Path Traversal just like web apps. Standard libraries (`argparse`) do not validate path safety by default.
**Prevention:** Always resolve paths using `os.path.abspath` and verify they are contained within the allowed directory using `os.path.commonpath`. Enforce this validation before any file operations.
