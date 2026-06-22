import os
import json
import asyncio
from datetime import datetime
from .base_agent import BaseAgent, Blackboard

DREAMS_FILE = "data/dreams.json"

class DreamBuilderAgent(BaseAgent):
    """
    The Dream Builder: Synthesizes system performance and market trends to
    generate long-term visions and specifications for new autonomous capabilities.
    """
    def __init__(self):
        super().__init__("DreamBuilderAgent",
                         dependencies=["analysis_stats", "research_data", "sigma_performance_report"],
                         provides=["long_term_visions"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Dreaming of new autonomous capabilities...")

        analysis = blackboard.get("analysis_stats", {})
        research = blackboard.get("research_data", {})
        sigma = blackboard.get("sigma_performance_report", {})

        market_trends = research.get("market_trends", [])
        impact = sigma.get("average_impact_score", 0)
        top_categories = analysis.get("top_categories", {})

        dreams = []

        # Dream 1: Strategic Scaling
        if impact > 0.7:
            dreams.append({
                "title": "Hyper-Scale Intelligence Swarm",
                "vision": "Expand agent population to 1000+ specialized micro-agents for granular market analysis.",
                "type": "ARCHITECTURAL"
            })

        # Dream 2: Market Integration
        for trend in market_trends:
            if "AI" in trend or "Agent" in trend:
                dreams.append({
                    "title": f"Autonomous {trend} Specialist",
                    "vision": f"Create a dedicated agent to dominate the {trend} niche.",
                    "type": "SKILL_ACQUISITION"
                })

        # Dream 3: Innovation based on Categories
        if top_categories:
            main_cat = list(top_categories.keys())[0]
            dreams.append({
                "title": f"Deep Dive Expert: {main_cat}",
                "vision": f"Develop advanced reasoning for {main_cat} content generation and analysis.",
                "type": "COGNITIVE"
            })

        # Fallback Dream
        if not dreams:
            dreams.append({
                "title": "Systemic Resilience Upgrade",
                "vision": "Enhance self-healing and redundancy protocols for 99.99% uptime.",
                "type": "STABILITY"
            })

        # Persist dreams
        self._persist_dreams(dreams)

        # Propose improvements based on dreams
        for dream in dreams:
            await blackboard.propose_improvement(self.name, {
                "vision_proposal": dream["title"],
                "vision_details": dream["vision"]
            })

        return {"long_term_visions": dreams}

    def _persist_dreams(self, dreams):
        os.makedirs(os.path.dirname(DREAMS_FILE), exist_ok=True)

        current_data = []
        if os.path.exists(DREAMS_FILE):
            try:
                with open(DREAMS_FILE, 'r') as f:
                    current_data = json.load(f)
            except Exception:
                pass

        new_entry = {
            "timestamp": datetime.now().isoformat(),
            "dreams": dreams
        }
        current_data.append(new_entry)

        try:
            with open(DREAMS_FILE, 'w') as f:
                json.dump(current_data, f, indent=4)
            self.logger.info(f"Persisted {len(dreams)} dreams to {DREAMS_FILE}")
        except Exception as e:
            self.logger.error(f"Failed to persist dreams: {e}")
