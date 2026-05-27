import os
import json
import logging
from datetime import datetime
from agents.analysis_agent import AnalysisAgent
from agents.health_agent import HealthCheckAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent
from agents.monetization_agent import MonetizationAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("SystemOrchestrator")

def main():
    logger.info("Starting Daily Autonomous Agent Run")

    # 1. Initialize Agents
    agents = [
        AnalysisAgent(),
        HealthCheckAgent(),
        ResearchAgent(),
        IntelligenceAgent(),
        CreativityAgent(),
        ContentAgent(),
        MonetizationAgent()
    ]

    # 2. Run Agents
    all_results = {}
    for agent in agents:
        try:
            agent.run()
            all_results[agent.name] = agent.get_results()
        except Exception as e:
            logger.error(f"Agent {agent.name} failed: {e}")
            all_results[agent.name] = {"error": str(e)}

    # 3. Compile Report
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_filename = f"results/DAILY_REPORT_{date_str}.md"

    generate_markdown_report(report_filename, all_results)
    logger.info(f"Daily run complete. Report saved to {report_filename}")

def generate_markdown_report(filename, results):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Daily Autonomous Report - {datetime.now().strftime('%Y-%m-%d')}\n\n")

        for agent_name, result in results.items():
            f.write(f"## {agent_name}\n")
            if "error" in result:
                f.write(f"**Error:** {result['error']}\n\n")
                continue

            for key, value in result.items():
                formatted_key = key.replace('_', ' ').title()
                if isinstance(value, list):
                    f.write(f"### {formatted_key}\n")
                    for item in value:
                        f.write(f"- {item}\n")
                elif isinstance(value, dict):
                    f.write(f"### {formatted_key}\n")
                    for k, v in value.items():
                        f.write(f"- **{k}**: {v}\n")
                else:
                    f.write(f"- **{formatted_key}**: {value}\n")
            f.write("\n---\n\n")

if __name__ == "__main__":
    main()
