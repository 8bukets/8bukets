## 2026-02-03 - Markdown Table & HTML Injection

**Vulnerability:** The `report_generator.py` script constructed Markdown tables by directly interpolating user-controlled strings (e.g., post titles, URLs) into the output. This allowed:
1.  **Table Injection:** Malicious inputs containing the pipe character `|` could break the Markdown table structure, rendering the report unreadable or injecting false columns.
2.  **HTML Injection/XSS:** HTML tags in inputs (e.g., `<script>`) were not escaped. Since many Markdown viewers render raw HTML, this posed a Cross-Site Scripting (XSS) risk.

**Learning:** "Internal" reports are often overlooked for security, but they frequently process untrusted data (like web-scraped titles). Markdown is a structured format that requires specific escaping rules, particularly for table delimiters (`|`) and HTML content.

**Prevention:**
1.  **Sanitize All Inputs:** Treat all data from external sources (DB, API, scraping) as untrusted.
2.  **Context-Specific Escaping:**
    *   For HTML content in Markdown: Use `html.escape()`.
    *   For Markdown tables: Replace `|` with `&#124;`.
3.  **Use Libraries:** Where possible, use established libraries for generating structured documents (like Markdown or CSV) rather than manual string concatenation.
