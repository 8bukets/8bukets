## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2025-01-31 - Markdown Injection in Analytics Report
**Vulnerability:** The analytics script injected untrusted data directly into Markdown tables and lists. Malicious input containing pipe characters (`|`) broke table structure, and HTML tags (`<script>`) posed a potential XSS risk if the report was rendered in a browser.
**Learning:** Text-based formats like Markdown have control characters that must be escaped when embedding untrusted data.
**Prevention:** Implement a `sanitize_markdown` function to escape `|`, `<`, and `>` and apply it to all dynamic fields in generated reports.
