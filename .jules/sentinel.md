## 2026-02-04 - Unsanitized Markdown Report Generation
**Vulnerability:** Scraped data containing HTML tags (e.g., `<script>`) and Markdown table delimiters (`|`) was injected directly into Markdown reports. This allowed for potential XSS (if rendered) and broke report layout integrity.
**Learning:** Report generation scripts often trust database content. In this project, `report_generator.py` assumed content was safe for Markdown tables.
**Prevention:** Implement and enforce a `sanitize_markdown` utility for any data inserted into Markdown tables or formatted text, specifically escaping `<`, `>`, `|` and handling newlines.
