import time
import logging
import os
import json
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent
from agents.programmatic_ads_agent import ProgrammaticAdsAgent
from agents.ads_agent import AdsAgent
from agents.market_simulation_agent import MarketSimulationAgent
from agents.monetization_agent import MonetizationAgent
from agents.health_check_agent import HealthCheckAgent
from agents.autonomous_intelligence_agent import AutonomousIntelligenceAgent
from core.web_protocols import CookieManager, RobotTxtHandler

# Configure system-wide logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Orchestrator")

def initialize_system():
    # Ensure necessary directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("generated_output", exist_ok=True)

    # Initialize DNA if missing
    dna_path = "data/dna.json"
    if not os.path.exists(dna_path):
        initial_dna = {
            "system_stats": {
                "iq": 25,
                "generation": 0,
                "total_revenue": 0.0
            },
            "parameters": {
                "bid_aggressiveness": 0.5,
                "creativity_level": 0.5,
                "risk_tolerance": 0.3,
                "learning_rate": 0.1,
                "cooperation_factor": 0.5
            },
            "policy": {
                "robots_txt_compliance": True,
                "cookie_sharing": "trusted_parties"
            }
        }
        with open(dna_path, 'w') as f:
            json.dump(initial_dna, f, indent=4)
        logger.info("Initialized system DNA.")

def run_daily_cycle(day_number):
    logger.info(f"=== Starting Day {day_number} Autonomous Cycle ===")

    # 1. Initialize Context (The "Mind")
    context = {}

    # 2. Simulate Web Compliance & Cooperation
    if RobotTxtHandler.check_compliance("http://internal-simulation"):
        context['cookies'] = CookieManager.share_data(context, "1st")

    # 3. Instantiate and Run Agents in Sequence
    # This represents the data flow: Analyze -> Research -> Decide -> Create -> Monetize -> Learn

    agents = [
        AnalysisAgent(),
        ResearchAgent(),
        IntelligenceAgent(),      # Strategize based on analysis/research
        CreativityAgent(),        # Generate ideas/code
        ContentAgent(),           # Write code to disk
        ProgrammaticAdsAgent(),   # Plan ads
        AdsAgent(),               # Create ads
        MarketSimulationAgent(),  # Test in market (Feedback)
        MonetizationAgent(),      # Collect Revenue
        HealthCheckAgent(),       # Verify Integrity
        AutonomousIntelligenceAgent() # Evolve DNA
    ]

    for agent in agents:
        try:
            agent.run_cycle(context)
        except Exception as e:
            logger.error(f"Error in {agent.name}: {e}")
            import traceback
            traceback.print_exc()

    logger.info(f"=== Day {day_number} Complete ===")

    revenue = context.get('financials', {}).get('cycle_revenue', 0)
    feedback_score = context.get('market_feedback', {}).get('quality_score', 0)
    logger.info(f"Summary: Revenue: ${revenue:.2f}, Quality Score: {feedback_score:.2f}")

if __name__ == "__main__":
    initialize_system()
    # Simulate a few days of operation to show evolution
    for day in range(1, 4):
        run_daily_cycle(day)
        time.sleep(1) # Pause between days
