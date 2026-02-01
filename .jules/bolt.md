## 2024-10-27 - SQLite Connection Reuse
**Learning:** Opening a new SQLite connection for every inserted row (inside a loop) causes significant overhead due to file locking and syscalls. In `scraper.py`, moving the connection to the class scope (`self.conn`) reduced insertion time by ~36% for 100 items.
**Action:** Always verify where database connections are opened and closed. For batch operations, open the connection once at the start and close it at the end.
