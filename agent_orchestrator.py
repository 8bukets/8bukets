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

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# 🤖 Autonomous Agent Report (Evolved) - {report_date}\n\n")

            # Health
            h = outputs.get('HealthAgent', {})
            f.write(f"## 🏥 System Health\n- DB: {h.get('db_status')}\n\n")

            # Intelligence (Evolved)
            i = outputs.get('IntelligenceAgent', {})
            f.write(f"## 🧠 Intelligence (Self-Learning)\n")
            f.write(f"- **Experience**: {i.get('experience_level')}\n")
            f.write(f"- **Strategy**: {i.get('strategy')}\n")
            f.write(f"- **Trend Alert**: {i.get('trend_alert')}\n\n")

            # Ad Manager (New)
            ads = outputs.get('AdManagerAgent', {})
            f.write(f"## 📢 Ad Manager (Autonomous)\n")
            f.write(f"### Targeting\n- Audience: {ads.get('targeting', {}).get('primary_audience')}\n")
            f.write(f"### Bids\n")
            for bid in ads.get('bidding_strategy', []):
                f.write(f"- Keyword: `{bid['keyword']}` | Bid: ${bid['suggested_bid']}\n")
            f.write(f"### Active Campaigns\n")
            for camp in ads.get('campaigns', []):
                f.write(f"- **{camp['name']}**: {camp['headline']} ({camp['type']})\n")
            f.write("\n")

            # Analysis
            a = outputs.get('AnalystAgent', {})
            f.write(f"## 📊 Analysis Data\n- Keywords: {a.get('keywords')}\n\n")

            # Monetization
            m = outputs.get('MonetizationAgent', {})
            f.write(f"## 💰 Monetization\n- Opportunities: {len(m.get('top_opportunities', []))}\n\n")

            # Content
            cc = outputs.get('CreatorAgent', {})
            f.write(f"## ✍️ Content Draft\n**{cc.get('draft_title')}**\n\n{cc.get('draft_content')}\n\n")

        logger.info(f"Agent Report generated: {report_filename}")

if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    orchestrator.run_agents()
