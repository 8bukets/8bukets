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

        domains = []
        all_categories = []
        dates = []
        authors = []

        for p in data:
            # 1. Domain Analysis
            ext_link = p.get('external_link')
            if ext_link:
                domains.append(self.get_domain(ext_link))

            # 2. Category Analysis
            cats = p.get('categories', [])
            if cats:
                all_categories.extend(cats)

            # 3. Date Analysis
            dt_str = p.get('datetime')
            if dt_str:
                try:
                    dt = datetime.fromisoformat(dt_str)
                    dates.append(dt)
                except ValueError:
                    pass

            # 4. Author Analysis
            author = p.get('author')
            if author:
                authors.append(author)

        domain_counts = Counter(domains).most_common(10)
        category_counts = Counter(all_categories).most_common(10)

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
