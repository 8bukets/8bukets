from .base_agent import BaseAgent
from collections import Counter
from itertools import chain
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

    async def process(self, data: List[Dict], shared_context: Dict[str, Any], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
        results = {}

        # Total Posts
        results['Total Posts'] = len(data)

        # Domain Analysis
        domain_counts = Counter(self.get_domain(p.get('external_link')) for p in data if p.get('external_link')).most_common(5)
        results['Top Domains'] = ", ".join([f"{d} ({c})" for d, c in domain_counts])

        # Category Analysis
        def get_cats(p):
            c = p.get('categories', [])
            return c if isinstance(c, list) else [c] if isinstance(c, str) else []

        category_counts = Counter(chain.from_iterable(get_cats(p) for p in data)).most_common(5)
        results['Top Categories'] = ", ".join([f"{c} ({n})" for c, n in category_counts])

        # Author Analysis
        author_counts = Counter(p.get('author') for p in data if p.get('author')).most_common(3)
        results['Top Authors'] = ", ".join([f"{a} ({c})" for a, c in author_counts])

        return results
