## 2024-05-22 - [CLI Output Formatting]
**Learning:** Standard string length calculations in Python (`len()`) do not account for the visual width of emojis (often 2 columns). This causes misalignment in CLI borders unless explicitly corrected by adding +1 for each emoji in the string length calculation.
**Action:** When calculating padding for CLI tables, always account for emoji visual width or use a library like `wcwidth` if dependencies are allowed. In zero-dependency scripts, manual adjustment (e.g., `len(s) + count_emojis`) is necessary.
