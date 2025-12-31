## 2024-01-01 - [Initial Setup]
**Learning:** This repo lacks a standard `package.json` but uses `pnpm` in spirit (as per user directive) and Python for backend agents. Performance verification must rely on Python `playwright` or manual verification scripts.
**Action:** When creating tests, rely on `playwright` (Python) to interact with the frontend since no Node test runner is configured.
