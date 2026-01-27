## 2026-01-27 - CLI Path Traversal
**Vulnerability:** `scraper.py` and `analytics.py` allowed arbitrary file paths via CLI arguments, enabling path traversal (reading/writing files outside CWD).
**Learning:** CLI tools often trust user input for file paths implicitly. `os.path.commonpath` is a robust way to validate paths against a safe root (like CWD).
**Prevention:** Always validate file paths provided by users or external sources. Use a dedicated `validate_path` function that resolves absolute paths and checks containment.
