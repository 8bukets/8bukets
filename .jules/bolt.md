## 2026-01-03 - [Robots.txt Caching]
**Learning:** Frequent calls to check `robots.txt` compliance (e.g., inside a crawler loop) can lead to excessive network requests if the `RobotFileParser` re-reads the file every time.
**Action:** Cache the `robots.txt` parsing result (e.g., using `urllib.robotparser`'s internal state or a custom cache) and only re-fetch if the domain changes or after a significant TTL. This is critical for high-performance crawlers.

## 2026-01-03 - [Evolutionary Architecture Initialization]
**Learning:** When building self-modifying systems (like agents reading/writing their own DNA/config), always implement robust initialization logic. If the configuration file is missing (e.g., fresh install), the system must fallback to a default state instead of crashing.
**Action:** Implement `initialize_default_state()` methods that are called when external config files are missing or corrupt.
