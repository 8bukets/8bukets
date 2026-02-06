## 2026-02-06 - Markdown Report Injection
**Vulnerability:** The analytics report generator (`analytics.py`) directly embedded user-controlled data (domain names, categories, authors) into Markdown tables without escaping. Malicious inputs containing `|` could break the table structure, and inputs with `<script>` could introduce XSS if rendered in a browser.
**Learning:** Generating structured text formats (Markdown, CSV, JSON) manually requires careful escaping of delimiters. Trusting `urlparse` to sanitize domains is insufficient as it preserves characters like `|`.
**Prevention:** Use a dedicated `escape_markdown` function for all dynamic content inserted into Markdown reports. Ensure tests cover malicious inputs with special characters (`|`, `<`, `>`, `[`, `]`).
