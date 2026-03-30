## 2024-03-24 - [CSV Injection Vulnerability in Scraper]
**Vulnerability:** The scraper was writing unsanitized content directly to CSV files, allowing CSV injection (Formula Injection) if the scraped content contained fields starting with =, +, -, or @.
**Learning:** External data, even when scraped from "trusted" sites, can contain malicious payloads designed to exploit data viewers. CSVs are particularly vulnerable because spreadsheet software interprets cells starting with these characters as formulas.
**Prevention:** Always sanitize data before writing to CSV. Prepend a single quote (') to any field starting with dangerous characters to force it to be treated as a string.
