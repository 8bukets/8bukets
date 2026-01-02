## Sentinel Journal

This journal records critical security learnings and vulnerability patterns discovered in the codebase.

## 2025-01-02 - Path Traversal in File Output
**Vulnerability:** The scraper accepted an arbitrary output file path via CLI, allowing attackers to overwrite sensitive files (e.g., `../../etc/passwd`) via path traversal.
**Learning:** `os.path.abspath` is insufficient for validation as it doesn't resolve symbolic links. `os.path.realpath` is required to ensure the true canonical path is checked.
**Prevention:** Always validate file paths against a whitelist or a confined directory (using `os.path.commonpath`) after resolving them with `os.path.realpath`.
