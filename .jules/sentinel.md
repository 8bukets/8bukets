## 2026-01-28 - CSV Formula Injection
**Vulnerability:** User-controlled data (scraped titles, etc.) was written directly to CSV without sanitization, allowing for formula injection (e.g., `=cmd|...`).
**Learning:** Even data scraped from public websites must be treated as untrusted. "Clean" text for display is not necessarily safe for all output formats (like CSV/Excel).
**Prevention:** Always sanitize fields starting with `=`, `+`, `-`, `@` by prepending a single quote `'` before writing to CSV.
