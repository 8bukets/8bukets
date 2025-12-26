import argparse
import subprocess
import sys
import os
import logging
from utils.gemini_client import GeminiClient
from utils.log_formatter import setup_logging

setup_logging()
logger = logging.getLogger("GeminiCLI")

def run_command(command, capture_output=True):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE if capture_output else None,
            stderr=subprocess.PIPE if capture_output else None
        )
        return True, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr

def build():
    logger.info("🔨 Building Docker environment...")
    success, out, err = run_command("docker-compose -f deployment/docker-compose.yml build")
    if success:
        logger.info("✅ Build successful!")
    else:
        logger.error("❌ Build failed.")
        if err:
            logger.error(err)
        # Here we could use Gemini to analyze build errors if we wanted

def deploy():
    logger.info("🚀 Deploying autonomous agents...")
    success, out, err = run_command("docker-compose -f deployment/docker-compose.yml up -d")
    if success:
        logger.info("✅ Deployment successful! Services are running.")
    else:
        logger.error("❌ Deployment failed.")
        if err:
            logger.error(err)

def debug():
    logger.info("🐞 Debugging mode initiated...")
    logger.info("Running orchestrator inside Docker container to capture trace...")

    # Run the orchestrator inside the container to ensure consistent environment
    # Using 'docker-compose run' which handles building if necessary
    success, out, err = run_command("docker-compose -f deployment/docker-compose.yml run --rm autonomous-agent python3 orchestrator.py --once --limit 1")

    if success:
        logger.info("✅ System ran successfully in container. No obvious errors to debug.")
        logger.info("Output summary:")
        print(out[-500:]) # Print last 500 chars
    else:
        logger.error("❌ System crashed!")
        logger.info("🔍 Analyzing crash with Gemini AI...")

        gemini = GeminiClient()
        analysis = gemini.analyze_error(err, out[-1000:] if out else "No stdout")

        print("\n" + "="*50)
        print("🤖 GEMINI DIAGNOSIS")
        print("="*50)
        print(analysis)
        print("="*50 + "\n")

def main():
    parser = argparse.ArgumentParser(description="AI Gemini CLI for Build, Debug & Deploy")
    parser.add_argument("action", choices=["build", "debug", "deploy"], help="Action to perform")

    args = parser.parse_args()

    if args.action == "build":
        build()
    elif args.action == "deploy":
        deploy()
    elif args.action == "debug":
        debug()

if __name__ == "__main__":
    main()
