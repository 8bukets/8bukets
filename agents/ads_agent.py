from .base_agent import BaseAgent
from typing import Dict, List

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Ads Agent")

    def process(self, research: Dict) -> List[str]:
        self.log("Generating ad copy...")

        ads = [
            "Unlock the power of Oracle Database on Google Cloud. Scale effortlessly. Start today!",
            "Multi-cloud made easy. Oracle + Google Cloud = Match made in heaven. Learn more."
        ]

        findings = research.get('key_findings', [])
        if any("Canada" in f for f in findings):
            ads.append("Canadian Enterprises: Oracle Database @ Google Cloud is finally here! Local compliance, global scale.")

        return ads
