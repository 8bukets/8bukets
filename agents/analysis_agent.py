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
        domains = [d for p in data if (d := p.get('domain'))]
        domain_counts = analytics.Counter(domains).most_common(10)

        categories = []
        for p in data:
            if p.get('categories'):
                categories.extend(p.get('categories'))
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
