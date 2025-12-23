from .base_agent import BaseAgent
from textblob import TextBlob
from collections import Counter

class AnalyzerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analyzer")

    def perform_task(self, data):
        # Data is assumed to be the list of posts from Researcher
        if not data:
            self.logger.warning("No data to analyze.")
            return {}

        self.logger.info(f"Analyzing {len(data)} posts...")

        sentiments = []
        all_content = ""
        categories_counter = Counter()

        for post in data:
            content = post.get('content', '')
            if content:
                blob = TextBlob(content)
                sentiments.append(blob.sentiment.polarity)
                all_content += " " + content

            for cat in post.get('categories', []):
                categories_counter[cat] += 1

        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0

        # Simple keyword extraction
        blob = TextBlob(all_content)
        # Filter for significant words
        words = [w.lower() for w in blob.words if len(w) > 4 and w.isalpha()]
        keywords = Counter(words).most_common(10)

        return {
            "total_posts": len(data),
            "average_sentiment": avg_sentiment,
            "top_categories": categories_counter.most_common(5),
            "top_keywords": keywords
        }
