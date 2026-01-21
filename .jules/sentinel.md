## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-21 - Markdown Injection in Reports
**Vulnerability:** `analytics.py` was taking text directly from `links.json` and inserting it into a Markdown report. If the source data contained characters like `|`, it could break the table structure, or `[link](javascript:...)` to introduce malicious links.
**Learning:** Markdown output generation must be treated like HTML generation when untrusted data is involved. Table structures are particularly fragile to unescaped pipes.
**Prevention:** Created `security_utils.py` with `sanitize_for_markdown` to escape special characters including pipes and backslashes.
