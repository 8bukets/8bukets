## 2024-05-23 - [CSV Formula Injection (CSV Injection)]
**Vulnerability:** Scraped data written directly to CSV files can contain fields starting with `=`, `+`, `-`, or `@`. When these files are opened in spreadsheet software (like Excel), these fields are interpreted as formulas, potentially executing arbitrary commands or exfiltrating data.
**Learning:** Never trust data extracted from the web, even if it looks like plain text. Data serialization formats like CSV have hidden "features" that can be weaponized.
**Prevention:** Sanitize all fields before writing to CSV by prepending a single quote `'` if the value starts with a dangerous character. This forces the spreadsheet software to treat the cell as text.
