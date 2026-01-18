import asyncio
import logging
import argparse
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.content_agent import ContentAgent, CreativityAgent
from agents.ad_agent import AdAgent, MonetizationAgent
from agents.intelligence_agent import IntelligenceAgent, HealthAgent

# Configure logging to show emojis and nice formatting
class ColorFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: grey + format_str + reset,
        logging.WARNING: yellow + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)

logger = logging.getLogger("System")
ch = logging.StreamHandler()
ch.setFormatter(ColorFormatter())
logging.getLogger().handlers = [] # Clear default handlers
logging.getLogger().addHandler(ch)
logging.getLogger().setLevel(logging.INFO)


async def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent Swarm")
    parser.add_argument("--url", default="https://markposition.wordpress.com/", help="Target URL")
    parser.add_argument("--limit", type=int, default=1, help="Max pages to research")
    args = parser.parse_args()

    logger.info("🚀 Initializing Autonomous Agent Swarm...")

    # Instantiate Agents
    brain = IntelligenceAgent() # Brain first to get strategy
    researcher = ResearchAgent()
    analyst = AnalysisAgent()
    creator = ContentAgent()
    artist = CreativityAgent()
    advertiser = AdAgent()
    accountant = MonetizationAgent()
    doctor = HealthAgent()

    # 0. Get Strategy from Intelligence (Memory)
    strategy = brain.get_mission_strategy()
    logger.info(f"🧠 Intelligence Level: IQ {strategy.get('iq')}. Bid Aggressiveness: {strategy.get('bid_aggressiveness')}")

    # 1. Health Check
    logger.info("🏥 Step 1: Pre-flight Health Check")
    health_res = await doctor.process({})
    if health_res.get("report", {}).get("overall_status") == "Critical":
        logger.error("System critical. Aborting.")
        return

    # 2. Research
    logger.info("🕵️ Step 2: Researching Target")
    research_res = await researcher.process({"target_url": args.url, "limit": args.limit})
    if research_res.get("status") != "success":
        logger.error("Research failed.")
        return

    # 3. Analysis
    logger.info("🧠 Step 3: Analyzing Data")
    # Research agent saved data to file, but we should pass the raw data if possible or re-read it.
    # The research agent returns the data in the "data" key.
    analysis_res = await analyst.process({"data": research_res.get("data")})

    # 4. Content Creation
    logger.info("✍️ Step 4: Drafting Content Strategy")
    # Pass creativity threshold from strategy (implied usage in ContentAgent/CreativityAgent)
    content_res = await creator.process({
        "insights": analysis_res.get("insights"),
        "creativity_threshold": strategy.get("creativity_threshold")
    })

    # 5. Creativity Injection
    logger.info("🎨 Step 5: Applying Creativity")
    creative_res = await artist.process({
        "content": content_res.get("content"),
        "creativity_threshold": strategy.get("creativity_threshold")
    })

    # 6. Ad Targeting
    logger.info("🎯 Step 6: Planning Ad Campaign")
    ad_res = await advertiser.process({
        "insights": analysis_res.get("insights"),
        "bid_aggressiveness": strategy.get("bid_aggressiveness")
    })

    # 7. Monetization Projection
    logger.info("💰 Step 7: Projecting Revenue")
    money_res = await accountant.process({"campaign": ad_res.get("campaign")})

    # 8. Intelligence / Learning
    logger.info("🤖 Step 8: System Learning & Decision")
    run_data = {
        "health": health_res.get("report"),
        "research_count": len(research_res.get("data", [])),
        "monetization": money_res.get("financials")
    }
    intelligence_res = await brain.process({"run_data": run_data})

    logger.info("✅ Mission Complete. System Status: " + intelligence_res.get("decision", "UNKNOWN"))

    # Final Summary Output
    print("\n--- 🏁 MISSION SUMMARY 🏁 ---")
    print(f"Target: {args.url}")
    print(f"IQ Level: {intelligence_res.get('iq')}")
    print(f"Articles Analyzed: {len(research_res.get('data', []))}")
    print(f"Top Strategy: {content_res.get('content', {}).get('strategy_brief')}")
    print(f"Creative Title: {creative_res.get('creative_content', {}).get('creative_titles', [''])[0]}")
    print(f"Ad Bid: ${ad_res.get('campaign', {}).get('suggested_bid')}")
    print(f"Projected ROI: {money_res.get('financials', {}).get('projected_roi')}")
    print("-----------------------------")

if __name__ == "__main__":
    asyncio.run(main())
