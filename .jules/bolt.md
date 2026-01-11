## 2026-01-11 - [Subprocess to Direct Import Optimization]
**Learning:** Replaced `subprocess` calls with direct python imports in `agents/researcher.py`. This eliminated overhead from spawning new Python processes and disk I/O (writing/reading intermediate JSON files), resulting in a ~26% performance improvement (from ~13.3s to ~9.7s).
**Action:** When integrating internal Python scripts, always prefer refactoring them into importable modules over executing them via `subprocess`.
