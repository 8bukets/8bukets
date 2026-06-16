from .base_agent import BaseAgent, Blackboard
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import analytics
from agents.telemetry import telemetry_manager

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("AnalysisAgent", provides=["analysis_stats"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Analysis...")

        total_posts = len(data)
        domains = []
        categories = []

        for p in data:
            domain = p.get('domain')
            if domain:
                domains.append(domain)

            cats = p.get('categories')
            if cats:
                categories.extend(cats)

        domain_counts = analytics.Counter(domains).most_common(10)
        category_counts = analytics.Counter(categories).most_common(10)

        # Telemetry for "Ad Ads Advertise"
        ad_count = dict(category_counts).get("Ad Ads Advertise", 0)
        telemetry_manager.record_event(self.name, "MARKET_DATA_ANALYSIS", {
            "ad_category_density": ad_count / total_posts if total_posts > 0 else 0,
            "total_ad_posts": ad_count
        })

        result = {
            "total_posts": total_posts,
            "top_domains": dict(domain_counts),
            "top_categories": dict(category_counts)
        }

        return {"analysis_stats": result}
