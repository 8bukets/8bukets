## 2026-01-15 - Enhancing CLI Feedback
**Learning:** Python's `logging` module can be easily extended with a custom formatter to support ANSI colors, significantly improving the readability of CLI output without adding heavy dependencies like `rich` or `colorama`.
**Action:** Use `CustomFormatter` pattern for all future Python CLI tools to ensure consistent, accessible visual feedback (Green for success, Red for errors).
