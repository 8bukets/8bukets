## 2024-05-22 - [CSV Formula Injection in Data Export]
**Vulnerability:** User-controlled input (e.g., post titles) starting with `=`, `+`, `-`, or `@` was written directly to CSV files. When opened in spreadsheet software like Excel, these could be executed as formulas, potentially leading to command execution (CSV Injection).
**Learning:** Data formats often considered "safe" or "text-only" (like CSV) can become executable in specific contexts (spreadsheet software). Validation/Sanitization must consider the *consumer* of the data.
**Prevention:** Sanitize all fields written to CSV by prepending a single quote `'` if they start with dangerous characters (`=`, `+`, `-`, `@`). This forces the spreadsheet to treat the cell as text.
