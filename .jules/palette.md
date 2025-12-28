## 2025-12-28 - CLI Output Stream Unification
**Learning:** Mixing `logging` (default stderr) and `print` (stdout) in CLI tools causes disordered output when subprocesses are involved or when output is buffered.
**Action:** Explicitly configure `logging.basicConfig(stream=sys.stdout)` for CLI tools to ensure chronological output consistency, especially when combined with visual elements like summary boxes.

## 2025-12-28 - ANSI Table Alignment
**Learning:** Visual alignment of CLI tables breaks when using ANSI colors because string length includes invisible codes.
**Action:** Always strip ANSI codes when calculating padding for table borders. Use a regex like `r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])'` to measure 'visible' length.
