import json
import logging
from collections import Counter
from textblob import TextBlob

logger = logging.getLogger("AnalyzeAgent")

class AnalyzeAgent:
    def __init__(self, data_file="links.json"):
        self.data_file = data_file

    def analyze(self):
        """Analyzes data for sentiment and keywords."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            return None

        analysis_results = {
            "total_articles": len(data),
            "articles": [],
            "top_keywords": []
        }

        all_keywords = []

        for article in data:
            title = article.get('title', '')
            blob = TextBlob(title)

            # Sentiment
            sentiment = blob.sentiment.polarity

            # Keywords (Noun Phrases)
            # Use 'words' if noun_phrases returns empty or for broader coverage
            keywords = blob.noun_phrases
            all_keywords.extend(keywords)

            analysis_results["articles"].append({
                "title": title,
                "sentiment": sentiment,
                "keywords": keywords
            })

        # Top keywords across all articles
        analysis_results["top_keywords"] = Counter(all_keywords).most_common(10)

        logger.info(f"📊 Analysis complete. Top keyword: {analysis_results['top_keywords'][0] if analysis_results['top_keywords'] else 'None'}")
        return analysis_results
