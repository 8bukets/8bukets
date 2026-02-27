import argparse
import asyncio
import aiohttp
import time
import json
import os
import sys
import subprocess
import logging
from datetime import datetime

import importlib
import pkgutil
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, TextColumn

from markposition import agents
from markposition.agents.base_agent import BaseAgent

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "name": record.name,
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_record)

# Configure Logging
log_handler = logging.StreamHandler()
if os.getenv("LOG_FORMAT", "TEXT") == "JSON":
    log_handler.setFormatter(JsonFormatter(datefmt='%Y-%m-%d %H:%M:%S'))
else:
    log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S'))

logger = logging.getLogger("SystemOrchestrator")
# Set up root logger to use our handler, and don't add it specifically to child
logging.getLogger().handlers = [log_handler]
logging.getLogger().setLevel(logging.INFO)

def run_scraper():
    logger.info("Starting Scraper...")
    try:
        # Now that it's a package, we might want to call it differently or keep it as subprocess
        result = subprocess.run(
            [sys.executable, "-m", "markposition.scraper", "--limit", "5"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            logger.error(f"Scraper failed: {result.stderr}")
            return False
        logger.info("Scraper finished successfully.")
        return True
    except Exception as e:
        logger.error(f"Failed to execute scraper: {e}")
        return False

def load_data(filepath="links.json"):
    if not os.path.exists(filepath):
        logger.error(f"Data file {filepath} not found.")
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON data: {e}")
        return []

def generate_daily_report(context, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Daily Autonomous Report: {datetime.now().strftime('%Y-%m-%d')}\n\n")

            f.write(f"**Autonomous Status:** {context.get('autonomous_status', 'UNKNOWN')}\n\n")

            f.write("## 1. Ecosystem Health\n")
            health = context.get("health_report", {})
            for check in health.get("checks", []):
                f.write(f"- {check}\n")
            robots = context.get("robots_txt", {})
            f.write(f"- **Robots.txt:** {robots.get('status', 'N/A')} (Disallowed: {len(robots.get('disallowed_paths', []))})\n")

            browser = context.get("browser_test", {})
            f.write(f"- **Browser Check:** {browser.get('status', 'N/A')}\n")
            if browser.get("screenshot"):
                f.write(f"  - [View Screenshot](../{browser.get('screenshot')})\n")

            f.write("\n## 2. Targeting & Strategy\n")
            targeting = context.get("targeting_profile", {})
            f.write(f"- **Persona:** {targeting.get('primary_persona', 'N/A')}\n")
            f.write(f"- **Intent:** {targeting.get('intent', 'N/A')}\n")

            f.write("\n## 3. Bid Intelligence\n")
            bid = context.get("bid_strategy", {})
            f.write(f"- **Strategy:** {bid.get('strategy', 'N/A')}\n")
            f.write(f"- **Recommended CPM:** ${bid.get('recommended_cpm', 0.00)}\n")
            f.write(f"- **Self-Optimization Factor:** {bid.get('adjustment_factor', 1.0)}\n")

            f.write("\n## 4. Ads Generation\n")
            for ad in context.get("generated_ads", []):
                f.write(f"### {ad.get('headline')}\n")
                f.write(f"- Target: {ad.get('target_audience')}\n")
                f.write(f"- CTA: {ad.get('cta')}\n")

            f.write("\n## 5. LLM System Reasoning\n")
            f.write(f"{context.get('llm_reasoning', 'N/A')}\n\n")
            f.write("**Recommendations:**\n")
            for rec in context.get("llm_recommendations", []):
                f.write(f"- {rec}\n")

            f.write("\n## 6. Identified Patterns\n")
            f.write("### Market Patterns\n")
            patterns = context.get("market_patterns", [])
            for p in patterns:
                f.write(f"- {p}\n")

            f.write("\n### Source Code Patterns\n")
            src_patterns = context.get("source_code_patterns", [])
            for p in src_patterns:
                f.write(f"- {p}\n")

            f.write("\n## 7. Market Analysis\n")
            stats = context.get("analysis_stats", {})
            f.write(f"- **Total Posts:** {stats.get('total_posts')}\n")

            f.write("\n## 8. Content Draft\n")
            f.write("```text\n")
            f.write(context.get("generated_content", ""))
            f.write("\n```\n")

        logger.info(f"Report generated at {filename}")
    except IOError as e:
        logger.error(f"Failed to write report: {e}")

def discover_agents():
    """Dynamically discover and instantiate agents from the agents/ directory."""
    discovered = []
    # Adjust path for walk_packages
    for loader, module_name, is_pkg in pkgutil.walk_packages(agents.__path__, agents.__name__ + "."):
        if module_name == "markposition.agents.base_agent":
            continue
        try:
            module = importlib.import_module(module_name)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, BaseAgent) and attr is not BaseAgent:
                    discovered.append(attr())
        except Exception as e:
            logger.error(f"Failed to load agent from {module_name}: {e}")
    return discovered

async def run_cycle(sim_date=None):
    console = Console()
    console.print("[bold blue]=== Starting Daily Autonomous Cycle ===[/bold blue]")

    # 1. Scrape
    if not run_scraper():
        logger.error("Cycle aborted due to scraper failure.")
        return

    # 2. Load Data
    data = load_data()
    if not data:
        logger.warning("No data loaded. Skipping agent execution.")
        return

    context = {}

    # 3. Dynamic Agent Pipeline
    all_agents = discover_agents()
    stages = {}
    for agent in all_agents:
        stage = getattr(agent, "execution_stage", 1)
        if stage not in stages:
            stages[stage] = []
        stages[stage].append(agent)

    distributed = os.getenv("DISTRIBUTED_MODE", "FALSE").upper() == "TRUE"

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        async with aiohttp.ClientSession() as session:
            for stage_num in sorted(stages.keys()):
                stage_agents = stages[stage_num]
                task_id = progress.add_task(description=f"Executing Stage {stage_num}...", total=len(stage_agents))

                if distributed:
                    from markposition.tasks import run_agent_task
                    logger.info(f"Stage {stage_num}: Dispatching {len(stage_agents)} agents to Celery.")

                    # Bridge: Dispatch to Celery and wait for results
                    tasks = []
                    for a in stage_agents:
                        # We pass the module and class name so the worker can re-instantiate
                        task = run_agent_task.delay(a.__module__, a.__class__.__name__, data, context)
                        tasks.append(task)

                    # Poll for completion (simplified bridge)
                    results = []
                    for t in tasks:
                        results.append(t.get()) # Blocking get in a loop for each stage
                else:
                    # Standard async local execution
                    for a in stage_agents:
                        a.session = session

                    results = await asyncio.gather(*[a.run(data, context) for a in stage_agents], return_exceptions=True)

                for res in results:
                    if isinstance(res, dict):
                        context.update(res)
                    elif isinstance(res, Exception):
                        logger.error(f"Error in stage {stage_num}: {res}")

                progress.update(task_id, advance=len(stage_agents))

    # Real-time Summary Dashboard
    table = Table(title="Agent Execution Summary")
    table.add_column("Agent", style="cyan")
    table.add_column("Stage", style="magenta")
    table.add_column("Status", style="green")

    for agent in all_agents:
        table.add_row(agent.name, str(getattr(agent, "execution_stage", 1)), "COMPLETED")

    console.print(table)

    # 4. Report
    report_date = sim_date if sim_date else datetime.now().strftime('%Y-%m-%d')
    report_file = f"results/DAILY_REPORT_{report_date}.md"
    generate_daily_report(context, report_file)

    logger.info("=== Cycle Complete ===")

async def main_async():
    parser = argparse.ArgumentParser(description="Autonomous Agent System")
    parser.add_argument("--loop", action="store_true", help="Run continuously every 24h")
    parser.add_argument("--dashboard", action="store_true", help="Start the web dashboard")
    parser.add_argument("--simulate-days", type=int, help="Simulate a number of days of execution")
    args = parser.parse_args()

    if args.simulate_days:
        logger.info(f"Simulating {args.simulate_days} days of operation...")
        from datetime import timedelta
        for day in range(args.simulate_days):
            sim_date = (datetime.now() - timedelta(days=args.simulate_days - day - 1)).strftime('%Y-%m-%d')
            logger.info(f"--- Simulating Day {day+1} ({sim_date}) ---")
            await run_cycle(sim_date=sim_date)
        return

    if args.dashboard:
        logger.info("Starting Web Dashboard...")
        # Since it's a module now
        subprocess.Popen([sys.executable, "-m", "markposition.dashboard"])

    if args.loop:
        logger.info("System starting in LOOP mode.")
        try:
            while True:
                await run_cycle()
                logger.info("Sleeping for 24 hours...")
                await asyncio.sleep(86400) # 24 hours
        except KeyboardInterrupt:
            logger.info("Loop interrupted by user.")
    else:
        await run_cycle()

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
