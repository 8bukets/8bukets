## 2025-10-16 - CLI Table Alignment with Colors
**Learning:** Standard string length calculations fail when ANSI color codes are present, causing misaligned borders in CLI tables/boxes.
**Action:** Always strip ANSI escape codes using regex (e.g., `re.sub(r'\x1b\[[0-9;]*m', '', text)`) before calculating padding or column widths for visual elements.
