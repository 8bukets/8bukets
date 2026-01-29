## 2026-01-29 - Markdown Table Injection in Analytics Report
**Vulnerability:** Unsanitized user input (domains, categories) was directly interpolated into Markdown table cells in `analytics.py`. Malicious inputs containing pipe characters (`|`) could break the table structure, and inputs with HTML tags could lead to stored XSS if the report is viewed in a vulnerable Markdown viewer.
**Learning:** Even internal reporting tools that process external data must sanitize their output. Text-based formats like Markdown are susceptible to injection attacks similar to SQL or HTML injection.
**Prevention:** Always escape control characters (like `|` in Markdown tables) and sanitize HTML when generating Markdown from untrusted sources. Use a dedicated `sanitize_markdown` utility.
