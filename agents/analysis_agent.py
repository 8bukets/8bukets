from collections import Counter
from typing import List, Dict, Any
from itertools import chain
from .base_agent import BaseAgent

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def run(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not data:
            return {"error": "No data to analyze"}

        total_posts = len(data)

        # Category Analysis
        # Optimization: Use chain.from_iterable to avoid creating a large intermediate list of all categories
        all_categories = chain.from_iterable((post.get('categories') or []) for post in data)
        category_counts = dict(Counter(all_categories).most_common(5))

        # Author Analysis
        # Optimization: Use generator expression to avoid creating intermediate list
        authors = (post.get('author') for post in data if post.get('author'))
        author_counts = dict(Counter(authors).most_common(5))

        # Domain Analysis
        # Optimization: Use generator expression to avoid creating intermediate list
        domains = (post.get('domain') for post in data if post.get('domain'))
        domain_counts = dict(Counter(domains).most_common(5))

        return {
            "total_posts": total_posts,
            "top_categories": category_counts,
            "top_authors": author_counts,
            "top_domains": domain_counts
        }

    def format_report(self, results: Dict[str, Any]) -> str:
        lines = [f"## {self.name} Report"]
        lines.append(f"**Total Posts Scanned:** {results.get('total_posts', 0)}")

        lines.append("\n### Top Categories")
        for cat, count in results.get('top_categories', {}).items():
            lines.append(f"- {cat}: {count}")

        lines.append("\n### Top Authors")
        for author, count in results.get('top_authors', {}).items():
            lines.append(f"- {author}: {count}")

        return "\n".join(lines)
