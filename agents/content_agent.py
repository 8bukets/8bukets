from agents.base_agent import BaseAgent
from datetime import datetime

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content")

    async def run(self, context: dict):
        self.log("Composing report...")
        analysis = context.get("analysis", {})
        insights = context.get("intelligence_insights", [])
        ideas = context.get("creative_ideas", [])
        monetization = context.get("monetization_ops", [])

        md = []
        md.append("# Autonomous Agents Report")
        md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Analysis Section
        md.append("\n## 1. Analysis")
        md.append(f"- Total Posts Scraped: {analysis.get('total_posts')}")
        md.append(f"- Date Range: {analysis.get('date_stats', {}).get('start')} to {analysis.get('date_stats', {}).get('end')}")

        if analysis.get('top_domains'):
            md.append("\n### Top Domains")
            for d, c in analysis['top_domains']:
                md.append(f"- {d}: {c}")

        # Intelligence Section
        md.append("\n## 2. Intelligence Insights")
        for insight in insights:
            md.append(f"- {insight}")

        # Creativity Section
        md.append("\n## 3. Creative Ideas")
        for idea in ideas:
            md.append(f"- {idea}")

        # Monetization Section
        md.append("\n## 4. Monetization Opportunities")
        md.append(f"Found {len(monetization)} potential items.")
        if monetization:
            md.append("\n| Title | Keywords | Link |")
            md.append("|---|---|---|")
            for op in monetization[:10]: # Limit to 10
                md.append(f"| {op['title']} | {', '.join(op['keywords'])} | [Link]({op['link']}) |")

        report_content = '\n'.join(md)
        output_file = "AGENTS_REPORT.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

        context["report_file"] = output_file
        self.log(f"Report saved to {output_file}")
