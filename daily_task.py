import logging
import argparse
import time
import os
import shutil
import json
from datetime import datetime, timedelta

from agents.research import ResearchAgent
from agents.health import HealthCheckAgent
from agents.analyze import AnalyzeAgent
from agents.intelligence import IntelligenceAgent
from agents.monetization import MonetizationAgent
from agents.creativity import CreativityAgent
from agents.content import ContentAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_seconds_until_next_run(target_hour=6):
    now = datetime.now()
    target = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    if now >= target:
        target += timedelta(days=1)
    return (target - now).total_seconds()

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def run_job(max_pages=None):
    today = datetime.now().strftime('%Y-%m-%d')
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    report_file = os.path.join(report_dir, f"REPORT_{today}.md")
    json_file = "links.json"
    csv_file = "links.csv"
    txt_file = "unique_links.txt"
    prev_json_file = "links_prev.json"

    logger.info(f"--- Starting Autonomous Job for {today} ---")

    # Initialize Agents
    research_agent = ResearchAgent()
    health_agent = HealthCheckAgent()
    analyze_agent = AnalyzeAgent()
    intel_agent = IntelligenceAgent()
    money_agent = MonetizationAgent()
    creative_agent = CreativityAgent()
    content_agent = ContentAgent()

    # 0. Health Check (Pre-flight)
    if not health_agent.run(url="https://webshop.business.blog"):
        logger.error("Pre-flight health check failed. Aborting job.")
        # Decide whether to continue. For robustness, we might try anyway or alert.
        # Here we continue but log error.

    # Backup data
    if os.path.exists(json_file):
        shutil.copy(json_file, prev_json_file)

    # 1. Research (Scraping)
    success = research_agent.run(json_file, csv_file, txt_file, max_pages=max_pages)
    if not success:
        logger.warning("Research agent reported issues.")

    # 2. Health Check (Data)
    if not health_agent.run(data_file=json_file):
        logger.error("Data integrity check failed.")
        return

    # Load Data
    current_data = load_json(json_file)
    prev_data = load_json(prev_json_file) if os.path.exists(prev_json_file) else None

    # 3. Analyze
    stats = analyze_agent.run(current_data)

    # 4. Intelligence
    intel = intel_agent.run(current_data, prev_data)

    # 5. Monetization
    money_opps = money_agent.run(current_data)

    # 6. Creativity
    creative_ideas = creative_agent.run(intel.get('keywords', []))

    # 7. Content Creation
    content_agent.run(stats, intel, money_opps, creative_ideas, report_file)

    logger.info(f"--- Job Finished. Report: {report_file} ---")

def main():
    parser = argparse.ArgumentParser(description="Autonomous Multi-Agent System")
    parser.add_argument("--loop", action="store_true", help="Run continuously 24/7")
    parser.add_argument("--limit", type=int, help="Limit scraped pages")
    parser.add_argument("--hour", type=int, default=6, help="Hour to run (0-23)")
    args = parser.parse_args()

    if args.loop:
        logger.info(f"System starting in autonomous mode. Schedule: {args.hour}:00 daily.")
        while True:
            try:
                run_job(max_pages=args.limit)
            except Exception as e:
                logger.critical(f"System Crash: {e}")

            sleep_sec = get_seconds_until_next_run(args.hour)
            wake_time = (datetime.now() + timedelta(seconds=sleep_sec)).strftime('%Y-%m-%d %H:%M:%S')
            logger.info(f"Agents sleeping. Next cycle: {wake_time}")
            time.sleep(sleep_sec)
    else:
        run_job(max_pages=args.limit)

if __name__ == "__main__":
    main()
