## 2026-02-04 - Markdown Table Sanitization
**Learning:** Generated Markdown tables break when dynamic content contains pipe characters (`|`), destroying the visual layout and readability.
**Action:** Always sanitize untrusted input in Markdown generators by escaping pipes (`&#124;`) and HTML characters.
