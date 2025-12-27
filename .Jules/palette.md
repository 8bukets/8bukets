## 2025-12-27 - Standardizing CLI Visuals
**Learning:** This project heavily relies on CLI scripts but lacked visual hierarchy (e.g., colored logs, summary boxes), making it hard to distinguish critical info from noise.
**Action:** Implemented a reusable `ColorFormatter` and `Colors` utility in `utils/logging_utils.py`. Future CLI tools should import these to maintain a consistent "Summary Box" pattern at the end of execution.
