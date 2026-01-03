## 2026-01-03 - CLI Visual Polish
**Learning:** ANSI color codes and emojis significantly improve the scanability of long-running CLI process logs (like scrapers) without adding heavy dependencies.
**Action:** Use self-contained `ColorFormatter` classes in CLI entry points to enhance UX without polluting the dependency tree.
