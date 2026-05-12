## 2025-02-18 - Path Traversal in Scraper Output
**Vulnerability:** The `scraper.py` script accepted file paths for output (`--json`, `--csv`, `--txt`) without validation, allowing a user to write files to arbitrary locations on the filesystem (Path Traversal).
**Learning:** Command-line tools that accept file paths are often overlooked for security compared to web apps, but they can be just as dangerous if used in automated pipelines or setuid contexts. Standard libraries like `argparse` do not sanitize paths by default.
**Prevention:** Always validate user-provided file paths using a strict allow-list or by ensuring they resolve within a specific safe directory using `os.path.abspath` and `os.path.commonpath`.
## 2026-02-06 - Markdown Report Injection
**Vulnerability:** The analytics report generator (`analytics.py`) directly embedded user-controlled data (domain names, categories, authors) into Markdown tables without escaping. Malicious inputs containing `|` could break the table structure, and inputs with `<script>` could introduce XSS if rendered in a browser.
**Learning:** Generating structured text formats (Markdown, CSV, JSON) manually requires careful escaping of delimiters. Trusting `urlparse` to sanitize domains is insufficient as it preserves characters like `|`.
**Prevention:** Use a dedicated `escape_markdown` function for all dynamic content inserted into Markdown reports. Ensure tests cover malicious inputs with special characters (`|`, `<`, `>`, `[`, `]`).
