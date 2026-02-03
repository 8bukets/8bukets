## 2025-10-26 - [Synchronous DOM Updates in Search]
**Learning:** The search functionality was triggering synchronous DOM layout thrashing on every keystroke, which is a scalability bottleneck for list filtering.
**Action:** Implement `debounce` pattern for all future user input event listeners that trigger DOM updates or expensive calculations.
