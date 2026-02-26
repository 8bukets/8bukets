from .base_agent import BaseAgent

class AdsAgent(BaseAgent):
    execution_stage = 5
    def __init__(self):
        super().__init__("AdsAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Generating Ad Campaigns...")

        # Collaborative dependency: Needs Targeting Profile
        targeting = context.get("targeting_profile", {})
        persona = targeting.get("primary_persona", "Unknown")

        # Collaborative dependency: Needs Creative Angles
        angles = context.get("creative_angles", ["Generic Ad"])

        campaigns = []
        for i, angle in enumerate(angles[:3]):
            campaigns.append({
                "id": f"CMP-{i+1:03d}",
                "headline": angle,
                "target_audience": persona,
                "cta": "Learn More" if "Deep Dive" in angle else "Get Started"
            })

        return {"generated_ads": campaigns}
