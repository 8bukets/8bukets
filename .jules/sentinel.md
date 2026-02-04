# Sentinel Journal

## 2026-02-04 - Unrestricted File Write in Scraper CLI
**Vulnerability:** The `scrape_informatic.py` CLI utility accepted an output file path (`-o`) without validation, allowing a user (or compromised agent) to overwrite arbitrary files on the system (Path Traversal/Arbitrary File Write).
**Learning:** CLI tools are often treated as "trusted" but when used as part of an automated chain (Agents), they become attack vectors. We assumed the user would provide a safe path.
**Prevention:** Always validate file paths provided by users or external configurations. Enforce strict boundaries (e.g., must be within CWD or a specific data directory) using `os.path.commonpath`. Fail fast if validation fails.
