## 2026-01-30 - Markdown Table Injection via Unsanitized Input
**Vulnerability:** User-controlled content (titles, old/new values) containing pipe characters `|` caused Markdown table layout breakage in generated reports. This is a form of integrity violation and potential injection.
**Learning:** Even simple text formats like Markdown have control characters that must be escaped when handling untrusted input. Ad-hoc string replacement (like replacing pipes with hyphens) was applied inconsistently.
**Prevention:** Implemented a centralized `sanitize_markdown` method to escape critical characters (`|`, `<`, `>`, `[`, `]`) and applied it consistently to all dynamic fields in the report generator.
