import logging
import sys
from agents.base_agent import AgentContext
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent
from agents.monetization_agent import MonetizationAgent
from agents.ad_agent import AdAgent
from agents.health_agent import HealthAgent
from agents.intelligence_agent import IntelligenceAgent

# Setup logging with visual polish (if ColorFormatter exists from previous task, use it)
try:
    from scraper import ColorFormatter
    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter())
    logging.basicConfig(level=logging.INFO, handlers=[handler])
except ImportError:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    logger = logging.getLogger("System")
    logger.info("🤖 Initializing Autonomous Agent System...")

    # Initialize Context
    context = AgentContext()

    # Initialize Workers
    research = ResearchAgent()
    analysis = AnalysisAgent()
    creativity = CreativityAgent()
    content = ContentAgent()
    monetization = MonetizationAgent()
    ads = AdAgent()
    health = HealthAgent()

    # Initialize Intelligence (Orchestrator)
    # The order here defines the default sequential flow if IntelligenceAgent just iterates
    workers = [health, research, analysis, creativity, content, monetization, ads]
    brain = IntelligenceAgent(workers)

    # Run the System
    try:
        brain.run(context)
        logger.info("✅ Autonomous Cycle Finished Successfully.")
    except KeyboardInterrupt:
        logger.info("🛑 System stopped by user.")
    except Exception as e:
        logger.error(f"❌ Critical System Failure: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
