# Sentinel Journal

This journal records critical security learnings, vulnerabilities, and prevention strategies.

## 2026-02-02 - CSV Injection in Scraper Output
**Vulnerability:** The scraper blindly trusted external content (titles, authors) when writing to CSV files. Strings starting with characters like `=`, `+`, `-`, or `@` could be interpreted as formulas by spreadsheet software (Excel, LibreOffice), potentially leading to arbitrary command execution (CSV Injection / Formula Injection).
**Learning:** Even "offline" file formats like CSV can be vectors for attacks if the data is meant to be opened by rich client applications. Input sanitization isn't just for SQL or HTML; it's for *any* destination format that has special characters.
**Prevention:** Always sanitize data written to CSV files by prepending a single quote (`'`) to any field starting with `=`, `+`, `-`, or `@`. This forces the spreadsheet to treat the content as a string literal.
