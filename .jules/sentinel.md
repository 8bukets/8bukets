# Sentinel Journal 🛡️

This journal records critical security learnings, vulnerability patterns, and prevention strategies identified during the security hardening process.

## Format
Each entry follows this structure:
```markdown
## YYYY-MM-DD - [Title]
**Vulnerability:** [What you found]
**Learning:** [Why it existed]
**Prevention:** [How to avoid next time]
```

## 2024-05-23 - CSV Injection (Formula Injection)
**Vulnerability:** The scraper was writing user-controlled input (article titles, links, authors) directly to a CSV file without sanitization. Malicious fields starting with `=`, `+`, `-`, or `@` could trigger formula execution in spreadsheet software (like Excel) when the CSV is opened.
**Learning:** Even structured text formats like CSV have injection risks when they are consumed by rich client applications. Trusting "plain text" formats without considering the consumer application's behavior is a common pitfall.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` to any field starting with dangerous characters (`=`, `+`, `-`, `@`). This forces the spreadsheet software to treat the cell content as a string.
