# Palette's Journal

## 2025-01-01 - CLI Output Ordering and Visualization
**Learning:** Python's `logging` module defaults to `sys.stderr`, while `print` uses `sys.stdout`. This causes interleaved output when using both in a CLI application. Configuring `logging` to use `sys.stdout` ensures correct chronological ordering.
**Action:** Always configure `logging.basicConfig(stream=sys.stdout)` for CLI tools where log messages and standard output are mixed.

## 2025-01-01 - Emoji Width in CLI Borders
**Learning:** Standard string length calculations in Python do not account for the visual width of emojis (often 2 columns), which causes misalignment in CLI borders unless explicitly corrected or carefully padded.
**Action:** Use a visual width library like `wcwidth` or manually adjust padding when emojis are involved in bordered text.
