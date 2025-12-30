## 2025-02-18 - CLI Output Ordering with Logging
**Learning:** Mixing `logging` (which often defaults to stderr) and `print` (stdout) in CLI tools creates disordered output where logs appear out of sync with styled text. This degrades the user experience by making the sequence of events confusing.
**Action:** When enhancing CLI tools with visual elements (print), always explicitly configure `logging` to use `stream=sys.stdout` to ensure strictly chronological output.
