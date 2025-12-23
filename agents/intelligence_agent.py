from .base_agent import BaseAgent
from typing import Dict, Any

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")

    def process(self, analysis_result: Dict) -> Dict:
        self.log("Extracting intelligence...")

        keywords = [w[0] for w in analysis_result.get('common_keywords', [])]

        insight = "Neutral"
        if "available" in keywords or "new" in keywords:
            insight = "Growth/Expansion Phase"

        return {
            "strategic_insight": insight,
            "focus_areas": keywords[:3]
        }
