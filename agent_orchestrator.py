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
