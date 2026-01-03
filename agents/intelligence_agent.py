from typing import List, Dict, Any
from .base_agent import BaseAgent
from collections import defaultdict

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        if not data:
            return {"error": "No data for intelligence"}

        # Cross-reference Author vs Category
        author_preferences = defaultdict(lambda: defaultdict(int))

        for post in data:
            author = post.get('author')
            categories = post.get('categories', [])
            if author and categories:
                for cat in categories:
                    author_preferences[author][cat] += 1

        # Identify "Specialists" (Authors who post mostly in one category)
        specialists = []
        for author, cat_counts in author_preferences.items():
            if not cat_counts:
                continue
            total_posts = sum(cat_counts.values())
            primary_cat = max(cat_counts, key=cat_counts.get)
            count = cat_counts[primary_cat]

            if count / total_posts > 0.7 and total_posts > 2: # 70% focus
                specialists.append({
                    "author": author,
                    "focus": primary_cat,
                    "intensity": f"{int((count/total_posts)*100)}%"
                })

        return {
            "author_specialists": specialists,
            "data_points_processed": len(data)
        }

    def format_report(self, results: Dict[str, Any]) -> str:
        lines = [f"## {self.name} Report"]

        lines.append("\n### Identified Specialists")
        if not results.get('author_specialists'):
            lines.append("No clear specialists identified based on current data.")
        else:
            for spec in results.get('author_specialists', []):
                lines.append(f"- **{spec['author']}** is a specialist in **{spec['focus']}** ({spec['intensity']} of their posts).")

        return "\n".join(lines)
