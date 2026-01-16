## 2026-01-16 - Markdown Injection in Analytics Reports
**Vulnerability:** Scraped data (category names, authors) was inserted directly into Markdown tables in `analytics.py` without sanitization, allowing pipe characters `|` to break table structure and potentially enabling HTML injection.
**Learning:** Even internal reporting tools parsing "passive" data (like scraped links) need output encoding if the output format (Markdown) has special characters that conflict with the data.
**Prevention:** Use a dedicated `escape_markdown` function for any dynamic data inserted into Markdown templates, specifically escaping pipes `|` and HTML tags `<` `>`.
