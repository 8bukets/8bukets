from typing import List, Dict, Any
from .base_agent import BaseAgent
import random

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Creativity Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        if not data or len(data) < 2:
            return {"error": "Not enough data for creativity"}

        # Use DNA for creativity weight
        weight = 0.5
        if dna:
            weight = dna.get("content_strategy", {}).get("creativity_weight", 0.5)

        # "Remix" Ideas: Combine title structures
        titles = [p.get('title') for p in data if p.get('title')]

        generated_ideas = []
        if titles:
            # Higher weight = more random combinations
            num_ideas = int(3 + (weight * 5))

            for _ in range(num_ideas):
                t1 = random.choice(titles)
                t2 = random.choice(titles)

                # Simple mashup logic: First half of A + Second half of B
                parts1 = t1.split()
                parts2 = t2.split()

                mid1 = len(parts1) // 2
                mid2 = len(parts2) // 2

                new_title = " ".join(parts1[:mid1] + parts2[mid2:])
                generated_ideas.append(new_title)

        return {
            "remixed_ideas": generated_ideas,
            "creativity_factor": weight
        }

    def format_report(self, results: Dict[str, Any]) -> str:
        lines = [f"## {self.name} Report"]
        lines.append("\n### Creative Brainstorming (Remixed Titles)")
        for idea in results.get('remixed_ideas', []):
            lines.append(f"- {idea}")
        return "\n".join(lines)
