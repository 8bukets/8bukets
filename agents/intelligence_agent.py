from .base_agent import BaseAgent
from .analyze_agent import AnalyzeAgent
from .research_agent import ResearchAgent
from .health_agent import HealthAgent
from .creativity_agent import CreativityAgent
from .content_agent import ContentAgent
from .monetization_agent import MonetizationAgent
from .ads_agent import AdsAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent (Orchestrator)")
        self.agents = {
            'health': HealthAgent(),
            'analyze': AnalyzeAgent(),
            'research': ResearchAgent(),
            'monetization': MonetizationAgent(),
            'creativity': CreativityAgent(),
            'content': ContentAgent(),
            'ads': AdsAgent()
        }

    def run(self, context):
        self.log("Initializing Autonomous System Sequence...")

        # 1. Health Check
        health_res = self.agents['health'].run(context)
        if not health_res['is_healthy']:
            self.log("CRITICAL: Site is unhealthy. Aborting sequence.")
            return

        # 2. Analyze
        analyze_res = self.agents['analyze'].run(context)
        context['top_keywords'] = analyze_res.get('top_keywords', [])

        # 3. Research
        self.agents['research'].run(context)

        # 4. Monetization
        self.agents['monetization'].run(context)

        # 5. Creativity (Requires Analysis)
        creative_res = self.agents['creativity'].run(context)
        context['ideas'] = creative_res.get('ideas', [])

        # 6. Content Creation
        self.agents['content'].run(context)

        # 7. Ads & Targeting
        self.agents['ads'].run(context)

        self.log("Autonomous sequence completed successfully.")

    def generate_robots_txt(self):
        """Generates an optimized robots.txt based on intelligence."""
        self.log("Generating Autonomous robots.txt...")
        content = """User-agent: *
Allow: /
Disallow: /wp-admin/

# Autonomously optimized for AdSense and Social Bots
User-agent: Mediapartners-Google
Allow: /
User-agent: GPTBot
Disallow: / # Optional: Decision by Intelligence Agent to protect IP?
"""
        return content
