from typing import List, Dict, Any
from .base_agent import BaseAgent

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Monetization Agent")
        # Heuristic keywords that imply higher CPM/Ad value
        self.high_value_keywords = {
            'finance': 10, 'crypto': 9, 'invest': 8, 'software': 7,
            'hosting': 7, 'insurance': 10, 'loan': 9, 'legal': 8,
            'health': 6, 'marketing': 6, 'tech': 5
        }

    def run(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not data:
            return {"error": "No data"}

        potential_placements = []

        for post in data:
            score = 0
            text_to_scan = (post.get('title', '') + " " + " ".join(post.get('categories', []))).lower()

            matched_keywords = []
            for kw, val in self.high_value_keywords.items():
                if kw in text_to_scan:
                    score += val
                    matched_keywords.append(kw)

            if score > 5:
                potential_placements.append({
                    "title": post.get('title'),
                    "score": score,
                    "keywords": matched_keywords,
                    "url": post.get('post_url')
                })

        # Sort by score
        potential_placements.sort(key=lambda x: x['score'], reverse=True)

        return {
            "high_value_opportunities": len(potential_placements),
            "top_opportunities": potential_placements[:5]
        }

    def format_report(self, results: Dict[str, Any]) -> str:
        lines = [f"## {self.name} Report"]
        lines.append(f"**High Value Content Identified:** {results.get('high_value_opportunities', 0)}")

        lines.append("\n### Top Monetization Opportunities")
        for opp in results.get('top_opportunities', []):
            lines.append(f"- [{opp['score']} pts] **{opp['title']}** (Keywords: {', '.join(opp['keywords'])})")

        return "\n".join(lines)
