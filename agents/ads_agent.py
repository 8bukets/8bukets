from .base_agent import BaseAgent
import random

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Ads Agent")

    def run(self, data: dict) -> dict:
        """
        Generates ad copy based on high-performing content.
        Input: dict containing 'analysis' and 'monetization' results.
        """
        monetization = data.get('monetization', {})
        top_opps = monetization.get('top_opportunities', [])

        ad_campaigns = []

        # Load past successful headlines from memory
        memory_data = self.memory.load_memory()
        successful_hooks = memory_data.get("learnings", {}).get("successful_hooks", ["Best Deal", "Top Rated"])

        for opp in top_opps:
            title = opp.get('title', 'Service')
            keywords = opp.get('keywords', [])

            # Create Ad Variations
            hook = random.choice(successful_hooks)
            headline = f"{hook}: {title}"
            description = f"Discover the best {', '.join(keywords)} solutions. Click to learn more about {title}."

            ad_campaigns.append({
                "headline": headline,
                "description": description,
                "keywords": keywords,
                "target_url": opp.get('link')
            })

        # Save run to memory
        self.memory.log_run({"generated_ads_count": len(ad_campaigns)})

        return {
            "ad_campaigns": ad_campaigns
        }
