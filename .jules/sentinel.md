## 2025-12-29 - Markdown Table Injection & XSS
**Vulnerability:** Unsanitized user inputs (e.g. scraped website titles/categories) injected into Markdown tables can break table layout using `|` or introduce XSS via HTML tags if the renderer supports it.
**Learning:** Markdown generation is not just string concatenation; it requires escaping of special characters just like HTML or SQL generation.
**Prevention:** Always escape `|` to `\|` and html-escape content when generating Markdown tables from dynamic data.
