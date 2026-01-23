## 2026-01-23 - CLI Progress Indicators
**Learning:** Users running long-running CLI processes (like scrapers) feel more confident and less anxious when they see dynamic progress indicators (spinners, counts) rather than scrolling logs or static silence. Using `sys.stdout.write` with `\r` provides a cleaner experience than log spam.
**Action:** Always implement dynamic progress bars for batch operations in CLI tools, using simple ANSI codes if libraries like `tqdm` are not available.
