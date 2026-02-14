## 2024-05-23 - Prevent CSV Formula Injection
**Vulnerability:** User-controlled content (e.g. blog post titles, authors) starting with `=`, `+`, `-`, or `@` can be interpreted as formulas by spreadsheet software (Excel, LibreOffice) when opened as CSV. This allows arbitrary code execution or data exfiltration on the victim's machine.
**Learning:** CSV is not just a text format; it is an input format for complex spreadsheet applications. Any field that can be controlled by an external source must be sanitized.
**Prevention:** Prepend a single quote `'` to any field starting with the trigger characters `=`, `+`, `-`, or `@` to force the application to treat the field as a string literal.
