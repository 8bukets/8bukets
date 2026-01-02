## 2024-05-23 - CLI UX Enhancement
**Learning:** Users perceive CLI tools as more polished and trustworthy when status messages are color-coded and include emojis. However, it's critical to respect `isatty` and `FORCE_COLOR` to prevent garbled output in CI/CD pipelines or file redirects.
**Action:** Always wrap CLI colorization logic in a helper that checks `sys.stderr.isatty()` (for logs) or `sys.stdout.isatty()` (for print) and `os.environ.get('FORCE_COLOR')`.
