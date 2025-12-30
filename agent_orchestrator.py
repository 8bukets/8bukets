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

    def sanitize_markdown(self, text):
        """Sanitize text to prevent Markdown injection."""
        if not isinstance(text, str):
            return text
        # Escape Markdown characters that could change formatting or create links
        # We focus on characters that create links or structure
        # [ ] ( ) < > * _ ` #
        # But for readability, let's stick to key ones that allow malicious links or scripts
        # [link](url) -> \[link\]\(url\)
        # <script> -> &lt;script&gt;

        # Simple implementation: escape special characters
        escape_chars = ['[', ']', '(', ')', '<', '>', '*', '_', '`', '#', '|']
        sanitized = text
        for char in escape_chars:
            sanitized = sanitized.replace(char, f"\\{char}")
        return sanitized

    def generate_report(self, outputs):
        report_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = os.path.join(self.report_dir, f"agent_report_{report_date}.md")

        def s(text):
            if isinstance(text, list):
                return [self.sanitize_markdown(str(item)) for item in text]
            return self.sanitize_markdown(str(text)) if text is not None else "None"

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# 🤖 Autonomous Agent Report (Evolved v2) - {report_date}\n\n")

            # Health
            h = outputs.get('HealthAgent', {})
            f.write(f"## 🏥 System Health\n- DB: {s(h.get('db_status'))}\n\n")

            # Intelligence
            i = outputs.get('IntelligenceAgent', {})
            f.write(f"## 🧠 Intelligence\n")
            f.write(f"- **Strategy**: {s(i.get('strategy'))}\n")
            f.write(f"- **Trend Alert**: {s(i.get('trend_alert'))}\n\n")

            # Curiosity & Innovation
            cur = outputs.get('CuriosityAgent', {})
            crt = outputs.get('CreativeAgent', {})
            f.write(f"## 🌌 Curiosity & Innovation (Google Antigravity Mode)\n")
            f.write(f"- **Explored**: '{s(cur.get('exploration_query'))}'\n")
            f.write(f"- **Findings**: {s(cur.get('findings'))}\n")
            f.write(f"### 💡 High Solution Interest Ideas\n")
            for idea in crt.get('system_improvement_ideas', []):
                f.write(f"- 🛠️ {s(idea)}\n")
            f.write("\n")

            # Ad Manager
            ads = outputs.get('AdManagerAgent', {})
            f.write(f"## 📢 Ad Manager\n")
            f.write(f"### Active Campaigns\n")
            for camp in ads.get('campaigns', []):
                f.write(f"- **{s(camp['name'])}**: {s(camp['headline'])} ({s(camp['type'])})\n")
            f.write("\n")

            # Monetization
            m = outputs.get('MonetizationAgent', {})
            f.write(f"## 💰 Monetization\n- Opportunities: {len(m.get('top_opportunities', []))}\n\n")

            # Content
            cc = outputs.get('CreatorAgent', {})
            f.write(f"## ✍️ Content Draft\n**{s(cc.get('draft_title'))}**\n\n{s(cc.get('draft_content'))}\n\n")

        logger.info(f"Agent Report generated: {report_filename}")

if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    orchestrator.run_agents()
