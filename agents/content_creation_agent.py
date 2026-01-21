import logging
import random
from datetime import datetime
from agents.security_utils import sanitize_for_markdown

logger = logging.getLogger("ContentCreationAgent")

class ContentCreationAgent:
    def __init__(self):
        pass

    def generate_content(self, trends, strategy):
        """Generates a blog post based on trends and strategy."""

        timestamp = datetime.now().strftime("%Y-%m-%d")
        mood = strategy.get("market_mood", "Neutral")
        focus = ", ".join(strategy.get("focus_areas", []))

        md_content = []
        md_content.append(f"# Oracle News Digest: {timestamp}")
        md_content.append(f"\n**Market Mood:** {mood}")
        md_content.append(f"**Focus Areas:** {focus}")
        md_content.append("\n## Executive Summary")
        md_content.append(f"Recent analysis indicates a **{mood.lower()}** sentiment in the latest Oracle news cycle. "
                          f"Key topics driving the conversation include **{focus}**.")

        md_content.append("\n## Trending Topics")

        for topic, titles in trends.items():
            if topic == "General": continue

            safe_topic = sanitize_for_markdown(topic)
            md_content.append(f"\n### Trend: {safe_topic.title()}")
            md_content.append(f"We've seen significant activity around **{safe_topic}**. Here are the headlines:")
            for title in titles[:5]: # Limit to 5
                safe_title = sanitize_for_markdown(title)
                md_content.append(f"- {safe_title}")

            # Creative addition
            creative_insight = self._generate_creative_insight(safe_topic)
            md_content.append(f"\n*> Insight: {creative_insight}*")

        return "\n".join(md_content)

    def _generate_creative_insight(self, topic):
        """Simulates creativity by associating topics with business concepts."""
        insights = [
            f"The rise of {topic} suggests a shift towards more automated enterprise workflows.",
            f"Investments in {topic} are likely to yield high ROI in the coming fiscal year.",
            f"Competitors should watch {topic} closely as Oracle doubles down on this capability.",
            f"{topic} is not just a buzzword; it's becoming a core infrastructure requirement."
        ]
        return random.choice(insights)
