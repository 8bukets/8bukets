## 2026-01-30 - Markdown Injection in Analytics Report
**Vulnerability:** User-controlled data (domains, categories, authors) was being written directly into a Markdown table in `analytics.py` without sanitization.
**Learning:** Even internal reporting tools can be vulnerable to injection attacks if they process untrusted data. Table injection breaks report integrity, and HTML injection poses XSS risks.
**Prevention:** Always sanitize data before writing to structured formats like Markdown or CSV. Use helper functions like `sanitize_markdown`.
