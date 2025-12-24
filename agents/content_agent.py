from agents.base_agent import BaseAgent
from datetime import datetime
import html
import os

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

        # Generate Markdown (Original Logic)
        md = ["# Autonomous Agents Report", f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]
        md.append("\n## 1. Analysis")
        md.append(f"- Total Posts Scraped: {analysis.get('total_posts')}")
        md.append(f"- Date Range: {analysis.get('date_stats', {}).get('start')} to {analysis.get('date_stats', {}).get('end')}")
        if analysis.get('top_domains'):
            md.append("\n### Top Domains")
            for d, c in analysis['top_domains']: md.append(f"- {d}: {c}")

        md.append("\n## 2. Intelligence Insights")
        for insight in insights: md.append(f"- {insight}")

        md.append("\n## 3. Advertising & Targeting (Autonomus Decisions)")
        if ad_strategies:
            for ad in ad_strategies: md.append(f"- **Target**: {ad['target_category']} | **Bid**: ${ad['suggested_bid']} | **Copy**: \"{ad['ad_copy']}\"")
        else: md.append("No ad strategies generated.")

        md.append("\n## 4. Creative Ideas")
        for idea in ideas: md.append(f"- {idea}")

        if antigravity:
            md.append("\n## 5. Google Antigravity & Fun")
            md.append(f"- **Hidden Gem**: {antigravity.get('hidden_gem')}")
            md.append(f"- **Range**: Shortest title ({len(antigravity.get('shortest_title',''))} chars) to Longest ({len(antigravity.get('longest_title',''))} chars)")

        md.append("\n## 6. Monetization Opportunities")
        md.append(f"Found {len(monetization)} potential items.")
        if monetization:
            md.append("\n| Title | Keywords | Link |")
            md.append("|---|---|---|")
            for op in monetization[:10]: md.append(f"| {op['title']} | {', '.join(op['keywords'])} | [Link]({op['link']}) |")

        md.append("\n## 7. Compliance")
        md.append(f"Robots.txt URL: {compliance.get('robots_txt_url')}")
        md.append(f"Disallowed paths found: {len(compliance.get('disallowed_paths', []))}")

        with open("AGENTS_REPORT.md", 'w', encoding='utf-8') as f:
            f.write('\n'.join(md))
        context["report_file"] = "AGENTS_REPORT.md"
        self.log("Report saved to AGENTS_REPORT.md")

        # Generate HTML Report (Palette UX Enhancement)
        try:
            self.generate_html_report(context)
        except Exception as e:
            self.log(f"Failed to generate HTML report: {e}")

    def generate_html_report(self, context):
        with open(os.path.join("templates", "report.html"), "r", encoding="utf-8") as f:
            template = f.read()

        an = context.get("analysis", {})
        ag = context.get("antigravity", {})
        now = datetime.now()

        # Helper to format list items
        fmt_list = lambda items: "".join([f"<li>{html.escape(str(i))}</li>" for i in items])

        # Prepare Ads Section
        ads_html = ""
        for ad in context.get("ad_strategies", []):
            ads_html += f"<div class='stat-card' style='margin-bottom:1rem;'><span class='tag badge-ad'>Strategy</span><p><strong>Target:</strong> {html.escape(ad.get('target_category',''))}</p><p><strong>Bid:</strong> ${ad.get('suggested_bid',0)}</p><p><strong>Copy:</strong> <em>\"{html.escape(ad.get('ad_copy',''))}\"</em></p></div>"
        if not ads_html: ads_html = "<p>No ad strategies generated.</p>"

        # Prepare Monetization Rows
        mon_rows = ""
        for op in context.get("monetization_ops", [])[:15]:
            kws = ", ".join([f"<span class='tag'>{k}</span>" for k in op.get('keywords', [])])
            mon_rows += f"<tr><td>{html.escape(op.get('title',''))}</td><td>{kws}</td><td><a href='{op.get('link','#')}' target='_blank'>Visit <span aria-hidden='true'>→</span></a></td></tr>"
        if not mon_rows: mon_rows = "<tr><td colspan='3'>No opportunities found.</td></tr>"

        replacements = {
            "{{ISOTIMESTAMP}}": now.isoformat(),
            "{{TIMESTAMP}}": now.strftime('%Y-%m-%d %H:%M:%S'),
            "{{TOTAL_POSTS}}": str(an.get('total_posts', 0)),
            "{{DISALLOWED_PATHS}}": str(len(context.get('compliance', {}).get('disallowed_paths', []))),
            "{{DATE_START}}": str(an.get('date_stats', {}).get('start')),
            "{{DATE_END}}": str(an.get('date_stats', {}).get('end')),
            "{{TOP_DOMAINS_LIST}}": "".join([f"<li><strong>{d}</strong>: {c}</li>" for d, c in an.get('top_domains', [])]),
            "{{INSIGHTS_LIST}}": fmt_list(context.get("intelligence_insights", [])),
            "{{ADS_SECTION}}": ads_html,
            "{{IDEAS_LIST}}": fmt_list(context.get("creative_ideas", [])),
            "{{ANTIGRAVITY_GEM}}": html.escape(str(ag.get('hidden_gem', 'None'))),
            "{{ANTIGRAVITY_SHORT}}": str(len(ag.get('shortest_title',''))),
            "{{ANTIGRAVITY_LONG}}": str(len(ag.get('longest_title',''))),
            "{{MONETIZATION_COUNT}}": str(len(context.get("monetization_ops", []))),
            "{{MONETIZATION_ROWS}}": mon_rows
        }

        for key, val in replacements.items():
            template = template.replace(key, val)

        with open("AGENTS_REPORT.html", "w", encoding="utf-8") as f:
            f.write(template)
        self.log("HTML Report saved to AGENTS_REPORT.html")
