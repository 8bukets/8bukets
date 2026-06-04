## 2026-01-27 - Path Traversal in CLI Output Arguments
**Vulnerability:** CLI tools (`scraper.py`) accepted output file paths directly from arguments without validation, allowing arbitrary file writes via path traversal (e.g., `../file.json`).
**Learning:** Python's `open()` does not sandbox file access; CLI tools accepting paths must explicitly validate them against a root directory.
**Prevention:** Use `os.path.abspath` and `os.path.commonpath` to enforce that resolved paths remain within the intended working directory.
# Sentinel Journal

This journal tracks critical security learnings and vulnerability fixes.

## 2024-10-27 - [Hardcoded Credentials in Developer Agent]
**Vulnerability:** The `DeveloperAgent` was generating Python code snippets with hardcoded database credentials (`password="welcome"`).
**Learning:** Hardcoded credentials in example code are often copy-pasted into production by developers, leading to security breaches.
**Prevention:** All generated code examples must use environment variables or secret management systems for credentials. Modified `DeveloperAgent` to use `os.environ.get`.
