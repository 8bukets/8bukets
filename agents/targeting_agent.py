from .base_agent import BaseAgent
from collections import Counter

class TargetingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Targeting Agent")

    def run(self, data: dict) -> dict:
        """
        Segments audience based on content analysis.
        Input: dict containing 'analysis' results.
        """
        analysis = data.get('analysis', {})
        top_cats = analysis.get('top_categories', {})

        segments = []
        for cat, count in top_cats.items():
            segment = {
                "name": f"{cat} Enthusiasts",
                "interest": cat,
                "size_estimate": count * 100, # Mock calculation
                "demographics": "Broad" if count > 50 else "Niche"
            }
            segments.append(segment)

        # Retrieve past targeting learnings
        learnings = self.memory.load_memory().get("learnings", {})
        prioritized_segments = learnings.get("priority_segments", [])

        # Prioritize segments present in memory
        for seg in segments:
            if seg["name"] in prioritized_segments:
                seg["priority"] = "High"
            else:
                seg["priority"] = "Standard"

        return {
            "audience_segments": segments
        }
