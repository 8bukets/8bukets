from agents.base import BaseAgent
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentAgent")

    def run(self, stats, intel, money_opps, creative_ideas, output_file):
        logger.info(f"[{self.name}] Generating content report...")

        md = []
        md.append("# Webshop Autonomous Report")
        md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Insights
        md.append("\n## 🧠 Intelligence Brief")
        new_posts = intel.get('new_posts', [])
        if new_posts:
            md.append(f"**🚀 {len(new_posts)} New Posts Detected!**")
            for p in new_posts[:5]:
                md.append(f"- [{p.get('title', 'Untitled')}]({p.get('post_url')})")
        else:
            md.append("No new posts since last run.")

        md.append("\n### Trending Keywords")
        md.append("| Keyword | Frequency |")
        md.append("| :--- | :---: |")
        for kw, count in intel.get('keywords', []):
            md.append(f"| {kw} | {count} |")

        # Basic Stats
        md.append("\n## 📊 Statistical Analysis")
        md.append(f"- **Total Posts:** {stats.get('total_posts', 0)}")
        md.append(f"- **Date Range:** {stats.get('start_date', 'N/A')} to {stats.get('end_date', 'N/A')}")
        md.append(f"- **Unique Domains:** {stats.get('unique_domains', 0)}")

        md.append("\n### Top Categories")
        for cat, count in stats.get('categories', []):
            md.append(f"- {cat}: {count}")

        # Monetization
        md.append("\n## 💰 Monetization Opportunities")
        if money_opps:
            md.append(f"Found {len(money_opps)} potential revenue targets.")
            for opp in money_opps[:5]:
                md.append(f"- **{opp['type']}**: {opp['post']}")
        else:
            md.append("No obvious high-value targets found.")

        # Creativity
        md.append("\n## 🎨 Content Ideas")
        for idea in creative_ideas:
            md.append(f"- {idea}")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md))

        return output_file
