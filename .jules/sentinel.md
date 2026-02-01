## 2026-02-01 - Missing Timeout in External Scraper Requests
**Vulnerability:** `scrape_informatic.py` used `requests.get` without a `timeout` parameter, allowing a malicious or unresponsive server to hang the process indefinitely (DoS).
**Learning:** Default library behaviors (like `requests` having no timeout) can lead to availability risks if not explicitly configured.
**Prevention:** Always enforce timeouts on all external network requests.
