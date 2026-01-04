## 2024-02-14 - Missing Request Timeouts
**Vulnerability:** The scraper used `requests.get` without a timeout parameter. This could cause the application to hang indefinitely if the target server is unresponsive or drops packets, leading to a Denial of Service.
**Learning:** Python's `requests` library does not set a timeout by default. Always explicitly set timeouts for network operations.
**Prevention:** Enforce timeouts on all network calls. Use `session.request(..., timeout=X)` or set it globally if possible (though `requests` requires per-call timeout).
