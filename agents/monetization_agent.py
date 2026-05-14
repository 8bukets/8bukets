from .base_agent import BaseAgent
from typing import Dict, List

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization Agent")

    def process(self, research: Dict) -> List[str]:
        self.log("Brainstorming monetization...")

        strategies = [
            "Affiliate marketing for Google Cloud courses",
            "Consulting services for Oracle-to-GCP migration",
            "Premium newsletter for multi-cloud architecture"
        ]

        if "Canada" in str(research):
            strategies.append("Target Canadian enterprise sector with localization services.")

        if "AI" in str(research):
            strategies.append("Consulting services for AI implementations on Oracle Cloud")
            strategies.append("Develop custom generative AI solutions leveraging Oracle infrastructure")

        return strategies
