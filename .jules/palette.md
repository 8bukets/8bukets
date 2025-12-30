## 2024-05-23 - [CLI Emoji Alignment]
**Learning:** Standard string length calculations in Python do not account for the visual width of emojis (often 2 columns), which causes misalignment in CLI borders unless explicitly corrected.
**Action:** When using emojis in CLI tables, manually adjust padding by subtracting 1 for each "wide" emoji (len 1, visual width 2) to ensure perfect alignment.
