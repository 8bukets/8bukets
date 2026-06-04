# BOLT'S JOURNAL

This journal documents critical performance learnings, patterns, and anti-patterns discovered while optimizing the codebase.

## Format
Each entry should follow this format:
`## YYYY-MM-DD - [Title]`
`**Learning:** [Insight]`
`**Action:** [How to apply next time]`

## 2024-05-22 - Debouncing Search Input
**Learning:** Attaching event listeners directly to the `input` event without debouncing causes synchronous DOM updates on every keystroke, leading to potential layout thrashing and UI lag.
**Action:** Always wrap high-frequency event listeners (input, scroll, resize) with a `debounce` or `throttle` function to batch updates and improve responsiveness.
