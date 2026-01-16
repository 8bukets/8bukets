# Palette's Journal

## 2026-01-16 - CLI Interaction Feedback
**Learning:** CLI tools often lack visual feedback for long-running processes (agents), leading to user uncertainty.
**Action:** Implement a `Spinner` context manager that shows a "processing" animation in TTY environments and graceful logging fallback in non-TTY environments.
