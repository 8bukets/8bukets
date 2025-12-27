## 2025-12-27 - Markdown Injection in Analytics Report
**Vulnerability:** The analytics report generator inserted category names and domains directly into Markdown tables. If these fields contained a pipe character (`|`), it broke the table structure and potentially allowed for malicious content injection (though limited by Markdown renderer).
**Learning:** Text-based formats like Markdown have their own injection risks. Structural characters must be escaped when inserting untrusted data.
**Prevention:** Implemented `sanitize_markdown_cell` to escape pipes (`|` -> `\|`) in all table cells.
