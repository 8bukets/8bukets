## 2025-02-18 - CSV Injection Vulnerability
**Vulnerability:** User-controlled input (or scraped content) starting with `=`, `@`, `+`, or `-` can be interpreted as formulas when CSV files are opened in spreadsheet software (Excel, LibreOffice). This can lead to arbitrary command execution or data exfiltration.
**Learning:** Even "read-only" formats like CSV can carry active content risks if the consuming application (spreadsheet viewer) interprets them. Sanitization must happen at the point of serialization.
**Prevention:** Always prepend a single quote (`'`) to fields starting with dangerous characters when exporting to CSV. This forces the spreadsheet software to treat the cell as text.
