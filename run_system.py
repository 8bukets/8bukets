import json
import os
import sys
import argparse
import subprocess
import logging
import time
from datetime import datetime
from agents.base_agent import Colors
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', stream=sys.stdout)
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
    return filepath

def print_summary(generated_files):
    """
    Prints a summary box with the list of generated files.
    """
    if not generated_files:
        return

    title = "🎨 EXECUTION SUMMARY"
    width = 60

    # Border characters
    TL, TR = "╭", "╮"
    BL, BR = "╰", "╯"
    H, V = "─", "│"

    print(f"\n{Colors.colorize(TL + H * (width - 2) + TR, Colors.BOLD)}")
    print(f"{V} {Colors.colorize(title.center(width - 4), Colors.HEADER)} {V}")
    print(f"{Colors.colorize(V + H * (width - 2) + V, Colors.BOLD)}")

    for file_info in generated_files:
        # Truncate filename if it's too long
        fname = file_info['name']
        status = file_info['status']

        # Calculate padding
        max_fname_len = width - 15
        if len(fname) > max_fname_len:
            display_name = fname[:max_fname_len-3] + "..."
        else:
            display_name = fname

        status_color = Colors.GREEN if status == "Saved" else Colors.FAIL
        status_text = Colors.colorize("✔ Saved", status_color) if status == "Saved" else Colors.colorize("✘ Failed", status_color)

        # Need to handle length calculation without ANSI codes for alignment
        # padding = width - 4 - len(display_name) - 7 (for "Saved") - 2 (space)
        # But "✔ Saved" has length 7 visually.

        padding = width - 4 - len(display_name) - 7
        spaces = " " * padding

        print(f"{V} {display_name}{spaces}{status_text} {V}")

    print(f"{Colors.colorize(BL + H * (width - 2) + BR, Colors.BOLD)}\n")

def run_pipeline(skip_scrape=False):
    current_date = datetime.now().strftime('%Y-%m-%d')
    logger.info(f"Starting Pipeline for {current_date}...")

    # 1. Scrape
    if not skip_scrape:
        logger.info("Starting Scraper...")
        subprocess.run(["python3", "scraper.py"], check=True)
    else:
        logger.info("Skipping scrape...")

    # 2. Load Data
    data = load_data("links.json")
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
    prog_ads_agent = ProgrammaticAdsAgent()
    ads_agent = AdsAgent()

    # 4. Pipeline Execution
    logger.info("Starting Agent Pipeline...")
    results_aggregator = {}
    generated_files = []

    # Health Check
    health_results = health_agent.process(data)
    fp = save_result("health_check.json", health_results, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})
    results_aggregator['health'] = health_results

    if health_results['status'] != "Healthy" and health_results['record_count'] == 0:
        logger.error("Data unhealthy or empty. Aborting pipeline.")
        return

    # Analysis
    analysis_results = analysis_agent.process(data)
    fp = save_result("analysis.json", analysis_results, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})

    # Research
    research_results = research_agent.process(data)
    fp = save_result("research.json", research_results, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})

    # Intelligence
    intelligence_results = intelligence_agent.process(analysis_results)
    fp = save_result("intelligence.json", intelligence_results, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})
    results_aggregator['intelligence'] = intelligence_results

    # Content
    content = content_agent.process(data, intelligence_results)
    fp = save_result("content_draft.md", content, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})

    # Monetization
    monetization_strategies = monetization_agent.process(research_results)
    fp = save_result("monetization.json", monetization_strategies, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})
    results_aggregator['monetization'] = monetization_strategies

    # Creativity
    headlines = creativity_agent.process(analysis_results['common_keywords'])
    fp = save_result("creative_headlines.json", headlines, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})

    # Ads
    prog_ads = prog_ads_agent.process(analysis_results['common_keywords'])
    fp = save_result("programmatic_ads_config.json", prog_ads, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})

    ad_copy = ads_agent.process(research_results)
    fp = save_result("ad_copy.json", ad_copy, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})

    # High-level Synthesis
    summary = ai_agent.process(results_aggregator)
    fp = save_result("executive_summary.txt", summary, current_date)
    generated_files.append({"name": os.path.basename(fp), "status": "Saved"})

    logger.info(f"Pipeline Complete for {current_date}. Check 'results/' directory.")
    print_summary(generated_files)

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
