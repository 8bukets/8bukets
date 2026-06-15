import logging
import random
from datetime import datetime

logger = logging.getLogger("ContentCreationAgent")

class ContentCreationAgent:
    def __init__(self):
        pass

    def generate_content(self, trends, strategy):
        """Generates a blog post based on trends and strategy."""

        timestamp = datetime.now().strftime("%Y-%m-%d")
        mood = strategy.get("market_mood", "Neutral")
        focus = ", ".join(strategy.get("focus_areas", []))

        # UX Enhancement: Emoji Mapping
        mood_emoji = {
            "Positive": "🟢",
            "Negative": "🔴",
            "Neutral": "🟡"
        }.get(mood, "⚪")

        md_content = []
        md_content.append(f"# 📰 Oracle News Digest: {timestamp} <a name='table-of-contents'></a>")

        # UX Enhancement: Table of Contents
        md_content.append("\n## 📋 Table of Contents")
        md_content.append("- [Executive Summary](#executive-summary)")
        md_content.append("- [Trending Topics](#trending-topics)")

        md_content.append(f"\n**Market Mood:** {mood_emoji} {mood}")
        md_content.append(f"**Focus Areas:** {focus}")

        md_content.append("\n## 📊 Executive Summary <a name='executive-summary'></a>")
        md_content.append(f"Recent analysis indicates a **{mood.lower()}** sentiment in the latest Oracle news cycle. "
                          f"Key topics driving the conversation include **{focus}**.")
        md_content.append("\n[⬆️ Back to Top](#table-of-contents)")

        md_content.append("\n## 📈 Trending Topics <a name='trending-topics'></a>")

        for topic, titles in trends.items():
            if topic == "General": continue

            md_content.append(f"\n### Trend: {topic.title()}")
            md_content.append(f"We've seen significant activity around **{topic}**. Here are the headlines:")

            # UX Enhancement: Collapsible Details
            md_content.append(f"<details>\n<summary>View {len(titles[:5])} Headlines</summary>\n")
            for title in titles[:5]: # Limit to 5
                md_content.append(f"- {title}")
            md_content.append("\n</details>")

            # Creative addition
            creative_insight = self._generate_creative_insight(topic)
            md_content.append(f"\n*> 💡 Insight: {creative_insight}*")

        md_content.append("\n[⬆️ Back to Top](#table-of-contents)")

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
