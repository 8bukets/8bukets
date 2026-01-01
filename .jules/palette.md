## 2024-05-23 - CLI Emoji Alignment
**Learning:** Standard string length calculations in Python do not account for the visual width of emojis (often 2 columns), which causes misalignment in CLI borders unless explicitly corrected.
**Action:** In future CLI improvements, use a library like `wcwidth` or manually adjust padding for known emojis to ensure perfect box alignment. For now, we accept slight misalignment or manually pad.
