## 2024-05-22 - Graceful Shutdowns in CLI Tools
**Learning:** Users treating CLI tools like long-running processes (e.g., scrapers) expect data persistence even when they manually interrupt the process (Ctrl+C). "Good UX" for CLI means anticipating impatience or the need to stop early without punishing the user with data loss.
**Action:** When designing long-running tasks, always wrap the main loop in a `try...finally` block (or handle `KeyboardInterrupt`) to save partial progress before exiting.
