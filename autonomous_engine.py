import argparse
import asyncio
import os
import logging
import sys
import json
import subprocess
from datetime import datetime

# Import components from existing modules
from run_system import run_scraper, run_cycle
from autonomous_audit import run_audit

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("AutonomousEngine")

def bootstrap():
    """Ensure the environment is ready for autonomous execution."""
    logger.info("🚀 Bootstrapping Autonomous Environment...")

    # 1. Create necessary directories
    directories = ["results", "data", "config", "logs", "scripts"]
    for d in directories:
        if not os.path.exists(d):
            os.makedirs(d)
            logger.info(f"Created directory: {d}")

    # 2. Initialize evolution configuration if missing
    config_file = "config/evolution_params.json"
    if not os.path.exists(config_file):
        initial_config = {
            "current_version": 1.0,
            "system_concurrency": 5,
            "seo_impact_threshold": 0.5,
            "last_evolution": datetime.now().strftime("%Y-%m-%d")
        }
        with open(config_file, 'w') as f:
            json.dump(initial_config, f, indent=4)
        logger.info(f"Initialized {config_file} with default values.")

    # 3. Check for owner info
    owner_file = "config/owner_info.json"
    if not os.path.exists(owner_file):
        owner_info = {
            "legal_owner": "Filip Keser",
            "owner_reference": "REFERENCE:SIGMA-CHAMPION-001"
        }
        with open(owner_file, 'w') as f:
            json.dump(owner_info, f, indent=4)
        logger.info(f"Initialized {owner_file}")

    logger.info("✅ Bootstrap complete.")

def process_work_orders():
    """Check for pending work orders and execute appropriate scripts."""
    orders_file = "data/work_orders.json"
    if not os.path.exists(orders_file):
        return

    try:
        with open(orders_file, 'r') as f:
            orders = json.load(f)
    except:
        return

    updated = False
    for order in orders:
        if order["status"] == "PENDING" or order["status"] == "IN_PROGRESS":
            if order["type"] == "DEPLOYMENT":
                logger.info(f"🔔 Executing Deployment Work Order: {order['id']}")
                try:
                    # Execute the rollout script
                    subprocess.run(["python3", "scripts/rollout_executor.py"], check=True)
                    order["status"] = "COMPLETED"
                    order["updated_at"] = datetime.now().isoformat()
                    updated = True
                    logger.info(f"✅ Deployment {order['id']} COMPLETED.")
                except subprocess.CalledProcessError as e:
                    logger.error(f"❌ Deployment {order['id']} FAILED: {e}")
                    order["status"] = "FAILED"
                    updated = True

    if updated:
        with open(orders_file, 'w') as f:
            json.dump(orders, f, indent=4)

async def main():
    parser = argparse.ArgumentParser(description="Full Autonomous Automatic Creation Order and Execution Engine")
    parser.add_argument("--loop", action="store_true", help="Run continuously every 24h")
    parser.add_argument("--token", type=str, help="Authentication token", default=os.environ.get("SYSTEM_AUTH_TOKEN", "default_dev_token"))
    parser.add_argument("--skip-scraper", action="store_true", help="Skip the scraping phase")
    parser.add_argument("--dry-run", action="store_true", help="Run a single cycle and exit (test mode)")
    args = parser.parse_args()

    bootstrap()

    if args.dry_run:
        logger.info("🛠️ Executing DRY-RUN cycle (Creation Order & Execution Validation)...")
        try:
            if not args.skip_scraper:
                run_scraper()
            await run_cycle(args.token, args.skip_scraper)
            process_work_orders()
            run_audit()
            logger.info("✅ DRY-RUN complete. System is stable.")
        except Exception as e:
            logger.error(f"❌ DRY-RUN FAILED: {e}")
            sys.exit(1)
        return

    if args.loop:
        logger.info("🔄 Autonomous Engine starting in LOOP mode (24/7 Persistence).")
        try:
            while True:
                logger.info(f"=== Starting New Autonomous Cycle: {datetime.now().isoformat()} ===")
                if not args.skip_scraper:
                    run_scraper()
                await run_cycle(args.token, args.skip_scraper)
                process_work_orders()
                run_audit()
                logger.info("Cycle complete. Sleeping for 24 hours...")
                await asyncio.sleep(86400)
        except asyncio.CancelledError:
            logger.info("Engine loop interrupted.")
        except Exception as e:
            logger.critical(f"Engine encountered a fatal error: {e}")
            sys.exit(1)
    else:
        logger.info("🏃 Executing Single Autonomous Cycle...")
        if not args.skip_scraper:
            run_scraper()
        await run_cycle(args.token, args.skip_scraper)
        process_work_orders()
        run_audit()
        logger.info("✅ Execution finished.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Engine shutdown requested by user.")
