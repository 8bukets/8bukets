## 2024-05-23 - [CLI Experience Improvement]
**Learning:** Even for backend scripts, providing visual feedback (colors) and safety mechanisms (graceful exit on Ctrl+C) significantly reduces user anxiety and data loss frustration.
**Action:** When building CLIs, always implement `KeyboardInterrupt` handling to save state, and use basic ANSI colors to differentiate success/error states without adding heavy dependencies.
