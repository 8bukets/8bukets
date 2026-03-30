from .base_agent import BaseAgent, Blackboard
from agents.telemetry import telemetry_manager

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("AdsAgent", dependencies=["targeting_profile", "creative_concepts"], provides=["generated_ads"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Generating Ad Campaigns...")

        targeting = blackboard.get("targeting_profile", {})
        concepts = blackboard.get("creative_concepts", [])

        ads = []
        for concept in concepts[:3]:
            ads.append({
                "headline": concept,
                "target_audience": targeting.get("primary_persona"),
                "cta": "Get Started" if "Trends" in concept else "Learn More"
            })

        telemetry_manager.record_event(self.name, "AD_STRATEGY_GENERATION", {
            "ad_count": len(ads),
            "target_persona": targeting.get("primary_persona")
        })

        return {"generated_ads": ads}
