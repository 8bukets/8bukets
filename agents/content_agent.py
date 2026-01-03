from typing import List, Dict, Any
from .base_agent import BaseAgent
from collections import Counter

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content Creation Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        if not data:
            return {"error": "No data"}

        # Use DNA to influence tone
        tone = "informative"
        if dna:
            tone = dna.get("content_strategy", {}).get("tone", "informative")

        # Determine dominant category
        all_cats = []
        for post in data:
            all_cats.extend(post.get('categories', []))

        if not all_cats:
            dominant_topic = "General News"
        else:
            dominant_topic = Counter(all_cats).most_common(1)[0][0]

        # Select top 3 articles for the digest
        top_articles = data[:3]

        # Draft a simple blog post
        draft_title = f"Daily Insight: The State of {dominant_topic} ({tone.title()} Edition)"
        draft_body = f"Today we are looking at the latest trends in {dominant_topic}.\n\n"
        draft_body += "Here are the top stories you shouldn't miss:\n"

        for article in top_articles:
            draft_body += f"- **{article.get('title')}**: A key piece by {article.get('author') or 'Unknown'}.\n"

        draft_body += "\nStay tuned for more updates tomorrow!"

        return {
            "draft_title": draft_title,
            "draft_body": draft_body,
            "topic": dominant_topic,
            "tone_used": tone
        }

    def format_report(self, results: Dict[str, Any]) -> str:
        lines = [f"## {self.name} Report"]
        lines.append("### Generated Content Draft")
        lines.append(f"**Title:** {results.get('draft_title')}\n")
        lines.append("**Body:**")
        lines.append(results.get('draft_body'))
        return "\n".join(lines)
