from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
from agents.base import BaseAgent
import logging

logger = logging.getLogger(__name__)

class AnalyzeAgent(BaseAgent):
    def __init__(self):
        super().__init__("AnalyzeAgent")

    def get_domain(self, url):
        if not url:
            return None
        try:
            return urlparse(url).netloc.replace('www.', '')
        except:
            return None

    def run(self, data):
        logger.info(f"[{self.name}] Analyzing data...")
        if not data:
            return {}

        stats = {}
        stats['total_posts'] = len(data)

        # Domain Analysis
        domains = [self.get_domain(p.get('external_link')) for p in data if p.get('external_link')]
        stats['domains'] = Counter(domains).most_common(10)
        stats['unique_domains'] = len(set(domains))

        # Category Analysis
        all_categories = []
        for p in data:
            cats = p.get('categories', [])
            if cats:
                all_categories.extend(cats)
        stats['categories'] = Counter(all_categories).most_common(10)

        # Date Analysis
        dates = []
        for p in data:
            dt_str = p.get('datetime')
            if dt_str:
                try:
                    dt = datetime.fromisoformat(dt_str)
                    dates.append(dt)
                except ValueError:
                    pass

        if dates:
            dates.sort()
            stats['start_date'] = dates[0].strftime('%Y-%m-%d')
            stats['end_date'] = dates[-1].strftime('%Y-%m-%d')
            years = [d.year for d in dates]
            year_counts = Counter(years).most_common()
            year_counts.sort(key=lambda x: x[0], reverse=True)
            stats['years'] = year_counts
        else:
            stats['start_date'] = "N/A"
            stats['end_date'] = "N/A"
            stats['years'] = []

        # Author Analysis
        authors = [p.get('author') for p in data if p.get('author')]
        stats['authors'] = Counter(authors).most_common()

        return stats
