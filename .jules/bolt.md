## 2025-01-14 - Unoptimized Input Handlers
**Learning:** Found direct DOM manipulation and text content reading inside high-frequency `input` event listeners in `main.js`. This causes layout thrashing on every keystroke.
**Action:** Always check `main.js` and other vanilla JS files for un-debounced event listeners on inputs.
