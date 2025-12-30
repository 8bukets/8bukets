# Palette's Journal

## 2025-01-28 - Initial Setup
**Learning:** This is a CLI-based project (Python scraper/analytics). UX improvements here mean improving the CLI output experience (colors, emojis, formatting).
**Action:** Focus on CLI output enhancements using ANSI codes or emojis to improve readability and "delight".

## 2025-01-28 - CLI Output Ordering
**Learning:** When using `logging` (which prints to stderr by default or if configured) mixed with `print` (stdout), the order of output can be surprising if not flushed or if they go to different streams. In my run, the summary box appeared *before* the logs because I used `print` (stdout) and `logging` (stderr) without strict ordering, or because `logging` might be buffered differently? Actually, looking at the output `python3 scraper.py --limit 1`, the summary appeared *first* in the console output provided by the tool, but in the `output.txt` redirection, only the summary was captured (because logs go to stderr by default).
**Action:** To ensure the summary appears *after* the logs, I should ensure logging is flushed or configured to use stdout if I want them interleaved sequentially in the same stream, OR accept that they are different streams. For a CLI tool, users often pipe stdout. Sending the summary to stdout is correct for the "result", while logs are "status". However, visually, having the summary at the top (before logs finish) is weird if it's printed *after* code execution. Wait, why did it appear first in the `run_in_bash_session` output?
Ah, `run_in_bash_session` might capture stdout and stderr separately and combine them, or the latency differs.
Actually, I called `self.print_summary` *after* `self.save_data`. `save_data` logs.
If `logging` writes to stderr (default), and `print` to stdout.
The shell usually mixes them.
The fix to make it consistent for the user is to ensure `logging` uses `sys.stdout` if we want them perfectly ordered, or just accept it.
But for a "Summary", it logically belongs at the end.
I will configure logging to use stdout to fix the ordering visual glitch.
