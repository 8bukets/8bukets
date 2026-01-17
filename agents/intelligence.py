from collections import Counter
import re
from agents.base import BaseAgent
import logging

logger = logging.getLogger(__name__)

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent")

    def analyze_keywords(self, data, top_n=10):
        stop_words = {
            'the', 'and', 'in', 'of', 'for', 'a', 'to', 'on', 'with', 'at', 'by',
            'from', 'is', 'it', 'your', 'my', 'webshop', 'online', 'store', 'shop',
            'official', 'website', 'site', 'hr', 'com', 'eu', 'collection', 'new',
            'sale', 'best', 'buy', 'free', 'shipping', 'delivery', 'price', 'deals',
            'offer', 'discount', 'save', 'get', 'up', 'off', 'all', 'more', 'za', 'i', 'u', 'na'
        }

        all_words = []
        for p in data:
            title = p.get('title', '').lower()
            words = re.findall(r'\b\w+\b', title)
            for w in words:
                if w not in stop_words and len(w) > 2:
                    all_words.append(w)

        return Counter(all_words).most_common(top_n)

    def detect_new_posts(self, current_data, prev_data):
        if not prev_data:
            return []

        prev_urls = {p.get('post_url') for p in prev_data if p.get('post_url')}
        new_posts = []

        for p in current_data:
            if p.get('post_url') and p.get('post_url') not in prev_urls:
                new_posts.append(p)

        return new_posts

    def run(self, current_data, prev_data=None):
        logger.info(f"[{self.name}] Generating intelligence...")
        intel = {}
        intel['keywords'] = self.analyze_keywords(current_data)
        intel['new_posts'] = self.detect_new_posts(current_data, prev_data)
        return intel
