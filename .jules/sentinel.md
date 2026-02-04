## 2026-02-04 - CSV Injection in Scraper
**Vulnerability:** The scraper exported unsanitized user-controlled data directly to CSV, allowing for Formula Injection (CSV Injection).
**Learning:** Standard CSV writers do not automatically sanitize fields against spreadsheet formula execution. Any input starting with `=`, `+`, `-`, or `@` is risky.
**Prevention:** Always sanitize CSV outputs by prepending a single quote `'` to fields starting with dangerous characters.
