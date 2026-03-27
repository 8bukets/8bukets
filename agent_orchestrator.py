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

        # 1. Independent / Foundational Agents
        outputs['HealthAgent'] = self.health_agent.run()
        outputs['AnalystAgent'] = self.analyst_agent.run()
        outputs['ResearcherAgent'] = self.researcher_agent.run()
        outputs['MonetizationAgent'] = self.monetization_agent.run()

        # 2. Collaborative Agents

        # Intelligence
        intel_context = {'keywords': outputs['AnalystAgent'].get('keywords', [])}
        self.intelligence_agent.perform_task(context=intel_context)
        outputs['IntelligenceAgent'] = self.intelligence_agent.results

        # AdManager
        ad_context = {
            'keywords': outputs['AnalystAgent'].get('keywords', []),
            'top_opportunities': outputs['MonetizationAgent'].get('top_opportunities', [])
        }
        self.ad_manager_agent.perform_task(context=ad_context)
        outputs['AdManagerAgent'] = self.ad_manager_agent.results

        # Curiosity (Exploration)
        # Needs no input, but uses DB.
        outputs['CuriosityAgent'] = self.curiosity_agent.run()

        # Creative (Innovation)
        # Needs Curiosity context
        creative_context = {
            'curiosity_findings': outputs['CuriosityAgent'].get('findings', []),
            'exploration_query': outputs['CuriosityAgent'].get('exploration_query', '')
        }
        self.creative_agent.perform_task(context=creative_context)
        outputs['CreativeAgent'] = self.creative_agent.results

        # Creator (Content)
        # Creator needs Ad/Strategy context
        # Ideally we pass Strategy here too
        outputs['CreatorAgent'] = self.creator_agent.run()

        self.generate_report(outputs)

    def generate_report(self, outputs):
        report_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = os.path.join(self.report_dir, f"agent_report_{report_date}.md")

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# 🤖 Autonomous Agent Report (Evolved v2) - {report_date}\n\n")

            # Table of Contents
            f.write("## Table of Contents\n\n")
            f.write("- [🏥 System Health](#system-health)\n")
            f.write("- [🧠 Intelligence](#intelligence)\n")
            f.write("- [🌌 Curiosity & Innovation](#curiosity-innovation)\n")
            f.write("- [📢 Ad Manager](#ad-manager)\n")
            f.write("- [💰 Monetization](#monetization)\n")
            f.write("- [✍️ Content Draft](#content-draft)\n\n")

            # Health
            h = outputs.get('HealthAgent', {})
            f.write(f"## <a id=\"system-health\"></a>🏥 System Health\n- DB: {h.get('db_status')}\n\n")

            # Intelligence
            i = outputs.get('IntelligenceAgent', {})
            f.write(f"## <a id=\"intelligence\"></a>🧠 Intelligence\n")
            f.write(f"- **Strategy**: {i.get('strategy')}\n")
            f.write(f"- **Trend Alert**: {i.get('trend_alert')}\n\n")

            # Curiosity & Innovation
            cur = outputs.get('CuriosityAgent', {})
            crt = outputs.get('CreativeAgent', {})
            f.write(f"## <a id=\"curiosity-innovation\"></a>🌌 Curiosity & Innovation (Google Antigravity Mode)\n")
            f.write(f"- **Explored**: '{cur.get('exploration_query')}'\n")
            f.write(f"- **Findings**: {cur.get('findings')}\n")
            f.write(f"### 💡 High Solution Interest Ideas\n")
            for idea in crt.get('system_improvement_ideas', []):
                f.write(f"- 🛠️ {idea}\n")
            f.write("\n")

            # Ad Manager
            ads = outputs.get('AdManagerAgent', {})
            f.write(f"## <a id=\"ad-manager\"></a>📢 Ad Manager\n")
            f.write(f"### Active Campaigns\n")
            for camp in ads.get('campaigns', []):
                f.write(f"- **{camp['name']}**: {camp['headline']} ({camp['type']})\n")
            f.write("\n")

            # Monetization
            m = outputs.get('MonetizationAgent', {})
            f.write(f"## <a id=\"monetization\"></a>💰 Monetization\n- Opportunities: {len(m.get('top_opportunities', []))}\n\n")

            # Content
            cc = outputs.get('CreatorAgent', {})
            f.write(f"## <a id=\"content-draft\"></a>✍️ Content Draft\n**{cc.get('draft_title')}**\n\n{cc.get('draft_content')}\n\n")

        logger.info(f"Agent Report generated: {report_filename}")

if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    orchestrator.run_agents()
