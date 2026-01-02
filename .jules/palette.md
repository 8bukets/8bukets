## 2026-01-02 - CLI Summary Box Layout
**Learning:** Fixed-width ASCII art summary boxes are fragile when displaying dynamic data (like filenames).
**Action:** Always truncate or ellipsize dynamic strings to a known maximum length (e.g., 22 chars) to prevent the box borders from misaligning.
