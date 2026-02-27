import asyncio
import logging
import json
import os
from agents.orchestrator import AgentOrchestrator
from agents.health_check_agent import HealthCheckAgent
from agents.analysis_agent import AnalysisAgent
from agents.research_agent import ResearchAgent
from agents.intelligence_agent import IntelligenceAgent
from agents.monetization_agent import MonetizationAgent
from agents.creativity_agent import CreativityAgent
from agents.content_agent import ContentAgent
from agents.robot_txt_agent import RobotTxtAgent
from agents.targeting_agent import TargetingAgent
from agents.ads_agent import AdsAgent
from agents.bid_agent import BidAgent
from agents.autonomous_intelligence_agent import AutonomousIntelligenceAgent

logging.basicConfig(level=logging.INFO)

async def verify():
    data = [
        {
            "title": "advertising.amazon",
            "date": "October 5, 2022",
            "datetime": "2022-10-05T07:47:49+02:00",
            "author": "Filip Keser",
            "categories": ["Ad Ads Advertise"],
            "external_link": "https://advertising.amazon.com/",
            "domain": "advertising.amazon.com",
            "post_url": "https://markposition.wordpress.com/2022/10/05/advertising-amazon/"
        }
    ]

    agents = [
        HealthCheckAgent(),
        RobotTxtAgent(),
        AnalysisAgent(),
        ResearchAgent(),
        IntelligenceAgent(),
        TargetingAgent(),
        CreativityAgent(),
        AdsAgent(),
        BidAgent(),
        MonetizationAgent(),
        ContentAgent(),
        AutonomousIntelligenceAgent()
    ]

    orchestrator = AgentOrchestrator(agents)

    print("--- Primary Execution ---")
    context = await orchestrator.execute_cycle(data)

    print("--- Peer Review ---")
    await orchestrator.run_peer_review()

    final_context = orchestrator.blackboard.get_all()
    print(f"Final Context Keys: {list(final_context.keys())}")
    print(f"Peer Review Log: {final_context.get('peer_review_log')}")

    if "generated_content" in final_context and "autonomous_status" in final_context:
        print("VERIFICATION SUCCESSFUL")
    else:
        print("VERIFICATION FAILED")

if __name__ == "__main__":
    asyncio.run(verify())
