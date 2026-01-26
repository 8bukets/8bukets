## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2024-05-24 - Path Traversal in Scraper Output Args
**Vulnerability:** The scraper accepted output file paths from CLI arguments without validation, allowing users to write files outside the current working directory (Path Traversal).
**Learning:** CLI tools are often assumed to be run by trusted users, but they still need to protect against accidental or malicious misuse of file paths.
**Prevention:** Always validate file paths provided as input using `os.path.abspath` and `os.path.commonpath` to ensure they stay within intended boundaries.
