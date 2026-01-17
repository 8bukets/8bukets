from .base_agent import BaseAgent, AgentContext
from analytics import load_data, generate_report
import os

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("AnalysisAgent 📊")

    def run(self, context: AgentContext):
        json_file = context.get("scraped_json", "links.json")

        if not os.path.exists(json_file):
            self.log(context, f"Data file {json_file} not found. Skipping analysis.")
            return

        self.log(context, f"Analyzing data from {json_file}...")

        data = load_data(json_file)
        report_file = "REPORT.md"

        # We can reuse the analytics function but maybe we want to store stats in context too
        generate_report(data, report_file)

        # Extract some key metrics for other agents
        total_posts = len(data)
        context.set("total_posts", total_posts)
        context.set("report_file", report_file)

        # Identify top categories for the Creativity Agent
        categories = []
        for p in data:
            categories.extend(p.get('categories', []))

        if categories:
            from collections import Counter
            top_cats = [c[0] for c in Counter(categories).most_common(3)]
            context.set("top_trends", top_cats)
            self.log(context, f"Identified top trends: {', '.join(top_cats)}")

        self.log(context, "Analysis complete. Report generated.")
