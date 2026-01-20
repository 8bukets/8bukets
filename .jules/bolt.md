## 2024-10-24 - Data Persistence in Scrapers
**Learning:** Running `scraper.py` locally (even with `--limit`) overwrites the production dataset (`links.json`, `links.csv`) with partial data. This leads to massive data loss regressions if committed.
**Action:** Always run `git restore --source=HEAD --staged --worktree links.json links.csv unique_links.txt REPORT.md` before committing changes to the scraper.
