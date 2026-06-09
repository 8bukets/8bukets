from agents.base_agent import BaseAgent
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime

class AnalyzeAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analyze")

    def get_domain(self, url):
        if not url:
            return None
        try:
            return urlparse(url).netloc.replace('www.', '')
        except:
            return None

    async def run(self, context: dict):
        self.log("Starting analysis...")
        data = context.get("raw_data", [])

        if not data:
            self.log("No data to analyze.")
            return

        # 1. Domain Analysis
        domains = [self.get_domain(p.get('external_link')) for p in data if p.get('external_link')]
        domain_counts = Counter(domains).most_common(10)

        # 2. Category Analysis
        all_categories = []
        for p in data:
            cats = p.get('categories', [])
            if cats:
                all_categories.extend(cats)
        category_counts = Counter(all_categories).most_common(10)

        # 3. Date Analysis
        dates = []
        for p in data:
            dt_str = p.get('datetime')
            if dt_str:
                try:
                    dt = datetime.fromisoformat(dt_str)
                    dates.append(dt)
                except ValueError:
                    pass

        date_stats = {}
        if dates:
            dates.sort()
            date_stats["start"] = dates[0].strftime('%Y-%m-%d')
            date_stats["end"] = dates[-1].strftime('%Y-%m-%d')
            years = [d.year for d in dates]
            date_stats["year_counts"] = Counter(years).most_common()
        else:
            date_stats["start"] = "N/A"
            date_stats["end"] = "N/A"
            date_stats["year_counts"] = []

        # 4. Author Analysis
        authors = [p.get('author') for p in data if p.get('author')]
        author_counts = Counter(authors).most_common()

        # Store in context
        context["analysis"] = {
            "total_posts": len(data),
            "unique_domains_count": len(set(domains)),
            "top_domains": domain_counts,
            "top_categories": category_counts,
            "date_stats": date_stats,
            "top_authors": author_counts
        }

        self.log("Analysis complete.")
