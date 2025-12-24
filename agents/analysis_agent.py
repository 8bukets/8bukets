from .base_agent import BaseAgent
from collections import Counter
from typing import List, Dict, Any
from urllib.parse import urlparse
from datetime import datetime

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def get_domain(self, url):
        if not url:
            return None
        try:
            return urlparse(url).netloc.replace('www.', '')
        except:
            return None

    async def process(self, data: List[Dict]) -> Dict[str, Any]:
        results = {}

        # Total Posts
        results['Total Posts'] = len(data)

        # Domain Analysis
        domains = [self.get_domain(p.get('external_link')) for p in data if p.get('external_link')]
        domain_counts = Counter(domains).most_common(5)
        results['Top Domains'] = ", ".join([f"{d} ({c})" for d, c in domain_counts])

        # Category Analysis
        all_categories = []
        for p in data:
            cats = p.get('categories', [])
            if isinstance(cats, list):
                all_categories.extend(cats)
            elif isinstance(cats, str):
                all_categories.append(cats)

        category_counts = Counter(all_categories).most_common(5)
        results['Top Categories'] = ", ".join([f"{c} ({n})" for c, n in category_counts])

        # Author Analysis
        authors = [p.get('author') for p in data if p.get('author')]
        author_counts = Counter(authors).most_common(3)
        results['Top Authors'] = ", ".join([f"{a} ({c})" for a, c in author_counts])

        return results
