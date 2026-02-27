from .base_agent import BaseAgent, Blackboard

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

        return {"generated_ads": ads}
