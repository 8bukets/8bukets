## 2026-01-29 - Navigation in Long Markdown Reports
**Learning:** For CLI tools that output Markdown reports, users treat them as "mini-websites". Without a Table of Contents and "Back to Top" links, long reports become hard to navigate. Explicit HTML anchors (`<a name="...">`) are necessary because auto-generated GitHub/Markdown anchors can be flaky with emojis or special characters.
**Action:** Always include a Table of Contents and deep links for any generated Markdown report exceeding one screen in length. Use explicit HTML anchors to ensure reliability.
