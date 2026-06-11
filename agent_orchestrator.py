import logging
import os
import concurrent.futures
from datetime import datetime
from agents.analyst import AnalystAgent
from agents.researcher import ResearcherAgent
from agents.intelligence import IntelligenceAgent
from agents.creator import CreatorAgent
from agents.health import HealthAgent
from agents.monetization import MonetizationAgent
from agents.creative import CreativeAgent
from agents.ad_manager import AdManagerAgent
from agents.curiosity import CuriosityAgent

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
        self.curiosity_agent = CuriosityAgent() # New
        self.creative_agent = CreativeAgent()
        self.ad_manager_agent = AdManagerAgent()
        self.creator_agent = CreatorAgent()

    def run_agents(self):
        logger.info("Orchestrating agents with Collaboration Protocol...")
        outputs = {}

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Phase 1: Start Independent Agents
            # These can run in background immediately
            future_health = executor.submit(self.health_agent.run)
            future_researcher = executor.submit(self.researcher_agent.run)
            future_creator = executor.submit(self.creator_agent.run)
            future_curiosity = executor.submit(self.curiosity_agent.run)

            # Dependencies for Phase 2
            future_analyst = executor.submit(self.analyst_agent.run)
            future_monetization = executor.submit(self.monetization_agent.run)

            # Phase 2: Collect Dependencies (Wait for Analyst & Monetization)
            outputs['AnalystAgent'] = future_analyst.result()
            outputs['MonetizationAgent'] = future_monetization.result()

            # Phase 3: Start Dependent Agents

            # Intelligence depends on Analyst
            intel_context = {'keywords': outputs['AnalystAgent'].get('keywords', [])}
            def run_intelligence(context):
                self.intelligence_agent.perform_task(context=context)
                return self.intelligence_agent.results
            future_intelligence = executor.submit(run_intelligence, intel_context)

            # AdManager depends on Analyst + Monetization
            ad_context = {
                'keywords': outputs['AnalystAgent'].get('keywords', []),
                'top_opportunities': outputs['MonetizationAgent'].get('top_opportunities', [])
            }
            def run_ad_manager(context):
                self.ad_manager_agent.perform_task(context=context)
                return self.ad_manager_agent.results
            future_ad_manager = executor.submit(run_ad_manager, ad_context)

            # Phase 4: Wait for Curiosity (needed for Creative)
            outputs['CuriosityAgent'] = future_curiosity.result()

            # Phase 5: Start Creative (depends on Curiosity)
            creative_context = {
                'curiosity_findings': outputs['CuriosityAgent'].get('findings', []),
                'exploration_query': outputs['CuriosityAgent'].get('exploration_query', '')
            }
            def run_creative(context):
                self.creative_agent.perform_task(context=context)
                return self.creative_agent.results
            future_creative = executor.submit(run_creative, creative_context)

            # Phase 6: Final Collection
            outputs['HealthAgent'] = future_health.result()
            outputs['ResearcherAgent'] = future_researcher.result()
            outputs['CreatorAgent'] = future_creator.result()
            outputs['IntelligenceAgent'] = future_intelligence.result()
            outputs['AdManagerAgent'] = future_ad_manager.result()
            outputs['CreativeAgent'] = future_creative.result()

        self.generate_report(outputs)

    def generate_report(self, outputs):
        report_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = os.path.join(self.report_dir, f"agent_report_{report_date}.md")

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# 🤖 Autonomous Agent Report (Evolved v2) - {report_date}\n\n")

            # Data preparation
            h = outputs.get('HealthAgent', {})
            m = outputs.get('MonetizationAgent', {})
            ads = outputs.get('AdManagerAgent', {})
            crt = outputs.get('CreativeAgent', {})

            # Summary Table
            f.write("## 📊 Executive Summary\n")
            f.write("| Metric | Status | Details |\n")
            f.write("| :--- | :--- | :--- |\n")

            db_icon = "✅" if h.get('db_status') == "OK" else "❌"
            f.write(f"| **System Health** | {db_icon} {h.get('db_status')} | DB Size: {h.get('db_size', 0)/1024:.1f} KB |\n")

            ops_count = len(m.get('top_opportunities', []))
            f.write(f"| **Monetization** | 💰 {ops_count} Ops | Top 3 listed below |\n")

            camp_count = len(ads.get('campaigns', []))
            f.write(f"| **Ad Campaigns** | 📢 {camp_count} Active | Strategy Active |\n\n")

            # Health
            f.write(f"## 🏥 System Health\n")
            f.write(f"- **Database Status**: {db_icon} {h.get('db_status')}\n")
            json_status = h.get('json_status', 'Unknown')
            json_icon = "✅" if json_status == "OK" else "❌"
            f.write(f"- **Scraper Data**: {json_icon} {json_status}\n\n")

            # Intelligence
            i = outputs.get('IntelligenceAgent', {})
            f.write(f"## 🧠 Intelligence\n")
            f.write(f"- **Strategy**: {i.get('strategy')}\n")
            f.write(f"- **Trend Alert**: {i.get('trend_alert')}\n\n")

            # Curiosity & Innovation
            cur = outputs.get('CuriosityAgent', {})
            f.write(f"## 🌌 Curiosity & Innovation (Google Antigravity Mode)\n")
            f.write(f"- **Explored**: `{cur.get('exploration_query')}`\n")
            f.write(f"- **Findings**: {cur.get('findings')}\n")

            ideas = crt.get('system_improvement_ideas', [])
            if ideas:
                f.write(f"### 💡 High Solution Interest Ideas\n")
                f.write(f"<details><summary>View {len(ideas)} Ideas</summary>\n\n")
                for idea in ideas:
                    f.write(f"- 🛠️ {idea}\n")
                f.write("\n</details>\n\n")
            else:
                f.write(f"### 💡 High Solution Interest Ideas\n*No new ideas generated.*\n\n")

            # Ad Manager
            f.write(f"## 📢 Ad Manager\n")
            campaigns = ads.get('campaigns', [])
            if campaigns:
                f.write(f"### Active Campaigns\n")
                f.write(f"<details><summary>View {len(campaigns)} Campaigns</summary>\n\n")
                for camp in campaigns:
                    f.write(f"- **{camp['name']}**: {camp['headline']} ({camp['type']})\n")
                f.write("\n</details>\n\n")
            else:
                f.write("No active campaigns.\n\n")

            # Monetization
            f.write(f"## 💰 Monetization\n")
            f.write(f"- **Total Opportunities**: {m.get('opportunities_count', 0)}\n")
            top_ops = m.get('top_opportunities', [])
            if top_ops:
                f.write(f"- **Top 3 Opportunities**:\n")
                for op in top_ops:
                    f.write(f"  - [{op['title']}]({op['url']})\n")
            f.write("\n")

            # Content
            cc = outputs.get('CreatorAgent', {})
            f.write(f"## ✍️ Content Draft\n")
            f.write(f"### {cc.get('draft_title')}\n\n")
            f.write(f"{cc.get('draft_content')}\n\n")

        logger.info(f"Agent Report generated: {report_filename}")

if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    orchestrator.run_agents()
