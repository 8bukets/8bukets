from .base import BaseAgent
from typing import Any, Dict
from collections import Counter
from datetime import datetime

class AnalyzeAgent(BaseAgent):
    def __init__(self):
        super().__init__("AnalyzeAgent")

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        data = context.get("scraped_data", [])
        if not data:
            self.log("No data to analyze.")
            return {"analysis": {}}

        self.log(f"Analyzing {len(data)} posts...")

        # Domain Analysis
        domains = [p.get('domain') for p in data if p.get('domain')]
        domain_counts = Counter(domains).most_common(5)

        # Category Analysis
        all_categories = []
        for p in data:
            cats = p.get('categories', [])
            if cats:
                all_categories.extend(cats)
        category_counts = Counter(all_categories).most_common(5)

        # Activity by Month (Simple)
        dates = []
        for p in data:
            dt_str = p.get('datetime')
            if dt_str:
                try:
                    dt = datetime.fromisoformat(dt_str)
                    dates.append(dt.strftime('%Y-%m'))
                except:
                    pass
        date_activity = Counter(dates).most_common(5)

        return {
            "analysis": {
                "total_posts": len(data),
                "top_domains": domain_counts,
                "top_categories": category_counts,
                "activity_by_month": date_activity
            }
        }
