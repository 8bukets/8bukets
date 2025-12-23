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
        self.agents = [
            HealthAgent(),
            AnalystAgent(),
            ResearcherAgent(),
            IntelligenceAgent(),
            MonetizationAgent(),
            CreativeAgent(),
            CreatorAgent()
        ]

    def run_agents(self):
        logger.info("Orchestrating agents...")
        agent_outputs = {}

        for agent in self.agents:
            logger.info(f"Running {agent.name}...")
            agent_outputs[agent.name] = agent.run()

        self.generate_report(agent_outputs)

    def generate_report(self, outputs):
        report_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = os.path.join(self.report_dir, f"agent_report_{report_date}.md")

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# 🤖 Autonomous Agent Report - {report_date}\n\n")

            # Health
            h = outputs.get('HealthAgent', {})
            f.write(f"## 🏥 System Health\n- DB Status: {h.get('db_status')} ({h.get('db_size')} bytes)\n- JSON Status: {h.get('json_status')}\n\n")

            # Analysis
            a = outputs.get('AnalystAgent', {})
            f.write(f"## 📊 Analysis\n- Total Posts: {a.get('total_posts')}\n- New Posts Today: {a.get('new_posts_count')}\n- Top Keywords: {a.get('keywords')}\n\n")

            # Research
            r = outputs.get('ResearcherAgent', {})
            f.write(f"## 🔬 Research (SEO)\n- Checked: {r.get('seo_checked')}\n- Rankings Found: {r.get('rankings_found')}\n- Top Rank: {r.get('top_rank')}\n\n")

            # Intelligence
            i = outputs.get('IntelligenceAgent', {})
            f.write(f"## 🧠 Intelligence\n- Strategy: {i.get('strategy')}\n- Trend Alert: {i.get('trend_alert')}\n\n")

            # Monetization
            m = outputs.get('MonetizationAgent', {})
            f.write(f"## 💰 Monetization\n- Opportunities Found: {m.get('opportunities_count')}\n- Top Picks: {m.get('top_opportunities')}\n\n")

            # Creativity
            c = outputs.get('CreativeAgent', {})
            f.write(f"## 🎨 Creativity\n- Brainstorm Ideas: {c.get('brainstorm')}\n\n")

            # Content
            cc = outputs.get('CreatorAgent', {})
            f.write(f"## ✍️ Content Draft\n**{cc.get('draft_title')}**\n\n{cc.get('draft_content')}\n\n")

        logger.info(f"Agent Report generated: {report_filename}")

if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    orchestrator.run_agents()
