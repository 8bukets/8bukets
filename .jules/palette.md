## 2025-12-28 - CLI Output Polish
**Learning:** CLI polish: Checking `sys.stdout.isatty()` is crucial to prevent escape codes from polluting log files in non-interactive environments.
**Action:** Always wrap ANSI escape codes in a conditional that checks if the output is a TTY.
