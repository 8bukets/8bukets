from .base_agent import BaseAgent
import sys
import os

# Add root directory to sys.path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analytics

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("AnalysisAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Analysis...")

        # Reuse logic from analytics.py
        # analytics.generate_report takes data and writes to file, but we want the stats directly if possible.
        # Since analytics.py generates a file, we will let it generate a temp file or just reimplement the extraction logic efficiently
        # to return a dict for the context.

        # Re-implementing core logic for cleaner dictionary output
        total_posts = len(data)
        domains = [analytics.get_domain(p.get('external_link')) for p in data if p.get('external_link')]
        domain_counts = analytics.Counter(domains).most_common(10)

        categories = []
        for p in data:
            if p.get('categories'):
                categories.extend(p.get('categories'))
        category_counts = analytics.Counter(categories).most_common(10)

        result = {
            "total_posts": total_posts,
            "top_domains": dict(domain_counts),
            "top_categories": dict(category_counts)
        }

        return {"analysis_stats": result}
