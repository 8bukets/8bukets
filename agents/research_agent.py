from .base_agent import BaseAgent
from collections import Counter
from security_utils import sanitize_for_markdown

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")

    def run(self, data):
        self.log("Identifying trends...")
        # Trend detection based on keywords in titles
        keywords = []
        for p in data:
            title = p.get('title', '').lower()
            words = [w for w in title.split() if len(w) > 4]
            keywords.extend(words)

        common_keywords = Counter(keywords).most_common(5)

        report = "### Research Trends\n"
        report += "**Emerging Keywords:**\n"
        for word, count in common_keywords:
            safe_word = sanitize_for_markdown(word)
            report += f"- {safe_word} ({count} mentions)\n"

        self.log("Research complete.")
        return report
