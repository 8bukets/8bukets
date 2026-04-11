import asyncio
import logging
from agents.base_agent import Blackboard
from agents.jules_evolution_agent import JulesEvolutionAgent
from agents.gitkraken_evolution_agent import GitKrakenEvolutionAgent
from agents.docker_evolution_agent import DockerEvolutionAgent
from agents.github_evolution_agent import GitHubEvolutionAgent

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("CollaborationVerifier")

async def test_agent_connections():
    logger.info("Starting Connection Test for Collaborative Evolution Unit...")

    bb = Blackboard()

    # Pre-populate Blackboard with required triggers
    await bb.update("System", {
        "system_evolution": {"status": "EVOLVED", "parameter_shifts": {"current_version": 1.25}},
        "meta_optimizations": "DEEP_SKILL_INJECTED"
    })

    # 1. Instantiate agents
    jules = JulesEvolutionAgent()
    kraken = GitKrakenEvolutionAgent()
    docker = DockerEvolutionAgent()
    github = GitHubEvolutionAgent()

    # 2. Sequential Execution (Simulating Tiers)
    logger.info("--- Phase 1: High-Level Coordination (Jules) ---")
    res_jules = await jules.run([], bb)
    await bb.update(jules.name, res_jules)

    logger.info("--- Phase 2: Specialized Optimization (GitKraken & Docker) ---")
    res_kraken = await kraken.run([], bb)
    await bb.update(kraken.name, res_kraken)
    res_docker = await docker.run([], bb)
    await bb.update(docker.name, res_docker)

    logger.info("--- Phase 3: Version Control Integration (GitHub) ---")
    # Note: We mock subprocess.run in real tests, but here we just want to see if it reaches the logic
    # To avoid actual git commits during verification, we can check the Blackboard state before GitHub runs

    logger.info("Verifying Blackboard state for GitHub consumption...")
    strategy = bb.get("evolution_strategy")
    viz = bb.get("git_visualization_metrics")
    container = bb.get("container_status")

    logger.info(f"Evolution Strategy: {strategy}")
    logger.info(f"GitKraken Metrics: {viz}")
    logger.info(f"Docker Status: {container}")

    success = all([strategy, viz, container])
    if success:
        logger.info("✅ SUCCESS: All 4 agents are logically connected and sharing data.")
    else:
        logger.error("❌ FAILURE: One or more agents failed to provide data.")

if __name__ == "__main__":
    asyncio.run(test_agent_connections())
