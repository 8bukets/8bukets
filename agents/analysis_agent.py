from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
from .base_agent import BaseAgent
import sys
import os

# Import generate_report logic or helper functions if possible,
# or keep as is if import is difficult due to structure.
# Since analytics.py is in the root and agents is a subdir, we can import it.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analytics import get_domain

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def run(self):
        self.log("Starting analysis...")
        if not self.data:
            self.log("No data to analyze.")
            return

        domain_counts = Counter()
        category_counts = Counter()
        author_counts = Counter()
        year_counts = Counter()

        min_date = None
        max_date = None
        unique_domains = set()

        for p in self.data:
            # Domains - Use shared logic from analytics.py
            external_link = p.get('external_link')
            if external_link:
                domain = get_domain(external_link)
                # Match analytics.py logic: Counter tracks raw domains (including None if get_domain returns it, though get_domain usually returns str or None)
                # In analytics.py refactor:
                # if external_link:
                #    domain = get_domain(external_link)
                #    domain_counts[domain] += 1
                #    unique_domains.add(domain)

                # Here we do the same
                domain_counts[domain] += 1
                unique_domains.add(domain)

            # Categories
            cats = p.get('categories', [])
            if cats:
                category_counts.update(cats)

            # Authors
            author = p.get('author')
            if author:
                author_counts[author] += 1

            # Dates
            dt_str = p.get('datetime')
            if dt_str:
                try:
                    dt = datetime.fromisoformat(dt_str)
                    if min_date is None or dt < min_date:
                        min_date = dt
                    if max_date is None or dt > max_date:
                        max_date = dt
                    year_counts[dt.year] += 1
                except ValueError:
                    pass

        self.results = {
            "total_posts": len(self.data),
            "unique_domains": len(unique_domains),
            "top_domains": domain_counts.most_common(10),
            "top_categories": category_counts.most_common(10),
            "top_authors": author_counts.most_common(5),
            "posts_by_year": dict(sorted(year_counts.items(), reverse=True)),
            "date_range": {
                "start": min_date.strftime('%Y-%m-%d') if min_date else "N/A",
                "end": max_date.strftime('%Y-%m-%d') if max_date else "N/A"
            }
        }
        self.log("Analysis complete.")
