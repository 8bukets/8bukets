from .base_agent import BaseAgent
import json
import collections
import re

class AnalyzeAgent(BaseAgent):
    def __init__(self):
        super().__init__("AnalyzeAgent")

    def run(self, context):
        self.log("Analyzing scraped data...")
        data_file = context.get('scraped_data_file', 'links.json')

        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.log("No data found to analyze.")
            return {}

        words = []
        stop_words = {'the', 'and', 'to', 'of', 'a', 'in', 'for', 'on', 'with', 'is', 'at', 'by', 'from', 'it', 'that', 'site', 'website'}

        for item in data:
            title = item.get('title', '').lower()
            tokens = re.findall(r'\b\w+\b', title)
            for token in tokens:
                if token not in stop_words and len(token) > 2:
                    words.append(token)

        word_counts = collections.Counter(words)
        top_keywords = [w for w, c in word_counts.most_common(10)]

        self.learn("top_keywords", top_keywords)
        self.log(f"Analysis complete. Top keywords: {top_keywords}")

        return {"top_keywords": top_keywords, "data_count": len(data)}
