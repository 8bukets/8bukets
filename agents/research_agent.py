from collections import Counter
from typing import List, Dict, Any
from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        if not data:
            return {"error": "No data for research"}

        # Extract external links that are not internal
        external_links = []
        for post in data:
            link = post.get('external_link')
            if link and 'markposition.wordpress.com' not in link:
                external_links.append(link)

        # "Research" the top domains (Simulated by analyzing domain diversity)
        domains = [post.get('domain') for post in data if post.get('domain')]
        unique_domains = set(domains)

        # Identify "Trending" topics based on repeated words in titles
        all_words = []
        for post in data:
            title = post.get('title', '').lower()
            words = [w for w in title.split() if len(w) > 4] # Simple filter
            all_words.extend(words)

        trending_keywords = dict(Counter(all_words).most_common(10))

        return {
            "unique_external_sources": len(unique_domains),
            "total_external_links": len(external_links),
            "trending_keywords": trending_keywords,
            "sample_external_links": external_links[:5]
        }

    def format_report(self, results: Dict[str, Any]) -> str:
        lines = [f"## {self.name} Report"]
        lines.append(f"**Unique External Sources:** {results.get('unique_external_sources', 0)}")

        lines.append("\n### Trending Keywords (Title Analysis)")
        for word, count in results.get('trending_keywords', {}).items():
            lines.append(f"- {word}: {count}")

        lines.append("\n### Sample External Sources")
        for link in results.get('sample_external_links', []):
            lines.append(f"- {link}")

        return "\n".join(lines)
