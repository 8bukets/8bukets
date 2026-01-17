from .base_agent import BaseAgent
import random

class DeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__("Developer Agent")

    def run(self, data: dict) -> dict:
        """
        Analyzes system metrics and data patterns to propose code improvements.
        Input: dict containing 'health', 'analysis' results.
        """
        health = data.get('health', {})
        analysis = data.get('analysis', {})

        proposals = []

        # 1. Scalability Check
        total_posts = analysis.get('total_posts', 0)
        if total_posts > 1000:
            proposals.append({
                "type": "Optimization",
                "title": "Implement Database Storage",
                "reason": f"Dataset has grown to {total_posts} records. JSON file storage will become a bottleneck.",
                "code_snippet": "class DatabaseManager:\n    def __init__(self, db_url): ..."
            })

        # 2. Domain-Specific Scraper Proposal
        top_domains = analysis.get('top_domains', {})
        for domain, count in top_domains.items():
            if count > 5 and "wordpress" not in domain:
                proposals.append({
                    "type": "New Feature",
                    "title": f"Create Scraper for {domain}",
                    "reason": f"High volume of content ({count} posts) linked from {domain}. A dedicated scraper could extract richer metadata.",
                    "code_snippet": f"class {domain.split('.')[0].capitalize()}Scraper(BaseScraper):\n    pass"
                })

        # 3. Curiosity/Random Innovation (The "100% Creativity" Factor)
        tech_keywords = ["AI", "Blockchain", "Quantum", "VR"]
        random_tech = random.choice(tech_keywords)
        proposals.append({
            "type": "Innovation",
            "title": f"Integrate {random_tech} Analysis Module",
            "reason": f"To stay ahead of the curve, the system should autonomously analyze content for {random_tech} relevance.",
            "code_snippet": f"def analyze_{random_tech.lower()}(text):\n    # TODO: Implement advanced logic\n    pass"
        })

        return {
            "feature_proposals": proposals,
            "status": "Active"
        }
