## 2026-01-02 - CLI Color Synchronization
**Learning:** Mixing `print` (stdout) and `logging` (defaulting to stderr) leads to disjointed output where colored prints from agents appear out of sync with system logs.
**Action:** When building CLI tools with mixed output sources, explicitly configure `logging.StreamHandler(sys.stdout)` to ensure strict chronological ordering of all messages.
