## 2026-01-07 - [Stored XSS in Markdown Reports]
**Vulnerability:** The application was vulnerable to Stored Cross-Site Scripting (XSS). Both `agents/content_agent.py` and `analytics.py` generated Markdown reports by directly interpolating untrusted data (article titles, author names, categories) into the output. If the source data contained HTML tags (e.g., `<script>`), these would be preserved in the Markdown report and potentially executed when viewed in a browser-based Markdown viewer.
**Learning:** Even "text-based" formats like Markdown can be vectors for XSS if they are rendered to HTML and the rendering environment allows inline HTML (which is standard behavior for Markdown). Sanitization is required at the point of output generation. Additionally, simply cleaning input (like `clean_text` in `scraper.py`) is often insufficient if it doesn't handle all contexts; output encoding is the most robust defense.
**Prevention:**
1. Always assume scraped data is hostile.
2. Use context-aware output encoding. For Markdown/HTML output, use `html.escape()` to convert special characters like `<`, `>`, `&`, `'`, and `"` into their HTML entity equivalents.
3. Apply this sanitization to *all* user-controlled fields before string interpolation.
