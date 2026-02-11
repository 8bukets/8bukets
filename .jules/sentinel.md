# Sentinel Journal

This journal tracks critical security learnings and vulnerability fixes.

## 2024-10-27 - [Hardcoded Credentials in Developer Agent]
**Vulnerability:** The `DeveloperAgent` was generating Python code snippets with hardcoded database credentials (`password="welcome"`).
**Learning:** Hardcoded credentials in example code are often copy-pasted into production by developers, leading to security breaches.
**Prevention:** All generated code examples must use environment variables or secret management systems for credentials. Modified `DeveloperAgent` to use `os.environ.get`.
