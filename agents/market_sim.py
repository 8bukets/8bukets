from .base import Agent
import random

class MarketSimulationAgent(Agent):
    def __init__(self):
        super().__init__("MarketSimulationAgent")

    def perform_task(self, context=None):
        """
        Context contains outputs from all other agents.
        Evaluates the 'quality' and 'market fit' of the generated content/ads.
        """
        analyst_data = context.get('AnalystAgent', {})
        ad_data = context.get('AdManagerAgent', {})
        creator_data = context.get('CreatorAgent', {})

        score = 5.0 # Baseline score
        feedback_details = []

        # 1. Evaluate Ad Relevance
        campaigns = ad_data.get('campaigns', [])
        keywords = analyst_data.get('keywords', [])

        if campaigns:
            # Simulate Click-Through-Rate (CTR) logic
            # High relevance between keywords and campaign name = higher score
            relevance_score = 0
            for camp in campaigns:
                camp_name_lower = camp['name'].lower()
                for kw, _ in keywords:
                    if kw in camp_name_lower:
                        relevance_score += 1

            if relevance_score > 0:
                score += 2.0
                feedback_details.append("ad_relevance_high")
            else:
                score -= 1.0
                feedback_details.append("ad_relevance_low")
        else:
            feedback_details.append("no_campaigns_generated")
            score -= 1.0

        # 2. Evaluate Content Quality (Creator)
        draft_content = creator_data.get('draft_content', "")
        if len(draft_content) > 500:
            score += 1.0
            feedback_details.append("content_depth_good")
        elif len(draft_content) < 100:
            score -= 1.0
            feedback_details.append("content_quality_low")

        # 3. Simulate Random Market Fluctuations
        fluctuation = random.uniform(-1.0, 1.0)
        score += fluctuation

        # Cap score
        score = max(0.0, min(10.0, score))

        self.results['score'] = score
        self.results['details'] = feedback_details
        self.logger.info(f"Market Simulation Complete. Score: {score:.2f}")
