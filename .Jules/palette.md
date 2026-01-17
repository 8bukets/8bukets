## 2024-05-24 - [CLI Visual Polish]
**Learning:** Python CLI tools often lack visual hierarchy. Standard logging is monotone. Adding ANSI colors and emojis significantly improves scannability for status updates (Green/Info), warnings (Yellow), and errors (Red).
**Action:** Use a custom `logging.Formatter` with ANSI codes in future Python CLI projects to enhance UX without adding heavy dependencies like `rich`.
