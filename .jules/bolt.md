## 2024-05-24 - [Debouncing Search Input]
**Learning:** High-frequency events like `input` or `scroll` can cause severe performance degradation (UI jank) if they trigger expensive operations (DOM manipulation, layout thrashing, or API calls) synchronously.
**Action:** Always debounce or throttle high-frequency event listeners. For search inputs, a 300ms debounce is a standard and effective value.
