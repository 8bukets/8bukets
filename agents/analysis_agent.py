from agents.base_agent import BaseAgent
from analytics import get_domain
from collections import Counter
from datetime import datetime

class AnalysisAgent(BaseAgent):
    def __init__(self, name: str = "Analysis"):
        super().__init__(name)

    async def process(self, data: dict) -> dict:
        """
        Expects data to contain 'data' (list of scraped posts).
        """
        raw_data = data.get("data", [])
        self.log(f"Analyzing {len(raw_data)} items...")

        if not raw_data:
            return {"status": "empty", "insights": {}}

        # Domain Analysis
        domains = [get_domain(p.get('external_link')) for p in raw_data if p.get('external_link')]
        domain_counts = Counter(domains).most_common(5)

        # Category Analysis
        all_categories = []
        for p in raw_data:
            cats = p.get('categories', [])
            if cats:
                all_categories.extend(cats)
        category_counts = Counter(all_categories).most_common(5)

        # Author Analysis
        authors = [p.get('author') for p in raw_data if p.get('author')]
        author_counts = Counter(authors).most_common(5)

        insights = {
            "top_domains": domain_counts,
            "top_categories": category_counts,
            "top_authors": author_counts,
            "total_posts": len(raw_data),
            "timestamp": datetime.now().isoformat()
        }

        self.log("Analysis complete.")
        return {"status": "success", "insights": insights}
