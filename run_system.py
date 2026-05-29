import json
import os
import argparse
import subprocess
import logging
import time
import asyncio
from datetime import datetime
from oracle_ai_scraper import OracleAIScraper
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.content_agent import ContentAgent
from agents.health_check_agent import HealthCheckAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent
from agents.autonomous_intelligence_agent import AutonomousIntelligenceAgent
from agents.programmatic_ads_agent import ProgrammaticAdsAgent
from agents.ads_agent import AdsAgent
from agents.targeting_agent import TargetingAgent
from agents.bidding_agent import BiddingAgent
from agents.innovation_agent import InnovationAgent
from agents.developer_agent import DeveloperAgent
from agents.jules_orchestrator_agent import JulesIntelligenceAgent
from agents.oracle_ai_agent import OracleAIAgent
from agents.memory_system import MemorySystem

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

RESULTS_DIR = "results"

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File {filepath} not found. Run scraper first.")
        return []

def save_result(filename, content, date_str=None):
    os.makedirs(RESULTS_DIR, exist_ok=True)

    if date_str:
        filename = f"{date_str}_{filename}"

    filepath = os.path.join(RESULTS_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        if isinstance(content, (dict, list)):
            json.dump(content, f, indent=4)
        else:
            f.write(str(content))
    logger.info(f"Saved result to {filepath}")

def run_pipeline(skip_scrape=False):
    current_date = datetime.now().strftime('%Y-%m-%d')
    logger.info(f"Starting Pipeline for {current_date}...")

    # 0. Initialize Memory
    memory_system = MemorySystem()
    logger.info(f"Memory Loaded. Iteration: {memory_system.get('iterations')}")

    # 1. Scrape
    if not skip_scrape:
        logger.info("Starting Scraper...")
        subprocess.run(["python3", "scraper.py"], check=True)

        logger.info("Starting Oracle AI Scraper...")
        scraper = OracleAIScraper(output_json="oracle_ai_docs.json", output_md="oracle_ai_docs.md")
        asyncio.run(scraper.scrape())
    else:
        logger.info("Skipping scrape...")

    # 2. Load Data
    data = load_data("links.json")
    oracle_ai_data = load_data("oracle_ai_docs.json")

    # Update memory with Oracle AI knowledge
    if oracle_ai_data:
        memory_system.update("oracle_ai_knowledge", oracle_ai_data)
        logger.info("Loaded Oracle AI knowledge into memory.")

    if not data:
        logger.warning("No data to process.")
        return

    # 3. Instantiate Agents
    analysis_agent = AnalysisAgent()
    research_agent = ResearchAgent()
    intelligence_agent = IntelligenceAgent()
    content_agent = ContentAgent()
    health_agent = HealthCheckAgent()
    monetization_agent = MonetizationAgent()
    creativity_agent = CreativityAgent()
    ai_agent = AutonomousIntelligenceAgent()
    # ads_agent = AdsAgent() # Legacy, keeping if needed or replaced by specialized

    # New Specialized Agents
    targeting_agent = TargetingAgent()
    bidding_agent = BiddingAgent()
    innovation_agent = InnovationAgent()
    developer_agent = DeveloperAgent()
    jules_agent = JulesIntelligenceAgent()
    oracle_ai_agent = OracleAIAgent()

    # 4. Pipeline Execution
    logger.info("Starting Agent Pipeline...")
    results_aggregator = {}

    # Oracle AI Knowledge Processing
    if 'oracle_ai_data' in locals() and oracle_ai_data:
        oracle_agent_results = oracle_ai_agent.process(data=oracle_ai_data, memory_system=memory_system)
        results_aggregator['oracle_ai'] = oracle_agent_results
        save_result("oracle_ai_insights.json", oracle_agent_results, current_date)

    # Health Check
    health_results = health_agent.process(data)
    save_result("health_check.json", health_results, current_date)
    results_aggregator['health'] = health_results

    if health_results['status'] != "Healthy" and health_results['record_count'] == 0:
        logger.error("Data unhealthy or empty. Aborting pipeline.")
        return

    # Analysis
    analysis_results = analysis_agent.process(data)
    save_result("analysis.json", analysis_results, current_date)

    # Research
    research_results = research_agent.process(data, memory_system.memory)
    save_result("research.json", research_results, current_date)

    # Intelligence
    intelligence_results = intelligence_agent.process(analysis_results)
    save_result("intelligence.json", intelligence_results, current_date)
    results_aggregator['intelligence'] = intelligence_results

    # Targeting & Bidding (New)
    targeting_config = targeting_agent.process(analysis_results['common_keywords'], memory_system.memory)
    save_result("targeting_config.json", targeting_config, current_date)

    bidding_config = bidding_agent.process(targeting_config, memory_system.memory)
    save_result("bidding_config.json", bidding_config, current_date)

    # Content Generation with Innovation (Antigravity)
    base_content = content_agent.process(data, intelligence_results, memory_system.memory)
    final_content = innovation_agent.process(base_content, memory_system.memory)
    save_result("content_draft.md", final_content, current_date)

    # Code Generation (Developer Agent)
    code_snippets = developer_agent.process(research_results)
    save_result("developer_code.md", code_snippets, current_date)

    # Monetization
    monetization_strategies = monetization_agent.process(research_results)
    save_result("monetization.json", monetization_strategies, current_date)
    results_aggregator['monetization'] = monetization_strategies

    # Creativity
    headlines = creativity_agent.process(analysis_results['common_keywords'], memory_system.memory)
    save_result("creative_headlines.json", headlines, current_date)

    # Integrate Oracle AI Knowledge
    oracle_ai_knowledge = oracle_ai_agent.process(memory_system=memory_system)
    save_result("oracle_ai_knowledge.json", oracle_ai_knowledge, current_date)

    # High-level Synthesis
    summary = ai_agent.process(results_aggregator, memory_system.memory)
    save_result("executive_summary.txt", summary, current_date)

    # 5. Jules Intelligence (Evolution & Learning)
    # Analyze all results and update memory for next run
    jules_agent.process(memory_system, results_aggregator)

    logger.info(f"Pipeline Complete for {current_date}. Check 'results/' directory.")

def main():
    parser = argparse.ArgumentParser(description="Run Autonomous Agents System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip the scraping step")
    parser.add_argument("--daemon", action="store_true", help="Run continuously every day")
    parser.add_argument("--interval", type=int, default=86400, help="Interval in seconds (default 24h)")
    args = parser.parse_args()

    if args.daemon:
        logger.info(f"Starting Daemon Mode. Running every {args.interval} seconds.")
        while True:
            try:
                run_pipeline(skip_scrape=args.skip_scrape)
            except Exception as e:
                logger.error(f"Pipeline failed: {e}")

            logger.info(f"Sleeping for {args.interval} seconds...")
            time.sleep(args.interval)
    else:
        run_pipeline(skip_scrape=args.skip_scrape)

if __name__ == "__main__":
    main()
