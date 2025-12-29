import asyncio
import json
import os
import argparse
import time
import re
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

# Import UX Utils
from utils.colors import Colors

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

def print_summary_box(title: str, stats: List[tuple]):
    """Prints a styled summary box."""
    # Determine the maximum width needed for content
    # We strip ANSI codes to get visual length
    def visual_len(s):
        return len(re.sub(r'\x1b\[[0-9;]*m', '', str(s)))

    content_width = 0
    for label, value in stats:
        line_len = visual_len(label) + visual_len(value) + 4 # 4 for spacing (at least 2 spaces padding + 2 spaces gap)
        if line_len > content_width:
            content_width = line_len

    # Add padding and ensure title fits
    # title has 2 spaces padding around it in the print statement below: f" {bold_title} "
    width = max(content_width, visual_len(title) + 4)

    # Border characters
    TL, TR = "┌", "┐"
    BL, BR = "└", "┘"
    H, V = "─", "│"

    print()
    print(Colors.cyan(f"{TL}{H * (width + 2)}{TR}"))

    # Title Centering
    styled_title = Colors.bold(title)
    # To center correctly with ANSI codes, we need to know how much 'invisible' string length to add to the center width
    invisible_len = len(styled_title) - visual_len(styled_title)
    # We want the visual area to be (width + 2) wide
    # So we pad the string to (width + 2 + invisible_len)
    centered_title = f" {styled_title} ".center(width + 2 + invisible_len)

    print(Colors.cyan(f"{V}") + centered_title + Colors.cyan(f"{V}"))
    print(Colors.cyan(f"{V}{' ' * (width + 2)}{V}"))

    for label, value in stats:
        # Calculate padding needed
        # We want: " label    value "
        # Total visual length must be width + 2
        # So spaces = (width + 2) - 1 (left space) - 1 (right space) - visual_len(label) - visual_len(value)
        # spaces = width - visual_len(label) - visual_len(value)
        space = width - visual_len(label) - visual_len(value)
        print(Colors.cyan(f"{V}") + f" {label}{' ' * space}{value} " + Colors.cyan(f"{V}"))

    print(Colors.cyan(f"{BL}{H * (width + 2)}{BR}"))
    print()

async def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping and use existing data")
    args = parser.parse_args()

    start_time = time.time()

    print(Colors.header(f"\n🎨 Autonomous Agent System Initialized"))
    print(Colors.cyan(f"=====================================\n"))

    # 1. Run Scraper (unless skipped)
    if not args.skip_scrape:
        print(Colors.blue("📦 Starting Scraper..."))
        scraper = MarkPositionScraperAsync(
            output_json=DATA_FILE,
            output_csv="links.csv",
            output_txt="unique_links.txt",
            concurrency=5
        )
        await scraper.scrape()
        print(Colors.green("✅ Scraping Complete"))
    else:
        print(Colors.warning("⏩ Skipping Scraper"))

    # 2. Load Data
    if not os.path.exists(DATA_FILE):
        print(Colors.fail(f"❌ Error: {DATA_FILE} not found. Cannot run agents."))
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data: List[Dict[str, Any]] = json.load(f)

    print(Colors.blue(f"📂 Loaded {Colors.bold(str(len(data)))} records."))

    # 3. Run Agents
    print(Colors.header(f"\n🤖 Starting Agent Swarm..."))
    full_report = [f"# Daily System Report - {datetime.now().strftime('%Y-%m-%d')}\n"]

    agents_success = 0
    agents_failed = 0

    for agent in AGENTS:
        print(f"   ⚙️  Running {Colors.cyan(agent.name)}...", end="\r")
        try:
            results = agent.run(data)
            report_section = agent.format_report(results)
            full_report.append(report_section)
            full_report.append("\n---\n")
            print(f"   ✅ Finished {Colors.green(agent.name)}   ") # Spaces to overwrite previous line
            agents_success += 1
        except Exception as e:
            print(f"   ❌ Failed {Colors.fail(agent.name)}: {e}")
            full_report.append(f"## {agent.name} Failed\nError: {str(e)}")
            agents_failed += 1

    # 4. Save Report
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    report_filename = f"{RESULTS_DIR}/daily_report_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_report))

    elapsed_time = time.time() - start_time

    # 5. Summary Box
    stats = [
        ("📂 Report:", Colors.bold(os.path.basename(report_filename))),
        ("📊 Records:", str(len(data))),
        ("✅ Success:", Colors.green(str(agents_success))),
        ("⏱️  Time:", f"{elapsed_time:.2f}s")
    ]

    if agents_failed > 0:
        stats.append(("❌ Failed:", Colors.fail(str(agents_failed))))

    print_summary_box("System Run Complete", stats)

if __name__ == "__main__":
    asyncio.run(main())
