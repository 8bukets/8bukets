import os
import sys
import json
import logging
import re
from datetime import datetime, timedelta
from agents.analysis_agent import AnalysisAgent
from agents.health_agent import HealthCheckAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent
from agents.monetization_agent import MonetizationAgent
from utils.colors import Colors

# Configure logging to stdout for correct ordering with print statements
# We need to remove existing handlers because base_agent.py might have already configured logging to stderr
root_logger = logging.getLogger()
if root_logger.handlers:
    for handler in root_logger.handlers:
        root_logger.removeHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    stream=sys.stdout
)
logger = logging.getLogger("SystemOrchestrator")

def should_run_report():
    """Checks if 14 days have passed since the last report."""
    results_dir = "results"
    if not os.path.exists(results_dir):
        return True

    # Find all report files
    files = os.listdir(results_dir)
    report_files = [f for f in files if f.startswith("BIWEEKLY_REPORT_") or f.startswith("DAILY_REPORT_")]

    if not report_files:
        return True

    # Extract dates
    dates = []
    for f in report_files:
        try:
            # Extract date string YYYY-MM-DD
            # Filename format: PREFIX_REPORT_YYYY-MM-DD.md
            date_part = f.split('_')[-1].replace('.md', '')
            date_obj = datetime.strptime(date_part, "%Y-%m-%d")
            dates.append(date_obj)
        except ValueError:
            continue

    if not dates:
        return True

    last_run_date = max(dates)
    days_since_last_run = (datetime.now() - last_run_date).days

    if days_since_last_run < 14:
        logger.info(Colors.warning(f"Skipping run. Last report was {days_since_last_run} days ago ({last_run_date.strftime('%Y-%m-%d')}). Next run in {14 - days_since_last_run} days."))
        return False

    return True

def main():
    print(Colors.header("\n🎨 Starting Bi-weekly Autonomous Agent Run..."))

    # Ensure results directory exists
    os.makedirs("results", exist_ok=True)

    if not should_run_report():
        return

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
    agent_status = []

    for agent in agents:
        try:
            logger.info(Colors.info(f"Running {agent.name}..."))
            agent.run()
            all_results[agent.name] = agent.get_results()
            agent_status.append({"name": agent.name, "status": "Success", "emoji": "✅"})
        except Exception as e:
            logger.error(Colors.fail(f"Agent {agent.name} failed: {e}"))
            all_results[agent.name] = {"error": str(e)}
            agent_status.append({"name": agent.name, "status": "Failed", "emoji": "❌"})

    # 3. Compile Report
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_filename = f"results/BIWEEKLY_REPORT_{date_str}.md"

    generate_markdown_report(report_filename, all_results)

    print_summary_box(agent_status, report_filename, title=" BI-WEEKLY RUN SUMMARY ")

def get_visible_length(text):
    """Calculates the visible length of a string by stripping ANSI codes."""
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return len(ansi_escape.sub('', text))

def print_summary_box(agent_status, report_filename, title=" RUN SUMMARY "):
    """Prints a summary box of the run."""
    print("\n")

    # Calculate widths
    max_name_len = 30
    # Truncate names if necessary and calculate max width
    processed_status = []
    for item in agent_status:
        name = item["name"]
        if len(name) > max_name_len:
            name = name[:max_name_len-3] + "..."
        processed_status.append({**item, "display_name": name})

    # Fixed width for the box
    box_width = 50

    # Top Border
    print(Colors.header("╔" + "═" * (box_width - 2) + "╗"))

    # Title
    padding = (box_width - 2 - len(title)) // 2
    # Ensure even padding if possible, or adjust
    # If title length is even, padding is (48 - len)/2.
    print(Colors.header("║") + " " * padding + Colors.style(title, Colors.BOLD) + " " * (box_width - 2 - padding - len(title)) + Colors.header("║"))

    # Separator
    print(Colors.header("╠" + "═" * (box_width - 2) + "╣"))

    # Rows
    for item in processed_status:
        name = item["display_name"]
        status_emoji = item["emoji"]
        status_text = item["status"]

        # Colorize status
        if status_text == "Success":
            status_display = Colors.success(status_text)
        else:
            status_display = Colors.fail(status_text)

        # Calculate padding
        emoji_width = 2
        content_visible_len = emoji_width + 1 + len(name)

        # Space available for content
        content_space = box_width - 4 # 2 for borders, 2 for padding

        dots_count = content_space - content_visible_len - len(status_text)
        if dots_count < 1:
            dots_count = 1

        dots = "." * dots_count

        row_str = f" {status_emoji} {name}{Colors.style(dots, Colors.OKBLUE)}{status_display} "

        print(Colors.header("║") + row_str + Colors.header("║"))

    # Bottom Border
    print(Colors.header("╚" + "═" * (box_width - 2) + "╝"))

    print(f"\n📄 Report saved to: {Colors.underline(report_filename)}\n")

def generate_markdown_report(filename, results):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Bi-weekly Autonomous Report - {datetime.now().strftime('%Y-%m-%d')}\n\n")

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
