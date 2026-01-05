## 2024-05-23 - [DoS Risk Mitigation in Scraper]
**Vulnerability:** The scraper lacked a timeout configuration for HTTP requests, making it susceptible to indefinite hanging (Denial of Service) if the target server becomes unresponsive.
**Learning:** `requests.Session` does not apply a global timeout by default. Timeouts must be explicitly passed to request methods. Relying on default network socket timeouts is insufficient for robust applications.
**Prevention:** Always specify a `timeout` parameter in `requests` calls or configure a custom adapter that enforces timeouts (though `requests` adapters don't natively support global timeouts easily without subclassing).
