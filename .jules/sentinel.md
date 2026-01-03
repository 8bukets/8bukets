## 2024-05-23 - [Missing Timeouts in Scrapers]
**Vulnerability:** The scraper lacked a `timeout` parameter in HTTP requests, which could lead to indefinite hanging if the target server stops responding without closing the connection.
**Learning:** Autonomous agents that rely on external data sources must have strict timeouts to prevent resource exhaustion and process deadlocks.
**Prevention:** Always enforce a global or request-level `timeout` in `requests.get()` or similar network calls.
