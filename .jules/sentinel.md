## 2024-05-23 - CSV Injection Vulnerability
**Vulnerability:** CSV Formula Injection (also known as CSV Injection)
**Learning:** Writing user-controlled data (like post titles or categories) directly into a CSV file without sanitization allows malicious payloads (starting with =, +, -, @) to be executed by spreadsheet software (like Excel) when the file is opened.
**Prevention:** Always sanitize fields before writing to CSV. Prepend a single quote (') to any field starting with the trigger characters (=, +, -, @) to force the spreadsheet application to treat it as a string.
