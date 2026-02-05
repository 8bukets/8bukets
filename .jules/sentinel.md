## 2026-02-05 - Hardcoded Secrets in Generated Code
**Vulnerability:** The `DeveloperAgent` was generating code snippets that included hardcoded database credentials (`hr/welcome`). While these were example credentials, presenting them directly encourages insecure coding practices (CWE-798).
**Learning:** Even "educational" or "example" code must adhere to security best practices, as users often copy-paste snippets directly into production.
**Prevention:** Always use environment variables or configuration placeholders in code examples. Specifically, replaced direct strings with `os.environ.get()`.
