## 2024-05-23 - CSV Injection Prevention
**Vulnerability:** User-controlled input (title, author, etc.) was written directly to CSV without sanitization, allowing for Formula Injection (CSV Injection).
**Learning:** Even if data is just "text", when it's exported to formats like CSV that are often opened in rich clients (Excel), special characters can trigger code execution.
**Prevention:** Sanitize any field starting with `=`, `+`, `-`, or `@` by prepending a single quote `'` before writing to CSV.
