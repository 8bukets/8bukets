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
        ad_strategies = context.get("ad_strategies", [])
        antigravity = context.get("antigravity", {})
        compliance = context.get("compliance", {})

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

        # Ad Strategy Section
        md.append("\n## 3. Advertising & Targeting (Autonomus Decisions)")
        if ad_strategies:
            for ad in ad_strategies:
                md.append(f"- **Target**: {ad['target_category']} | **Bid**: ${ad['suggested_bid']} | **Copy**: \"{ad['ad_copy']}\"")
        else:
            md.append("No ad strategies generated.")

        # Creativity Section
        md.append("\n## 4. Creative Ideas")
        for idea in ideas:
            md.append(f"- {idea}")

        # Antigravity Section
        if antigravity:
            md.append("\n## 5. Google Antigravity & Fun")
            md.append(f"- **Hidden Gem**: {antigravity.get('hidden_gem')}")
            md.append(f"- **Range**: Shortest title ({len(antigravity.get('shortest_title',''))} chars) to Longest ({len(antigravity.get('longest_title',''))} chars)")

        # Monetization Section
        md.append("\n## 6. Monetization Opportunities")
        md.append(f"Found {len(monetization)} potential items.")
        if monetization:
            md.append("\n| Title | Keywords | Link |")
            md.append("|---|---|---|")
            for op in monetization[:10]: # Limit to 10
                md.append(f"| {op['title']} | {', '.join(op['keywords'])} | [Link]({op['link']}) |")

        # Compliance Info
        md.append("\n## 7. Compliance")
        md.append(f"Robots.txt URL: {compliance.get('robots_txt_url')}")
        md.append(f"Disallowed paths found: {len(compliance.get('disallowed_paths', []))}")

        report_content = '\n'.join(md)
        output_file = "AGENTS_REPORT.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

        context["report_file"] = output_file
        self.log(f"Report saved to {output_file}")
