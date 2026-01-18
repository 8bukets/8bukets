## 2025-12-25 - [CLI Visual Polish]
**Learning:** Even in backend/CLI tools, adding visual hierarchy through colors and emojis significantly improves scannability. Users can instantly distinguish between phases (Scraping vs Analysis) and status (Success vs Error).
**Action:** When working on CLI tools in the future, always implement a basic `ColorFormatter` or use a library like `rich` or `click` if dependencies allow. For "no-dependency" requests, a simple ANSI wrapper is high-impact.
