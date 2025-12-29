## 2025-12-29 - [CLI Output Ordering]
**Learning:** `logging` in Python defaults to `stderr` while `print` goes to `stdout`. To ensure chronological ordering in CLI tools, logging must be explicitly configured with `stream=sys.stdout` and existing handlers cleared if imported modules have already configured logging.
**Action:** Always check imported modules for `logging.basicConfig` and reset handlers in the main entry point if strict output ordering is required.

## 2025-12-29 - [Emoji Visual Width]
**Learning:** Emojis often consume 2 visual columns but have a string length of 1. Standard padding calculations will result in misaligned borders.
**Action:** Explicitly account for emoji width (usually +1 char) or use a library that handles visual width when building TUI tables.
