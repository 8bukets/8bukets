## 2025-12-30 - Avoid Vertical Borders in Emoji-Rich CLI UIs
**Learning:** Standard Python string length calculations do not account for the visual width of emojis (often 2 columns), which causes misalignment in CLI borders if using vertical separators (like `║`).
**Action:** When designing CLI summary boxes that include emojis, use horizontal dividers only (like `==` or `--`) and avoid vertical side borders to ensure consistent layout across terminals.
