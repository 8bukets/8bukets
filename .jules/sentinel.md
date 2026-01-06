## 2024-02-18 - Unbounded Resource Consumption in Async Scraper
**Vulnerability:** The `scraper.py` module used `aiohttp.ClientSession` without explicit timeouts and read unlimited response bodies into memory via `await response.text()`.
**Learning:** Default configurations in HTTP clients often lack safety limits. A malicious or misconfigured server could cause the scraper to hang indefinitely (socket exhaustion) or consume all available memory (OOM) by serving an infinite stream or extremely large file.
**Prevention:** Always enforce explicit timeouts (`aiohttp.ClientTimeout`) and response size limits (Content-Length check + body size check) when fetching external resources.
