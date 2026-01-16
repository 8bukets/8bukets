import json
import os
import argparse
import subprocess
import logging
import time
import threading
import sys
from datetime import datetime
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

RESULTS_DIR = "results"

class Spinner:
    def __init__(self, message="Processing..."):
        self.message = message
        self.stop_running = False
        self.thread = None

    def _spin(self):
        spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        idx = 0
        while not self.stop_running:
            sys.stderr.write(f"\r{spinner_chars[idx]} {self.message}")
            sys.stderr.flush()
            idx = (idx + 1) % len(spinner_chars)
            time.sleep(0.1)

    def start(self):
        self.stop_running = False
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()

    def stop(self):
        self.stop_running = True
        if self.thread:
            self.thread.join()
        sys.stderr.write(f"\r✅ {self.message} Done!          \n")
        sys.stderr.flush()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"❌ File {filepath} not found. Run scraper first.")
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
    logger.info(f"💾 Saved result to {filepath}")

def run_pipeline(skip_scrape=False):
    current_date = datetime.now().strftime('%Y-%m-%d')
    logger.info(f"🚀 Starting Pipeline for {current_date}...")

    # 1. Scrape
    if not skip_scrape:
        with Spinner("Running Scraper..."):
            try:
                subprocess.run(
                    ["python3", "scraper.py"],
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.PIPE
                )
            except subprocess.CalledProcessError as e:
                logger.error(f"❌ Scraper failed: {e}")
                if e.stderr:
                    logger.error(f"Detailed error: {e.stderr.decode('utf-8')}")
                return
    else:
        logger.info("⏩ Skipping scrape...")

    # 2. Load Data
    data = load_data("links.json")
    if not data:
        logger.warning("⚠️ No data to process.")
        return

    # 3. Instantiate Agents
    with Spinner("Initializing Agents..."):
        analysis_agent = AnalysisAgent()
        research_agent = ResearchAgent()
        intelligence_agent = IntelligenceAgent()
        content_agent = ContentAgent()
        health_agent = HealthCheckAgent()
        monetization_agent = MonetizationAgent()
        creativity_agent = CreativityAgent()
        ai_agent = AutonomousIntelligenceAgent()
        prog_ads_agent = ProgrammaticAdsAgent()
        ads_agent = AdsAgent()

    # 4. Pipeline Execution
    logger.info("🤖 Starting Agent Pipeline...")
    results_aggregator = {}

    # Helper to run agent with spinner
    def run_agent(agent, *args, label="Processing"):
        with Spinner(f"{label}..."):
            return agent.process(*args)

    # Health Check
    health_results = run_agent(health_agent, data, label="Health Check")
    save_result("health_check.json", health_results, current_date)
    results_aggregator['health'] = health_results

    if health_results['status'] != "Healthy" and health_results['record_count'] == 0:
        logger.error("❌ Data unhealthy or empty. Aborting pipeline.")
        return

    # Analysis
    analysis_results = run_agent(analysis_agent, data, label="Analyzing Data")
    save_result("analysis.json", analysis_results, current_date)

    # Research
    research_results = run_agent(research_agent, data, label="Researching")
    save_result("research.json", research_results, current_date)

    # Intelligence
    intelligence_results = run_agent(intelligence_agent, analysis_results, label="Gathering Intelligence")
    save_result("intelligence.json", intelligence_results, current_date)
    results_aggregator['intelligence'] = intelligence_results

    # Content
    content = run_agent(content_agent, data, intelligence_results, label="Generating Content")
    save_result("content_draft.md", content, current_date)

    # Monetization
    monetization_strategies = run_agent(monetization_agent, research_results, label="Planning Monetization")
    save_result("monetization.json", monetization_strategies, current_date)
    results_aggregator['monetization'] = monetization_strategies

    # Creativity
    headlines = run_agent(creativity_agent, analysis_results['common_keywords'], label="Brainstorming Headlines")
    save_result("creative_headlines.json", headlines, current_date)

    # Ads
    prog_ads = run_agent(prog_ads_agent, analysis_results['common_keywords'], label="Configuring Ads")
    save_result("programmatic_ads_config.json", prog_ads, current_date)

    ad_copy = run_agent(ads_agent, research_results, label="Writing Ad Copy")
    save_result("ad_copy.json", ad_copy, current_date)

    # High-level Synthesis
    summary = run_agent(ai_agent, results_aggregator, label="Synthesizing Summary")
    save_result("executive_summary.txt", summary, current_date)

    logger.info(f"✨ Pipeline Complete for {current_date}. Check 'results/' directory.")

def main():
    parser = argparse.ArgumentParser(description="Run Autonomous Agents System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip the scraping step")
    parser.add_argument("--daemon", action="store_true", help="Run continuously every day")
    parser.add_argument("--interval", type=int, default=86400, help="Interval in seconds (default 24h)")
    args = parser.parse_args()

    if args.daemon:
        logger.info(f"🕰️ Starting Daemon Mode. Running every {args.interval} seconds.")
        while True:
            try:
                run_pipeline(skip_scrape=args.skip_scrape)
            except Exception as e:
                logger.error(f"❌ Pipeline failed: {e}")

            logger.info(f"💤 Sleeping for {args.interval} seconds...")
            time.sleep(args.interval)
    else:
        run_pipeline(skip_scrape=args.skip_scrape)

if __name__ == "__main__":
    main()
