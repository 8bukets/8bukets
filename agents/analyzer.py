from .base_agent import BaseAgent
from textblob import TextBlob
from collections import Counter
import logging
import sys
import subprocess

class AnalyzerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analyzer")
        # Ensure corpora are available
        try:
            TextBlob("test").sentiment
        except Exception:
            self.logger.warning("TextBlob corpora missing. Downloading...")
            subprocess.run([sys.executable, "-m", "textblob.download_corpora"], check=True)

    def perform_task(self, data):
        # Data is output from Researcher (dict with blog_posts and google_listings)
        blog_posts = data.get('blog_posts', [])
        google_listings = data.get('google_listings', [])

        result = {
            "total_posts": len(blog_posts),
            "google_listings_count": len(google_listings),
            "average_sentiment": 0,
            "top_categories": [],
            "top_keywords": []
        }

        if not blog_posts:
            self.logger.warning("No blog posts to analyze.")
            return result

        self.logger.info(f"Analyzing {len(blog_posts)} posts...")

        sentiments = []
        all_words = []
        categories_counter = Counter()

        for post in blog_posts:
            content = post.get('content', '')
            if content:
                blob = TextBlob(content)
                sentiments.append(blob.sentiment.polarity)
                # Optimization: reuse existing blob
                words = [w.lower() for w in blob.words if len(w) > 4 and w.isalpha()]
                all_words.extend(words)

            for cat in post.get('categories', []):
                categories_counter[cat] += 1

        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0

        keywords = Counter(all_words).most_common(10)

        result["average_sentiment"] = avg_sentiment
        result["top_categories"] = categories_counter.most_common(5)
        result["top_keywords"] = keywords

        return result
