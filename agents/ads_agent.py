from .base_agent import BaseAgent
from typing import Dict, List

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Ads Agent")

    def process(self, research: Dict, iq: int = 25) -> List[str]:
        self.log(f"Generating ad copy (IQ: {iq})...")

        ads = [
            "Unlock the power of Oracle Database on Google Cloud. Scale effortlessly. Start today!",
            "Multi-cloud made easy. Oracle + Google Cloud = Match made in heaven. Learn more."
        ]

        # Higher IQ generates more sophisticated copy
        if iq > 30:
            ads.append("Synergize your data estate. Oracle's robustness meets Google's AI. The future is multi-cloud.")

        findings = research.get('key_findings', [])
        if any("Canada" in f for f in findings):
            ads.append("Canadian Enterprises: Oracle Database @ Google Cloud is finally here! Local compliance, global scale.")

        return ads
