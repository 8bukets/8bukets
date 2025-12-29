import os
import sys
import json
import logging
import re
from datetime import datetime
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

def main():
    print(Colors.header("\n🎨 Starting Daily Autonomous Agent Run..."))

    # Ensure results directory exists
    os.makedirs("results", exist_ok=True)

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
    report_filename = f"results/DAILY_REPORT_{date_str}.md"

    generate_markdown_report(report_filename, all_results)

    print_summary_box(agent_status, report_filename)

def get_visible_length(text):
    """Calculates the visible length of a string by stripping ANSI codes."""
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return len(ansi_escape.sub('', text))

def print_summary_box(agent_status, report_filename):
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
    title = " DAILY RUN SUMMARY "
    padding = (box_width - 2 - len(title)) // 2
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
        # Visible length calculation: emoji (2 chars width usually but 1 char in len) + space + name + space + status
        # Note: len("✅") is 1, but visually 2. Standard string length calcs are tricky with emojis.
        # Memory says: "Standard string length calculations in Python do not account for the visual width of emojis (often 2 columns), which causes misalignment in CLI borders unless explicitly corrected."

        # We will assume emojis are 2 columns wide.
        # Visible content: " {emoji} {name} ... {status} "

        emoji_width = 2
        content_visible_len = emoji_width + 1 + len(name)

        # Right align status
        # We want: "║ ✅ Analysis Agent            Success ║"

        # Space available for content
        content_space = box_width - 4 # 2 for borders, 2 for padding

        dots_count = content_space - content_visible_len - len(status_text)
        if dots_count < 1:
            dots_count = 1 # Should not happen with truncation

        dots = "." * dots_count

        row_str = f" {status_emoji} {name}{Colors.style(dots, Colors.OKBLUE)}{status_display} "

        print(Colors.header("║") + row_str + Colors.header("║"))

    # Bottom Border
    print(Colors.header("╚" + "═" * (box_width - 2) + "╝"))

    print(f"\n📄 Report saved to: {Colors.underline(report_filename)}\n")

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
