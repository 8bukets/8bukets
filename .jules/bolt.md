## 2025-05-23 - [Debouncing Search Input]
**Learning:** Even in simple static sites, operations that trigger layout thrashing (like searching on every keystroke) can be significant bottlenecks. Debouncing is a cheap and effective way to mitigate this.
**Action:** Always check `input` event listeners for expensive operations and apply debouncing or throttling.
