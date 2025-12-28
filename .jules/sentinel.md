## 2024-05-23 - Path Traversal & CSV Injection Mitigation
**Vulnerability:** The scraper accepted arbitrary file paths via CLI arguments, allowing writing to any location the user had permission for (Path Traversal). It also wrote user-controlled data directly to CSV without sanitization (CSV Injection).
**Learning:** Security features described in "memory" or documentation may not exist in the actual codebase (e.g., `validate_path` and `sanitize_for_csv` were missing despite being "remembered"). Always verify code against security claims.
**Prevention:** Implemented strict path validation enforcing output to the current working directory and CSV sanitization for formula triggers (`=`, `+`, `-`, `@`).
