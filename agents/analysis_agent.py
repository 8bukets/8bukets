from .base_agent import BaseAgent
from collections import Counter

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def run(self, data, context=None):
        self.log("Starting analysis...")
        total_posts = len(data)

        # Domain Analysis
        domains = [p.get('domain') for p in data if p.get('domain')]
        domain_counts = Counter(domains).most_common(5)

        # Category Analysis
        categories = []
        for p in data:
            if p.get('categories'):
                categories.extend(p.get('categories'))
        category_counts = Counter(categories).most_common(5)

        report = "### Analysis Report\n"
        report += f"- **Total Posts Processed:** {total_posts}\n"
        report += "- **Top Domains:**\n"
        for d, c in domain_counts:
            report += f"  - {d}: {c}\n"
        report += "- **Top Categories:**\n"
        for c, count in category_counts:
            report += f"  - {c}: {count}\n"

        self.log("Analysis complete.")
        return report
