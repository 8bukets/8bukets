## 2025-05-22 - Debouncing Search Input
**Learning:** In vanilla JavaScript applications, binding `input` event listeners directly to complex DOM manipulation (like filtering a list) causes significant reflow/repaint overhead on every keystroke.
**Action:** Always wrap high-frequency event listeners (input, scroll, resize) with a debounce or throttle function to limit execution rate.
