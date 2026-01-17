from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
from .base_agent import BaseAgent

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def _get_domain(self, url):
        if not url:
            return None
        try:
            return urlparse(url).netloc.replace('www.', '')
        except:
            return None

    def run(self, data: list) -> dict:
        """
        Performs statistical analysis on the scraped data.
        Logic ported and adapted from analytics.py.
        """
        if not data:
            return {"error": "No data provided"}

        # 1. Domain Analysis
        domains = [self._get_domain(p.get('external_link')) for p in data if p.get('external_link')]
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

        start_date = "N/A"
        end_date = "N/A"
        if dates:
            dates.sort()
            start_date = dates[0].strftime('%Y-%m-%d')
            end_date = dates[-1].strftime('%Y-%m-%d')

        return {
            "total_posts": len(data),
            "top_domains": dict(domain_counts),
            "top_categories": dict(category_counts),
            "date_range": f"{start_date} to {end_date}"
        }
