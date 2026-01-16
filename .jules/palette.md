# Palette's Journal

## 2025-10-26 - CLI UX Patterns
**Learning:** In CLI tools without a GUI, the "loading state" is effectively the stream of log messages. Users rely on distinct visual cues (colors, emojis) to distinguish phases of execution in a scrolling terminal.
**Action:** When improving CLI tools, introduce a standard `Style` class early to manage ANSI codes and ensure consistency across different script outputs. Always check `sys.stdout.isatty()` before applying colors to avoid polluting pipe outputs.
