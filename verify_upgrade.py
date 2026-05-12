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
from agents.telemetry_agent import TelemetryAgent
from agents.sigma_agent import SixSigmaAgent
from agents.architect_agent import ArchitectAgent
from agents.meta_coding_agent import MetaCodingAgent
from agents.jules_evolution_agent import JulesEvolutionAgent
from agents.gitkraken_evolution_agent import GitKrakenEvolutionAgent
from agents.docker_evolution_agent import DockerEvolutionAgent
from agents.github_evolution_agent import GitHubEvolutionAgent

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

    from agents.react_agent import ReActAgent
    from agents.knowledge_agent import KnowledgeAgent
    from agents.cloud_workflow_agent import CloudWorkflowAgent
    from agents.gitlab_evolution_agent import GitLabEvolutionAgent

    agents = [
        HealthCheckAgent(),
        RobotTxtAgent(),
        KnowledgeAgent(),
        AnalysisAgent(),
        ResearchAgent(),
        IntelligenceAgent(),
        ReActAgent(),
        TargetingAgent(),
        CreativityAgent(),
        AdsAgent(),
        BidAgent(),
        MonetizationAgent(),
        ContentAgent(),
        AutonomousIntelligenceAgent(),
        TelemetryAgent(),
        SixSigmaAgent(),
        ArchitectAgent(),
        MetaCodingAgent(),
        JulesEvolutionAgent(),
        GitKrakenEvolutionAgent(),
        DockerEvolutionAgent(),
        GitLabEvolutionAgent(),
        CloudWorkflowAgent(),
        GitHubEvolutionAgent()
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
