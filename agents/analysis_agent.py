from .base_agent import BaseAgent
from collections import Counter

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("Analysis Agent")

    def run(self, data):
        self.log("Starting analysis...")
        total_posts = len(data)

        # Domain Analysis
        domains = [p.get('domain') for p in data if p.get('domain')]
        unique_domains = len(set(domains))
        domain_counts = Counter(domains).most_common(10)

        # Category Analysis
        categories = []
        for p in data:
            if p.get('categories'):
                categories.extend(p.get('categories'))
        category_counts = Counter(categories).most_common(10)

        top_cat = category_counts[0][0] if category_counts else 'N/A'

        report = "### 📊 Analysis Report\n\n"

        # Executive Summary
        report += "| Metric | Value | Status |\n| :--- | :--- | :---: |\n"
        report += f"| **Total Posts** | {total_posts} | ✅ |\n"
        report += f"| **Unique Domains** | {unique_domains} | 🌐 |\n"
        report += f"| **Top Category** | {top_cat} | 📁 |\n\n"

        # Top Domains
        report += "#### 🌐 Top Domains\n"
        report += "<details>\n<summary>View Top 10 Domains</summary>\n\n"
        for d, c in domain_counts:
            report += f"- **{d}**: {c}\n"
        report += "</details>\n\n"

        # Top Categories
        report += "#### 📂 Top Categories\n"
        report += "<details>\n<summary>View Top 10 Categories</summary>\n\n"
        for c, count in category_counts:
            report += f"- **{c}**: {count}\n"
        report += "</details>\n"

        self.log("Analysis complete.")
        return report
