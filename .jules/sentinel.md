## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-07 - Markdown Injection and Stored XSS in Reports
**Vulnerability:** The analytics report generator (`analytics.py`) included scraped data (domain, author, category) directly into a Markdown file without sanitization.
**Learning:** Untrusted input can break the report structure (e.g., by injecting `|` into tables) or introduce Stored XSS vulnerabilities (e.g., `<script>` tags) if the Markdown is rendered as HTML by a vulnerable viewer.
**Prevention:** Implement output encoding for Markdown generation. I added a `clean_markdown_cell` function that escapes HTML characters (`html.escape`) and the Markdown table separator (`|`).
