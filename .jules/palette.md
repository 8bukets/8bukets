## 2024-05-23 - [CLI Emoji Alignment]
**Learning:** Standard string length calculations in Python do not account for the visual width of emojis (often 2 columns), which causes misalignment in CLI borders unless explicitly corrected.
**Action:** When calculating padding for CLI tables, code must measure the 'visible' string length by stripping ANSI color codes and manually adjusting for known double-width emojis.
