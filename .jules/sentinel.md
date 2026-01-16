## 2024-05-23 - CSV Injection in Scraper Output
**Vulnerability:** Scraped data (e.g., post titles, authors) was written directly to CSV without sanitization. If the scraped site contained fields starting with `=, +, -, @`, Excel would execute them as formulas.
**Learning:** Even when scraping "safe" sites, the output format (CSV) can introduce vulnerabilities if the consuming application (Excel) interprets the data as executable.
**Prevention:** Sanitize all untrusted input before writing to CSV by prepending `'` to dangerous characters.

## 2026-01-16 - Markdown Injection / XSS in Analytics Report
**Vulnerability:** Data extracted from JSON (categories, authors) was directly embedded into Markdown tables without sanitization. Malicious input containing `|` could break table structure, and HTML tags like `<script>` could lead to XSS if the report was viewed in a browser.
**Learning:** Generating reports (Markdown, HTML, PDF) from external data is a sink for injection attacks. "Displaying" data is as dangerous as executing it if the viewer interprets the format.
**Prevention:** Escape special characters relevant to the output format (e.g., `|` for Markdown tables, `< >` for HTML) before embedding dynamic data.
