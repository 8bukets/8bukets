## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-02-05 - Markdown Injection in Analytics Report
**Vulnerability:** User-controlled data (e.g., author names, categories) was inserted directly into Markdown tables. Malicious input containing `|` could break table structure, and HTML tags could lead to Stored XSS if the report is rendered in a browser.
**Learning:** Markdown generation is not just text concatenation; it requires context-aware escaping (HTML entity encoding + escaping Markdown delimiters like `|` and `\`).
**Prevention:** Use a dedicated `escape_markdown` function that handles both HTML and Markdown special characters before inserting data into reports.
## 2024-05-24 - Path Traversal in File Output
**Vulnerability:** `scraper.py` accepted arbitrary output file paths (e.g., `../file.json`), allowing potential overwriting of sensitive system files.
**Learning:** CLI tools often trust user input for file paths implicitly. `argparse` does not validate paths, and `open()` follows traversal characters.
**Prevention:** Always resolve paths to absolute paths and verify they are contained within the intended root directory (e.g., using `os.path.commonpath`) before opening files.
## 2026-02-06 - Markdown/HTML Injection in Analytics Report
**Vulnerability:** User-controlled data (categories, author names) was directly embedded into Markdown tables in `REPORT.md`, allowing HTML injection (XSS in viewers) and table structure manipulation (via pipe characters).
**Learning:** Markdown generation is susceptible to injection attacks similar to HTML/SQL. Pipe characters in data can break table layouts, and HTML tags are often rendered by Markdown viewers.
**Prevention:** Implemented `escape_markdown()` helper to sanitize inputs by escaping HTML entities and pipe characters before generating the report.
