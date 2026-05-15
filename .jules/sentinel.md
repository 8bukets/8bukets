<<<<<<< sentinel-path-traversal-fix-11594538796228867279
## 2026-01-27 - Path Traversal in Scraper Outputs
**Vulnerability:** CLI scrapers (`scrape_informatic.py`, `google_search_scraper.py`) blindly trusted user-provided output paths, allowing writes to arbitrary locations (e.g., `/tmp/`, potentially system files).
**Learning:** Even internal CLI tools can be entry points for attacks if they run with elevated privileges or in shared environments. `os.path.abspath` alone resolves paths but doesn't validate boundaries.
**Prevention:** Enforce a sandbox by checking `os.path.commonpath([cwd, abs_path]) == cwd`. Centralize this validation in a `utils.py` module.
=======
## 2024-05-23 - Markdown Injection in Report Generation
**Vulnerability:** The `MonetizationAgent` included raw blog post titles in the generated Markdown report. Scraped titles containing Markdown syntax (e.g., links, images) were rendered, creating a risk of phishing or XSS in vulnerable viewers.
**Learning:** External inputs must be sanitized before inclusion in rich text formats like Markdown. Trusting scraped content to be plain text is risky.
**Prevention:** Use context-aware escaping functions (e.g., `sanitize_markdown`) when embedding untrusted data into structured documents. Treat all external data as potentially malicious.
>>>>>>> jules-scrape-informatic-6598290821327070927
