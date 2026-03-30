## 2026-01-29 - Missing Session Reuse in Scraper
**Learning:** The scraper was establishing a new TCP/SSL connection for every single page request, adding significant latency (approx 26% overhead locally).
**Action:** Always check `scraper.py` or loop-heavy network code for `requests.Session()` reuse.
