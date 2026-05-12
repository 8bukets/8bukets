## 2026-01-27 - Stored XSS in Markdown Reports
**Vulnerability:** The report generator took untrusted data (post titles and URLs) from the database and wrote them directly into a Markdown file. This allowed malicious inputs to break table formatting (pipe injection) and create XSS vectors (unsafe javascript: links).
**Learning:** Generating Markdown from database content requires strict sanitization, similar to HTML. Just because it's a "text file" doesn't mean it's safe, especially if viewed in a rich renderer.
**Prevention:** Implemented `sanitize_markdown` to escape special characters (`|`, `[`, `]`) and `get_safe_url` to whitelist safe protocols (`http`, `https`).
## 2026-02-06 - [SSRF in Scraper]
**Vulnerability:** Unrestricted URL input in `scraper.py` allowed scraping of local services (SSRF) via CLI arguments.
**Learning:** `requests.get` will fetch any URL provided, including `localhost` or private IPs, and follows redirects by default. Validating only the scheme is insufficient for SSRF protection.
**Prevention:** Implement strict input validation using `urllib.parse` and `ipaddress` to check for schemes (http/https only) and reject private/loopback IP addresses. Note that complete protection against DNS rebinding requires lower-level network control or disabling redirects.
