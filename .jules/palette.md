## 2025-12-25 - CLI Progress Indication
**Learning:** CLI tools often lack feedback, making them feel unresponsive. Simple ANSI updates significantly improve perceived performance.
**Action:** Always verify `sys.stdout.isatty()` before using ANSI escape codes to ensure logs remain clean in non-interactive environments.
