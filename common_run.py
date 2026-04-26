import os
import sys
import subprocess
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("CommonRun")

def setup_environment():
    """Ensure required environment variables are set."""
    logger.info("Setting up environment variables...")

    # Auth Token
    if not os.getenv("SYSTEM_AUTH_TOKEN"):
        logger.info("SYSTEM_AUTH_TOKEN not found. Using default 'default_dev_token'.")
        os.environ["SYSTEM_AUTH_TOKEN"] = "default_dev_token"

    # Gemini API Key
    if not os.getenv("GEMINI_API_KEY"):
        logger.warning("GEMINI_API_KEY not found. JulesEvolutionAgent will operate in fallback mode.")
        # Set a dummy key to prevent crashes if something strictly checks for existence
        os.environ["GEMINI_API_KEY"] = "dummy_key_for_fallback"

def run_step(name: str, command: list):
    """Run a subprocess command and handle errors."""
    logger.info(f"=== Starting Phase: {name} ===")
    try:
        # Run the command, stream output to stdout/stderr
        result = subprocess.run(command, check=True, text=True)
        logger.info(f"=== Phase {name} Completed Successfully ===\n")
    except subprocess.CalledProcessError as e:
        logger.error(f"!!! Phase {name} Failed with exit code {e.returncode} !!!")
        logger.error("Halting common run execution to prevent cascading failures.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"!!! Unexpected error during Phase {name}: {e} !!!")
        sys.exit(1)

def main():
    logger.info("Initializing Markposition Autonomous System - Common Run")
    setup_environment()

    # Ensure data and results directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    # Phase 1: Scrape
    run_step("Data Ingestion (Scraping)", [sys.executable, "scraper.py"])

    # Phase 2: Autonomous Cycle
    # We pass --skip-scraper because we just explicitly ran it
    run_step("Autonomous Agent Cycle", [sys.executable, "run_system.py", "--skip-scraper"])

    # Phase 3: Analytics
    run_step("Analytics & Reporting", [sys.executable, "analytics.py"])

    logger.info("All phases of the Common Run completed successfully. Check the 'results' directory for reports.")

if __name__ == "__main__":
    main()
