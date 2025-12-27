## 2025-12-27 - Markdown Injection Vulnerability
**Vulnerability:** Markdown table structure was vulnerable to injection via pipe characters in scraped data (Domain, Category).
**Learning:** Generating Markdown tables by string concatenation without escaping delimiters allows content to break layout or inject malicious rows.
**Prevention:** Always escape pipe characters (`|` -> `\|`) and sanitize HTML entities in user-controlled data before inserting into Markdown tables.
