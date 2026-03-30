## 2025-01-29 - Regex Compilation in Loops
**Learning:** Compiling regex patterns as class attributes significantly improves performance when the method is called frequently (e.g., in a loop).
**Action:** Always pre-compile regex patterns that are constant and used in methods called repeatedly.
