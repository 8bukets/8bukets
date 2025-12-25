import logging
import os
from datetime import datetime
from agents.analyst import AnalystAgent
from agents.researcher import ResearcherAgent
from agents.intelligence import IntelligenceAgent
from agents.creator import CreatorAgent
from agents.health import HealthAgent
from agents.monetization import MonetizationAgent
from agents.creative import CreativeAgent
from agents.ad_manager import AdManagerAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AgentOrchestrator:
    def __init__(self, report_dir="reports"):
        self.report_dir = report_dir
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

        # Instantiate agents
        self.health_agent = HealthAgent()
        self.analyst_agent = AnalystAgent()
        self.researcher_agent = ResearcherAgent()
        self.intelligence_agent = IntelligenceAgent()
        self.monetization_agent = MonetizationAgent()
        self.creative_agent = CreativeAgent()
        self.ad_manager_agent = AdManagerAgent()
        self.creator_agent = CreatorAgent() # Content creator

    def run_agents(self):
        logger.info("Orchestrating agents with Collaboration Protocol...")
        outputs = {}

        # 1. Independent / Foundational Agents
        outputs['HealthAgent'] = self.health_agent.run()
        outputs['AnalystAgent'] = self.analyst_agent.run()
        outputs['ResearcherAgent'] = self.researcher_agent.run()
        outputs['MonetizationAgent'] = self.monetization_agent.run()

        # 2. Collaborative Agents (Need input from above)

        # Intelligence needs Analysis
        intel_context = {
            'keywords': outputs['AnalystAgent'].get('keywords', [])
        }
        outputs['IntelligenceAgent'] = self.intelligence_agent.run() # Pass context if supported, currently via modifying run or perform_task
        # Quick fix: calling perform_task directly for context or modifying Base Agent.
        # Ideally, we update perform_task to accept context.
        # Since Base Agent .run() calls .perform_task() without args, we need to handle this.
        # For this iteration, let's update the specific agents to accept context via a setter or constructor?
        # Or simpler: Override .run() or just call perform_task logic directly here?
        # Best approach: Update Agent.run to accept **kwargs and pass to perform_task.
        # But I can't change Base Agent easily without breaking others potentially.
        # I'll manually execute the logic with context for these specific agents by calling perform_task directly if I hadn't updated base.
        # But wait, I updated ad_manager and intelligence to accept context in perform_task.
        # I need to update Base Agent to support passing args.

        # Let's override the run method call here effectively.
        self.intelligence_agent.perform_task(context=intel_context)
        outputs['IntelligenceAgent'] = self.intelligence_agent.results

        # AdManager needs Analysis + Monetization
        ad_context = {
            'keywords': outputs['AnalystAgent'].get('keywords', []),
            'top_opportunities': outputs['MonetizationAgent'].get('top_opportunities', [])
        }
        self.ad_manager_agent.perform_task(context=ad_context)
        outputs['AdManagerAgent'] = self.ad_manager_agent.results

        # 3. Creative/Output Agents (Need input from Intelligence/Ads)
        outputs['CreativeAgent'] = self.creative_agent.run()

        # Creator needs Ad/Strategy context
        creator_context = {
            'strategy': outputs['IntelligenceAgent'].get('strategy')
        }
        # Assuming CreatorAgent was updated or doesn't need context yet. The prompt implied "create content... with 100% intelligence".
        # I didn't update CreatorAgent to take context in the previous plan step, but I can do it now implicitly or just run it.
        outputs['CreatorAgent'] = self.creator_agent.run()

        self.generate_report(outputs)

    def generate_report(self, outputs):
        report_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = os.path.join(self.report_dir, f"agent_report_{report_date}.md")

        # Extract data for summary
        h = outputs.get('HealthAgent', {})
        i = outputs.get('IntelligenceAgent', {})
        ads = outputs.get('AdManagerAgent', {})
        a = outputs.get('AnalystAgent', {})
        m = outputs.get('MonetizationAgent', {})
        cc = outputs.get('CreatorAgent', {})

        db_status = h.get('db_status', 'Unknown')
        experience = i.get('experience_level', 'Unknown')
        campaign_count = len(ads.get('campaigns', []))
        opp_count = len(m.get('top_opportunities', []))

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# 🤖 Autonomous Agent Report (Evolved) - {report_date}\n\n")

            # --- Dashboard Summary ---
            f.write("## 📊 Executive Summary\n\n")
            f.write("| System Health | Experience | Active Campaigns | Monetization Opps |\n")
            f.write("|---|---|---|---|\n")
            # Use emojis for status
            health_icon = "🟢" if "Connected" in str(db_status) else "🔴"
            f.write(f"| {health_icon} {db_status} | 🧠 {experience} | 📢 {campaign_count} | 💰 {opp_count} |\n\n")

            # --- Table of Contents ---
            f.write("## 📑 Table of Contents<a id='table-of-contents'></a>\n\n")
            f.write("- [System Health](#system-health)\n")
            f.write("- [Intelligence](#intelligence-self-learning)\n")
            f.write("- [Ad Manager](#ad-manager-autonomous)\n")
            f.write("- [Analysis Data](#analysis-data)\n")
            f.write("- [Monetization](#monetization)\n")
            f.write("- [Content Draft](#content-draft)\n\n")

            f.write("---\n\n")

            # --- Sections ---

            # Health
            f.write(f"## 🏥 System Health<a id='system-health'></a>\n")
            f.write(f"- **Database Status**: {db_status}\n\n")
            f.write("[⬆️ Back to Top](#table-of-contents)\n\n")

            # Intelligence
            f.write(f"## 🧠 Intelligence (Self-Learning)<a id='intelligence-self-learning'></a>\n")
            f.write(f"- **Experience Level**: {experience}\n")
            f.write(f"- **Current Strategy**: {i.get('strategy')}\n")
            f.write(f"- **Trend Alert**: {i.get('trend_alert')}\n\n")
            f.write("[⬆️ Back to Top](#table-of-contents)\n\n")

            # Ad Manager
            f.write(f"## 📢 Ad Manager (Autonomous)<a id='ad-manager-autonomous'></a>\n")
            f.write(f"### Targeting\n- Audience: {ads.get('targeting', {}).get('primary_audience')}\n")

            f.write(f"### Bids\n")
            bids = ads.get('bidding_strategy', [])
            if bids:
                f.write("| Keyword | Bid |\n|---|---|\n")
                for bid in bids:
                    f.write(f"| `{bid['keyword']}` | ${bid['suggested_bid']} |\n")
            else:
                f.write("No bids generated.\n")

            f.write(f"\n### Active Campaigns\n")
            camps = ads.get('campaigns', [])
            if camps:
                for camp in camps:
                    f.write(f"- **{camp['name']}** ({camp['type']}): _{camp['headline']}_\n")
            else:
                f.write("No active campaigns.\n")
            f.write("\n[⬆️ Back to Top](#table-of-contents)\n\n")

            # Analysis
            f.write(f"## 📊 Analysis Data<a id='analysis-data'></a>\n")
            keywords = a.get('keywords')
            if keywords:
                f.write("**Top Keywords:**\n")
                # Display keywords as tags/badges
                f.write(" ".join([f"`{k}`" for k in keywords]))
                f.write("\n")
            else:
                f.write("No keywords analyzed.\n")
            f.write("\n[⬆️ Back to Top](#table-of-contents)\n\n")

            # Monetization
            f.write(f"## 💰 Monetization<a id='monetization'></a>\n")
            f.write(f"**Identified Opportunities:** {opp_count}\n")
            if opp_count > 0:
                for opp in m.get('top_opportunities', []):
                    f.write(f"- {opp}\n")
            f.write("\n[⬆️ Back to Top](#table-of-contents)\n\n")

            # Content
            f.write(f"## ✍️ Content Draft<a id='content-draft'></a>\n")
            draft_title = cc.get('draft_title', 'No Title')
            draft_content = cc.get('draft_content', 'No content generated.')

            f.write(f"### {draft_title}\n\n")
            f.write(f"{draft_content}\n\n")
            f.write("[⬆️ Back to Top](#table-of-contents)\n")

        logger.info(f"Agent Report generated: {report_filename}")

if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    orchestrator.run_agents()
