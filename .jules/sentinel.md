## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-24 - Path Traversal in File Output
**Vulnerability:** `scraper.py` accepted arbitrary output file paths (e.g., `../file.json`), allowing potential overwriting of sensitive system files.
**Learning:** CLI tools often trust user input for file paths implicitly. `argparse` does not validate paths, and `open()` follows traversal characters.
**Prevention:** Always resolve paths to absolute paths and verify they are contained within the intended root directory (e.g., using `os.path.commonpath`) before opening files.
