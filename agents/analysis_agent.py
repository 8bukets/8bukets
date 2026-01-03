from collections import Counter
from typing import List, Dict, Any
from .base_agent import BaseAgent

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        if not data:
            return {"error": "No data to analyze"}

        total_posts = len(data)

        # Category Analysis
        all_categories = []
        for post in data:
            all_categories.extend(post.get('categories', []))
        category_counts = dict(Counter(all_categories).most_common(5))

        # Author Analysis
        authors = [post.get('author') for post in data if post.get('author')]
        author_counts = dict(Counter(authors).most_common(5))

        # Domain Analysis
        domains = [post.get('domain') for post in data if post.get('domain')]
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
