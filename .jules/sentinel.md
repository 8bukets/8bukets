## 2026-02-04 - Markdown Injection in Analytics Reports
**Vulnerability:** Unsanitized scraped data (categories, domains) was inserted directly into Markdown tables in `analytics.py`. This allowed malicious content (e.g., pipes `|` or HTML tags) to break table structure or introduce XSS vulnerabilities if the report was rendered in a browser.
**Learning:** Input sanitization (like `sanitize_for_csv` in the scraper) is often insufficient for all downstream consumers. Context-aware output encoding (escaping pipes for Markdown, HTML entities for XSS) is required at the point of report generation.
**Prevention:** Implement output-specific sanitization functions (e.g., `sanitize_markdown`) and wrap all dynamic data fields when generating formatted reports.
