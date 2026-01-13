## 2026-01-13 - [DoS Protection via Timeout]
**Vulnerability:** External network requests in `scrape_informatic.py` lacked a timeout configuration (`session.get(url)`), making the scraper susceptible to infinite hanging if the target server is unresponsive or malicious (DoS).
**Learning:** Even internal tools scraping public sites need explicit timeouts to ensure robust execution and prevent resource exhaustion, especially in automated/scheduled contexts.
**Prevention:** Enforce a strict `timeout` parameter (e.g., 30s) on all `requests` calls. Use a centralized constant `TIMEOUT_SECONDS` for maintainability.
