# Sentinel's Journal

This journal documents critical security learnings, vulnerability patterns, and architectural security gaps found in the codebase.

## Format
Each entry should follow this format:
```
## YYYY-MM-DD - [Title]
**Vulnerability:** [What you found]
**Learning:** [Why it existed]
**Prevention:** [How to avoid next time]
```

## 2025-02-18 - CSV Injection in Scraper Output
**Vulnerability:** User-controlled content (post titles, authors, etc.) was written directly to CSV files without sanitization. If fields started with special characters like `=`, `+`, `-`, or `@`, they could be interpreted as formulas by spreadsheet software (Excel, Sheets), leading to potential command execution on the victim's machine.
**Learning:** Trusting scraped data to be "safe" is risky. Even if the source seems benign, malicious actors can inject payloads into titles or comments that are then scraped and exported.
**Prevention:** Always sanitize data before exporting to CSV. A common technique is to prepend a single quote `'` to any field starting with dangerous characters (`=`, `+`, `-`, `@`) to force it to be treated as a string.
