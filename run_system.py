import asyncio
import json
import os
import argparse
import sys
from datetime import datetime
from typing import List, Dict, Any

# Import Agents
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.health_agent import HealthCheckAgent
from agents.monetization_agent import MonetizationAgent
from agents.content_agent import ContentAgent
from agents.creativity_agent import CreativityAgent

# Import Scraper
from scraper import MarkPositionScraperAsync

class Colors:
    """Handles ANSI color codes for CLI output."""
    _is_tty = sys.stdout.isatty()

    HEADER = '\033[95m' if _is_tty else ''
    BLUE = '\033[94m' if _is_tty else ''
    CYAN = '\033[96m' if _is_tty else ''
    GREEN = '\033[92m' if _is_tty else ''
    WARNING = '\033[93m' if _is_tty else ''
    FAIL = '\033[91m' if _is_tty else ''
    ENDC = '\033[0m' if _is_tty else ''
    BOLD = '\033[1m' if _is_tty else ''
    UNDERLINE = '\033[4m' if _is_tty else ''

    @staticmethod
    def print_header(msg):
        print(f"{Colors.HEADER}{Colors.BOLD}{msg}{Colors.ENDC}")

    @staticmethod
    def print_success(msg):
        print(f"{Colors.GREEN}{msg}{Colors.ENDC}")

    @staticmethod
    def print_info(msg):
        print(f"{Colors.CYAN}{msg}{Colors.ENDC}")

    @staticmethod
    def print_warning(msg):
        print(f"{Colors.WARNING}{msg}{Colors.ENDC}")

    @staticmethod
    def print_error(msg):
        print(f"{Colors.FAIL}{Colors.BOLD}{msg}{Colors.ENDC}")

AGENTS = [
    AnalysisAgent(),
    ResearchAgent(),
    IntelligenceAgent(),
    HealthCheckAgent(),
    MonetizationAgent(),
    ContentAgent(),
    CreativityAgent()
]

DATA_FILE = "links.json"
RESULTS_DIR = "results"

def print_summary_box(report_path: str, data_count: int, agent_count: int):
    width = 60
    # Use standard string length for border calculation as recommended
    report_display = report_path
    if len(report_display) > 40:
        report_display = "..." + report_display[-37:]

    print(f"\n{Colors.CYAN}┌{'─' * (width - 2)}┐{Colors.ENDC}")
    print(f"{Colors.CYAN}│{Colors.BOLD}{' SYSTEM EXECUTION COMPLETE '.center(width - 2)}{Colors.ENDC}{Colors.CYAN}│{Colors.ENDC}")
    print(f"{Colors.CYAN}├{'─' * (width - 2)}┤{Colors.ENDC}")

    # Rows
    rows = [
        ("📅 Date", datetime.now().strftime('%Y-%m-%d %H:%M')),
        ("📊 Records Scraped", str(data_count)),
        ("🤖 Agents Run", str(agent_count)),
        ("📄 Report", report_display)
    ]

    for label, value in rows:
        # Calculate padding needed.
        # Visible length is label length + value length + 2 (for ": ")
        visible_len = len(label) + len(value) + 2
        padding = width - 4 - visible_len

        # visual fix for wide chars (emojis) roughly taking 2 chars space visually but 1 in len
        # date icon (1), bar chart (1), robot (1), page (1)
        # Assuming typical terminal fonts
        padding -= 1

        print(f"{Colors.CYAN}│ {Colors.ENDC}{label}: {Colors.GREEN}{value}{Colors.ENDC}{' ' * padding}{Colors.CYAN} │{Colors.ENDC}")

    print(f"{Colors.CYAN}└{'─' * (width - 2)}┘{Colors.ENDC}")

async def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping and use existing data")
    args = parser.parse_args()

    Colors.print_header("\n🚀 AUTONOMOUS AGENT SYSTEM INITIATED")

    # 1. Run Scraper (unless skipped)
    if not args.skip_scrape:
        Colors.print_info("--- Starting Scraper ---")
        scraper = MarkPositionScraperAsync(
            output_json=DATA_FILE,
            output_csv="links.csv",
            output_txt="unique_links.txt",
            concurrency=5
        )
        await scraper.scrape()
        Colors.print_success("--- Scraping Complete ---")
    else:
        Colors.print_warning("⏩ Skipping Scraper")

    # 2. Load Data
    if not os.path.exists(DATA_FILE):
        Colors.print_error(f"❌ Error: {DATA_FILE} not found. Cannot run agents.")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data: List[Dict[str, Any]] = json.load(f)

    Colors.print_info(f"📂 Loaded {len(data)} records.")

    # 3. Run Agents
    full_report = [f"# Daily System Report - {datetime.now().strftime('%Y-%m-%d')}\n"]

    Colors.print_header("\n🤖 ACTIVATING AGENTS")

    for agent in AGENTS:
        if sys.stdout.isatty():
            print(f"{Colors.BLUE}⟳ Running {agent.name}...{Colors.ENDC}", end="\r")
        else:
            print(f"Running {agent.name}...")

        try:
            results = agent.run(data)
            report_section = agent.format_report(results)
            full_report.append(report_section)
            full_report.append("\n---\n")
            if sys.stdout.isatty():
                print(f"{Colors.GREEN}✓ {agent.name} completed{' ' * 20}{Colors.ENDC}")
            else:
                print(f"{agent.name} completed")

        except Exception as e:
            if sys.stdout.isatty():
                print(f"{Colors.FAIL}✗ {agent.name} failed: {e}{' ' * 20}{Colors.ENDC}")
            else:
                print(f"{agent.name} failed: {e}")
            full_report.append(f"## {agent.name} Failed\nError: {str(e)}")

    # 4. Save Report
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    report_filename = f"{RESULTS_DIR}/daily_report_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_report))

    print_summary_box(report_filename, len(data), len(AGENTS))

if __name__ == "__main__":
    asyncio.run(main())
