## 2024-10-26 - [Missing Timeouts in HTTP Requests]
**Vulnerability:** External HTTP requests using `requests.get()` without a `timeout` parameter can hang indefinitely if the server does not respond, leading to Denial of Service (DoS) or resource exhaustion.
**Learning:** Default behavior of libraries like `requests` often favors functionality (waiting forever) over security/availability. Explicit timeouts are mandatory for robust systems.
**Prevention:** Always enforce a `timeout` parameter (e.g., `timeout=10`) for all network operations.
