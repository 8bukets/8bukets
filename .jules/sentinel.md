## 2025-05-23 - [CSV Formula Injection Vulnerability]
**Vulnerability:** User-controlled input (like titles, authors) is written directly to CSV without sanitization, allowing for formula injection (e.g., fields starting with `=`, `+`, `-`, `@`).
**Learning:** Even internal scraping tools can be vectors for client-side attacks if the output is consumed by vulnerable applications like Excel.
**Prevention:** Implement a sanitization layer that escapes dangerous characters (prepending `'`) before writing to CSV.