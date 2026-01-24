## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-24 - Arbitrary File Write via Path Traversal
**Vulnerability:** `scraper.py` allowed outputting files to arbitrary locations via absolute paths or traversal sequences (`../`), enabling arbitrary file overwrite.
**Learning:** CLI tools accepting file paths must validate they are within expected boundaries, especially if they might be automated or exposed to user input.
**Prevention:** Validate output paths using `os.path.abspath` and `os.path.commonpath` to ensure they are contained within the current working directory.
