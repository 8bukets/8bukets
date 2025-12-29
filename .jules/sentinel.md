## 2024-02-14 - [Indefinite HTTP Request Hanging]
**Vulnerability:** The scraper used `requests.Session().get()` without a `timeout` argument.
**Learning:** Python's `requests` library does not apply a default timeout, meaning a connection to a non-responsive server can hang indefinitely, causing a Denial of Service (DoS) for the scraper agent.
**Prevention:** Always enforce a `timeout` (e.g., `timeout=10`) on all external HTTP calls.
