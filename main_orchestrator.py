import logging
import sys
from agents.researcher import ResearcherAgent
from agents.analyzer import AnalyzerAgent
from agents.intelligence import IntelligenceAgent
from agents.content_creator import ContentCreatorAgent
from agents.health_check import HealthCheckAgent
from agents.monetization import MonetizationAgent
from agents.creativity import CreativityAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("Orchestrator")

def run_orchestration():
    logger.info(">>> STARTING AUTONOMOUS AGENT SWARM <<<")

    # 1. Health Check
    health_agent = HealthCheckAgent()
    health_status = health_agent.run()
    logger.info(f"Health Status: {health_status}")

    if health_status.get("status") != "healthy":
        logger.error("Target site is unhealthy. Aborting operation.")
        return

    # 2. Research
    research_agent = ResearcherAgent()
    # Limit to 2 pages for quick demonstration
    raw_data = research_agent.run({"limit": 2})

    if not raw_data:
        logger.warning("No data scraped.")
        return

    # 3. Analyze
    analyzer_agent = AnalyzerAgent()
    analysis_result = analyzer_agent.run(raw_data)

    # 4. Intelligence
    intelligence_agent = IntelligenceAgent()
    intelligence_result = intelligence_agent.run(analysis_result)
    logger.info(f"Strategic Insight: {intelligence_result.get('recommended_focus')}")

    # 5. Creativity
    creativity_agent = CreativityAgent()
    creative_result = creativity_agent.run(analysis_result)
    for idea in creative_result.get("creative_ideas", []):
        logger.info(f"Creative Idea: {idea}")

    # 6. Monetization
    monetization_agent = MonetizationAgent()
    monetization_result = monetization_agent.run(raw_data)
    logger.info(f"Monetization Summary: {monetization_result.get('summary')}")

    # 7. Create Content
    content_agent = ContentCreatorAgent()
    content_draft = content_agent.run(intelligence_result)

    # Output Draft
    with open("agent_generated_draft.md", "w") as f:
        f.write(content_draft.get("draft_content", ""))
    logger.info("Content draft saved to agent_generated_draft.md")

    logger.info(">>> SWARM OPERATION COMPLETE <<<")

if __name__ == "__main__":
    run_orchestration()
