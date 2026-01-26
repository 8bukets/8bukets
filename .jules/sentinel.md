## 2026-01-21 - [Markdown Table Injection & Stored XSS]
**Vulnerability:** User-controlled data (e.g., categories, authors) was being inserted directly into Markdown tables in `analytics.py`. This allowed:
1.  **Table Injection:** Using pipes `|` to break the table structure and add extra columns.
2.  **Stored XSS:** Inserting raw HTML (e.g., `<script>`) which some Markdown renderers execute.

**Learning:** When generating Markdown programmatically, simply replacing strings is unsafe if the input contains Markdown syntax characters (like `|`, `*`, `_`, `[`, `]`) or HTML. Python's standard `html.escape` handles HTML but not Markdown-specific syntax like table delimiters.

**Prevention:**
1.  Use `html.escape()` for all untrusted input destined for Markdown.
2.  Explicitly escape Markdown meta-characters, especially `|` inside tables (replace with `\|`).
3.  Implemented `sanitize_markdown` helper function in `analytics.py` to handle this centrally.
