## 2025-12-31 - CLI Color Support
**Learning:** Checking `sys.stdout.isatty()` is crucial for CLI tools to prevent printing garbage ANSI codes into log files or pipes.
**Action:** Always wrap color codes in a condition or class that checks `isatty()` or `FORCE_COLOR` env var.
