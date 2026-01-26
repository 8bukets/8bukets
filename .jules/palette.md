## 2026-01-26 - [CLI Logging UX]
**Learning:** In Python logging, libraries/agents often add their own handlers which conflict with the main application's configuration, causing double logging and inconsistent formatting. Centralizing logging configuration and checking `logging.getLogger().handlers` before adding new handlers solves this.
**Action:** Always implement a centralized `configure_logging` utility and use `sys.stdout.isatty()` to conditionally apply colors for better CLI readability.
