from .base import BaseAgent
from typing import Any, Dict
from datetime import datetime
import os

class ContentAgent(BaseAgent):
    def __init__(self, output_dir: str = "reports"):
        super().__init__("ContentAgent")
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    async def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self.log("Generating daily report...")

        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = os.path.join(self.output_dir, f"daily_report_{date_str}.md")

        health = context.get("health_status", {})
        analysis = context.get("analysis", {})
        intelligence = context.get("intelligence", {})
        monetization = context.get("monetization", {})
        creativity = context.get("creativity", {})

        md = []
        md.append(f"# Daily Agent Report - {date_str}")

        # Health
        md.append("\n## 🏥 Health Check")
        if health.get("is_healthy"):
            md.append(f"✅ **System Normal** - {health.get('url')} ({health.get('status_code')})")
        else:
            md.append(f"❌ **System Issue** - {health.get('url')} - {health.get('error') or health.get('status_code')}")

        # Analysis
        md.append("\n## 📊 Data Analysis")
        md.append(f"- **Total Posts Scraped:** {analysis.get('total_posts', 0)}")

        md.append("\n**Top Domains:**")
        for domain, count in analysis.get('top_domains', []):
            md.append(f"- {domain}: {count}")

        md.append("\n**Top Categories:**")
        for cat, count in analysis.get('top_categories', []):
            md.append(f"- {cat}: {count}")

        # Intelligence
        md.append("\n## 🧠 Intelligence & Trends")
        md.append("**Trending Keywords:**")
        keywords = ", ".join([f"{k} ({v})" for k, v in intelligence.get('top_keywords', [])])
        md.append(keywords if keywords else "No keywords found.")

        # Monetization
        md.append("\n## 💰 Monetization Opportunities")
        md.append(f"Found {monetization.get('opportunity_count', 0)} potential opportunities.")
        if monetization.get('top_opportunities'):
            md.append("\n| Title | Type | Link |")
            md.append("| :--- | :--- | :--- |")
            for opp in monetization.get('top_opportunities', []):
                md.append(f"| {opp.get('title')} | {opp.get('type')} | [Link]({opp.get('link')}) |")

        # Creativity
        md.append("\n## 🎨 Creative Ideas")
        for idea in creativity.get('generated_ideas', []):
            md.append(f"- 💡 {idea}")

        # Save
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md))

        self.log(f"Report saved to {filename}")
        return {"report_path": filename}
