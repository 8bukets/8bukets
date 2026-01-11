"""
This module contains the ContentAgent class which is responsible for composing
and saving the final report based on the analysis from other agents.
"""
from datetime import datetime

from agents.base_agent import BaseAgent


class ContentAgent(BaseAgent):
    """
    Agent responsible for generating the final Markdown report.
    It aggregates data from all other agents and formats it into a readable report.
    """
    def __init__(self):
        super().__init__("Content")

    def _generate_ascii_bar(self, count, max_count, width=20):
        if max_count == 0:
            return ""
        filled = int((count / max_count) * width)
        bar_str = "█" * filled + "░" * (width - filled)
        return bar_str

    async def run(self, context: dict): # pylint: disable=too-many-locals, too-many-branches, too-many-statements
        self.log("Composing report...")
        analysis = context.get("analysis", {})
        insights = context.get("intelligence_insights", [])
        ideas = context.get("creative_ideas", [])
        monetization = context.get("monetization_ops", [])
        ad_strategies = context.get("ad_strategies", [])
        antigravity = context.get("antigravity", {})
        compliance = context.get("compliance", {})
        innovations = context.get("innovations", [])

        md = []
        md.append("# Autonomous Agents Report")
        md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Analysis Section
        md.append("\n## 1. Analysis")
        md.append(f"- Total Posts Scraped: {analysis.get('total_posts')}")
        date_stats = analysis.get('date_stats', {})
        md.append(f"- Date Range: {date_stats.get('start')} to {date_stats.get('end')}")

        if analysis.get('top_domains'):
            md.append("\n### Top Domains")
            max_count = analysis['top_domains'][0][1] if analysis['top_domains'] else 0
            md.append("| Domain | Count | Distribution |")
            md.append("|---|---|---|")
            for d, c in analysis['top_domains']:
                bar_str = self._generate_ascii_bar(c, max_count)
                md.append(f"| {d} | {c} | {bar_str} |")

        if analysis.get('top_categories'):
            md.append("\n### Top Categories")
            max_cat = analysis['top_categories'][0][1] if analysis['top_categories'] else 0
            md.append("| Category | Count | Distribution |")
            md.append("|---|---|---|")
            for c, count in analysis['top_categories']:
                bar_str = self._generate_ascii_bar(count, max_cat)
                md.append(f"| {c} | {count} | {bar_str} |")

        # Intelligence Section
        md.append("\n## 2. Intelligence Insights")
        for insight in insights:
            md.append(f"- {insight}")

        # Ad Strategy Section
        md.append("\n## 3. Advertising & Targeting (Autonomus Decisions)")
        if ad_strategies:
            for ad in ad_strategies:
                md.append(f"- **Target**: {ad['target_category']} | **Bid**: "
                          f"${ad['suggested_bid']} | **Copy**: \"{ad['ad_copy']}\"")
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
            shortest = len(antigravity.get('shortest_title', ''))
            longest = len(antigravity.get('longest_title', ''))
            md.append(f"- **Range**: Shortest title ({shortest} chars) to "
                      f"Longest ({longest} chars)")

        # Innovation Section
        md.append("\n## 6. System Innovation & Code Integration Ideas")
        if innovations:
            md.append("| Trigger | Idea | Complexity |")
            md.append("|---|---|---|")
            for inn in innovations:
                md.append(f"| {inn['trigger']} | {inn['idea']} | {inn['complexity']} |")
        else:
            md.append("No innovations generated this cycle.")

        # Monetization Section
        md.append("\n## 7. Monetization Opportunities")
        md.append(f"Found {len(monetization)} potential items.")

        if monetization:
            if len(monetization) > 10:
                md.append("\n<details>")
                md.append("<summary>Click to view all opportunities</summary>\n")

            md.append("\n| Title | Keywords | Link |")
            md.append("|---|---|---|")

            for op in monetization:
                md.append(f"| {op['title']} | {', '.join(op['keywords'])} | [Link]({op['link']}) |")

            if len(monetization) > 10:
                md.append("\n</details>")

        # Compliance Info
        md.append("\n## 8. Compliance")
        md.append(f"Robots.txt URL: {compliance.get('robots_txt_url')}")
        md.append(f"Disallowed paths found: {len(compliance.get('disallowed_paths', []))}")

        report_content = '\n'.join(md)
        output_file = "AGENTS_REPORT.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

        context["report_file"] = output_file
        self.log(f"Report saved to {output_file}")
