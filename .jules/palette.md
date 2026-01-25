## 2026-01-25 - CLI Delight
**Learning:** Adding ANSI colors and a summary box to a CLI tool significantly improves perceived performance and user satisfaction, even without functional changes.
**Action:** Always wrap ANSI codes in `sys.stdout.isatty()` checks to ensure logs remain clean when redirected.
