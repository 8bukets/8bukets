import os
import json
import logging
import sys
import threading
import itertools
import time
from datetime import datetime
from agents.analysis_agent import AnalysisAgent
from agents.health_agent import HealthCheckAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent
from agents.monetization_agent import MonetizationAgent

# UX Classes
class Style:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def colorize(text, color):
        if sys.stdout.isatty():
            return f"{color}{text}{Style.ENDC}"
        return text

class Spinner:
    def __init__(self, message="Loading...", delay=0.1):
        self.spinner = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        self.delay = delay
        self.message = message
        self.running = False
        self.thread = None

    def spin(self):
        while self.running:
            sys.stdout.write(f"\r{next(self.spinner)} {self.message}")
            sys.stdout.flush()
            time.sleep(self.delay)
            # Clear line for next frame
            sys.stdout.write('\r')
            sys.stdout.flush()

    def __enter__(self):
        if sys.stdout.isatty():
            self.running = True
            self.thread = threading.Thread(target=self.spin)
            self.thread.start()
        else:
            print(f"{self.message}...")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.running:
            self.running = False
            self.thread.join()
            # Clear the line completely
            sys.stdout.write('\r' + ' ' * (len(self.message) + 2) + '\r')
            sys.stdout.flush()

            if exc_type is None:
                print(f"{Style.colorize('✓', Style.GREEN)} {self.message}")
            else:
                print(f"{Style.colorize('✗', Style.FAIL)} {self.message}")

# Configure logging
# We want logs to go to a file to keep the CLI clean
log_filename = "system.log"

# Clear any handlers that might have been added by imported modules (like agents.base_agent)
root_logger = logging.getLogger()
if root_logger.handlers:
    for handler in root_logger.handlers:
        root_logger.removeHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler(log_filename, mode='w', encoding='utf-8')
    ]
)
logger = logging.getLogger("SystemOrchestrator")

def main():
    print(f"\n{Style.colorize('Starting Daily Autonomous Agent Run', Style.HEADER + Style.BOLD)}\n")
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
            with Spinner(f"Running {agent.name}"):
                agent.run()
                all_results[agent.name] = agent.get_results()
        except Exception as e:
            logger.error(f"Agent {agent.name} failed: {e}")
            all_results[agent.name] = {"error": str(e)}

    # 3. Compile Report
    date_str = datetime.now().strftime("%Y-%m-%d")
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)
    report_filename = f"{results_dir}/DAILY_REPORT_{date_str}.md"

    with Spinner("Compiling Report"):
        generate_markdown_report(report_filename, all_results)

    logger.info(f"Daily run complete. Report saved to {report_filename}")
    print(f"\n{Style.colorize('✨ Daily run complete!', Style.GREEN + Style.BOLD)}")
    print(f"Report saved to: {Style.colorize(report_filename, Style.BLUE)}\n")

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
