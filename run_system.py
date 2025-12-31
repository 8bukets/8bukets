import asyncio
import json
import os
import argparse
import time
import re
from datetime import datetime
from typing import List, Dict, Any
import wcwidth

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
    # We need to account for visual width of emojis and characters
    def visual_len(s):
        # Strip ANSI codes first
        clean_s = re.sub(r'\x1b\[[0-9;]*m', '', str(s))
        # Use wcwidth to get correct display width (handles emojis, CJK, etc)
        return wcwidth.wcswidth(clean_s)

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

    # Calculate visible width
    v_len = visual_len(title)

    # Calculate padding needed to reach (width + 2) visual columns
    # We print: " " + title + " "
    # Total visual width needed: width + 2
    # Current visual width: v_len + 2
    # Padding needed: (width + 2) - (v_len + 2) = width - v_len

    padding_needed = width - v_len
    left_pad = padding_needed // 2
    right_pad = padding_needed - left_pad

    # Construct the centered line
    # We use raw spaces for padding, then the styled title
    # Note: styled_title contains ANSI codes but they have 0 width
    centered_line = f"{' ' * (left_pad + 1)}{styled_title}{' ' * (right_pad + 1)}"

    print(Colors.cyan(f"{V}") + centered_line + Colors.cyan(f"{V}"))
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

def should_run_report(force: bool = False) -> bool:
    """
    Determines if the report should run based on bi-weekly schedule.
    Schedule: Every even week's Monday.
    """
    if force:
        return True

    today = datetime.now()
    year, week, day = today.isocalendar()

    # Bi-weekly schedule: Run on Monday (1) of even weeks
    is_biweekly_monday = (day == 1) and (week % 2 == 0)

    return is_biweekly_monday

async def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--skip-scrape", action="store_true", help="Skip scraping and use existing data")
    parser.add_argument("--force", action="store_true", help="Force run ignoring schedule")
    args = parser.parse_args()

    start_time = time.time()

    print(Colors.header(f"\n🎨 Autonomous Agent System Initialized"))
    print(Colors.cyan(f"=====================================\n"))

    # 0. Check Schedule
    if not should_run_report(args.force):
        print(Colors.warning(f"⏩ Skipping Run: Not scheduled for today (Bi-weekly Mondays)."))
        print(Colors.blue("ℹ️  Use --force to override."))
        return

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

    # Generate bi-weekly filename parts
    today_date = datetime.now().strftime('%Y-%m-%d')
    current_year, current_week, _ = datetime.now().isocalendar()

    full_report = [f"# Bi-Weekly System Report - {today_date} (Week {current_week})\n"]

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

    report_filename = f"{RESULTS_DIR}/biweekly_report_{today_date}_W{current_week}.md"
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
