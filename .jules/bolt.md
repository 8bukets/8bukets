## 2024-05-23 - [Debounce Search Input]
**Learning:** In vanilla JS applications manipulating the DOM directly, input event listeners on search fields can cause significant layout thrashing if not debounced, as every keystroke triggers a reflow.
**Action:** Always wrap input handlers that trigger DOM updates or expensive calculations in a debounce function (standard 300ms delay is usually sufficient).
